==========
Background
==========

Introduction: Welcome to the Internet
=====================================

Internet is global, in both and good and bad. Intenet allows us to connect to anybody in a blink of an eye. Internet allows us to have all the information in the world in our fingertips, no matter who wrote it, where and when. The advancements in communications have brought the unimaginable pace of development and research.

What makes Internet to be what it is, global and everpresent? When you plug your device to Internet, you make a social contract saying you accept any traffic coming over the wire, even if you don't like it. Internet itself doesn't discriminate. No evil bit exists in a network packet telling you maybe you should not open it, since there are no universal moral standards for evil. What might be a horredous cyber act of a killing well-intentioned startup for one might be a small victory against the oppressors of a thief nation for the other.

Thus, in its heart, Internet is a lawless cyberanarchy. The hostile actors are foreign and often state sponsored - there is no legal remedy against them as they are not criminal by their own standards. Having an IP address of an adversary doesn't help if you cannot bring justice on the opposite side of the planet. There is no world police who would hear your case.

Internet has always been this way. However, today's threats are no longer just fiction in cyberthrillers. The landscape of Internet security changed greatly during 2010s. As more business and personal life moves online, we have become dependent on Internet. We can receive more damage over Internet: there is more to lose in privacy, financial, business, industrial and political aspects. Those who could benefit of exploiting this know this as well.

When Internet itself is greater than the justice system of any nation only way to cope against threats is to build hack-proof services. It is possible. It is not difficult. It is what this guide is all about.

However hack-proof services do not happen with phrases like "in our privacy policy we state we follow modern security practices" or "our data is encrypted". Opaque statements like these lack factual content - the reader doesn't know *which* practices are followed and *how* your data is encrypted. The service user or peers cannot *find security* there. Alas, the history shows that the sentences like this often don't mean anything, as they have been written in the policies of every compromised service.

To build safer Internet with real security we must work together to find transparent ways to educate and evalute services and their operators. This guide aims to be a step to this direction.

Mission statement
=================

|opsec| tells you how to design secure Internet services and how to assess their level of security.

**Building responsible security culture yields to healthy Internet society**. Every day more and more of our lives is transformed to online. People who create and nurture online services act as the deputies in this society. The motivation towards transparent trust and safety declarations must start with these people and resonate through their work.

**Security should be open and free**: Nobody should need to pay to the ensure the state of the art security of their work. A willing person should be able to learn information and access tools needed to build safe Internet services for free.

**Security should be transparent**: There should be an effective way or appromaximation to say whether one can trust to the safety of a service. There should be ways for service operators to communicate their intent of security in veriafable facts, not just in claim.

Guide goals
===========

|opsec| is an effort towards safer Internet services. There exist similar projects with partially overlapping scopes. This project is geared towards Internet services operators and business decision makers following the principles on which Internet itself was built. The guide aims to be

* **Holistic**: The guide tells how to guarantee the security of the project as a whole. This includes organization practices, tools and devices, infrastructure and e.g. is not limited to one task like software development practices. 

* **Grassroots effort**: from bottom to up, from individuals to decision makers. The effort sprouts from real life security practices. The authors and audience are not limited to security researchers, but include software developers and project managers.

* **Open**: The content is hosted on Github and the editing open-ended for everybody.

* **Lightweight**: Everybody from a single person startup should be able to follow the guide.

* **High critical service**: The services storing private data or financial data are the most valued targets. The guide focus is on these services as their operators have the highest responsibility to guarantee the safe future of Internet.

Chapters and evaluation points
==============================

The guide is divided to different chapters, each chapter reflecting different organizational or IT functionality.

The chapters consist of questions, called *evalution points*, on a specific matter. Ultimately you want to be able to answer yes to every evaluation point.

Applicable criteria
===================

Some evaluation points might not be applicable for small businesses. For example, having a tool for managing server login keys might not be in the reach of a team of few members or less. Or it would be not needed at all, because only one person has access to the servers. Thus, each evaluation point contains an applicable criteria.

The following rough rules can be used to decide whether your organization should consider the evaluation point:

* **Everybody**: Everybody should do this, regardless of the mature and resources of their organization

* **Medium and large enterprises**: Organizations with more than two million yearly revenue or two million raised capital. These organizations generally have multiple people working on the service and can afford to hire a security consultancy, training and tools.

Prior art
=========

This guide was started 2015. It is based on the empirical experiences of building services which are highly attractive targets for cybercrime.

Further reading and related work include

* `The Open Web Application Security Project (OWASP) <https://www.owasp.org/index.php/Main_Page>`_. Whereas OWASP goes in-detail to software security, it does not discuss the holistic approach to the organizational issues outside the software development perspective itself.

* `National Institute of Standards and Technology (NIST), Computer Security publications <http://csrc.nist.gov/publications/PubsSPs.html>`_. NIST publishes comprehensive guides for security, catering everything from embedded devices to payment processing. However, their guides do not address the security of Internet services very well.

* `PCI Security Sandard Council, The Payment Card Industry Data Security Standard <https://www.pcisecuritystandards.org/security_standards/documents.php?agreements=pcidss&association=pcidss>`_ addresses the security from credit card payment processing industry. The requirements are detailed, but the level of documentation, process management and reviews is not in the reach of small business, like 24/7 security staff. PCI DSS is very relevant for large enterprises where the organization does not see profit in maintaining the security and must be forced to do so by an external factor.

* `Health Insurance Portability and Accountability Act (HIPAA) <http://www.hhs.gov/ocr/privacy/>`_ defines how US national standard for health  care companies handling private information in electronic form. `The text is in legal like <http://www.hhs.gov/ocr/privacy/hipaa/administrative/combined/index.html>`_, more useful for lawyers than the service operators or developers.
