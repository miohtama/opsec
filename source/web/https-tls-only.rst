
.. This is a generated file from data/. DO NOT EDIT.

.. _https-tls-only:

HTTPS / TLS only
==============================================================

**Service is HTTPS-only with security HTTP headers?** Yes / No

The service is available only over an encrypted connection. A plain HTTP connection is allowed only for the initial redirect. Furthermore, the HTTP responses should include security headers like *HTTP Strict Transport Security*, *X-Frame-Option* and HTTPS-only cookies with no JavaScript access.

Encryption protects again man-in-the-middle attacks which include:

* Malware tapping traffic locally

* Compromised Wi-Fi routers

* Malicious Tor exit nodes

* Nationstate actors and mass surveillance

The *X-Frame-Option* HTTP response header prevents clickjacking attacks, though it is not related to transport security directly.

If the site loads resources from external content delivery networks (CDNs), these downloads should be marked with subresource integrity tags to prevent attacks through a compromised CDN provider.



Applies for: Everyone



Related incidences:

- :ref:`tor`

- :ref:`soho`

- :ref:`maxcdn`




Links:


- `Let’s Encrypt, a free, automated, and open certificate authority brought to you by the Internet Security Research Group (ISRG) <https://letsencrypt.org/>`_



- `Security/Server Side TLS (Mozilla Wiki) <https://wiki.mozilla.org/Security/Server_Side_TLS>`_



- `Clickjacking (OWASP) <https://www.owasp.org/index.php/Clickjacking>`_



- `X-Frame-Option (Mozilla Developer Network) <https://developer.mozilla.org/en-US/docs/Web/HTTP/X-Frame-Options>`_



- `Subresource Integrity (Mozilla Developer Network) <https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity>`_



- `Subresource Integrity (W3C specification) <http://w3c.github.io/webappsec/specs/subresourceintegrity/>`_



