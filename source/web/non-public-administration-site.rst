
.. This is a generated file from data/. DO NOT EDIT.

.. _non-public-administration-site:

Non-public administration site
==============================================================

**The administration site is not accessible or known to the public?** Yes / No


Many common software platforms come with the default administration site in a location like */admin/*.

If administrative URLs are well known, the potential attack surface expands. The attacker can guess administration HTTP endpoints with vulnerabilities and try to exploit those.

The administration interface should be in a non-guessable, non-end-user-visible URL. Besides authorization, additional access restrictions should be placed upon the administration interface with two-factor authentication, VPN and IP restrictions  (see :doc:`Team security <../team/index>`).



Applies for: Everyone



Related incidences:

- :ref:`veeder-root`

- :ref:`patreon`




Links:


- `Failure to restrict URL Access in OWASP <https://www.owasp.org/index.php/Top_10_2010-A8-Failure_to_Restrict_URL_Access>`_



