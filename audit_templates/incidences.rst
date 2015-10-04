{# One chapter of the questions #}
.. This is a generated file from data/. DO NOT EDIT.

==========
Incidences
==========

This chapter contains references to historical security breaches, their implications and what operational security measurements could have been taken to prevent them.

Incident summary
================

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

Indicent list
=============

.. toctree::
    :maxdepth: 2
{% for incidence_id, incidence in incidences.items() %}
    {{ incidence_id }}
{% endfor %}




