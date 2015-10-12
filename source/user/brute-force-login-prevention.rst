
.. This is a generated file from data/. DO NOT EDIT.

.. _brute-force-login-prevention:

Brute force login prevention
==============================================================

**Service login attempts are throttled in multiple ways?** Yes / No


Attackers may try to brute force the logins of users. The service should have adequate measures to prevent multiple login attempts and to effectively stop them.

There are a few different brute force attack modes:

  * Spearhead a brute force attack against a single high-value victim.

  * Known email and known password combination list, leaked from a third-party site or bought from the black market.

  * Known email and common password list, guessing the 1000 most-common passwords.

Attackers have been shown to possess thousands of IP addresses, so blocking individual IP addresses is not effective against a well-versed attacker.

To prevent brute force attacks, counter actions should include:

  * Prevent multiple login attempts per user: require CAPTCA verification on second login attempt; allow only one wrong password attempt per user.

  * Prevent multiple login attempts from the same IP address or network.

  * Force all users to go through CAPTCHA before login if the system global login rate is abnormally high (botnet-based attack).

Relying solely on CAPTCHA to prevent brute forcing is not recommended, as the automated CAPTCHA solving success rates are counted in the tens of percents. Thus, the malicious networks should be identified and dropped.

Beside the security ramifications, a well-armed brute force logging attacker may cause denial of service, as the system is not able to handle all the login attempts.

.. note::

  Forcing users to choose long passwords brings limited additional value. Passwords are effectively dead. It doesn't matter how complex the password is, as usually the whole password is lost due to phishing or keylogging malware. Instead, two-factor authentication should be encouraged as the primary option for increasing account security.



Applies for: Everyone



Related incidences:

- :ref:`icloud`




Links:


- `Blocking Brute Force Attacks (OWASP) <https://www.owasp.org/index.php/Blocking_Brute_Force_Attacks>`_



- `Rolling time window counters with Redis and mitigating botnet (Mikko Ohtamaa) <https://opensourcehacker.com/2014/07/09/rolling-time-window-counters-with-redis-and-mitigating-botnet-driven-login-attacks/>`_



- `reCAPTCHA <https://www.google.com/recaptcha/intro/index.html>`_



- `Password strength (Wikipedia) <https://en.wikipedia.org/wiki/Password_strength#Guidelines_for_strong_passwords>`_



