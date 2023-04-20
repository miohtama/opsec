
.. This is a generated file from data/. DO NOT EDIT.

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



