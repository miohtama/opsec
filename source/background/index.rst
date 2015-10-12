==========
Background
==========

Opening word: Welcome to Internet
=================================

In good and bad, Internet has been a dominant factor shaping the globalization and shrunking our planet. Intenet allows us to connect to anybody in a blink of an eye. Internet allows us to have all the information in the world in our fingertips, no matter who wrote it, where and when. The advancements in communications have brought the unimaginable pace of development and research.

What makes Internet to be what it is, global and everpresent? When you plug your device to Internet, you make a social contract saying you accept any traffic coming over the wire, even if you don't like it. Internet itself doesn't discriminate. No evil bit exists in a network packet telling you maybe you should not open it, since there are no universal moral standards for evil. What might be a horredous cyber act of a killing well-intentioned startup for one might be a small victory against the oppressors of a thief nation for the other.

Thus, in its heart, Internet is a lawless cyberanarchy. The hostile actors are foreign and often state sponsored - there is no legal remedy against someone who is not criminal by their own standards. Knowing the IP address of an adversary doesn't help if you cannot bring justice on the opposite side of the planet. There is no world police who would hear your case.

Internet has always been this way. However, today's threats are no longer just fiction in cyberthrillers. The landscape of Internet security changed greatly during 2010s. As more business and personal life moves online, we have become dependent on Internet. We can receive more damage over Internet: there is more to lose in privacy, financial, business, industrial and political aspects. Those benefiting of exploiting weaknesses know this as well.

Something being greater than a justice system of any nation doesn't leave options for post-mortem appeals. Instead, one must recognize the environment where they are working and cope against the threats. One needs to resist them and one needs survive them on their own. Threat models and defences are well known. Building a hack-resistant system is possible and in the reach of anybody, as this guide shows.

Hack-resistancy does not happen with phrases like "our privacy policy states we follow modern security practices" or "our data is encrypted". These kind of opaque statements lack factual content - they don't tell *which* practices are followed and *how* your data is encrypted. Service users or peers cannot *find security* there. Alas, the history shows that every compromised service had statements like these.

To create a safer Internet we need a build a culture of security. The motivation towards this must come from the developers, operators and decision makers themselves. The first step is taking responsibility of what is at the stake and recognizing security is not something slapped on the top afterwards. Security is something crossing the business horizontally and touching all aspects of it. The future lies in finding transparent, verifiable, ways to guarantee the security and educating peers and users about this. This guide aims to be an initiative to this direction.

Mission statement
=================

|opsec| works towards building a safer Internet.

**Building responsible security culture yields to healthy Internet society**. Every day more and more of our lives is transformed to online. People who create and nurture online services act as the deputies in this society. The motivation towards transparent trust and safety declarations must start with these people and resonate through their work.

**Security should be open and free**: Nobody should need to pay to the ensure the state of the art security of their work. A willing person should be able to learn information and access tools needed to build safe Internet services for free.

**Security should be transparent**: There should be an effective way or appromaximation to say whether one can trust to the safety of a service. There should be ways for service operators to communicate their intent of security in veriafable facts, not just in claim.

Goals
=====

There exist similar projects with partially overlapping scopes. This project is geared towards Internet services operators and business decision makers following the principles on which Internet itself was built. The guide aims to be

* **Holistic**: The guide tells how to guarantee the security of the project as a whole. This includes organization practices, tools and devices, infrastructure and e.g. is not limited to one business function like software development practices.

* **Grassroots effort**: from bottom to up, from individuals to decision makers. The effort sprouts from real life security practices. The authors and audience are not limited to security researchers, but include software developers and project managers.

* **Open**: The content is hosted on Github and the editing open-ended for everybody.

* **Lightweight**: Everybody from a single person startup should be able to follow the guide.

* **High critical service**: The services storing private data or financial data are the most valued targets. The guide focus is on these services as their operators have most on the stake in Internet safety.

Prior art
=========

|opsec| greatly owes to earlier work in the field of information security. There exist few projects with partially overlapping scopes and the guide makes its best to cross reference them when possible.

* `The Open Web Application Security Project (OWASP) <https://www.owasp.org/index.php/Main_Page>`_. OWASP is a non-profit foundation focusing to improve the security of the software. OWASP goes in-detail to good software development practices and offers invaluable advices for developers.

* `PCI Security Standard Council, The Payment Card Industry Data Security Standard <https://www.pcisecuritystandards.org/security_standards/documents.php?agreements=pcidss&association=pcidss>`_ addresses information security concerns in credit card and payment processing industry. PCI DSS pursues the security from compliance enforcing viewpoint. The requirements are detailed, but the level of documentation, process management and reviews is not in the reach of small business. PCI DSS is relevant for large enterprises where organizations themselves may not see profit in security improvements, but see it as an externalized cost. Thus, in this kind of industries, security considerations must be forced by external auditors.

* `National Institute of Standards and Technology (NIST), Computer Security publications <http://csrc.nist.gov/publications/PubsSPs.html>`_. NIST publishes comprehensive guides for security, catering everything from embedded devices to payment processing.

* `Health Insurance Portability and Accountability Act (HIPAA) <http://www.hhs.gov/ocr/privacy/>`_ defines how US national standard for health care companies handling private information in electronic form. `The text is in legal like <http://www.hhs.gov/ocr/privacy/hipaa/administrative/combined/index.html>`_, mainly geared toward legal advisors than the service operators or developers.
