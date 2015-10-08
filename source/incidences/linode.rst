
.. This is a generated file from data/. DO NOT EDIT.

.. _linode:

Linode
==============================================================

*Date: 2012-03-01*





Assets stolen: **230k USD**


A vulnerability in the customer support system of Linode, a hosting provider, was used to obtain administrator access to the servers of multiple Bitcoin services.

Linode offers budget virtual servers for hosting. Several Bitcoin companies where hosting their site at Linode back in 2012.

The attackers exploited a vulnerability in the Linode customer support interface. The web interface for server maintenance offered a root password reset through a single user mode reboot. The attackers used this feature to the servers and root passwords. Then the attackers proceeded to logging in the servers and drained the hot wallets of victim Bitcoin services. 230k USD worth of Bitcoins were stolen.

Linode has not disclosed what kind of vulnerability it had.



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

