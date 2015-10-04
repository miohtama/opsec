
.. This is a generated file from data/. DO NOT EDIT.

.. _maxcdn:

MaxCDN
==============================================================

*Date: 2013-07-02*

MaxCDN, a content-delivery network service hosting bootstrapcdn.com, the default CDN option for popular Bootstrap front end framework, got compromised.

The vendor of MaxCDN had laid off a support engineer with access to the servers where BootstrapCDN runs. The credentials of the engineer were not revoked. The attackers gained these credentials. Then the attackers rebooted a server into single-user mode, changed the root password, and SSH’d into the server. Bootstrap JavaScript files were modified to serve an exploit toolkit.

Because Bootstrap is widely deployed and CDN option is one recommended way to include it on your site, the attack payload got served to tens of thousands of visitors in short period of time.



Related evaluation points:

- :ref:`passphrase-on-server-login-keys`

- :ref:`audited-server-login-keys`

- :ref:`https-tls-only`





Links:

- `BootstrapCDN Security Post-Mortem <https://www.maxcdn.com/blog/bootstrapcdn-security-post-mortem/?utm_source=text>`_

