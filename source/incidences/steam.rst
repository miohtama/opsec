
.. This is a generated file from data/. DO NOT EDIT.

.. _steam:

Steam
==============================================================

*Date: 2015-07-25*

A flaw in password reset procedure allowed login to any Steam account without two-factor authentication.

A bug in Steam, a popular gaming platform and store by Valve, allowed to reset the password of the user without entering the verification token send to the email. User accounts with two-factor authentication enabled were protected.

One could submit empty ("") verification code and it passed as valid.

Valve forced the users with suspected malicious password reset to go through additional password reset procedure.



Related evaluation points:

- :ref:`user-audit-logs`





Links:

- `Steam accounts hacked during security lapse "bug" (TrustedReviews) <http://www.trustedreviews.com/news/steam-accounts-hacked-during-security-lapse-bug#Jih1G6ugCR2SeEOV.99>`_

- `Valve patches huge password reset hole that allowed anyone to hijack Steam accounts (ComputerWorld) <http://www.computerworld.com/article/2953016/cybercrime-hacking/valve-patches-huge-password-reset-hole-that-allowed-anyone-to-hijack-steam-accounts.html>`_

