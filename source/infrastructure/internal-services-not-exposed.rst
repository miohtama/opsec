
.. This is a generated file from data/. DO NOT EDIT.

.. _internal-services-not-exposed:

Internal services not exposed
==============================================================

**Internal servers, services and domains cannot be discovered through public records?** 

Internal services, testing and staging servers should not be exposed to the public. DNS records should not contain services which are not for public consumption.

Usually testing and staging servers have more people with privileged access. This increases the potential attack surface from compromised devices and accounts. If there is no specific reason why the server needs to be publicly accessible, it should be hidden behind VPN and not be visible in public DNS records. For internal services, run a custom DNS server or use a non-guessable secondary domain name.

A firewall should be only a secondary layer protecting human errors. The services should be configured in a manner such that they do not bind to publicly exposed IPs, but bind only to localhost or internal IPs. Furthermore, firewalling outgoing connections might be problematic, as many services today rely on third-party API service.

Within the server, any installed software is run under a non-admin (non-root) account. This limits the impact of an attack if arbitrary code execution vulnerability in the native applications is exploited. The attacker cannot leave further backdoors in the system and is able to gain only limited intel.





Related incidences:

- :ref:`patreon`




Links:


- `Nmap <https://nmap.org/>`_



- `Privledge separation (Wikipedia) <https://en.wikipedia.org/wiki/Privilege_separation>`_



- `Basic access authentication (Wikipedia) <https://en.wikipedia.org/wiki/Basic_access_authentication>`_



