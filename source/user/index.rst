
.. This is a generated file from data/. DO NOT EDIT.

===========================================
Protecting site users
===========================================

This chapter discussed protecting the service end users and guiding them to secure their accounts properly.

Background
==========


Even if the team members and the service maintains high security standards, the malicious actors can go after the end users. For example, phishing operations target a group of users who are likely users of the service. If the service users give out their login credentials to the phisher, the phisher may damage this individual user, even though the integrity of the service as a whole is not compromised.

The service should take several measures to protect it users, so that even if the attacker gains access to the user email inbox or password, cannot cause harm to the user.





.. _two-factor-authentication:

Two-factor authentication
==============================================================

**The site users are encouraged to use two-factor authentication?** Yes / No

The site user loes their password through many channels: passwords are recycled across multiple sites (e.g. email account), passwords are too weak, password are given out through phishing emails or devices are compromised by malware. In this case, the two-factor authentication should stop the attacker with a mere password to access the user account.

Having the two-factor authentication as optional is not often enough, as the users only see the reduced usability (longer login process) and are not aware of thread models. Incentives, like reduced fees, should be used to encourage enabling the two-factor authentication. From business perspective, this can be justified as reduced support cost of dealing with hacked account cases.

Popular two-factor authentication methods include Time-Based One Time Password (TOTP, mobile apps, Google Authenticator), One time pad (HOTP, paper codes, used by many European banks), SMS and hardware devices (like YubiKey).

External services like Authy and Clef provide two-factor-as-a-service.

Google Authenticator is a popular open mobile two-factor app. Despite the name says Google, you can use it on your own site, the application can be used independently of Google services, offline, the RFC is open and there are multiple open source implementations.

.. note::

  SMS is not deemed secure in large scale. SMS messages are intercepted by mobile malware. SMS may travel in plain text and various parties in operator business can read them. Mobile number portability opens a vector for the attacker to gain access to the victims phone number. SMS may not be reliable in third world countries, thus making it not viable option for global business.



Applies for: Everyone



Related incidences:

- :ref:`icloud`

- :ref:`slack`

- :ref:`sms-malware`




Links:


- `HMAC-based One-time Password Algorithm (Wikipedia) <https://en.wikipedia.org/wiki/HMAC-based_One-time_Password_Algorithm>`_



- `Time-based One-time Password Algorithm (Wikipedia) <https://en.wikipedia.org/wiki/Time-based_One-time_Password_Algorithm>`_



- `Two-factor Authentication List <https://twofactorauth.org/>`_



- `$45k stolen in phone porting scam (SC Magazine) <http://www.itnews.com.au/news/45k-stolen-in-phone-porting-scam-282310/page0>`_



- `What is YubiKey? <https://www.yubico.com/faq/yubikey/>`_



- `Google Authenticator (Wikipedia) <https://en.wikipedia.org/wiki/Google_Authenticator>`_



- `Authy <https://www.authy.com/>`_



- `Clef <https://getclef.com/>`_






.. _third-factor-authentication:

Third-factor authentication
==============================================================

**The user login goes through additional check in abnormal circumstanses?** 

The users might not have two-factor authentication enabled. Even with the two-factor authentication there is a chance that the tokens are compromised through a phishing site. In these cases the service should detect abnormal conditions and perform additional checks before letting the login to proceed.

The common third factor authentication criteria include
* Country of the IP
* New device or browser by stored permacookie

In these cases the service should prompt the login to go through additional verification step. This could be

* Email confirmation
* SMS confirmation

.. note ::

  Third-factor authentication does not protect against cases where the device of the user is compromised by malware and the service cannot differetiate between the legit and the malicious traffic coming from the same device.





Related incidences:

- :ref:`lastpass`

- :ref:`blockchaininfo`




Links:


- `Detecting suspicious account activity (Google) <http://gmailblog.blogspot.fi/2010/03/detecting-suspicious-account-activity.html>`_



