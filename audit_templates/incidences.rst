{# One chapter of the questions #}
.. This is a generated file from data/. DO NOT EDIT.

==========
Incidences
==========

This chapter contains references to historical security breaches, their implications and what operational security measurements could have been taken to prevent them.

{% for incidence_id, incidence in incidences.items() %}

.. _{{ incidence_id|normalize_id }}:

{{ incidence.title }}
==============================================================

*Date: {{ incidence.date }}*

{{ incidence.description }}

{% if incidence.references %}
Related evaluation points:
{% for chapter_id, question_id in incidence.references %}
- :ref:`{{ question_id|normalize_id }}`
{% endfor %}

{% endif %}

{% if incidence.links %}
Links:
{% for link in incidence.links %}
- `{{ ','.join(link.split(',')[0:-1]) }} <{{ ((link.split(',')|length) > 1) and link.split(',')[-1].strip() }}>`_
{% endfor %}
{% endif %}

{% endfor %}

