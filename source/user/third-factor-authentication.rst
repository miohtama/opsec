
.. This is a generated file from data/. DO NOT EDIT.

.. _third-factor-authentication:

Third-factor authentication
==============================================================

**The login process goes through an additional check in abnormal circumstances?** 


The login process should perform an additional check if there is a reason to believe that the login attempt might not be genuine.

The users might not have two-factor authentication enabled. Even with two-factor authentication enabled, there is a chance that the user will give out the codes on a phishing site. In these cases, the service should detect abnormal conditions and perform additional checks before letting the login proceed.

The common criteria triggering third-factor authentication include:

* The country of the user’s IP address has changed.

* The device or the web browser of the user has not been seen before, identified by a stored permacookie.

In these cases, the service should prompt the login to go through additional verification steps. This could be:

* Email confirmation

* SMS confirmation

.. note ::

  Third-factor authentication does not protect against cases in which the device of the user is compromised by malware and the service cannot differentiate between legit and malicious traffic coming from the same device.





Related incidences:

- :ref:`lastpass`

- :ref:`blockchaininfo`




Links:


- `Detecting suspicious account activity (Google) <http://gmailblog.blogspot.fi/2010/03/detecting-suspicious-account-activity.html>`_



- `Introducing Login Approvals (Facebook) <https://www.facebook.com/notes/facebook-engineering/introducing-login-approvals/10150172618258920>`_



