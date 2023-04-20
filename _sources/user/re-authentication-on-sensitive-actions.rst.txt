
.. This is a generated file from data/. DO NOT EDIT.

.. _re-authentication-on-sensitive-actions:

Re-authentication on sensitive actions
==============================================================

**Sensitive actions should prompt for authentication again?** Yes / No


Security-sensitive actions should ask for an additional authentication attempt. Mere logging in to the service should not enable the attacker to perform sensitive actions.

The additional authentication step can be:

* Give the password again.

* Email confirmation.

* SMS confirmation.

* Give another two-factor authentication token.

Sensitive actions may include:

* Making a withdrawal from the service.

* Sending money to another user.

* Changing password, email or phone number.

* Closing the account.

Asking for an additional authentication makes it difficult to automatize malicious actions, creating another layer of protection against phishing and XSS attacks.

Sensitive operations, like those in which money is transferred out from the service, should require a minimum of two different two-factor authentication codes: one for login and one for transfer. This makes phishing site operations, which intercept two-factor authentication codes, less robust. Users are more likely to notice bad URLs the longer they need to spend time on the phishing site. The reuse of two-factor authentication codes allows the attacker to transfer out the assets if the victim logs into the phishing site even once.





Related incidences:

- :ref:`blockchaininfo`




