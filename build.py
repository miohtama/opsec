import os
import jinja2
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


def get_audit_data(chapter):
    with open("data/{}.yaml".format(chapter), "rt") as inp:
        struct = ordered_load(inp, yaml.SafeLoader)
    return struct

loader = jinja2.FileSystemLoader(os.path.join(os.getcwd(), "audit_templates"))
env = jinja2.Environment(loader=loader)

chapter_template = env.get_template('chapter.rst')
chapters = load(open("data/index.yaml", "rt"))

# Generate index
index_template = env.get_template('index.rst')
doc = index_template.render(chapters=chapters)
with open("source/index.rst", "wt") as out:
    out.write(doc)

# Generate chapters
for chapter in chapters:
    struct = get_audit_data(chapter)
    md = chapter_template.render(answers=ANSWERS, applies=APPLIES, **struct)
    with open("source/{}/index.rst".format(chapter), "wt") as out:
        out.write(md)



