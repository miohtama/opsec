
.. This is a generated file from data/. DO NOT EDIT.

===========================================
Web development practices
===========================================

This chapter discusses the need for web development best practices when creating sensitive Internet services.

Background
==========

When developing a sensitive Internet service, special attention should be paid to the security. It is very possible to build unhackable services. Accomplishing this requires discipline and security awareness from the development team.

Most application-level vulnerabilities are related to the input handling. Any Internet facing service accepts incoming traffic and user input, both good and bad. It's a social contract: when you plug in your service to the Internet, you acknowledge that anyone in the world is allowed to use the service.

HTTP and HTML were built during an era with fewer threat models and less of a need for security. Many security features are retrofitted or they are hacked on top of the original HTML. Anyone who is not an expert in HTTP, HTML and JavaScript has a lot to learn about potential attack modes. Thus, it is an imperative that the development team uses a proper *software development framework* to build the service. Usually framework authors are well-versed in security matters and have thought out and documented the proper processes for things like form submission handling, file uploads and exposing the database to the world.





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






.. _database-injection:

Database injection
==============================================================

**Software uses a framework for database queries?** Yes / No

One of the most common web application vulnerabilities is a database injection attack. Developers are allowed to write queries by hand without properly sanitizing input going into the queries.

In most cases, the database is SQL based, providing an opportunity for SQL injections. This can be easily prevented by never constructing database statements by hand and by always using a framework to construct the queries so that all values are properly escaped. Manual SQL manipulation should be prevented by the application developers so that no room is left for human error.



Applies for: Everyone



Related incidences:

- :ref:`sebastian`




Links:


- `SQL injection in Wikipedia <https://en.wikipedia.org/wiki/SQL_injection>`_



- `SQL injection in OWASP <https://www.owasp.org/index.php/SQL_Injection>`_



- `PCI DSS v3.1 requirement 6.5.1 <https://www.pcisecuritystandards.org/documents/PCI_DSS_v3-1.pdf>`_



- `SQL injection hall of shame <http://codecurmudgeon.com/wp/sql-injection-hall-of-shame/>`_



- `Exploits of Mom (XKCD) <https://xkcd.com/327/>`_






.. _cross-site-scripting-xss:

Cross-site scripting (XSS)
==============================================================

**Software is written in a manner such that there is no possibility of a cross-site scripting attack?** Yes / No

A cross-site scripting attack is a way to perform actions on behalf of the user when the user views or clicks a compromised payload.

The usual cross-site scripting attack involves posting comments or files where the payload is not well-escaped HTML. The attack may target site visitors or site administrators.

XSS can be avoided by using a proper software development framework which always escapes variables in template output and does not rely on developers to manually escape variables in page templates, JavaScript or HTML JSON embeds.

Special attention should be paid to file uploads: both the file content and the file name provide an attack channel. It is recommended that user-uploaded content always be served from a separate top level domain (TLD).



Applies for: Everyone



Related incidences:

- :ref:`facebook`




Links:


- `Cross site scripting (Wikipedia) <https://en.wikipedia.org/wiki/Cross-site_scripting>`_



- `Cross site scripting (OWASP) <https://www.owasp.org/index.php/Cross-site_Scripting_%28XSS%29>`_



- `Handling untrusted JSON safely (WhiteHat Security) <https://blog.whitehatsec.com/handling-untrusted-json-safely/>`_



- `Unrestricted File Upload (OWASP) <https://www.owasp.org/index.php/Unrestricted_File_Upload>`_



- `Secure user uploads and exploiting served user content (Mikko Ohtamaa) <https://opensourcehacker.com/2013/07/31/secure-user-uploads-and-exploiting-served-user-content/>`_



- `User-uploaded content (Django security) <https://docs.djangoproject.com/en/1.8/topics/security/#user-uploaded-content>`_



- `Sending form data (Mozilla Developer Network) <https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Forms/Sending_and_retrieving_form_data>`_






.. _cross-site-request-forgery-csrf:

Cross-site request forgery (CSRF)
==============================================================

**Software is written in a manner that it doesn't accept cross-site requests?** 


Cross-site request forgery is an attack in which the JavaScript payload or link hosted on a third-party site performs an attack on behalf of the user of the targeted website.

The malicious third-party site loads JavaScript which makes AJAX requests to the target site where the user is logged in.

The software should be written using a framework which prevents HTTP POST submissions without the CSRF token. Any state-changing action (login, create, modify, delete) should not be an HTTP GET request.





Related incidences:

- :ref:`twitter`

- :ref:`soho`




Links:


- `Cross-site request forgery (Wikipedia) <https://en.wikipedia.org/wiki/Cross-site_request_forgery>`_



- `Cross-Site Request Forgery (CSRF) (OWASP) <https://www.owasp.org/index.php/Cross-Site_Request_Forgery_%28CSRF%29>`_



