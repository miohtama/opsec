
.. This is a generated file from data/. DO NOT EDIT.

===========================================
Team security
===========================================

This chapter discusses how to guarantee the safety and integrity of team members, credentials, devices, tools and software.

Background
==========


Instead of trying to exploit the service directly, the adversaries may go after team members, managers and partners working on the project. The project should aim to protect team communications, devices and authorization keys so that they are unlikely to get compromised. This involves following basic IT security practices, cyberhygiene, key management and limiting the impact of potentially leaked data.

Physical security, like door access keys and security cameras, is de-emphasized because these security aspects rarely reflect the reality of a mobile contemporary worker. Regardless of the broken physical security, the service should stay intact and uncompromised.





.. _basic-security-practices:

Basic security practices
==============================================================

**Team members follow the basic IT security practices?** Yes / No

Team members are trained on and aware of common cyber threats like phishing attacks and social engineering. They can identify basic attacks, like spearhead phishing emails, and do not fall victim to them.

Team members maintain cyberhygiene and do not use work devices to visit sites which might compromise the web browser. Software, both desktop and server, is maintained in up-to-date versions in which known vulnerabilities do not exist.



Applies for: Everyone



Related incidences:

- :ref:`bitpay`







.. _dangerous-file-attachments:

Dangerous file attachments
==============================================================

**Potentially dangerous file attachments are handled securely?** Yes / No

File attachments in email and chat are one of the most common attack vectors.

Rigged files may include:

* Office files (Microsoft Word, Microsoft Excel, and related)

* Flash animations

* PDF files

Dangerous communication channels include anything on which team members can be freely contacted, including:

* Email

* Skype

* WhatsApp

The desktop applications and web browser plugins opening this kind of content should be disabled. If disabling is not an option, the attachments in an email or outside team internal communication tool should be opened securely and never using the productivity applications themselves. Secure open methods include opening the file in a web-based viewer, web email preview or otherwise sandboxed tool. Furthermore, a safe version of a desktop productivity suite, which is preferably an up-to-date open source tool, should be used.



Applies for: Everyone



Related incidences:

- :ref:`bitstamp`




Links:


- `Office Editing for Docs, Sheets & Slides (Google Chrome add-on) <https://chrome.google.com/webstore/detail/office-editing-for-docs-s/gbkeegbaiigmenfmjfclcdgdpimamgkj?hl=en>`_



- `Google Docs Viewer (Firefox add-on) <https://addons.mozilla.org/en-us/firefox/addon/google-docs-viewer-pdf-doc-/>`_



- `LibreOffice <https://www.libreoffice.org/>`_






.. _password-manager:

Password manager
==============================================================

**Team members use a password manager?** Yes / No

All team members use a password manager for their passwords. Randomization using a password manager is the only cognitively safe way to manage a lot of sensitive and strong passwords. Without randomized passwords, one compromised password may lead to the loss of other passwords due to password reuse or password pattern reuse.

Whether one can trust a third-party cloud-based service to store passwords is subject to discussion depending on the sensitivity of the project.



Applies for: Everyone



Related incidences:

- :ref:`lastpass`

- :ref:`hacking-team`




Links:


- `List of password managers (Wikipedia) <https://en.wikipedia.org/wiki/List_of_password_managers>`_



- `KeePassX <https://www.keepassx.org/>`_






.. _third-party-devices:

Third party devices
==============================================================

**Team members do not use third-party devices for logging in?** Yes / No

If a device comes from a non-trusted party, it may contain keyloggers and other malware to record the user’s actions. Such devices include Internet kiosks, school and library computers, and other free terminals.

Team members use only assigned devices for their work. Furthermore, the devices should be sourced from a reputable vendor.



Applies for: Everyone



Related incidences:

- :ref:`chinese-android`







.. _encrypted-computers:

Encrypted computers
==============================================================

**Work computers have disk encryption?** Yes / No

The permanent storage, SSD or hard disk on team members’ computers is fully encrypted.

All desktop operating systems have disk encryption technology available: FileVault (OSX), dm-crypt (Linux) or BitLocker (Windows). The usage of disk encryption implies password authentication upon computer power-on and wake-up so that powered-on devices cannot be accessed.

A lost device, when encrypted, cannot lead to any kind of compromise.



Applies for: Everyone



Related incidences:

- :ref:`nasa`




Links:


- `Use FileVault to encrypt the startup disk on your Mac (Apple) <https://support.apple.com/en-us/HT204837>`_



- `FullDiskEncryptionHowto (Ubuntu) <https://help.ubuntu.com/community/FullDiskEncryptionHowto>`_



- `BitLocker Drive Encryption Overview (Microsoft) <http://windows.microsoft.com/en-us/windows-vista/bitlocker-drive-encryption-overview>`_






.. _encrypted-mobile-devices:

Encrypted mobile devices
==============================================================

**Team members have disk encryption on their phones and tablets?** Yes / No


A lost device, when encrypted, cannot lead to any kind of compromise. Even if the device were not to contain sensitive data per se, it could contain active email inboxes and team chats, leading to further account compromise and phishing.

