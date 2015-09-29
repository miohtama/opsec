
.. This is a generated file from data/. DO NOT EDIT.

===========================================
Web security
===========================================



Background
==========

Ultimately any Internet facing service must accept user input over the Internet. If the application is not written following the best practices, it's trivial to conduct an attack exploiting the application vulnerabilities.
This section does not discuss the web application vulnerabilities and mitigating them in detail. Instead, the team should use proper well-known secure framework in their application development, as usually the framework authors are well-versed in security matters and have thought out and documented the proper security matters.




.. _https-tls-only:

HTTPS / TLS only
==============================================================

**The service is HTTPS only with security HTTP headers?** Yes / No

The service offers traffic only over encrypted channels. Any sensitive service has no excuse not to to use full encryption anymore. It is well known that powerful actors tap and modify Internet traffic globally. Furthermore, the HTTP response headers should include security headers, like  HTTP Strict Transport Security and X-Frame-Option which mitigate the man-in-the-middle attack risk in the case the user's network is compromised.


Applies for: Everyone



Related incidences:

- :ref:`tor`

- :ref:`soho`




Links:


- `Let’s Encrypt, a free, automated, and open certificate authority brought to you by the Internet Security Research Group (ISRG) <https://letsencrypt.org/>`_



- `Security/Server Side TLS in Mozilla Wiki <https://wiki.mozilla.org/Security/Server_Side_TLS>`_



- `X-Frame-Option on MDN <https://developer.mozilla.org/en-US/docs/Web/HTTP/X-Frame-Options>`_






.. _database-injection:

Database injection
==============================================================

**The software is written in a manner that there is no possibility of database injection attack?** Yes / No

One of the most common web application vulnerabilities is a database injection attack. In the most cases, the database is SQL based, providing opportunity for SQL injections. This can be easily prevented by never constructing database statements by hand and always using a framework to construct the queries, so that all values are properly escaped. The manual SQL manipulation should be prevented from the application developers, so that no room is left for a human error.


Applies for: Everyone



Related incidences:

- :ref:`sebastian`




Links:


- `SQL injection in Wikipedia <https://en.wikipedia.org/wiki/SQL_injection>`_



- `SQL injection in OWASP <https://www.owasp.org/index.php/SQL_Injection>`_



- `PCI DSS v3.1 requirement 6.5.1 <https://www.pcisecuritystandards.org/documents/PCI_DSS_v3-1.pdf>`_



- `SQL injection hall of shame <http://codecurmudgeon.com/wp/sql-injection-hall-of-shame/>`_






.. _cross-site-scripting-xss:

Cross-site scripting (XSS)
==============================================================

**The software is written in a manner that there is no possibility of cross-site scripting attack?** Yes / No

Cross-site scripting attack is a way to perform actions on the behalf of the user when the user views or clicks a compromised payload. The attack target can be the site visitor or the site administrator. The usual cross-site scripting attack is posting text or file attachment which payload is not well-escaped HTML. This attack can be avoided by using a proper software development framework which always escapes variables in output and not relying the developers to manually escape variables in page templates, JavaScript or HTML JSON embeds.


Applies for: Everyone



Related incidences:

- :ref:`facebook`




Links:


- `Cross site scripting (Wikipedia) <https://en.wikipedia.org/wiki/Cross-site_scripting>`_



- `Cross site scripting (OWASP) <https://www.owasp.org/index.php/Cross-site_Scripting_%28XSS%29>`_



- `Handling untrusted JSON safely (WhiteHat Security) <https://blog.whitehatsec.com/handling-untrusted-json-safely/>`_






.. _cross-site-request-forgery-csrf:

Cross-site request forgery (CSRF)
==============================================================

**The software is written in a manner that there is no possibility of cross-site request forgery attack?** 

Cross-site request forgery is an attack where a JavaScript payload hosted on a third party site performs attack on the behalf on the user on the targeted website.
The software should be written using a framework which prevents HTTP POST submissions without CSRF token. Any state changing action (login, create, modify, delete) should not be GET request.




Related incidences:

- :ref:`twitter`




Links:


- `Cross-site request forgery (Wikipedia) <https://en.wikipedia.org/wiki/Cross-site_request_forgery>`_






.. _password-storage-best-practices:

Password storage best practices
==============================================================

**The user passwords and two-factor seeds are hashed and salted so that bruteforcing them is not viable.?** Yes / No

This protects the user password integrity in the case the database is compromised. The developers should not do password management themselves, but use a specialized library to do the password hashing and salting for persistent storage.


