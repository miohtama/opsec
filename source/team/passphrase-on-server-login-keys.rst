
.. This is a generated file from data/. DO NOT EDIT.

.. _passphrase-on-server-login-keys:

Passphrase on server login keys
==============================================================

**The terminal access to the server requires passphrase protected key?** Yes / No

Logging in to the server containing private data is allowed only with passphrase-protected key files.

The usual logging method is by SSH secure shell connection, but if alternative methods to access the server exist, the key files should be used there, too.

Using key files instead of passwords protects against brute force attacks, simple keylogging attacks, weak password attacks and such. Furthermore, the keys must be passphrase protected so that in case a key file itself leaks, it is useless to the attacker.

.. note ::

  If the hosting provider has a console, terminal or root password reset option on the server, special attention should be paid to this. It is better to either disable this feature or to make sure it is behind two-factor authentication and cannot be performed by hosting provider personnel.



Applies for: Everyone



Related incidences:

- :ref:`linode`

- :ref:`maxcdn`




Links:


- `SSH key and passwordless login basics for developers (Mikko Ohtamaa) <https://opensourcehacker.com/2012/10/24/ssh-key-and-passwordless-login-basics-for-developers/>`_



- `Linode Hacks (Bitcoin Thefts) <https://bitcointhefts.com/details/linode-hacks>`_



