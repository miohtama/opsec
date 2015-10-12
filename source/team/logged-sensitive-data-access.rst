
.. This is a generated file from data/. DO NOT EDIT.

.. _logged-sensitive-data-access:

Logged sensitive data access
==============================================================

**Sensitive data access by administrators is logged?** Yes / No

All actions related to administrators’ accessing and manipulating sensitive data are logged. This includes direct database connections, API services and other internal access methods.

In case of privacy breach claims, these logs can be used to reconstruct the scenario regarding who has been accessing or manipulating the data. Sensitive data access logs protect against insider threats. Knowing that one cannot get away without being caught discourages malicious attempts.

Access logs should be detailed as possible, including timestamp and details of performed actions. Access logging can be implemented, for example, by storing the full HTTP request logs, including POST parameters and body, from all logged-in administrators.

See also :ref:`log-server` and :ref:`user-audit-logs`.



Applies for: Everyone



Related incidences:

- :ref:`ashley-madison`




