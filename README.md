# Operations Security book

OPSEC - Operations security is a guide and assessment tool for Internet service development.
Developers, system administrators and decision-makers can learn to guarantee the safety of their projects against external and internal threats. The practical guide applies to one-man teams as well as large organizations building websites. A special emphasis is put on high-value targets like cryptocurrency services.

# Background

The online book was originally written in 2015 as a security guide.
It was self-published at `operationssecurity.org`, but got unmaintained
2017-2023. In 2023, the content was resurrected and put back online again.

# Generating the content

Install:

```shell
poetry install
```

Building the Sphinx content material:

```shell
poetry shell
make book
```

Building the website and viewing HTML locally:

```shell
ln -s build/html/ site/output/docs/
cd site
make clean html serve
```

Building and publishing the site:

    make clean html && aws s3 sync output s3://operationssecurity.org --exclude "*node_modules*" --follow-symlinks

# Technicals

This Git repository is a Pelican, Sphinx and YAML source code for building the book.

* YAML is the authoritative source code for text

* Sphinx drives the generation of online documentation and eBook

* Pelican drives the generation of a static website and blog

# Contact

mikko at opensourcehacker dot com
