
.. This is a generated file from data/. DO NOT EDIT.

===========================================
Infrastructure security
===========================================

This chapter discusses how to protect servers and other infrastructure needed to run the service.


Background
==========


Infrastructure here covers everything what runs your Internet service. It is mostly territory for system administrators, who know how to tune servers and what keeps them ticking. Everything cannot be done in-house and one most likely needs to rely on third party services for some things and they should be accounted too.





.. _encrypted-server-data:

Encrypted server data
==============================================================

**Data is stored on encrypted partitions?** 

All data should be stored on encrypted partitions or files. In the case of unauthorized physical access or unauthorized reboot the data cannot be compromised. Encryption should also apply for backups and other offsite files.

Data on encrypted partitions protect against

* Hosting provider attacks or social engineering attacks against the hosting provider where the root password is reset through single-user mode reboot

* Law enforcement attacks where the servers are physically confiscated

Disk encryption protects the data when the server is offline. All sensitive databases should reside on the partitions which are not accessible if the physical machine is compromised.

If the server is rebooted without authorization the server should ask a passphrase to decrypt the data partitions. The easiest way to achieve this is to have separate partitions for boot volume and data volume. By having separate "high" and "low" states the server cannot enter to to the state with access to data unless an authorized person enters a passphrase through a terminal.

All unaccounted reboots should be suspicious as when the server is offline the boot mechanism can be compromised to record the data decryption keys.

.. note ::

  Virtual machines, like ones provided by Amazon EC2 or Digital Ocean, are ultimately unsafe. It's possible to make a silent copy of a virtual machine and its disk, even if encrypted, without the authorization of the server owner. If the adversaries include law enforcement agencies and nation state actors it is recommended to use physical servers with chassis removal detection in a locked rack.





Related incidences:

- :ref:`bitly`

- :ref:`linode`

- :ref:`maxcdn`




Links:


- `How To Use DM-Crypt to Create an Encrypted Volume on an Ubuntu (Digital Ocean) <https://www.digitalocean.com/community/tutorials/how-to-use-dm-crypt-to-create-an-encrypted-volume-on-an-ubuntu-vps>`_



- `Duplicity, encrypting backup utility <http://duplicity.nongnu.org/>`_






.. _security-proxy:

Security proxy
==============================================================

**Servers are behind security proxy?** 

Security proxy services act as a front end for the web traffic and mitigate attacks and accelerate the site traffic.

Using a security proxy service hides the IP of your servers from the attacker, thus making denial-of-service attacks more difficult to perform. The security proxies are provided by specialized companies who maintain geographically distributed servers and a lot of bandwidth to withstand attacks. The security proxies may utilize IP reputation system and force botnet IP addresses to go through additional CAPTCHAs before allowed to connect.

The security proxies also mitigate legal threats against your hosting provider. Without public knowledge who is hosting the servers it is more difficult to take legal action against the service.







Links:


- `CloudFlare <http://cloudflare.com/>`_



- `Incapsula <https://www.incapsula.com/>`_






.. _internal-services-not-exposed:

Internal services not exposed
==============================================================

**Internal servers, services and domains cannot be discovered through public records?** 

Internal services, testing and staging servers, should not be exposed to public. The DNS records should not contain services which are not for public consumption.

Usually testing and staging servers have more people with privileged access. This increases the potential attack surface from compromised devices and accounts. If there is no specific reason why the server needs to be publicly accessible, it should be hidden behind VPN and not be visible in public DNS records. For internal services run a custom DNS server or use a non-guessable secondary domain name.

Firewall should be only a secondary layer protecting human errors. The services should be configure in a manner that they to do not bind to publicly exposed IPs, but only bind to localhost or internal IPs. If public IP addresses are needed the internal service should minimally have HTTP Basic Authentication password prompt, so that scanners and robots cannot find it.

Within the server any installed software is run under non-admin (non-root) account. This limits the impact of attack if arbitrary code execution vulnerability in the native applications is exploited. The attacker cannot leave further backdoors in the system and is able to gain only limited intel.





Related incidences:

- :ref:`patreon`




Links:


- `Nmap <https://nmap.org/>`_



- `Privledge separation (Wikipedia) <https://en.wikipedia.org/wiki/Privilege_separation>`_



- `Basic access authentication (Wikipedia) <https://en.wikipedia.org/wiki/Basic_access_authentication>`_






.. _traffic-throttle:

Traffic throttle
==============================================================

**Throttle or ban IP addresses with excessive requests?** Yes / No

Prevent denial-of-service, brute force and scraping attacks against your service by blocking clients doing excessive traffic.

Normal users and clients should be able to do only four to twenty burst HTTP requests to the service. If there is more incoming traffic and the client is not whitelisted then the client is unlikely coming with good intentions.

A log monitoring software like fail2ban can do this with almost zero configuration for stock applications like SSH and common web servers.

Please note that IP blocking alone is not effective against adversaries with botnets and thousands of global IPs in their possession.

.. note ::

    Don't accidentally ban good known bots, like GoogleBot and Bing.



Applies for: Everyone





Links:


- `NGINX - throttle requests to prevent abuse (ServerFault) <http://serverfault.com/q/179646/74975>`_



- `fail2ban <http://www.fail2ban.org/>`_



- `Banning IPv6 addresses (ServerFault) <http://serverfault.com/q/631160/74975>`_






.. _log-server:

Log server
==============================================================

**Critical logs are mirrored to a log service?** 

Critical log files should be mirrored to a destination where the logs can be only appended. The logs cannot be read back or manipulated.

The log service should have different access credentials from the administrators of normal systems. In the case the attacker gains access to the infrastructure, this prevents wiping or manipulating logs. This allows robust recovery and post-mortem from potential attacks.



Applies for: Medium and large enterprises





Links:


- `Amazon CloudWatch <https://aws.amazon.com/cloudwatch/>`_



- `Creating a Centralized Syslog Server (Linux Journal) <http://www.linuxjournal.com/content/creating-centralized-syslog-server>`_






.. _secure-server-to-server-connections:

Secure server-to-server connections
==============================================================

**Server-to-serve connections are secure?** 

Nation state actors and other capable adversaries are proven to be able to tap Internet backbone connections and data centers.

The server-to-server connections should be encrypted in a manner that anyone tapping physical cables cannot extract any information, like raw database traffic.

The connection encryption methods VPN and SSH tunnels.







Links:


- `Room 641A (Wikipedia) <https://en.wikipedia.org/wiki/Room_641A>`_



- `Googlers say “F*** you” to NSA, company encrypts internal network (Ars Technica) <http://arstechnica.com/information-technology/2013/11/googlers-say-f-you-to-nsa-company-encrypts-internal-network/>`_



- `Reports that NSA taps into Google and Yahoo data hubs infuriate tech giants (The Guardian) <http://www.theguardian.com/technology/2013/oct/30/google-reports-nsa-secretly-intercepts-data-links>`_






.. _intrusion-detection:

Intrusion detection
==============================================================

**Intrusion detection alerts on unexpected server activity?** 

Intrusion detection software monitors the servers and alerts in the case there is unexpected activity.

Intrusion detection is monitoring measure to detect server compromises. Intrusion detection software monitors processes, file system, configuration files, passwords and user database. In the case there are changes not matching the predefined ruleset an alert is fired.

Intrusion detection cannot detect in-process compromises and tailored attack payloads. Thus, it efficiency against well-versed adversaries is questionable.



Applies for: Medium and large enterprises





Links:


- `Tripwire <http://www.tripwire.com/>`_



- `OSSEC <http://www.ossec.net/>`_





