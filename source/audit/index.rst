=============
Audit process
=============

Introduction
============

The operations security audit is a process to verify that a Internet service is secure in fact, not just in claim. This operations security guide is build in such a manner that audit process is transparent and open. Thus, the guide consists of evaluation points which are easy to verify and have only outcomes "it's secure" or "it's not secure" - there is no room for claiming grey area or generic, vague, statements.

A third party can audit your Internet service based on OperationsSecurity.org audit protocol. The primary goal of the audit is to strengthen the service security and address potential issues. The secondary goal of the audit is to increase the trust to the service - the auditor is a party who enjoys the trust of Internet goers and does not have incentive to make false statements regarding the state of the service security. If the auditor is aligned with *OperationsSecurity.org* the result summary is published on this site.

Ultimately the auditing is a trust building matter: it is also possible for the service operators to audit the service themselves based on this guide and publish the results themselves. However in this case it is very tempting to make shortcuts or not include the full picture in the audit process.

Audit protocol
==============

At the beginning of the audit, the *audit protocol* is locked. This is the set of the evaluation points which are audited. Because the content of this guide is live, each audit must record which version of the guide was used in the process.

Audit process
=============

The following audit process

* The organization signs NDA with the auditor

* The auditor goes through the :doc:`evaluation points <../background/index>` with the representatives of organization

* Each evaluation point is confirmed with manual inspection. If the organzation claims the devices are encrypted, the auditor checks that this is indeed in the case, probably starting from the laptop and mobile phone of the CEO.

* The auditor gives feedback to address the issues. For example, if a two-factor authentication is not enabled on the hosting provider account, the auditor and the representative enable it during the audit.

* If there is sensitive material, like site source code, it is handled only offline, through USB stick. The material is copied only to a specific computer which is reset before and after the audit. This shields auditor itself against any potential compromises.

* The report and evaluation point notes are also written offline on the same specific computer. The evaluation point notes are never put online.

* The auditor gives feedback to the organization including the full evaluation point notes and scores.

* The auditor writes a public statement regarding the service security. The statement includes evaluation point score summaries for each chapter and written letter of recommendation.

* The organization can decide whether the statement is published. The statements are published on operationssecurity.org and the service can use operationssecurity.org badge on their website.

* If some of the issues noted during the audit are too cumbersome to be addresses on the spot, the organization can have the second audit round. The auditor comes back and goes through the remaining issues to see they were addresses and the evaluation point clears green.