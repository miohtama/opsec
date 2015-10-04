
.. This is a generated file from data/. DO NOT EDIT.

.. _cloudflare:

CloudFlare
==============================================================

*Date: 2012-06-04*

Matthew Prince, the CEO of CloudFlare, a security proxy service company, had his personal Google email account hacked. The account was protected by two-factor authentication.

Google offers two-factor authentication on their web based email a.k.a. GMail. Two-factor authentication should protect against cases where the attacked somehow gains access to the password. In this case, the two-factor authentication is believed to be reset through social engineering AT&T customer support. Prince’s voicemail message was modified by the attacker in order to receive and record an automated phone call from Google with a audible code that could be used to reset his account.

The personal email account of Prince was the recovery email for Google Apps for Business. After gaining the access to Apps, the attacker could read some transaction email traffic, including password reset emails, which was BCC'ed to CloudFlare team. BCC feature was mostly for error diagnostics. The attacker performed password reset on 4Chan.org account, grabbed the password reset email, logged in to 4Chan account and then was able to redirect all 4Chan.org traffic to a page under the control of the attacker.



Related evaluation points:

- :ref:`two-factor-authentication-on-email`





Links:

- `The Four Critical Security Flaws that Resulted in Last Friday's Hack (CloudFlare) <https://blog.cloudflare.com/the-four-critical-security-flaws-that-resulte/>`_

- `Google Two-Factor Authentication Flaw Exposed Google Apps Customers (SecurityWeek) <http://www.securityweek.com/exclusive-google-two-factor-authentication-flaw-exposed-google-apps-customers>`_

