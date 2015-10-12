{# One question inside a chapter #}
.. This is a generated file from data/. DO NOT EDIT.

.. _{{ question_title|normalize_id }}:

{{ question_title }}
==============================================================

**{{ question.question }}?** {{ answers[question.answers] or question.answers }}

{{ question.rationale }}

{% if question.applies %}
Applies for: {{ applies[question.applies] }}
{% endif %}

{% if question.incidences %}
Related incidences:
{% for incidence_id in question.incidences %}
- :ref:`{{ incidence_id }}`
{% endfor %}
{% endif %}

{% if question.links %}
Links:
{% for link in question.links %}
{% if link.split %}
- `{{ ','.join(link.split(',')[0:-1]) }} <{{ link.split(',')[-1].strip() }}>`_
{% endif %}
{% endfor %}
{% endif %}

