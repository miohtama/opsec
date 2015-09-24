
.. This is a generated file from data/. DO NOT EDIT.

===========================================
Protecting individual users
===========================================

This chapter discussed protecting your users and guiding them to maintain necessary security.

Background
==========

Even if the Internet service itself is well secured, the malicious actors can go after invididual users. For example, phishing operations target a group of users who are likely users of the service. If the service users give out their login credentials to the phisher, the phisher may damage this individual user, even though the integrity of the service as a whole is not compromised.




.. _two-factor-authentication:

Two-factor authentication
==============================================================

**The site users can enable two-factor authentication for login?** Yes / No

The site users use the service for the sensitive purposes. The site user may recycle their password across multiple sites, may use weak password or, most likely, the site users gets his or her devices compromised by malware. In this case, the two-factor authentication should stop the attacker with a mere password to access the user account.

Applies for: Everyone


Related incidences:

- :ref:`slack`




Links:

- `Two-factor Authentication List <https://twofactorauth.org/>`_





.. _effective-session-kill:

Effective session kill
==============================================================

**When the user account is deactivated, all related sessions are killed?** 

If the attacker gains access to an user account the system administrators must be able to kick out the attacker. The account deactivation may only affect the database records of the account, not dropping the active HTTP sessions which are stored in a separate store. When an user account is deactivated, all communication channels to this user must be dropped.

Applies for: 


Related incidences:

- :ref:`slack`




Links:

- `Simultaneous Session Logons (OWASP) <https://www.owasp.org/index.php/Session_Management_Cheat_Sheet#Considerations_When_Using_Multiple_Cookies>`_





.. _user-audit-logs:

User audit logs
==============================================================

**x?** 

x

Applies for: 




Links:

- `Logging Sessions Life Cycle: Monitoring Creation: Usage, and Destruction of Session IDs (OWASP) <https://www.owasp.org/index.php/Session_Management_Cheat_Sheet#Considerations_When_Using_Multiple_Cookies>`_




