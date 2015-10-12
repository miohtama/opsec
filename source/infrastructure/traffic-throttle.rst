
.. This is a generated file from data/. DO NOT EDIT.

.. _traffic-throttle:

Traffic throttle
==============================================================

**Throttle or ban IP addresses with excessive requests?** Yes / No

Prevent denial-of-service, brute force and scraping attacks against your service by blocking clients doing excessive traffic.

Normal users and clients should be able to do only four to twenty burst HTTP requests to the service. If there is more incoming traffic and the client is not whitelisted, the client likely does not have good intentions.

A log monitoring software like fail2ban can do this with almost zero configuration for stock applications like SSH and common web servers.

Please note that IP blocking alone is not effective against adversaries with botnets and thousands of global IPs in their possession.

.. note ::

  Don't accidentally ban good known bots like GoogleBot and Bing.



Applies for: Everyone





Links:


- `NGINX - throttle requests to prevent abuse (ServerFault) <http://serverfault.com/q/179646/74975>`_



- `fail2ban <http://www.fail2ban.org/>`_



- `Banning IPv6 addresses (ServerFault) <http://serverfault.com/q/631160/74975>`_