The device should be protected by password and a not-easily guessable pattern or easily foolable fingerprint scanner.

.. note ::

  Having any kind of online recovery option for a forgotten device password is unsafe. In the case of a forgotten password, the device should be wiped and factory reset.

.. note ::

  Remote wiping tools give almost zero protection in the case of a lost device. It's trivial to take a mobile device offline and extract data from a powered-down device.



Applies for: Everyone





Links:


- `Encrypt your data on Android (Google) <https://support.google.com/nexus/answer/2844831?hl=en>`_



- `iOS: Understanding data protection (Apple) <https://support.apple.com/en-us/HT202064>`_



- `How To Bypass Android Lock Screen (Übergizmo) <http://www.ubergizmo.com/how-to/bypass-android-lock-screen/>`_



- `iPhone 6 Touch ID Fingerprint Scanner Hacked Days After Launch <http://www.ibtimes.co.uk/iphone-6-touch-id-fingerprint-scanner-hacked-days-after-launch-1466843>`_






.. _minimized-email-usage:

Minimized email usage
==============================================================

**Email is not used for internal communications?** 

Email as media is insecure. Email travels plain-text through the Internet. Even if the message content itself is encrypted, the metadata is still readable.

Instead of email, closed tools and services should be used for team internal communications.

For highly sensitive projects, the communication should be contained in an in-house server.





Related incidences:

- :ref:`bitpay`




Links:


- `Email Privacy (Wikipedia) <https://en.wikipedia.org/wiki/Email_privacy>`_



- `Modern Team Communication Tools for Developers (Stefan Mayer) <http://stefanmayer.me/2014/08/28/slack-flowdock-hipchat-comparison/>`_






.. _two-factor-authentication-on-email:

Two-factor authentication on email
==============================================================

**Team members’ work and personal email accounts require two-factor authentication to log in.?** Yes / No

Inboxes contain sensitive information. Often email acts as the key to third-party services and infrastructure, as email is used for logging in with a forgotten password option. Thus, getting into the inbox further compromises other services.

Email is an attractive target to hack, as email is either public or easily guessable. Even if the email account is protected by a strong password, flaws may exist in the password reset process, e.g., by intercepting the voice mail of the target user. Two-factor authentication provides additional protection against such attacks.



Applies for: Everyone



Related incidences:

- :ref:`bitpay`

- :ref:`cloudflare`




Links:


- `Two-factor Authentication List <https://twofactorauth.org/>`_



- `Google 2-Step Verification <https://www.google.com/landing/2step/>`_






.. _two-factor-authentication-on-critical-services:

Two-factor authentication on critical services
==============================================================

**Infrastructure services require two-factor authentication?** Yes / No


If infrastructure services provide a two-factor authentication, this option is used.

Internet services often rely on third-party services for infrastructure. The infrastructure services could include:

* Server hosting

* Domain name services

* Certificates

* Transactional email

* SMS

* Proxy and CDN services, etc.

Two-factor authentication provides an additional layer of security against cases in which passwords of team members get compromised. It also gives protection against social engineering and password reset attacks which the attacker may try against the infrastructure service accounts.





Related incidences:

- :ref:`bitly`




Links:


- `Two-factor Authentication List <https://twofactorauth.org/>`_



- `Multi-Factor Authentication (Amazon Web Services) <https://aws.amazon.com/iam/details/mfa/>`_






.. _two-factor-authentication-for-admins:

Two-factor authentication for admins
==============================================================

**Website administrators use two-factor authentication?** Yes / No

Team members, support personnel and other people with administrative access to the website use two-factor authentication.

Internet services often provide an administrative site or access in which the site managers perform in-house updates, edits and other support tasks. This kind of administrative access should be available only through two-factor authentication.

If the attacker compromises a password of a team member, the attacker should not be able to get into the administrative site. Furthermore, administrative access can be limited to VPN or other well-known (office) IPs.

See also :ref:`two-factor-authentication`.



Applies for: Everyone





Links:


- `Two-factor Authentication List <https://twofactorauth.org/>`_






.. _passphrase-on-server-login-keys:

Passphrase on server login keys
==============================================================

**The terminal access to the server requires passphrase protected key?** Yes / No

Logging in to the server containing private data is allowed only with passphrase-protected key files.

The usual logging method is by SSH secure shell connection, but if alternative methods to access the server exist, the key files should be used there, too.

Using key files instead of passwords protects against brute force attacks, simple keylogging attacks, weak password attacks and such. Furthermore, the keys must be passphrase protected so that in case a key file itself leaks, it is useless to the attacker.

.. note ::

  If the hosting provider has a console, terminal or root password reset option on the server, special attention should be paid to this. It is better to either disable this feature or to make sure it is behind two-factor authentication and cannot be performed by hosting provider personnel.



Applies for: Everyone



Related incidences:

- :ref:`linode`

- :ref:`maxcdn`




Links:


- `SSH key and passwordless login basics for developers (Mikko Ohtamaa) <https://opensourcehacker.com/2012/10/24/ssh-key-and-passwordless-login-basics-for-developers/>`_