- `Introducing Login Approvals (Facebook) <https://www.facebook.com/notes/facebook-engineering/introducing-login-approvals/10150172618258920>`_






.. _re-authentication-on-sensitive-actions:

Re-authentication on sensitive actions
==============================================================

**Security sensitive actions should prompt for authentication?** Yes / No

Security sensitive actions should ask the user perform additional authentication besides loggging in to the system.

The additional authetication could be

* Give the password again

* Email confirmation

* Give another two-factor authentication token

Security sensitive actions include e.g.

* Making withdraw from the service

* Sending money to another user

* Changing password, email or phone number

* Closing the account

Asking the additional authentication gives another layer of protection against phishing and XSS attacks.

The most sensitive operations, like where money is transferred out from the system, should require minimum of two different two-factor tokens: one for login and one for transfer. This makes two-factor intercepting phishing site operation less robust, as the users are more likely notice bad URLs if they need to spend more time on the phishing site. With only one authentication token the phishing site can do transfer out on the second the user hits the login, making phishing more likely to success.










.. _brute-force-login-prevention:

Brute force login prevention
==============================================================

**Site login attemps are throttled in multiple ways?** Yes / No

The attackers try to brute force the logins of the users. The site should take adequate measures that so that multiple login attempts are effectively stopped.

There are few different password brute force attack modes:

  * Spearhead bruteforcing targetting a single user

  * Email and password combination guessing from a third party site leak or blackmarket

  * Email and common password list guessing, like 1000 most common passwords

  * Scraping the site for user account names and then combining them with above

The attacker may be in possession of thousands of IP addresses.

The counter actions should include:

  * CAPTCA on second login (allow one wrong password attempt per user)

  * Prevent login attempts per IP (fail2ban)

  * Prevent login attempts per username (spearhead attack)

  * Force all users to go through CAPTCHA before login if the system global login rate is abnormal high (botnet-based attack)

Relying solely to CAPTCHA to prevent brute forcing is not recommended, as the automated CAPTCHA solving success rates are counted in tens of percents.

Beside the security ramifications, well-armed brute force logging attacker may cause denial of service, as the system is not able to handle all the login attempts.

.. note::

  Forcing the users to choose long passwords brings limited additional value. Passwords are effectively dead. It doesn't matter how complex the password is, as usually the whole password is lost due to phishing or keylogging malware. Instead, two-factor authentication should be encouraged as the primary option to increase the account security.



Applies for: Everyone



Related incidences:

- :ref:`icloud`




Links:


- `Blocking Brute Force Attacks (OWASP) <https://www.owasp.org/index.php/Blocking_Brute_Force_Attacks>`_



- `Rolling time window counters with Redis and mitigating botnet (Mikko Ohtamaa) <https://opensourcehacker.com/2014/07/09/rolling-time-window-counters-with-redis-and-mitigating-botnet-driven-login-attacks/>`_



- `reCAPTCHA <https://www.google.com/recaptcha/intro/index.html>`_






.. _effective-session-kill:

Effective session kill
==============================================================

**When the user account is deactivated, all related sessions are killed?** 

If the attacker gains access to an user account the system administrators must be able to kick out the attacker. The account deactivation may only affect the database records of the account, not dropping the active HTTP sessions which are stored in a separate store. When an user account is deactivated, all communication channels to this user must be dropped.

All user sessions should be dropped on

* Account delete

* Password change

* Email change

* Third factor authentication





Related incidences:

- :ref:`slack`




Links:


- `Simultaneous Session Logons (OWASP) <https://www.owasp.org/index.php/Session_Management_Cheat_Sheet#Considerations_When_Using_Multiple_Cookies>`_






.. _user-audit-logs:

User audit logs
==============================================================

**The service keeps audit logs of sensitive user actions?** 

All sensitive actions of the users should be logged to a user specific action list. In the case case of a crime, the user audit log may be handed to the officials. The user itself may or may not review his past actions based on this list.

