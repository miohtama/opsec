
.. This is a generated file from data/. DO NOT EDIT.

===========================================
Team security
===========================================

Ensure the integrity of team personal accounts and devices. This chapter discusses how to protect team interperson communications, devices and authorization keys so that they are unlikely to be compromised. This involves key management best practices, cyberhygiene and limiting the scope of the data in a potential leak.

Background
==========

The physical security, like door access keys or security cameras, is de-emphasized because these security aspects rarely longer reflect the reality of a mobile contemporary worker. Regardless of the broken physical security, the service should stay intact and uncompromised.




.. _basic-security-practices:

Basic security practices
==============================================================

**The team members are trained and follow the basic security practices?** Yes / No

The team members are trained and aware of common cyber threads like phishing attacks, social engineering. They can identify the basic attacks, like spearhead phishing emails, and do not fall victim to those. The team members maintain cyber hygiene and do not use working devices to visit sites which might compromise the web browser. Software, both desktop and server software, is maintained in up-to-date versions where know vulnerabilities do not exist.



Applies for: Everyone



Related incidences:

- :ref:`bitstamp`







.. _unsafe-file-attachments:

Unsafe file attachments
==============================================================

**Potentially dangerous file attachments are handled securely?** Yes / No

File attachments in email and chat are one of the most common attack vectors. is The desktop applications opening likely rigged payloads, like office suite files, PDFs and Flash animations are disabled or the team members do not use them to view the files. Instead, the suspicious attachments, especially ones coming outside the security barrier, are opened in a web browser based viewer or similarly sandboxed tool.


Applies for: Everyone



Related incidences:

- :ref:`bitstamp`







.. _password-manager:

Password manager
==============================================================

**The team members use password manager?** Yes / No

All team members use password manager for their passwords. The password manager is the only cognitive sane way to manage a lot of sensitive, strong and random passwords. Without randomized passwords, a compromised third party site may lead to loss of other passwords due to password reuse or password pattern reuse.
Whether one can trust third party service to store password is a subject to discussion depending on the sensitivity of the project.


Applies for: Everyone



Related incidences:

- :ref:`lastpass`

- :ref:`hacking-team`




Links:


- `KeePassX <https://www.keepassx.org/>`_






.. _third-party-devices:

Third party devices
==============================================================

**The team members do not use third party devices for logging in?** Yes / No

If the device comes from an untrusted party, it may contain keyloggers and other malware to record the user actions. Such devices include internet kiosks and other free terminals. The team members use only their own working devices for the work.


Applies for: Everyone



Related incidences:

- :ref:`chinese-android`







.. _encrypted-computers:

Encrypted computers
==============================================================

**The team members have disk encryption enabled on their personal computers?** Yes / No

The permanent storage, SSD or hard disk, on the team laptops and desktop computers is encrypted.

This implies the usage of disk encryption technology like FileVault (OSX), dm-crypt (Linux) or BitLocker (Windows).

A lost device, when encrypted, cannot lead to any kind of compromises as password is always required to unlock the device. Even if the device wakes up from hibernation.



Applies for: Everyone



Related incidences:

- :ref:`nasa`







.. _encrypted-mobile-devices:

Encrypted mobile devices
==============================================================

**The team members have disk encryption enabled on their mobiles and tablets. The devices are password protected?** Yes / No


A lost device, when encrypted, cannot lead to any kind of compromises. Even if the device were not to contain sensitive data it could contain active email inboxes and team chats leading to further account compromise and phishing.



Applies for: Everyone





Links:


- `Encrypt your data on Android (Google) <https://support.google.com/nexus/answer/2844831?hl=en>`_



- `iOS: Understanding data protection (Apple) <https://support.apple.com/en-us/HT202064>`_






.. _two-factor-authentication-on-email:

Two-factor authentication on email
==============================================================

**The team member email accounts require two-factor authentication to log in?** Yes / No

Email accounts contain sensitive information and they can be used to reset the master password of services and infrastructure. Email account is also attractive target to hack in as they are either public or easily guessable. Even if email account is protected by strong password, flaws may exist in the password reset process, e.g. by intercepting the voice mail of the target user. Two-factor authentication provides additional protection against such attacks.


Applies for: Everyone



Related incidences:

- :ref:`cloudflare`




Links:


- `Two-factor Authentication List <https://twofactorauth.org/>`_



- `Google 2-Step Verification <https://www.google.com/landing/2step/>`_






