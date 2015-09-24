import os
import jinja2
from slugify import slugify
from yaml import safe_load as load
import yaml

from collections import OrderedDict

def ordered_load(stream, Loader=yaml.Loader, object_pairs_hook=OrderedDict):
    class OrderedLoader(Loader):
        pass
    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))
    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)


ANSWERS = {
    "default": "Yes / No"
}

APPLIES = {
    "everyone": "Everyone",
    "mle": "Medium and large enterprises"
}


@jinja2.contextfilter
def normalize_id(jinja_ctx, context, **kw):
    return slugify(context)


def get_audit_data(chapter):
    with open("data/{}.yaml".format(chapter), "rt") as inp:
        struct = ordered_load(inp, yaml.SafeLoader)
    return struct


def get_chapters(chapter_ids):
    chapters = OrderedDict()
    for chapter_id in chapter_ids:
        with open("data/{}.yaml".format(chapter_id), "rt") as inp:
            struct = ordered_load(inp, yaml.SafeLoader)
        chapters[chapter_id] = struct
    return chapters


def get_incidences_data(chapters):
    with open("data/incidences.yaml", "rt") as inp:
        struct = ordered_load(inp, yaml.SafeLoader)

    # Build cross-reference data incidence -> question
    for incidence_id, incidence in struct.items():
        incidence["references"] = []
        for chapter_id, chapter_data in chapters.items():
            for question_id, question in chapter_data["questions"].items():
                if incidence_id in [inc.lower() for inc in question.get("incidences", [])]:
                    incidence["references"].append((chapter_id, question_id))


    return struct


loader = jinja2.FileSystemLoader(os.path.join(os.getcwd(), "audit_templates"))
env = jinja2.Environment(loader=loader)
env.filters["normalize_id"] = normalize_id

chapter_template = env.get_template('chapter.rst')
chapter_ids = load(open("data/index.yaml", "rt"))
chapters = get_chapters(chapter_ids)


# Generate index
index_template = env.get_template('index.rst')
doc = index_template.render(chapters=chapters)
with open("source/index.rst", "wt") as out:
    out.write(doc)

# Generate incidences
incidences_template = env.get_template('incidences.rst')
incidences = get_incidences_data(chapters)
doc = incidences_template.render(incidences=incidences)
with open("source/incidences/index.rst", "wt") as out:
    out.write(doc)

# Generate chapters
for chapter_id, chapter in chapters.items():
    md = chapter_template.render(answers=ANSWERS, applies=APPLIES, **chapter)
    with open("source/{}/index.rst".format(chapter_id), "wt") as out:
        out.write(md)



