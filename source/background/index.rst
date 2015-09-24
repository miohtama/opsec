==========
Background
==========

Introduction
============

This Operations Security guide provides information for designing secure Internet services and a tool to do as security assessments.

The landscape of the Internet security has greatly changed during 2010s. The cyberthriller worst case threat scenarios are no longer fiction. Foreign malicious actors are state sponsored - in the case of an incident there is no remedy through legal means. The global nature of Internet makes it a lawless anarchy. When you plug your server to Internet, you make a social contract that you accept any traffic coming over the wire, even if it is malicious.

Even if the service is not a high value target per se, one might host information which is valuable blackmail or cyber reconnaissance material for a nation-state actor. If you are carefree you might even be stamped by an attack which was not especially targeting you. The worst case scenario is that the incident will strip everything of the service and it's unlikely there is an insurance fund which will cover this.

In most cases saying "our data is encrypted" does not mean anything. Having the server disks encrypted protects only against very unlikely event that the physical access of the offline server is compromised. Data must be decryptable for the service to be able to run. Thus, the data must always pass in plain text in the server memory. Anybody gaining the access to the live server, through the application vulnerability or the compromised team member device, has the full data access.

Our goals
=========

This guide is a collaborate effort from people who need to deal with Internet security in their professional life. There exist similar projects, but

There exist many similar project, but here we aim to be

* **Holistic**: We aim to guarantee the security of the project as a whole. This includes organization practices, tools and devices, infrastructure and not just a piece of software.

* **Grassroots effort**: from bottom to up, from individuals to decision makers. The effort sprouts from on real-life, practical, best practices.

* **Open**: The content is hosted on Github and the editing open-ended for everybody.

* **Lightweight**: Everybody from a single person startup should be able to follow the guide.

* **High critical service**: The services storing private data or financial data are high risk targets. We focus is on these services as operators of these services have the responsible to guarantee the safe future of Internet.

Guide structure and evaluation points
=====================================

The guide is divided to different chapters, each reflecting the specific organization or development operations functionality.

Each chapter consists of questions, called *evalution points*, on a specific matter. Ultimately you want to be able to answer yes to every evaluation point.

Evaluation point applicable criteria
====================================

Some evaluation points might not be applicable for small businesses. For example, having a tool for managing server login keys might not be in the reach of a team of few members or less. Or it would be not needed at all, because only one person has access to the servers. Thus, each evaluation point contains an applicable criteria. The used criteria is following

* **Everybody**: Everybody should do this, regardless of the mature and resources of their organization

* **Medium and large enterprises**: Organizations with more than two million yearly revenue or two million raised capital. These organizations generally have multiple people working on the service and can afford to hire a security consultancy, training and tools.

Prior art
=========

This guide was started 2015. It is based on the empirical experiences of building services which are highly attractive targets for cybercrime.

Further reading and related work include

* `The Open Web Application Security Project (OWASP) <https://www.owasp.org/index.php/Main_Page>`_. Whereas OWASP goes in-detail to software security, it does not discuss the holistic approach to the organizational issues outside the software development perspective itself.

* `National Institute of Standards and Technology (NIST), Computer Security publications <http://csrc.nist.gov/publications/PubsSPs.html>`_. NIST publishes comprehensive guides for security, catering everything from embedded devices to payment processing. However, their guides do not address the security of Internet services very well.

* `PCI Security Sandard Council, The Payment Card Industry Data Security Standard <https://www.pcisecuritystandards.org/security_standards/documents.php?agreements=pcidss&association=pcidss>`_ addresses the security from credit card payment processing industry. The requirements are detailed, but the level of documentation, process management and reviews is not in the reach of small business, like 24/7 security staff. PCI DSS is very relevant for large enterprises where the organization does not see profit in maintaining the security and must be forced to do so by an external factor.


