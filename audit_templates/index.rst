.. This is a generated file from data/. DO NOT EDIT.


Operations Security guide
=========================

This is an online guide for operations security (OPSEC) for Internet services.

.. note ::

    This is a living, work-in-progress, document. We kindly ask you no to refer to this document or use the material presented here until the authors release the version 1.0.

What is operations security (OPSEC)
===================================

Operations security (OPSEC) is multidisciplinary approach for protecting information and services. Though the term has a wider general meaning, this guide discusses OPSEC in the context of securing Internet services. This includes, but is not limited to, protecting information from industrial espionage, blackhat hackers, law enforcement, social engineering, and mass surveillance. `Please read further introduction to OPSEC in Wikipedia <https://en.wikipedia.org/wiki/Opsec>`_.

About this guide
================

*OperationsSecurity.org* is guide and assessment tool to audit the security of Internet services. The aim is to provide 100% transparent, open, lightweight and practical way to develop and evaluate the security of a service from a holistic perspective. The scope of the guide is interdisciplinary, covering the full range of business operations from the mobile phone of CEO to safe software development practices.

The developers and system administrators can use the guide as a reference when building and :doc:`assessing security of their organizations <assessment/index>`. Furthermore, with the :doc:`evaluation points <background/index>` provided by the guide a third party can audit an organization and provide a public track record of the matter.

Audience
========

Not all Internet services are equally critical. This guide is aimed for the services dealing with private and financial data. It can be used as a reference for other kind of services, but in this case some evaluation points might not apply. The guide is not a general guide for IT administrators or normal IT service deployments dealing with issues like provisioning workstations or maintaining intranet.

The audience of the guide includes, but is not limited, to

* Website developers

* System administrators and infrastructure operators

* Technology and security officers

* ...or everybody how is responsible for making sure their services and users do not get hacked.

Chapters
========

.. toctree::
    :maxdepth: 1

    background/index
    assessment/index
    {% for chapter in chapters %}
    {{ chapter }}/index
{% endfor %}

License and copyright
=====================

The material is licensed under `Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) license <http://creativecommons.org/licenses/by-sa/4.0/>`_.

You are free to:

* Share — copy and redistribute the material in any medium or format
* Adapt — remix, transform, and build upon the material

for any purpose, even commercially.
