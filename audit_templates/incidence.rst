{# One chapter of the questions #}
.. This is a generated file from data/. DO NOT EDIT.

.. _{{ incidence_id|normalize_id }}:

{{ incidence.title }}
==============================================================

*Date: {{ incidence.date }}*

{{ incidence.description }}

{% if incidence.references %}
Related evaluation points:
{% for chapter_id, question_id, question_title in incidence.references %}
- :ref:`{{ question_id|normalize_id }}`
{% endfor %}

{% endif %}

{% if incidence.links %}
Links:
{% for link in incidence.links %}
- `{{ ','.join(link.split(',')[0:-1]) }} <{{ ((link.split(',')|length) > 1) and link.split(',')[-1].strip() }}>`_
{% endfor %}
{% endif %}
