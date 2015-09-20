
.. This is a generated file from data/. DO NOT EDIT.

===========================================
Team security
===========================================

Ensure integrity of team personal accounts and development tools.

Background
==========

The physical security, like door access keys or security cameras, is de-emphasized because these aspects might no longer reflect the reality of a mobile worker.




Password manager
==============================================================

**The team members use password manager?** 

All team members use password manager for all of their the passwords. The password manager is the only rational way to manager sensitive, strong and random passwords. If no password manager is used the cognitive load for maintaining secure passwords is too high. Without randomized passwords, a compromised third party site may lead to loss of other passwords due to password or password pattern reuse.

Applies for: Everyone





Third party devices
==============================================================

**The team members do not use third party devices for logging in?** 

If the device comes from an untrusted party, it may contain keyloggers and other malware to record the user actions. Such devices include internet kiosks and other free terminals.

Applies for: Everyone





Encrypted computers
==============================================================

**The team members have disk encryption enabled on their personal computers?** Yes / No

The disk encryption implies password login to the computer wake up. A lost device, when encrypted, cannot lead to any kind of compromises

Applies for: Everyone





Encrypted mobile devices
==============================================================

**The team members have disk encryption enabled on their mobiles and tablets. The devices are password protected?** Yes / No

A lost device, when encrypted, cannot lead to any kind of compromises. Even if the device were not to contain sensitive data it may contain an accessible email session which can be used to further account compromise and phishing.

Applies for: Everyone





Two-factor authentication on email
==============================================================

**The team member email accounts require two-factor authentication to log in?** Yes / No

Email accounts contain sensitive information and they can be used to reset the master password of services and infrastructure. Email account is also attractive target to hack in as it is public. Even if email account is protected by strong password, various flaws may exist in the password reset process, e.g. by intercepting the voice mail of the target user. Two-factor authentication provides additional protection against such attacks.

Applies for: Everyone





Two-factor authentication on critical services
==============================================================

**Administrating infrastructure services requires two-factor authentication?** Yes / No

The team relies on third party services for infrastructure: hosting, domain name, certificates, email, SMS, attack mitigation proxies, etc. If these services provide a two-factor authentication this option is used. This adds additional layer of security if the infrastructure provider becomes a target of attack and the master password can be reset e.g. through phishing.

Applies for: Everyone





Server login keys are passphrase protected
==============================================================

**The server logging in is by keys only which are passphrase protected?** Yes / No

The logging in to production or staging servers is only allowed with the key files. The key files are passphrase protected. The usual logging method is by SSH, but if alternative methods exist accessing the servers they must provide similar method. This protects against brute force attacks against devop access. Furthermore keys must be passphrase protected so in the the case keys are accidentally leaked they are not useful.

Applies for: Everyone





Server login requires two-factor authentication
==============================================================

**The server logging in requires one time token?** Yes / No

The server login is further restricted to two-factor authentication, so that even in the case the devop laptop is hijacked by malware, this laptop cannot login to the server without a token from an external device.

Applies for: Everyone





Server login keys are audited
==============================================================

**A real-time method of maintaining and revoking keys across all servers is used?** 

In any point of time, the system administrators of the company can revoke any key in the whole organization. Full audit logs of key usage is available and stored separately. This allows quickly to address issues when a key compromise is suspected.

Applies for: Medium and large enterprises





Software comes from secure sources
==============================================================

**Software installation comes from knonw good sources?** 

Pirated software is riddled with malware. The team installs software which comes from legit sources only, reducing the risk the software comes with maware.

Applies for: Everyone





Backend sensitive data access is limited
==============================================================

**Backend sensitive data access is limited?** 

If multiple people access the backend data, the access is limited in a way that the sensitive information is not exposed unless necessary for performing the work.

Applies for: Everyone





Data scrubbing is used
==============================================================

**When working with datasets, it is cleaned from sensitive information?** 

Instead of working with full datasets, there exist a documented process of making a cleaned dataset with reduced sensitive information. This cleaned dataset is given for team members who need to analyse, test and develop against the data. This also limits the impact of data dump leak in the case the data dump ends up to the hands of a third party.

Applies for: Everyone




