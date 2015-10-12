
.. This is a generated file from data/. DO NOT EDIT.

.. _transaction-verification:

Transaction verification
==============================================================

**Withdraws are verified by heuristics?** 

Withdraws are verified by heuristics so that unusual outgoing transactions need another round of authorization from the customer or human interaction from the support team.

Outgoing transaction verification provides an additional layer of protection against asset theft:

* Customer withdraws are verified. If the parameters of the transaction do not match prior customer activity and a malicious withdraw is suspected, the customer must reauthorize the transaction (see :ref:`third-factor-authentication`).

* How wallet drain attacks are prevented, as the heuristics would detect such and stop them.

Transaction verification is usually implemented as a multi-signature service with a third party. A third party holds one key required to make the transaction. When a transaction is created, the third-party service checks the transaction parameters against known good rules. If the transaction looks okay, the third-party service signs its part of the transaction. Because the third party is independent and specialized in the transaction verification process, it is unlikely that the attacker would manage to compromise it, too.





Related incidences:

- :ref:`bitstamp`

- :ref:`linode`




Links:


- `BitGo <https://www.bitgo.com/>`_



- `BitGoD (Github) <https://github.com/BitGo/bitgod>`_



