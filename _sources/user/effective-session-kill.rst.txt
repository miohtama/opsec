
.. This is a generated file from data/. DO NOT EDIT.

.. _effective-session-kill:

Effective session kill
==============================================================

**When the user account is deactivated or changed, the related sessions are dropped?** 

If the attacker gains access to a user account, system administrators must be able to kick out the attacker. In certain security-related actions, it is also good practice to drop the sessions of the user.

Account deactivation, besides marking the user account deactivated in the database records, should also drop the active sessions which are usually stored in a separate backend like Memcached or Redis. When a user account is deactivated, all communication channels to this user must be dropped: HTTP sessions, WebSocket sessions, mobile application sessions and so on.

Furthermore, all user sessions should be dropped when the users themselves perform changes which may affect account security. These include:

* Password change

* Email address change

* Phone number change

After the change has been performed, the user must relogin to the service. This allows the users themselves to act quickly in situations in which they notice that somebody has hacked into the account, e.g., via an incoming email notification. In this case, the user is still probably logged into the system with stolen credentials and the user may hurry to change the password to kick the attacker out.





Related incidences:

- :ref:`slack`




Links:


- `Simultaneous Session Logons (OWASP) <https://www.owasp.org/index.php/Session_Management_Cheat_Sheet#Considerations_When_Using_Multiple_Cookies>`_



