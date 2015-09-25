
.. This is a generated file from data/. DO NOT EDIT.

===========================================
Infrastructure security
===========================================

This chapter discussed protecting your servers and other infrastructure used to run your application.

Background
==========

None




.. _login-throttle:

Login throttle
==============================================================

**Throttle or ban IPs with multiple login attempts?** Yes / No

Prevent bruteforce attacks against your service by blocking multiple login attempts.
Log monitoring software like fail2ban can do this with almost zero configuration for stock applications like SSH and common web servers.
Please note that IP blocking is not effective against adversaries with botnets with thousands of global IPs in their posession.

Applies for: Everyone




Links:

- `fail2ban <http://www.fail2ban.org/>`_





.. _security-proxy:

Security proxy
==============================================================

**Put your servers behind a security proxy?** 

Using a security proxy service hides the IP of your servers from the attacker, thus making denial-of-service attacks more difficult to perform.
The security proxy services are provided by specialized companies who possess geographically distributed servers, a lot of bandwidth and can thus withstand attacks. Furthermore these services apply rules on the traffic to prevent common malicious visitors and crawlers.

Applies for: 




Links:

- `CloudFlare <http://cloudflare.com/>`_

- `Incapsula <https://www.incapsula.com/>`_




