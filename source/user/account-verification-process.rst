
.. This is a generated file from data/. DO NOT EDIT.

.. _account-verification-process:

Account verification process
==============================================================

**The creation of bogus accounts is prevented?** Yes / No / Not applicable

In services in which it is possible to spam or harass other users, fake accounts are a common problem.

To keep the service clean, one should prevent the creation of fake and robot accounts. The cost of automated account creation should be high enough that there is no financial gain to create and use accounts for spamming. On the other hand, the account creation process should still be smooth enough that it doesn't discourage users from signing up.

Account verification is also important for anti-money laundering (AML) and know-your-customer (KYC) cases in which it is imperative to know that one is dealing with the rightful holder of the financial assets.

Common account verification methods include:

* CAPTCHA

* Email verification

* Phone verification

* Browser verification by security proxy (CloudFlare, etc.)

* IP reputation system (block countries where you have no business, block Tor and VPN IPs)

* Piggybacking the authentication mechanism of a large service (Facebook, Twitter, Google OAuth)

* Government ID verification services (available as-a-service like Jumio and Trulioo)

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



