
.. This is a generated file from data/. DO NOT EDIT.

.. _log-server:

Log server
==============================================================

**Critical logs are mirrored to a log service?** 


Critical log files should be mirrored to a destination where the logs can be only appended. The logs cannot be read back or manipulated.

The log service should have different access credentials from the administrators of normal systems. In case the attacker gains access to the infrastructure, this prevents the wiping or manipulating of logs. This allows robust recovery and post-mortem from potential attacks.



Applies for: Medium and large enterprises





Links:


- `Amazon CloudWatch <https://aws.amazon.com/cloudwatch/>`_



- `Creating a Centralized Syslog Server (Linux Journal) <http://www.linuxjournal.com/content/creating-centralized-syslog-server>`_