Applies for: Everyone



Related incidences:

- :ref:`sebastian`

- :ref:`slack`

- :ref:`lastpass`

- :ref:`hacking-team`




Links:


- `PBKDF2 (Password-Based Key Derivation Function 2) in Wikipedia <https://en.wikipedia.org/wiki/PBKDF2>`_



- `Password storage cheat sheet in OWASP <https://www.owasp.org/index.php/Password_Storage_Cheat_Sheet>`_






.. _authorization-and-permission-framework:

Authorization and permission framework
==============================================================

**Private pages and data access is protected by authorization framework?** Yes / No

When protecting the private data a systematic authorization framework us used instead of ad-hoc conditions.
In †he systematic approach
* The same methods are used in the all permission checks
* Manual conditions (ifs) are unnecessary to make permission checks as the approach is human error prone
* All data is preferably private unless explicitly made public




Related incidences:

- :ref:`purse`




Links:


- `Role-based access control (Wikipedia) <https://en.wikipedia.org/wiki/Role-based_access_control>`_



- `Permissions and Authorization (Django) <https://docs.djangoproject.com/en/1.8/topics/auth/default/#topic-authorization>`_



- `Pundit, Minimal authorization object-oriented design for Ruby on Rails <https://github.com/elabs/pundit>`_








.. _no-caching-policy:

No caching policy
==============================================================

**Sensitive resources are not cached?** Yes / No

Front end web server and web browsers caches pages and documents by default. Sensitive pages and downloads should have explicit no caching headers present.
Thread models include
* A caching front end web server may also result session leakage when HTTP response with a private cookie is accidentally cached
* The device of the user is compromised and sensitive information is exctracted from the browser cache






Links:


- `The Security Impact of HTTP Caching Headers (SANS ISC InfoSec) <https://isc.sans.edu/forums/diary/The+Security+Impact+of+HTTP+Caching+Headers/17033/>`_






.. _non-guessable-ids:

Non-guessable ids
==============================================================

**Publicly exposed ids are not guessable?** Yes / No

If the service uses running counters as database primary keys, these ids should not be exposed to the public.

Knowing the id sequence allows the attacker to gain knowledge of the item count. If HTTP endpoints or pages lack proper permission checks, guessing the id sequence allows the attacker to scrape private data.

It is recommended to use known good ID generation method, like Universally unique identifier (UUID) version 4 "random" which provide 122 truly random bits to prevent guessing.



Applies for: Everyone



Related incidences:

- :ref:`purse`




Links:


- `UUID (Wikipedia) <https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_.28random.29>`_



- `URL safe UUIDs in the smallest number of characters (StackOverlow) <http://stackoverflow.com/q/11431886/315168>`_






.. _non-public-administration-site:

Non-public administration site
==============================================================

**The administration site is not easily accessible to public?** Yes / No

Many common software platforms come with the default administration site in a location like */admin/*. If the administrative URLs are well-known the attacker can exploit this and guess weak administration interface HTTP endpoints to exploit those. The administration interface should be in non-guessable, non-end user visible, URL. Furthermore the additional access restrictions can be placed with two-factor authentication, VPN and IP restrictions (see :doc:`Team security <../team/index>`).


Applies for: Everyone



Related incidences:

- :ref:`veeder-root`




Links:


- `Failure to restrict URL Access in OWASP <https://www.owasp.org/index.php/Top_10_2010-A8-Failure_to_Restrict_URL_Access>`_






.. _whitehat-program:

Whitehat program
==============================================================

**The service has a public whitehat or security bounty program?** Yes / No

A whitehat program, also known as a security bountry program, is a published guide how the service deals with the security researchers. The purpose of a whitehat program is to encourage legit security research to cover issues on the service and credit third parties for doing this work.
The third party security researches usually scan the service using a web security audit tools like Burp Suite and try to discover XSS, CSRF, database injection and authorization flaws.
The whitehat program usually includes
* How to contact the service when reporting a security issues
* What response time one should expect
* Security issues types eglible to bounty
* What is the amount of bounty and how it is paid
* Crediting the researcher for uncovering the issue
There exist third party services providing the creation and management of whitehat programs (Cobalt, HackerOne).


Applies for: Medium and large enterprises



Related incidences:

- :ref:`coinbase`




Links:


- `Cobalt <https://cobalt.io/>`_



- `HackerOne <https://hackerone.com/>`_



- `Burp <https://portswigger.net/burp/>`_





