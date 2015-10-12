"""Create sitemap for HTML files."""
import os
import jinja2
from datetime import date
import stat

loader = jinja2.FileSystemLoader(os.getcwd())
env = jinja2.Environment(loader=loader)

sitemap_files = []

os.chdir("output")

for root, dirs, files in os.walk(".", topdown=False, followlinks=True):
    for name in files:

        if root.startswith("./theme"):
            continue

        if name.endswith(".html"):
            path = os.path.join(root, name)
            statbuf = os.stat(path)
            fdate = date.fromtimestamp(statbuf[stat.ST_MTIME])
            lastmod = fdate.strftime('%Y-%m-%d')

            # Remove ./output
            path = path[len("."):]

            sitemap_files.append(dict(path=path, lastmod=lastmod))

template = env.get_template('sitemap.xml')
doc = template.render(files=sitemap_files)


with open("sitemap.xml", "wt") as out:
    out.write(doc)

