
.. This is a generated file from data/. DO NOT EDIT.

===========================================
Infrastructure security
===========================================

This chapter discussed protecting your servers and other infrastructure used to run your application.
This chapter uses the term infrastructure to cover whatever is needed to run a custom software. One needs to have servers somewhere. One needs to access and protect the servers somehow. One needs to trust the server provider. Many parts of the infrastructure (DNS) cannot be under the direct control of the stakeholders.

Background
==========

None




.. _login-throttle:

Login throttle
==============================================================

**Throttle or ban IPs with multiple login attempts?** Yes / No

Prevent bruteforce attacks against your service by blocking multiple login attempts. asdf
Log monitoring software like fail2ban can do this with almost zero configuration for stock applications like SSH and common web servers.
Please note that IP blocking is not effective against adversaries with botnets with thousands of global IPs in their posession.


Applies for: Everyone





Links:


- `fail2ban <http://www.fail2ban.org/>`_



- `Banning IPv6 addresses (ServerFault) <http://serverfault.com/q/631160/74975>`_






.. _security-proxy:

Security proxy
==============================================================

**Servers are behind security proxy?** 

Using a security proxy service hides the IP of your servers from the attacker, thus making denial-of-service attacks more difficult to perform.
The security proxy services are provided by specialized companies who possess geographically distributed servers, a lot of bandwidth and can thus withstand attacks. Furthermore these services apply rules on the traffic to prevent common malicious visitors and crawlers.






Links:


- `CloudFlare <http://cloudflare.com/>`_



- `Incapsula <https://www.incapsula.com/>`_






.. _internal-domains-not-exposed:

Internal domains not exposed
==============================================================

**Internal services cannot be discovered from public data?** 

Internal services, testing and staging servers, which are likely to be less protected and monitor, should not be publicly known. The public DNS records should not expose any services which are not public.
For internal services run a custom DNS server or use a non-guessable secondary domain name.









.. _log-server:

Log server
==============================================================

**Critical logs are mirrored to a append only service?** 

Critical log files should be mirrored to a destination where the logs can be only appended. The logs cannot be read back or manipulated. The log server or service should have different access credentials from the administrators of normal systems.
In the case the attacker gains access to infrastructure, this prevents wiping or manipulating logs. This allows robust recovery and post-mortem from potential infrastructure attack.


Applies for: Medium and large enterprises





Links:


- `Amazon CloudWatch <https://aws.amazon.com/cloudwatch/>`_



- `Creating a Centralized Syslog Server (Linux Journal) <http://www.linuxjournal.com/content/creating-centralized-syslog-server>`_






.. _encrypted-server-data:

Encrypted server data
==============================================================

**Data is stored on encrypted partitions?** 

All user data should be stored on encrypted partitions or files. In the case of unauthorized physical access the data cannot be compromised. Encryption should apply for backups and other offsite files too.

Disk encryption protects the data when the server is offline. All sensitive databases should reside on the partitions which are not accessible if the physical machine is compromised. If the server is rebooted without authorization the server should ask a passphrase to unecrypt the data partitions. The easiest way to achieve this is to have separate partitions for boot volume and data volume. Having separate "high" and "low" states the server cannot enter to to the state with access to data unless an authorized person enters a passphrase through a terminal.

This protects the loss of data against

* Hosting provider attacks or social engineering attacks against the hosting provider

* Law enforcement attacks

.. note ::

  All virtual machines, like ones provided by Amazon EC2, are ultimately unsafe. It's possible to make a silent copy of a virtual machine and its disk, even if encrypted, without the authorization of the server owner. If your adversiers include law enforcement agencies and nation state actors it is recommended to use only physical servers which cannot be rebooted without notice. The servers should be enabled with physical chassis removal detection which stop at BIOS boot if they detect the server chassis to be opened.

Furthermore all dedicated servers which you do not install yourself in your own rack can be deemed as unsafe. If you do not have the key to th  physical lock at the rack you can never be sure that somebody tampers with the server.





Related incidences:

- :ref:`bitly`

- :ref:`linode`




Links:




- `Analyzing the FBI’s Explanation of How They Located Silk Road (Nik Cubrilovic) <https://www.nikcub.com/posts/analyzing-fbi-explanation-silk-road/>`_



- `LocalBitcoins received an attack against the site infrastructure (Hacker News) <https://news.ycombinator.com/item?id=7692750>`_






.. _secure-server-to-server-connections:

Secure server-to-server connections
==============================================================

**Server-to-serve connections are secure?** 

Nation state actors and other capable adversaries are proven to be able to tap Internet backbone connections and data centers.

The server-to-server connections should be encrypted in a manner that anyone tapping a physical cable cannot any extract any information.

The connection encryption methods include SSH tunnels and VPN.







Links:


- `Room 641A (Wikipedia) <https://en.wikipedia.org/wiki/Room_641A>`_



- `Googlers say “F*** you” to NSA, company encrypts internal network (Ars Technica) <http://arstechnica.com/information-technology/2013/11/googlers-say-f-you-to-nsa-company-encrypts-internal-network/>`_



- `Reports that NSA taps into Google and Yahoo data hubs infuriate tech giants (The Guardian) <http://www.theguardian.com/technology/2013/oct/30/google-reports-nsa-secretly-intercepts-data-links>`_






.. _publicly-exposed-services-and-firewalling:

Publicly exposed services and firewalling
==============================================================

**Unnecessary services are not exposed to Internet?** 

All private services like databases, queue services and caches should be not Internet accessible.

The services should bind to private network or localhost IPs only.

The easiest method to verify this is to scan the ports of all public IPs. Only the publicly accessible endpoints, like HTTP and HTTPS, should be available.

.. note ::

  A firewall should be only a secondary measure. By default the services should be configure in a manner that they to do not bind to publicly exposed IPs. Furthermore firewalling outgoing connections might be problematic, as many services rely on third party API service today.







Links:


- `Nmap <https://nmap.org/>`_






.. _intrusion-detection:

Intrusion detection
==============================================================

**Intrusion detection alerts on unexpected server activity?** 

Intrusion detection software monitors the servers and alerts in the case there is unexpected activity.

Intrusion detection is a measure to detect compromised servers. Intrusion detection software monitors processes, file system, configuration files, passwords and user database. In the case there are changes not matching the predefined ruleset an alert is fired.



Applies for: Medium and large enterprises





Links:


- `Tripwire <http://www.tripwire.com/>`_



- `OSSEC <http://www.ossec.net/>`_






.. _priviledge-separated-software-installation:

Priviledge separated software installation
==============================================================

**Software installations are under custom accounts and rights?** 

Any installed software is under non-root (non-admin) account. The compromise of the software throguh an exploit cannot compromise the server as a whole.







Links:


- `Privledge separation (Wikipedia) <https://en.wikipedia.org/wiki/Privilege_separation>`_





