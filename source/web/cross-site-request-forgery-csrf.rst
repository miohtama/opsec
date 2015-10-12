
.. This is a generated file from data/. DO NOT EDIT.

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



