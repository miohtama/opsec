{# One chapter of the questions #}
.. This is a generated file from data/. DO NOT EDIT.

==============================
Security incidence reference
==============================

This chapter contains references to historical security incidences, why they happened, the implications and what operational security measurements could have been taken to prevent them.

.. note ::

    The list was updated 2013-2015. It does not contain recent incidences. There has been
    only very few new attack vectors since then, so all best practices and malpractices
    found here stil apply.

Incidences
===================

Last time list updated: 2015

Number of incidence summaries: **{{ incidences|length }}**

Compromised user accounts: **{{ compromised_accounts|round(2, 'floor') }}M**

Lost assets: **{{ assets_lost|round(2, 'floor') }}M USD**

.. raw :: html

    <table class="table-incidences">
        <thead>
            <tr>
                <th>Name</th>
                <th>Date</th>
                <th>Related security assessment points</th>
            </tr>
        </thead>
        <tbody>
            {% for incidence_id, incidence in incidences.items() %}
                <tr>
                    <td>
                        <a href="{{ incidence_id|normalize_id }}.html">{{ incidence.title }}</a>
                    </td>
                    <td class="col-date">
                        {{ incidence.date }}
                    </td>
                    <td>
                        {% for chapter_id, question_id, question_title in incidence.references %}
                            <p>
                                <a href="../{{ chapter_id }}/index.html#{{ question_id|normalize_id }}">{{ question_title }}</a>
                            </p>
                        {% endfor %}
                    </td>
                </tr>
            {% endfor %}
        </tbody>
    </table>

Indicent index
==============

.. toctree::
    :maxdepth: 2
{% for incidence_id, incidence in incidences.items() %}
    {{ incidence_id }}
{% endfor %}




