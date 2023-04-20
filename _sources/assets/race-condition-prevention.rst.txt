
.. This is a generated file from data/. DO NOT EDIT.

.. _race-condition-prevention:

Race condition prevention
==============================================================

**A systematic development method prevents race conditions?** Yes / No

A systematic development method is applied to all financial transactions so that race conditions cannot compromise transaction integrity. Otherwise exploiting the race condition allows the attacker to manipulate account balances.

For all financial transactions:

* Optimistic database-level transaction isolation is applied or...

* Pessimistic application level locks are applied.

The software should be developed in such a manner that there is only one function to make transfers out from the system or within the system. This function has a locking mechanism such that simultaneous transactions from the same account cannot compromise the atomicity, leading to double top up, double withdraw or account overdrawn.





Related incidences:

- :ref:`cryptoine`

- :ref:`starbucks`




Links:


- `Lock (database) (Wikipedia) <https://en.wikipedia.org/wiki/Lock_%28database%29>`_



- `Race condition (Wikipedia) <https://en.wikipedia.org/wiki/Race_condition>`_



- `Atomicity (Wikipedia) <https://en.wikipedia.org/wiki/Atomicity_(database_systems)>`_



- `Transaction Isolation (PostgreSQL) <http://www.postgresql.org/docs/9.1/static/transaction-iso.html>`_



- `How I stole roughly 100 BTC from an exchange and how I could have stolen more <https://www.reddit.com/r/Bitcoin/comments/1wtbiu/how_i_stole_roughly_100_btc_from_an_exchange_and/>`_



