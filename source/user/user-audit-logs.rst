
.. This is a generated file from data/. DO NOT EDIT.

.. _user-audit-logs:

User audit logs
==============================================================

**Service retains audit logs of sensitive user actions?** 

All sensitive actions should be logged to a user-specific action log.

The users may or may not be able to view these log entries themselves. In the case of a user reporting a hacked account, the action log can be reviewed for swift judgement. In the case of a filed police report, due to an account hack, the user audit log can be handed to the officials.

The user audit log also serves an important role in protecting the service operator itself against fraud. For example, a user can make a frivolous claim that the user’s account got hacked, then threaten to sue the service and publish the incident unless there is (incorrectly) reimbursement. In fact, the user might have just transferred out assets himself/herself to a friendly third party. The user audit logs prove the correct password and authentication codes were used to initiate the transfer and shift the responsibility to the user himself or herself.

The user audit log should include at least:

* User logins and login attempts

* Password change and reset operations

* Enabling and disabling two-factor authentication

* Email change operations

* All financial operations

* Timestamp with timezone

* IP address

* User agent





Related incidences:

- :ref:`steam`




Links:


- `Logging Sessions Life Cycle: Monitoring Creation: Usage, and Destruction of Session IDs (OWASP) <https://www.owasp.org/index.php/Session_Management_Cheat_Sheet#Considerations_When_Using_Multiple_Cookies>`_



- `Investigation report of the claimed security breach at LocalBitcoins <http://localbitcoins.blogspot.fi/2014/04/investigation-report-of-claimed.html>`_



