
.. This is a generated file from data/. DO NOT EDIT.

===========================================
Protecting service users
===========================================

This chapter discussed protecting the end users and guiding them to secure their accounts properly.

Background
==========


Even if the team members maintains high security standards internally, the malicious actors can go after the end users. For example, phishing operations target a group of users who are likely users of the service. If the end users give out their login credentials in the phishing attack, the attacker may damage these user, even though the integrity of the service as a whole is not compromised.

The service should take several measures to protect its users, so that even if the attacker gains access to the user email inbox or password, the harm to the user is minimized.





.. _two-factor-authentication:

Two-factor authentication
==============================================================

**The service users are encouraged to use two-factor authentication?** Yes / No

Two-factor authentication a.k.a multifactor authentication a.k.a. secure login is a method to ask one-time token from the user when logging in. The primary purpose of two-factor authentication is to protect the user against password compromise.

The end users may lose their passwords through multiple threats, like

* The user device is compromised by malware and the password is keylogged or extracted from the running password manager

* The password is reused across multiple sites and one of the sites gets compromised. You can buy stock email and password lists on the black market.

* The password are given out on a phishing site (see :ref:`trademark-protection`)

* The password is extracted through man-in-the-middle attack (see :ref:`https-tls-only`)

Two-factor authentication stops the attacker, equipped with a mere password, to access the victim's account.

Having the two-factor authentication as an option is not enough. The users should be educated about the two-factor authentication. Often users are not aware of threat models and harm they may receive because of lax security. Incentives, like reduced fees, should be applied to encourage enabling the two-factor authentication. From business perspective, this can be justified as reduced support cost of dealing with hacked account cases.

Popular two-factor authentication methods include

* Mobile apps: Time-Based One Time Password (TOTP), Google Authenticator

* Paper codes: One time pad, HOTP, popular with European banks

* SMS and other phone based methods

* Hardware devices: YubiKey, others

External services like Authy and Clef provide two-factor-as-a-service.

Google Authenticator is a popular two-factor mobile app. Despite the name says Google, you can use it on your own site. The application can be used independently from Google services, offline. Google Authenticator is based on RFC 6238. There are multiple open source implementations for all desktop and mobile operating systems.

.. note::

  SMS is not deemed secure in large scale. SMS messages are intercepted by mobile malware. SMS may travel in plain text and various parties in operator business chain can read them. Mobile number portability opens a vector for the attacker to gain access to the victims phone number. SMS may not be reliable in third world countries, thus making it not viable option for global business.



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



- `Google Authenticator Project (Github) <https://github.com/google/google-authenticator/wiki>`_



- `Authy <https://www.authy.com/>`_



- `Clef <https://getclef.com/>`_






.. _third-factor-authentication:

Third-factor authentication
==============================================================

**The login process goes through additional check in abnormal circumstances?** 

The login process should perform an additional check if there is a reason to believe the login attempt might not be genuine.

The users might not have two-factor authentication enabled. Even with two-factor authentication enabled there is a chance that the user gives out the codes on a phishing site. In these cases the service should detect abnormal conditions and perform additional checks before letting the login to proceed.

The common criteria triggering the third factor authentication include

* The country of the user IP address has changed

* The device or the web browser of the user has not been seen before, identified by a stored permacookie

In these cases the service should prompt the login to go through additional verification step. This could be

* Email confirmation

* SMS confirmation

.. note ::

  Third-factor authentication does not protect against cases where the device of the user is compromised by malware and the service cannot differentiate between legit and malicious traffic coming from the same device.





Related incidences:

- :ref:`lastpass`

- :ref:`blockchaininfo`




Links:


- `Detecting suspicious account activity (Google) <http://gmailblog.blogspot.fi/2010/03/detecting-suspicious-account-activity.html>`_



- `Introducing Login Approvals (Facebook) <https://www.facebook.com/notes/facebook-engineering/introducing-login-approvals/10150172618258920>`_






.. _re-authentication-on-sensitive-actions:

Re-authentication on sensitive actions
==============================================================

**Sensitive actions should prompt for authentication again?** Yes / No

Security sensitive actions should ask for an additional authentication attempt. Mere logging in to the service should not enable the attacker to perform sensitive actions.

The additional authentication step can be

* Give the password again

* Email confirmation

* SMS confirmation

* Give another two-factor authentication token

Sensitive actions may include e.g.

* Making withdraw from the service

* Sending money to another user

* Changing password, email or phone number

* Closing the account

Asking for an additional authentication makes it difficult to automatize malicious actions, creating another layer of protection against phishing and XSS attacks.

The sensitive operations, like where money is transferred out from the service, should require minimum of two different two-factor authentication codes: one for login and one for transfer. This makes phishing site operations, which intercept two-factor authentication codes, less robust. The users are more likely to notice bad URLs the longer they need to spend time on the phishing site. The reuse of two-factor authentication codes allows the attacker to transfer out the assets if the victim logs in to the phishing site even once.





Related incidences:

- :ref:`blockchaininfo`







.. _brute-force-login-prevention:

Brute force login prevention
==============================================================

**Service login attempts are throttled in multiple ways?** Yes / No


The attackers may try to brute force the logins of the users. The service should have adequate measures to prevent multiple login attempts and make them effectively stopped.

There are few different brute force attack modes:

  * Spearhead brute force attack against a single high value victim

  * Known email and known password combination list, leaked from a third party site or bought from black market

  * Known email and common password list, guessing 1000 most common passwords

