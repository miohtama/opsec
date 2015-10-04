
.. This is a generated file from data/. DO NOT EDIT.

.. _tor:

Tor
==============================================================

*Date: 2014-01-22*

Security researches detected Tor exit nodes performing man-in-the-middle attack on the traffic.

Tor is a layered network to obfuscate the source of the traffic i.e. hide your tracks. It is used by criminals, privacy advocates and security researchers. Tor relies on *exit nodes* where the traffic comes out from Tor network and connects to normal Internet.

Malicious Tor exit nodes where intercepting the traffic. They performed HTTP traffic snooping, HTTP -> HTTPS redirection interception and HTTPS man-in-the-middle with self-signed certificate. There are recorded cases where the victim accepted the invalid HTTPS certificate even though Firefox-based Tor browser presented a red warning screen with difficult options to proceed beyond it.



Related evaluation points:

- :ref:`https-tls-only`





Links:

- `What the "Spoiled Onions" paper means for Tor users <https://blog.torproject.org/blog/what-spoiled-onions-paper-means-tor-users>`_

- `Scientists detect “spoiled onions” trying to sabotage Tor privacy network <http://arstechnica.com/security/2014/01/scientists-detect-spoiled-onions-trying-to-sabotage-tor-privacy-network/>`_

