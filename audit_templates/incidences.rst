{# One chapter of the questions #}
.. This is a generated file from data/. DO NOT EDIT.

==============================
Security incidence reference
==============================

This chapter contains references to historical security incidences, why they happened, the implications and what operational security measurements could have been taken to prevent them.

.. attention ::

    *All Internet service incidences listed here could have been avoided by following the security practices presented in this guide.*

Some of the incidences are not directly related to a particular Internet service, e.g. SMS intercepting, but the case reflects the associated security risk it may pose to any Internet service and its user.

Incidences
===================

Number of incidence summaries: **{{ incidences|length }}**

Compromised user accounts: **{{ compromised_accounts|round(2, 'floor') }}M**

Lost assets: **{{ assets_lost|round(2, 'floor') }}M USD**

Bankcrupted companies: **1**

Fired employees: **0**

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




