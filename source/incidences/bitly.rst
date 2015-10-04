
.. This is a generated file from data/. DO NOT EDIT.

.. _bitly:

Bitly
==============================================================

*Date: 2014-05-08*

Bitly unecrypted backups got compromised.

Bitly is a URL shortening service. The users can log in with their Facebook and Twitter accounts. In the incidence, the attacked gained access to offsite unencrypted database backups. It is assumed the database contained (OAuth) tokens to take actions in Facebook and Twitter on behalf of the user.

"On May 8 [2014], the Bitly security team learned of the potential compromise of Bitly user credentials from the security team of another technology company. We immediately began operating under the assumption that we had a breach and started the search for all possible compromise vectors." (More detail)

"They observed that we had an unusually high amount of traffic originating from our offsite database backup storage that was not initiated by Bitly." (More detail)

"We audited the security history for our hosted source code repository that contains the credentials for access to the offsite database backup storage and discovered an unauthorized access on an employee’s account.  We immediately enabled two-factor authentication for all Bitly accounts on the source code repository and began the process of securing the system against any additional vulnerabilities." (More detail)

"Hashed passwords were exposed but plain text passwords were not.  All passwords are salted and hashed.  If you registered, logged in or changed your password after January 8th, 2014, your password was converted to be hashed with BCrypt and HMAC using a unique salt.  Before that, it was salted MD5." (More detail)

The authoritative report "More detail", by Bitly, is now taken down (http://blog.bitly.com/#85169217199).



Related evaluation points:

- :ref:`two-factor-authentication-on-critical-services`

- :ref:`encrypted-server-data`





Links:

- `Bitly users must change passwords, account credentials might have been compromised <http://www.techtimes.com/articles/6773/20140510/bitly-users-must-change-passwords-account-credentials-might-have-been-compromised.htm>`_

- `More detail (Bitly blog in the Wayback machine) <https://web.archive.org/web/20140515093107/http://blog.bitly.com/>`_