- `Sending form data (Mozilla Developer Network) <https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Forms/Sending_and_retrieving_form_data>`_






.. _password-storage-best-practices:

Password storage best practices
==============================================================

**User passwords and two-factor seeds are hashed and salted against bruteforcing?** Yes / No

Password hashing is a method to prevent cleartext password storage.

This protects user password integrity in case the database is compromised and logins and passwords are dumped somewhere. Developers should not invent password storage schemes themselves, but should use a specialized library to do the password hashing and salting for persistent storage.



Applies for: Everyone



Related incidences:

- :ref:`sebastian`

- :ref:`slack`

- :ref:`lastpass`

- :ref:`hacking-team`




Links:


- `PBKDF2 (Password-Based Key Derivation Function 2) in Wikipedia <https://en.wikipedia.org/wiki/PBKDF2>`_



- `Password storage cheat sheet in OWASP <https://www.owasp.org/index.php/Password_Storage_Cheat_Sheet>`_



- `Password strength (Wikipedia) <https://en.wikipedia.org/wiki/Password_strength>`_






.. _authorization-and-permission-framework:

Authorization and permission framework
==============================================================

**Private pages and data access is protected by authorization framework?** Yes / No

When protecting private data, a systematic authorization framework is used instead of ad-hoc conditions. A standardized permission check method leaves less room for human error in fragile permission check conditions.

In †he authorization framework approach:

* The same process is used in all permission checks.

* Manual conditions (ifs) are unnecessary to make permission checks, as the approach is prone to human error.

* All data is preferably private unless explicitly made public.

* The checks follow a standardized authorization pattern like an access control list or activity-based checks.





Related incidences:

- :ref:`purse`




Links:


- `Access Control Cheat Sheet (OWASP) <https://www.owasp.org/index.php/Access_Control_Cheat_Sheet>`_



- `Role-based access control (Wikipedia) <https://en.wikipedia.org/wiki/Role-based_access_control>`_



- `Attribute-based access control (Wikipedia) <https://en.wikipedia.org/wiki/Attribute-based_access_control>`_



- `Permissions and Authorization (Django) <https://docs.djangoproject.com/en/1.8/topics/auth/default/#topic-authorization>`_



- `Pundit, Minimal authorization object-oriented design for Ruby on Rails <https://github.com/elabs/pundit>`_



- `MustBe, Authorization Plumbing For NodeJS <https://github.com/derickbailey/mustbe>`_






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






.. _non-guessable-ids:

Non-guessable IDs
==============================================================

**Publicly exposed ids are not guessable?** Yes / No


If the service uses running counters as database primary keys, these IDs should not be exposed to the public.

Knowing the ID sequence allows the attacker to gain knowledge of the item count, weakening service security.

* If HTTP endpoints or pages lack proper permission checks, guessing the ID sequence allows the attacker to scrape private data.

* Sensitive business information, like user count or trade count, is exposed to the public.

Use a random ID generation method like the Universally Unique identifier (UUID) version 4 "random," which provides 122 truly random bits for each ID.



Applies for: Everyone



Related incidences:

- :ref:`purse`




Links:


- `UUID (Wikipedia) <https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_.28random.29>`_



- `URL safe UUIDs in the smallest number of characters (StackOverlow) <http://stackoverflow.com/q/11431886/315168>`_






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






.. _whitehat-program:

Whitehat program
==============================================================

**The service has a public whitehat or security bounty program?** Yes / No


A whitehat program, also known as a security bounty program, is a published guide that shows how the service deals with security researchers. The purpose of a whitehat program is to encourage legit security research to cover issues on the service and credit third parties for doing this work.

The third-party security researches usually scan the service using web security audit tools like Burp Suite and try to discover XSS, CSRF, database injection and authorization flaws.

The whitehat program usually includes information about:

* How to contact the service when reporting security issues

* What response time one should expect

* Security issue types that are eligible for bounty

* The amount of the bounty and how it is paid

* Crediting the researcher for uncovering the issue

There exist third party services facilitating the creation and management of whitehat programs (Cobalt, HackerOne).



Applies for: Medium and large enterprises



Related incidences:

- :ref:`starbucks`

- :ref:`coinbase`




Links:


- `Cobalt <https://cobalt.io/>`_



- `HackerOne <https://hackerone.com/>`_






.. _code-reviews:

Code reviews
==============================================================

**Source code is reviewed?** Yes / No

The team uses code review, also known as code inspection, as the best practice when merging changes.

All code going to the production should be reviewed at least one person who is not the original author of the code. Two pairs of eyes see better than one to catch possible mistakes.



Applies for: Medium and large enterprises





Links:


- `Code Review (Wikipedia) <https://en.wikipedia.org/wiki/Code_review>`_



- `OWASP Code Review Guide <https://www.owasp.org/index.php/OWASP_Code_review_V2_Table_of_Contents>`_