The list is also important to protect the service operator itself against fraud. For example. the user can arrange stealing of the user account. The thief transfers the assets of the user to the friendly party of theirs. Then the user can blackmail and threat to sue the service unless the user is (incorrecly) reimbursed. The user audit logs prove  the correct password and authentications codes were used to initiate the transfer and shift the resposibility to the users themselves.

The log should include at least:

* The user logins and login attempts

* Password change and reset operations

* Enabling and disabling two-factor authentication

* Email change operations

* All financial operations

* Timestamp with timezone

* IP address

* User agent


Furthermore the user audit logs can be used to recover the system in the case of flaw leading to a mass account compromise.





Related incidences:

- :ref:`steam`




Links:


- `Logging Sessions Life Cycle: Monitoring Creation: Usage, and Destruction of Session IDs (OWASP) <https://www.owasp.org/index.php/Session_Management_Cheat_Sheet#Considerations_When_Using_Multiple_Cookies>`_



- `Investigation report of the claimed security breach at LocalBitcoins <http://localbitcoins.blogspot.fi/2014/04/investigation-report-of-claimed.html>`_






.. _account-verification-process:

Account verification process
==============================================================

**The creation of bogus accounts is prevented?** Yes / No / Not applicable

This only applies for services where users can interact with other users or the world e.g. spam and harrash them.

To keep the system clean, one should prevent the creation of fake and robot accounts. The cost of automatic account creation should be so high that there is no financial gain to use the account for automated harrashment. The account creation proces should be still easy enough not to discourage the users to sign up.

The account verification is also important for anti-money laundering (AML) and know-your-customer (KYC) cases where it is imperative to know one is dealing with the rightful holder of the financial assets.

The common account verification methods include:

* CAPTCHA

* Email verification

* Phone verification

* Browser verification by security proxy (CloudFlare, etc.)

* IP reputation system (block countries where you have no business, block Tor and VPN IPs)

* Piggybacking the authentication mechanism of a large service (Facebook, Twitter, Google OAuth)

* Government id verification services (available as-a-service like Jumio and Trulioo)

Please note that all of these can be defeated if the financial incentive of the attacker is high enough.





Related incidences:

- :ref:`instagram`




Links:


- `reCAPTCHA <https://www.google.com/recaptcha/intro/index.html>`_



- `Dialing Back Abuse on Phone Verified Accounts <http://static.googleusercontent.com/media/research.google.com/en/us/pubs/archive/43134.pdf>`_



- `Trafficking Fraudulent Accounts: The Role of the Underground Market in Twitter Spam and Abuse <http://www.icir.org/vern/papers/twitter-acct-purch.usesec13.pdf>`_



- `Priceless: The Role of Payments in Abuse-advertised Goods <http://www.icir.org/vern/papers/twitter-acct-purch.usesec13.pdf>`_



- `Facebook Asks Every User For A Verified Phone Number To Prevent Security Disaster (TechCrunch) <http://techcrunch.com/2012/06/14/facebook-security-tips/>`_



- `Facebook Requesting Government ID to Unlock Accounts (TheBlaze) <http://www.theblaze.com/stories/2013/10/29/absurd-facebook-requesting-government-id-to-unlock-accounts-again/>`_



- `Jumio <https://www.jumio.com/>`_



- `Trulioo <https://www.trulioo.com/>`_






.. _flood-action-throttle:

Flood action throttle
==============================================================

**Actions sending messages to other users are throttled?** Yes / No

When the service provides actions to message or contact other users or users outside the service, these actions should be throttled so that flood attack is not possible.

Example actions include

* Sending messages to the other users

* Sending invitation emails

If a malicious actor is free to send infinite number of messages, this can be used to harrass people. Even if direct financial damage is not possible, the service takes a reputation hit and the brand suffers.

Actions sending outgoing messages or signals should be throttled, so that a malicious actor cannot flood the system. If the threshold of the actions in a time window exceeds the limit what a normal person would do, the action should be disabled or the user banned.





Related incidences:

- :ref:`coinbase`






