
.. This is a generated file from data/. DO NOT EDIT.

.. _no-caching-policy:

No caching policy
==============================================================

**Sensitive resources are not cached?** Yes / No

The front-end web server and web browsers cache pages and documents by default. Sensitive pages and downloads should have explicit no caching headers present.

Thread models include:

* A caching front-end web server may lead user sessions when the HTTP response with a private cookie is accidentally cached.

* The user device is compromised and sensitive information is extracted from the browser cache.

Generally, special attention should be paid to HTTP responses like:

* Generated image, audio, video and other media downloads

* Document downloads (Office files, PDF, CSV, TXT)







Links:


- `The Security Impact of HTTP Caching Headers (SANS ISC InfoSec) <https://isc.sans.edu/forums/diary/The+Security+Impact+of+HTTP+Caching+Headers/17033/>`_



