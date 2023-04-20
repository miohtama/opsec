
.. This is a generated file from data/. DO NOT EDIT.

.. _database-injection:

Database injection
==============================================================

**Software uses a framework for database queries?** Yes / No

One of the most common web application vulnerabilities is a database injection attack. Developers are allowed to write queries by hand without properly sanitizing input going into the queries.

In most cases, the database is SQL based, providing an opportunity for SQL injections. This can be easily prevented by never constructing database statements by hand and by always using a framework to construct the queries so that all values are properly escaped. Manual SQL manipulation should be prevented by the application developers so that no room is left for human error.



Applies for: Everyone



Related incidences:

- :ref:`sebastian`




Links:


- `SQL injection in Wikipedia <https://en.wikipedia.org/wiki/SQL_injection>`_



- `SQL injection in OWASP <https://www.owasp.org/index.php/SQL_Injection>`_



- `PCI DSS v3.1 requirement 6.5.1 <https://www.pcisecuritystandards.org/documents/PCI_DSS_v3-1.pdf>`_



- `SQL injection hall of shame <http://codecurmudgeon.com/wp/sql-injection-hall-of-shame/>`_



- `Exploits of Mom (XKCD) <https://xkcd.com/327/>`_