The attackers have been shown to possess of thousands of IP addresses, so blocking individual IP addresses is not effective against well-versed attacker.

To prevent the brute force attacks the counter actions should include:

  * Prevent multiple login attempts per user: require CAPTCA verification on second login attempt - allow only one wrong password attempt per user

  * Prevent multiple login attempts from the same IP address or network

  * Force all users to go through CAPTCHA before login if the system global login rate is abnormal high (botnet-based attack)

Relying solely to CAPTCHA to prevent brute forcing is not recommended, as the automated CAPTCHA solving success rates are counted in tens of percents. Thus, the malicious networks should be identified and dropped.

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



- `Password strength (Wikipedia) <https://en.wikipedia.org/wiki/Password_strength#Guidelines_for_strong_passwords>`_






.. _effective-session-kill:

Effective session kill
==============================================================

**When the user account is deactivated or changed, the related sessions are dropped?** 

If the attacker gains access to an user account the system administrators must be able to kick out the attacker. In certain security related actions it is also good practice to drop the sessions of the user.

The account deactivation, besides marking the user account deactivated in the database records, should also drop the active sessions which are usually stored in a separate backend like Memcached or Redis. When a user account is deactivated, all communication channels to this user must be dropped: HTTP sessions, WebSocket sessions, mobile application sessions and so on.

Furthermore, all user sessions should be dropped on when the users themselves perform changes which may affect the account security. These includes

* Password change

* Email address change

* Phone number change

After the change has been performed the user must relogin to the service. This allows the users themselves to act quickly in situations where they notice that somebody has hacked into the account, e.g. via an incoming email notification. In this case the user is still probably logged in to the system with stolen credentials and user may hurry to change the password to kick the attacker out.





Related incidences:

- :ref:`slack`




Links:


- `Simultaneous Session Logons (OWASP) <https://www.owasp.org/index.php/Session_Management_Cheat_Sheet#Considerations_When_Using_Multiple_Cookies>`_






.. _user-audit-logs:

User audit logs
==============================================================

**The service retains audit logs of sensitive user actions?** 

All sensitive actions should be logged to a user specific action log.

The users may or may not be able view these log entries themselves. In the case the user reports hacked account the action log can be reviewed for swift judgement. In the case filed police report, due to an account hack, the user audit log can be handed to the officials.

The user audit log also serve in an important role to protect the service operator itself against fraud. For example, a user can make a frivolous claim their account got hacked and threats to sue the service and publish the incident unless there is (incorrecly) reimbursement. In fact the user might just transferred out assets himself / herself to a friendly third party. The user audit logs prove the correct password and authentications codes were used to initiate the transfer and shift the responsibility to the user themselves.

The user audit log should include at least:

* The user logins and login attempts

* Password change and reset operations

* Enabling and disabling two-factor authentication

* Email change operations

* All financial operations

* Timestamp with timezone

* IP address

* User agent





Related incidences:

- :ref:`steam`




Links:


- `Logging Sessions Life Cycle: Monitoring Creation: Usage, and Destruction of Session IDs (OWASP) <https://www.owasp.org/index.php/Session_Management_Cheat_Sheet#Considerations_When_Using_Multiple_Cookies>`_



- `Investigation report of the claimed security breach at LocalBitcoins <http://localbitcoins.blogspot.fi/2014/04/investigation-report-of-claimed.html>`_






.. _account-verification-process:

Account verification process
==============================================================

**The creation of bogus accounts is prevented?** Yes / No / Not applicable

In services where it is possible to spam or harass other users fake accounts are a common problem.

To keep the service clean, one should prevent the creation of fake and robot accounts. The cost of automated account creation should be  high enough that there is no financial gain to create and use the accounts for spamming. On the other hand, the account creation process should be still smooth enough that it doesn't discourage the users to signs up.

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

When the service provides ways to message or contact other users, these actions should be throttled so that one cannot flood messaging by sending a large number of useless messages.

Example actions that should be throttled include

* Sending messages to the other users

* Sending invitation emails

* Sending SMS messages

If a malicious actor is free to send infinite number of messages this can be exploited for harassment. Even if the exploit doesn't lead to direct financial gain to the attacker, the service may take a reputation hit and the brand suffers due to poor user experience.

Throttling can be done by having time window thresholds how much messages one user can send or how much messages can be send on global level. If the frequency of actions exceeds the limit what a normal person would do, the action should be disabled or the user banned.





Related incidences:

- :ref:`coinbase`




Links:


- ` <Rolling time window counters with Redis and mitigating botnet (Mikko Ohtamaa)>`_






.. _trademark-protection:

Trademark protection
==============================================================

**Is the name of the service trademarked??** 

A trademark helps to protect against advertisement phishing.

If you type the service name into Google or web browser address bar search, Google displays advertisements on the top of the actual search results. These advertisement can be bought out to create misleading phishing links, like  *www.blockchain.com.de/wallet/login*. Normal end users cannot distinct between phishing advertisements and actual search results.

If you have properly trademarked your service name, you can ask Google AdWords to not to allow it being used in the advertisements, making advertisement phishing harder.

Google AdWords is know to take down phishing advertisement quite slowly when reported.



Applies for: 



Related incidences:

- :ref:`blockchaininfo`




Links:


- `AdWord Trademark Policy <https://support.google.com/adwordspolicy/answer/6118?hl=en>`_



- `Report a phishing page (SafeBrowsing) <https://www.google.com/safebrowsing/report_phish/>`_





