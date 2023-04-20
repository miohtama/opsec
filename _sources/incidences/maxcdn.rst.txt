
.. This is a generated file from data/. DO NOT EDIT.

.. _maxcdn:

MaxCDN
==============================================================

*Date: 2013-07-02*






MaxCDN, a content-delivery network service had their servers compromised. MaxCDN is running bootstrapcdn.com, a CDN download for popular Bootstrap front end framework.

The vendor of MaxCDN had laid off a support engineer having access to the servers where BootstrapCDN runs. The credentials of the support engineer were not properly revoked. The attackers had gained access to these credentials. The attackers rebooted the server into single-user mode, changed the root password, and SSH’d into the server. Bootstrap JavaScript files were modified to serve an exploit toolkit.

Bootstrap is widely deployed and CDN option is one of the recommended ways to include Bootstrap on your website. BootstrapCDN gets a lot of downloads. Thus, the attack payload was served to tens of thousands of visitors in short period of time.



Related evaluation points:

- :ref:`passphrase-on-server-login-keys`

- :ref:`audited-server-login-keys`

- :ref:`https-tls-only`





Links:

- `BootstrapCDN Security Post-Mortem <https://www.maxcdn.com/blog/bootstrapcdn-security-post-mortem/?utm_source=text>`_

