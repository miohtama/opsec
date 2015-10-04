
.. This is a generated file from data/. DO NOT EDIT.

.. _lastpass:

LastPass
==============================================================

*Date: 2015-06-10*

A popular password management service, LastPass, got compromised.

LastPass account email addresses, password reminders, server per user salts, and authentication hashes were compromised.

The salted user master passwords where exposed to the attacker. A weak master password could lead to the compromise of the whole password vault of a user. All users were prompted to change their master passwords. LastPass does third factor authentication on its users, claiming this could have protected the potential victims.



Related evaluation points:

- :ref:`password-manager`

- :ref:`password-storage-best-practices`

- :ref:`third-factor-authentication`





Links:

- `LastPass Security Notice <https://blog.lastpass.com/2015/06/lastpass-security-notice.html/>`_

- `Hack Brief: Password Manager LastPass Got Breached Hard <http://www.wired.com/2015/06/hack-brief-password-manager-lastpass-got-breached-hard/>`_

