
.. This is a generated file from data/. DO NOT EDIT.

.. _flood-action-throttle:

Flood action throttle
==============================================================

**Actions sending messages to other users are throttled?** Yes / No

When the service provides ways to message or contact other users, these actions should be throttled so that one cannot flood messaging by sending a large number of useless messages.

Example actions that should be throttled include:

* Sending messages to other users

* Sending invitation emails

* Sending SMS messages

If a malicious actor is free to send an infinite number of messages, this can be exploited for harassment. Even if the exploitation doesn't lead to direct financial gain for the attacker, the service may take a reputation hit and the brand suffers due to poor user experience.

Throttling can be done by having time window thresholds for how many messages one user can send or how many messages can be sent on a global level. If the frequency of actions exceeds the limit of what a normal person would do, the action should be disabled or the user banned.





Related incidences:

- :ref:`coinbase`




Links:


- ` <Rolling time window counters with Redis and mitigating botnet (Mikko Ohtamaa)>`_