- `Linode Hacks (Bitcoin Thefts) <https://bitcointhefts.com/details/linode-hacks>`_






.. _two-factor-authentication-on-server-login:

Two-factor authentication on server login
==============================================================

**Terminal access to the server requires two-factor authentication?** Yes / No

Logging in to the server containing private data requires two-factor authentication.

Server login is further restricted with two-factor authentication, so that even in case the computer of a server administrator is hijacked by malware, this computer cannot log in to the server without user interaction and a two-factor token from a separate device. This makes it nearly impossible to hijack the secure connection to the server unnoticed.

See also :ref:`two-factor-authentication`.



Applies for: Everyone



Related incidences:

- :ref:`bitstamp`

- :ref:`linode`




Links:


- `SSH login with Google Authenticator TTOP two-factor <http://sam.xnet.tk/2014/09/ubuntu-2-factor-login-public-key-google-authenticator/>`_



- `Two-Factor-Authentication with SSH (Carsten Heesch) <https://sysconfig.org.uk/two-factor-authentication-with-ssh.html>`_






.. _audited-server-login-keys:

Audited server login keys
==============================================================

**A real-time method of maintaining and revoking keys across all servers?** Yes / No

In any point of time, the administrators of the project can revoke any key used by the team. Full audit logs of key provision andAt any point in time, administrators of the project can revoke any key used by the team. Full audit logs of key provision and usage are available and stored separately.

This allows for the quick address of issues when a compromise is suspected.



Applies for: Medium and large enterprises



Related incidences:

- :ref:`maxcdn`

- :ref:`ashley-madison`




Links:


- `Universal SSH Key Manager (SSH Communications Security) <http://www.ssh.com/products/universal-ssh-key-manager>`_






.. _software-installation-from-safe-sources:

Software installation from safe sources
==============================================================

**Software is installed from known good sources?** Yes / No


Pirated software is riddled with malware. Team members install software coming from legit sources only, reducing the risk that the software comes with malware.


Safe software channels include:

* App stores by operating system vendors

* Official, signed, UNIX distribution repositories

* Programming community package repositories

Basic security understanding and cyberhygiene should still be applied when installing from safe channels (e.g., Google Play is known to host several rigged applications).

Even if malware is not targeting the project itself, malware authors inspect infected computers for high-value targets and may open an attack if they notice such a successful infection.



Applies for: Everyone



Related incidences:

- :ref:`xcode`

- :ref:`squirrelmail`




Links:


- `Malware that Just Won’t Give Up on Google Play (Avast) <https://blog.avast.com/2015/07/24/malware-that-just-wont-give-up-on-google-play/>`_





- `PEP 0458 -- Surviving a Compromise of PyPI <https://www.python.org/dev/peps/pep-0458/>`_






.. _limited-sensitive-data-access:

Limited sensitive data access
==============================================================

**Sensitive data access by administrators is limited?** Yes / No / Not applicable

Administrative access often implies the ability to view users’ private data.

When team members access private data, the access is limited in a way such that sensitive information is not exposed unless necessary for performing work. For example, social security numbers are not viewable among normal data unless the administrator chooses to explicitly show them.

See also: ref:`Authorization and permission framework`.



Applies for: Everyone



Related incidences:

- :ref:`ashley-madison`

- :ref:`hacking-team`

- :ref:`patreon`







.. _logged-sensitive-data-access:

Logged sensitive data access
==============================================================

**Sensitive data access by administrators is logged?** Yes / No

All actions related to administrators’ accessing and manipulating sensitive data are logged. This includes direct database connections, API services and other internal access methods.

In case of privacy breach claims, these logs can be used to reconstruct the scenario regarding who has been accessing or manipulating the data. Sensitive data access logs protect against insider threats. Knowing that one cannot get away without being caught discourages malicious attempts.

Access logs should be detailed as possible, including timestamp and details of performed actions. Access logging can be implemented, for example, by storing the full HTTP request logs, including POST parameters and body, from all logged-in administrators.

See also :ref:`log-server` and :ref:`user-audit-logs`.



Applies for: Everyone



Related incidences:

- :ref:`ashley-madison`







.. _data-scrubbing:

Data scrubbing
==============================================================

**Data dumps are cleaned of sensitive information?** Yes / No

Instead of working with full production datasets, there exists a repeatable process of making a cleaned dataset with sensitive information removed from the data.

The data scrubbing process can reset:

* User email addresses

* Phone numbers, physical addresses and social security numbers

* Password hashes

* Two-factor tokens

The cleaned dataset is then given to the team members who need to analyse, test and develop against the data.

The cleaning process limits the impact of potential data leak in cases in which the data dump accidentally ends up at the third party. Furthermore, the cleaned data ensures that messages from the testing environment cannot reach actual users.



Applies for: Everyone



Related incidences:

- :ref:`ashley-madison`

- :ref:`patreon`




Links:


- `How to Anonymize Data in a PostgreSQL Database (Michael Krenz) <http://www.michaelkrenz.de/2012/08/05/how-to-anonymize-data-in-a-postgresql-database/>`_





