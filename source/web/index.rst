
.. This is a generated file from data/. DO NOT EDIT.

===========================================
Web development security
===========================================

This chapter discusses about the web development best practices for sensitive Internet services.

Background
==========

When developing a sensitive Internet service, special attention should be paid on the security. It is very possible to build unhackable services. Accomplishing this needs discipline and security awareness from the development team.

Most application-level vulnerabilities are related to the input handling. Any Internet facing service accepts incoming traffic and user input, both good and bad. It's a social contract: when you plug in your service to Internet, you acknowledge that anyone in the world is allowed to use the service.

HTTP and HTML where built on the era where thread models and security issues where different. Many security features have retrofitted or they are hacked on the top of the original HTML. Anyone who is not expert in HTTP, HTML and JavaScript has a lot to learn about potential attack modes. Thus, it is an imperative that the development team uses a proper *software development framework* to built the service. Usually the framework authors are well-versed in the security matters and have thought out and documented the proper processes for things like form submission handling, file uploads and exposing database to the world.





.. _https-tls-only:

HTTPS / TLS only
==============================================================

**The service is HTTPS-only with security HTTP headers?** Yes / No

The service is available only over encrypted connection. Plain HTTP connection is only allowed for the initial redirect. Furthermore, the HTTP responses should include security headers, like *HTTP Strict Transport Security*, *X-Frame-Option* and HTTPS-only cookies with no JavaScript access.

Encryption protects again man-in-the-middle attacks which include

* Malware tapping traffic locally

* Compromised wi-fi routers

* Malicious Tor exit nodes

* Nationstate actors and mass surveillance

*X-Frame-Option* HTTP response header prevents clickjacking attacks, though is not related to transport security directly.

If the site loads resources from external content delivery networks (CDN) these downloads should be marked with subresource integrity tags to prevent attacks through a compromised CDN provider.



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

**The software uses a framework for database queries?** Yes / No

One of the most common web application vulnerabilities is a database injection attack. The developers are allowed to write queries by hand without properly sanitizing input going into the queries.

In the most cases, the database is SQL based, providing opportunity for SQL injections. This can be easily prevented by never constructing database statements by hand and always using a framework to construct the queries, so that all values are properly escaped. The manual SQL manipulation should be prevented from the application developers, so that no room is left for a human error.



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

**The software is written in a manner that there is no possibility of cross-site scripting attack?** Yes / No

Cross-site scripting attack is a way to perform actions on the behalf of the user when the user views or clicks a compromised payload.

 The usual cross-site scripting attack is posting comments or files were the payload is not well-escaped HTML. The attack may target site visitor or site administrator.

 XSS can be avoided by using a proper software development framework which always escapes variables in template output and does not rely the developers to manually escape variables in page templates, JavaScript or HTML JSON embeds.

 Special attention should be paid for file uploads: both the file content and file name provide an attack channel. It is recommended that user uploaded content is always served from a separate top level domain (TLD).



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

**The software is written in a manner that it doesn't accept cross-site requests?** 

Cross-site request forgery is an attack where JavaScript payload or link hosted on a third party site performs attack on the behalf on the user on the targeted website.

The malicious third party site loads JavaScript which makes AJAX requests to the target site where the user is logged in.

The software should be written using a framework which prevents HTTP POST submissions without CSRF token. Any state changing action (login, create, modify, delete) should not be a HTTP GET request.





Related incidences:

- :ref:`twitter`




Links:


- `Cross-site request forgery (Wikipedia) <https://en.wikipedia.org/wiki/Cross-site_request_forgery>`_



- `Cross-Site Request Forgery (CSRF) (OWASP) <https://www.owasp.org/index.php/Cross-Site_Request_Forgery_%28CSRF%29>`_



- `Sending form data (Mozilla Developer Network) <https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/Forms/Sending_and_retrieving_form_data>`_






.. _password-storage-best-practices:

Password storage best practices
==============================================================

**The user passwords and two-factor seeds are hashed and salted against bruteforcing?** Yes / No

Password hashing is a method to prevent cleartext password storage.

This protects the user password integrity in the case the database is compromised and logins and passwords dumped somewhere. The developers should not invent password storage schemes themselves, but use a specialized library to do the password hashing and salting for persistent storage.



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

When protecting the private data a systematic authorization framework us used instead of ad-hoc conditions. A standardized permission check method leaves less room for human errors in fragile permission check conditions.

In †he authorization framework approach

* The same process is used in the all permission checks

* Manual conditions (ifs) are unnecessary to make permission checks as the approach is human error prone

* All data is preferably private unless explicitly made public

* The checks follow a standardized authorization pattern like access control list or activity-based checks





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

Front end web server and web browsers caches pages and documents by default. Sensitive pages and downloads should have explicit no caching headers present.

Thread models include

* A caching front end web server may lead user sessions when HTTP response with a private cookie is accidentally cached

* The user device is compromised and sensitive information is extracted from the browser cache

Generally special attention should be paid HTTP responses like

* Generated image, audio, video and other media downloads

* Document downloads (Office files, PDF, CSV, TXT)







Links:


- `The Security Impact of HTTP Caching Headers (SANS ISC InfoSec) <https://isc.sans.edu/forums/diary/The+Security+Impact+of+HTTP+Caching+Headers/17033/>`_






.. _non-guessable-ids:

Non-guessable ids
==============================================================

**Publicly exposed ids are not guessable?** Yes / No

If the service uses running counters as database primary keys, these ids should not be exposed to the public.

Knowing the id sequence allows the attacker to gain knowledge of the item count weakening the service security.

* If HTTP endpoints or pages lack proper permission checks, guessing the id sequence allows the attacker to scrape private data.

* Sensitive business information, like user count or trade count, is exposed to public.

Use random id generation method, like Universally unique identifier (UUID) version 4 "random", which provide 122 truly random bits to for each id.



Applies for: Everyone



Related incidences:

- :ref:`purse`




Links:


- `UUID (Wikipedia) <https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_.28random.29>`_



- `URL safe UUIDs in the smallest number of characters (StackOverlow) <http://stackoverflow.com/q/11431886/315168>`_






.. _non-public-administration-site:

Non-public administration site
==============================================================

**The administration site is not accessible or known to public?** Yes / No

Many common software platforms come with the default administration site in a location like */admin/*.

If the administrative URLs are well known it expands the potential attack surface. The attacker can guess administration HTTP endpoints with vulnerabilities and try to exploit those.

The administration interface should be in non-guessable, non-end user visible, URL. Besides authorization, additional access restrictions should be placed upon the administration interface with two-factor authentication, VPN and IP restrictions (see :doc:`Team security <../team/index>`).



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

* Security issues types eligible to bounty

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





