
.. This is a generated file from data/. DO NOT EDIT.

.. _data-scrubbing:

Data scrubbing
==============================================================

**Data dumps are cleaned of sensitive information?** Yes / No

Instead of working with full production datasets, there exists a repeatable process of making a cleaned dataset with sensitive information removed from the data.

The data scrubbing process can reset:

* User email addresses

* Phone numbers, physical addresses and social security numbers

* Password hashes

* Two-factor tokens

The cleaned dataset is then given to the team members who need to analyse, test and develop against the data.

The cleaning process limits the impact of potential data leak in cases in which the data dump accidentally ends up at the third party. Furthermore, the cleaned data ensures that messages from the testing environment cannot reach actual users.



Applies for: Everyone



Related incidences:

- :ref:`ashley-madison`

- :ref:`patreon`




Links:


- `How to Anonymize Data in a PostgreSQL Database (Michael Krenz) <http://www.michaelkrenz.de/2012/08/05/how-to-anonymize-data-in-a-postgresql-database/>`_



