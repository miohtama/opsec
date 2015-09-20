{# One chapter of the questions #}
.. This is a generated file from data/. DO NOT EDIT.

===========================================
{{ meta.title }}
===========================================

{{ meta.description }}

Background
==========

{{ meta.background }}

{% if questions %}
{% for question_title, question in questions.items() %}

{{ question_title }}
==============================================================

**{{ question.question }}?** {{ answers[question.answers] }}

{{ question.rationale }}

Applies for: {{ applies[question.applies] }}

{% if question.categores %}
    Categories: {{ question.categories }}
{% endif %}

{% endfor %}
{% endif %}
