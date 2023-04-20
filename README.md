# Operations Security guide

This Git repository is a Pelican, Sphinx and YAML source code for building the book.

# Background

The online book was originally written in 2015 as a security guide.
It was self-published at `operationssecurity.org`, but got unmainained
2017-2023. In 2023, the content was resurrected and put back online again.

# Generating the content

Install:

```shell
poetry install
```

Building the book:

```shell
poetry shell
make book
```

Viewing HTML locally:

```shell
open build/html/index.html
```

Building and publishing the site:

    make clean html && aws s3 sync output s3://operationssecurity.org --exclude "*node_modules*" --follow-symlinks

# Technicals

* YAML is the authoritative source code for text

* Sphinx drives the generation of online documentation and eBook

* Pelican drives the generation of a static web site and blog
