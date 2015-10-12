Please see [operationssecurity.org](http://www.operationssecurity.org/)

This is a Pelican, Sphinx and YAML source code for the site.

* YAML is the authoritative source code for text

* Sphinx drives the generation of online documentation and eBook

* Pelican drives the generation of a static web site and blog

sphinx_rtd_theme base:

    pip install -e "git+git@github.com:snide/sphinx_rtd_theme.git@012d42db6a2b00f799223963fb8b0aa3754630eb#egg=sphinx_rtd_theme"

Building docs:

    python build.py && make clean html

Building and publishing the site:

    make clean html && aws s3 sync output s3://operationssecurity.org --exclude "*node_modules*" --follow-symlinks

