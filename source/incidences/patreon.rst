
.. This is a generated file from data/. DO NOT EDIT.

.. _patreon:

Patreon
==============================================================

*Date: 2015-09-01*

Patreon, a crowdfunding site, had their development server compromised, leading to the loss of production data and source code.

Email addresses, private messages and bcrypt-encrypted passwords of 2 million users were lost, totaling 15 gigabytes of data. The data was copied off from Amazon AWS development server. The development server contained full dataset without any scrubbed data. The development server had on-authenticated debug interface connected to the Patreon Python web application (Werkzeuk on Flash). Anyone could connect to it with full access to the system.

The credit card data was hosted on an external service, Stripe, and was not lost.

Patreon claims social security numbers and tax information was further encrypted, but does not clarify if the attacker gained the key to decrypt this information.

As the writing of this, it is not disclosed who the attackers gained access to the development server.



Related evaluation points:

- :ref:`limited-sensitive-data-access`

- :ref:`data-scrubbing`

- :ref:`non-public-administration-site`

- :ref:`internal-services-not-exposed`





Links:

- `Important Security Notice from Patreon <https://www.patreon.com/posts/important-notice-3457485>`_

- `Gigabytes of user data from hack of Patreon donations site dumped online (Ars Technica) <http://arstechnica.com/security/2015/10/gigabytes-of-user-data-from-hack-of-patreon-donations-site-dumped-online/>`_

- `How Patreon got hacked – Publicly exposed Werkzeug Debugger (Detectify Labs) <http://labs.detectify.com/post/130332638391/how-patreon-got-hacked-publicly-exposed-werkzeug>`_

