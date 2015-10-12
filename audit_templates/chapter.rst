{# One chapter of the questions #}
.. This is a generated file from data/. DO NOT EDIT.

===========================================
{{ meta.title }}
===========================================

*{{ meta.description }}*

{{ meta.background }}

{% if questions %}

.. toctree::
    :maxdepth: 2

{% for question_title, question in questions.items() %}
    {{ question_title|normalize_id }}
{% endfor %}

{% endif %}
