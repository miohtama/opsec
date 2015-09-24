{# One chapter of the questions #}
.. This is a generated file from data/. DO NOT EDIT.

==========
Incidences
==========

This chapter contains references to historical security breaches, their implications and what operational security measurements could have been taken to prevent them.

{% for incidence_id, incidence in incidences.items() %}

{{ incidence.title }}
==============================================================

{{ incidence.description }}


{% if incidence.references %}
Related evaluation points:
{% for chapter_id, question_id in incidence.references %}
- {{ chapter_id }}, {{ question_id }}
{% endfor %}

{% endif %}

{% if incidence.links %}
Links:
{% for link in incidence.links %}
- `{{ link.split(',')[0].strip() }} <{{ link.split(',')[1].strip() }}>`_
{% endfor %}
{% endif %}

{% endfor %}

