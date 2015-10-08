.. This is a generated file from data/. DO NOT EDIT.


.. image:: _static/logo-text.png
    :align: center
    :width: 610
    :alt: Opsec - Operations Security


.. note ::

    This is a living, work-in-progress, document. We kindly ask that you not to refer to this document or use the material presented herein until the authors release the version 1.0.

OPSEC - Operations Security
===========================

This is an online guide for operations security (OPSEC) for Internet services.

Operations security (OPSEC) is a multidisciplinary approach for protecting information and services. Though the term has a wider general meaning, this guide discusses OPSEC in the context of securing Internet services. This includes, but is not limited to, protecting information from industrial espionage, blackhat hackers, law enforcement, social engineering, and mass surveillance. `Please read further a introduction to OPSEC on Wikipedia <https://en.wikipedia.org/wiki/Opsec>`_.

About this guide
================

|opsec| is a security guide and assessment tool for developing sensitive Internet services.

The aim is to provide transparent, lightweight and practical ways to develop and evaluate the security of an Internet service from a holistic viewpoint. The scope of the guide is interdisciplinary, covering the full range of business operations from team computer and mobile phone setup to safe software development practices. :doc:`Read more about how and why this guide was created <background/index>`.

The guide presents {{ security_assesment_point_count }} assesment points to evaluate different aspects of team and service. The security assessment points are referred in {{ incidence_count }} :doc:`historical security incidences <incidences/index>` which could have been avoided if the operators had followed practices presented here.

Chapters
========

.. toctree::
    :maxdepth: 1

    background/author
    background/audience
    background/index
    assessment/index
{% for chapter in chapters %}
    {{ chapter }}/index
{% endfor %}
    incidences/index
    background/contact
    background/license

More
====

`Follow us on Twitter <https://twitter.com/OpSecSanta>`_.


