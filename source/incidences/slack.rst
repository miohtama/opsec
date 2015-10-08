
.. This is a generated file from data/. DO NOT EDIT.

.. _slack:

Slack
==============================================================

*Date: 2015-03-01*


Compromised user accoutns: **500k**





The database of Slack, a popular team communication tool, was leaked.

Slack is a popular team communication tool among software development companies. The database of Slack got compromised, leading to the exposure of salted passwords.

Slack did not disclose how the attackers got access to their database.

After the breach Slack detected suspicious activity targeting some of its customers. Slack reseted the passwords for these customers. Furthermore, after the incident, Slack enabled two-factor authentication and kill switch as options for its users. Two-factor authentication was not an option before Slack got hacked.

Whether two-factor authentication effectively stops the attackers in the case of database breach is a subject to discussion. If the salted passwords are compromised you usually also lose the two-factor authentication tokens stored in the same database.



Related evaluation points:

- :ref:`password-storage-best-practices`

- :ref:`two-factor-authentication`

- :ref:`effective-session-kill`





Links:

- `March 2015 Security Incident and the Launch of Two Factor Authentication <http://slackhq.com/post/114696167740/march-2015-security-incident-and-launch-of-2fa>`_

- `Slack enables two-factor authentication following security breach <http://www.theverge.com/2015/3/27/8301031/slack-office-app-two-factor-authentication-secure>`_

