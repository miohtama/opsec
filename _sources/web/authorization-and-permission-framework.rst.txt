
.. This is a generated file from data/. DO NOT EDIT.

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