.. _two-factor-authentication-on-critical-services:

Two-factor authentication on critical services
==============================================================

**Administrating infrastructure services requires two-factor authentication?** Yes / No

The team relies on third party services for infrastructure: hosting, domain name, certificates, email, SMS, attack mitigation proxies, etc. If these services provide a two-factor authentication this option is used. This adds additional layer of security if the infrastructure provider becomes a target of attack and the master password can be reset e.g. through phishing.


Applies for: Everyone



Related incidences:

- :ref:`bitly`

- :ref:`icloud`




Links:


- `Two-factor Authentication List <https://twofactorauth.org/>`_






.. _two-factor-authentication-on-the-administrative-site:

Two-factor authentication on the administrative site
==============================================================

**The administrative part of the website requires two-factor authentication?** Yes / No

Usually the Internet services provide an administrative site or a backend site where the site managers and support personell can perform in-house tasks. If the attackers compromise the passwords of the team members they should not be able to get in to the administrative site just with the password. Instead, a two-factor authentication token is required for the site admins to log in. Furthermore the administrative address can be limited to VPN or other well-known (office) IPs.


Applies for: Everyone





Links:


- `Two-factor Authentication List <https://twofactorauth.org/>`_






.. _passphrase-on-server-login-keys:

Passphrase on server login keys
==============================================================

**The server logging in is by keys only which are passphrase protected?** Yes / No

The logging in to production or staging servers is only allowed with the key files. The key files are passphrase protected. The usual logging method is by SSH, but if alternative methods exist accessing the servers they must provide similar method. This protects against brute force attacks against devop access. Furthermore keys must be passphrase protected so in the the case keys are accidentally leaked they are not useful.


Applies for: Everyone





Links:


- `SSH key and passwordless login basics for developers (Mikko Ohtamaa) <https://opensourcehacker.com/2012/10/24/ssh-key-and-passwordless-login-basics-for-developers/>`_






.. _two-factor-authentication-on-server-login:

Two-factor authentication on server login
==============================================================

**The server logging in requires one time token?** Yes / No

The server login is further restricted to two-factor authentication, so that even in the case the devop laptop is hijacked by malware, this laptop cannot login to the server without a token from an external device.


Applies for: Everyone



Related incidences:

- :ref:`bitstamp`




Links:


- `SSH login with Google Authenticator TTOP two-factor <http://sam.xnet.tk/2014/09/ubuntu-2-factor-login-public-key-google-authenticator/>`_






.. _audited-server-login-keys:

Audited server login keys
==============================================================

**A real-time method of maintaining and revoking keys across all servers is used?** Yes / No

In any point of time, the system administrators of the company can revoke any key in the whole organization. Full audit logs of key usage is available and stored separately. This allows quickly to address issues when a key compromise is suspected.


Applies for: Medium and large enterprises








.. _software-comes-from-secure-sources:

Software comes from secure sources
==============================================================

**Software installation comes from knonw good sources?** Yes / No

Pirated software is riddled with malware. The team installs software which comes from legit sources only, reducing the risk the software comes with maware.


Applies for: Everyone



Related incidences:

- :ref:`xcode`







.. _sensitive-data-access-limitations:

Sensitive data access limitations
==============================================================

**Backend sensitive data access is limited?** Yes / No / Not applicable

If multiple people access the backend data, the access is limited in a way that the sensitive information is not exposed unless necessary for performing the work.


Applies for: Everyone



Related incidences:

- :ref:`ashley-madison`

- :ref:`hacking-team`







.. _sensitive-data-access-logs:

Sensitive data access logs
==============================================================

**Backend sensitive data access is logged?** Yes / No / Not applicable

All actions of team and support persons accessing and manipulating sensitive data are logged. In the case of privacy breach claims these logs can be used to reconstruct the scenario who have been accessing the data.
See also :ref:`log-server`.


Applies for: Everyone



Related incidences:

- :ref:`ashley-madison`







.. _data-scrubbing:

Data scrubbing
==============================================================

**When working with datasets, it is cleaned from sensitive information?** Yes / No

Instead of working with full datasets, there exist a repeatable process of making a cleaned dataset with reduced sensitive information from the production data. This cleaned dataset is given for the team members who need to analyse, test and develop against the data. This limits the impact of data dump leak in the case the data dump ends up to the hands of an unknown party.


Applies for: Everyone



Related incidences:

- :ref:`ashley-madison`






