
.. This is a generated file from data/. DO NOT EDIT.

.. _linode:

Linode
==============================================================

*Date: 2012-03-01*

A vulnerability in the customer support system of a Linode webhost was used to obtain administrator access to the servers of multiple Bitcoin companies.

Linode offers budget virtual servers for hosting. Several Bitcoin companies where hosting their site at Linode.

The attackers exploited a vulnerability in the Linode customer support interface. The root password was changed and the servers were restarted through web-based administrator panel. Then the attackers proceeded to logging in the servers and drained the hot wallets. 230k USD worth of Bitcoins were stolen.



Related evaluation points:

- :ref:`passphrase-on-server-login-keys`

- :ref:`two-factor-authentication-on-server-login`

- :ref:`encrypted-server-data`

- :ref:`cold-wallet`

- :ref:`transaction-verification`





Links:

- `Cloud Service Linode Hacked, Bitcoin Accounts Emptied (ThreatPost) <https://threatpost.com/cloud-service-linode-hacked-bitcoin-accounts-emptied-030212/76278/#sthash.PMEXbvX9.dpuf>`_

- `Linode Hacks (Bitcoin Thefts) <https://bitcointhefts.com/details/linode-hacks>`_

- `Customer support transcript with Linode (Marek Palatinus) <http://pastebin.com/UW7iT5fj>`_

