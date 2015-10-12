
.. This is a generated file from data/. DO NOT EDIT.

.. _password-storage-best-practices:

Password storage best practices
==============================================================

**User passwords and two-factor seeds are hashed and salted against bruteforcing?** Yes / No

Password hashing is a method to prevent cleartext password storage.

This protects user password integrity in case the database is compromised and logins and passwords are dumped somewhere. Developers should not invent password storage schemes themselves, but should use a specialized library to do the password hashing and salting for persistent storage.



Applies for: Everyone



Related incidences:

- :ref:`sebastian`

- :ref:`slack`

- :ref:`lastpass`

- :ref:`hacking-team`




Links:


- `PBKDF2 (Password-Based Key Derivation Function 2) in Wikipedia <https://en.wikipedia.org/wiki/PBKDF2>`_



- `Password storage cheat sheet in OWASP <https://www.owasp.org/index.php/Password_Storage_Cheat_Sheet>`_



- `Password strength (Wikipedia) <https://en.wikipedia.org/wiki/Password_strength>`_



