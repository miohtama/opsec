
.. This is a generated file from data/. DO NOT EDIT.

.. _two-factor-authentication:

Two-factor authentication
==============================================================

**Service users are encouraged to use two-factor authentication?** Yes / No

Two-factor authentication, a.k.a. multifactor authentication, a.k.a. secure login, is a method to ask for a one-time token from the user when logging in. The primary purpose of two-factor authentication is to protect the user from password compromise.

End users may lose their passwords through multiple threats like:

* The user device is compromised by malware and the password is keylogged or extracted from the running password manager

* The password is reused across multiple sites and one of the sites gets compromised. You can buy stock email and password lists on the black market.

* The password is given out on a phishing site (see :ref:`trademark-protection`)

* The password is extracted through a man-in-the-middle attack (see :ref:`https-tls-only`)

Two-factor authentication stops the attacker, equipped with a mere password, from accessing the victim's account.

Having two-factor authentication as an option is not enough. Users should be educated about two-factor authentication. Often users are not aware of threat models and the harm they may face because of lax security. Incentives, like reduced fees, should be applied to encourage the enabling of the two-factor authentication. From a business perspective, this can be justified as a reduced support cost of dealing with hacked account cases.

Popular two-factor authentication methods include:

* Mobile apps: Time-Based One Time Password (TOTP), Google Authenticator

* Paper codes: One time pad, HOTP, popular with European banks

* SMS and other phone-based methods

* Hardware devices: YubiKey, others

External services like Authy and Clef provide two-factor-as-a-service.

Google Authenticator is a popular two-factor mobile app. Despite the fact that the name says Google, you can use it on your own site. The application can be used offline independently from Google services. Google Authenticator is based on RFC 6238. There are multiple open-source implementations for all desktop and mobile operating systems.

.. note::

  SMS is not deemed secure in the large scale. SMS messages are intercepted by mobile malware. SMS may travel in plain text, and various parties in the operator business chain can read them. Mobile number portability opens a vector for the attacker to gain access to the victim’s phone number. SMS may not be reliable in third-world countries, thus making it not a viable option for global business.



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



