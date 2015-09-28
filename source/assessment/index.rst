==================
Assessing security
==================

Introduction
============

Sometimes it's necessary to know that the organization and its services are secure in fact, not just in claim. Every privacy policy has a disclaimer saying they follow the industry security best practices. Rarely anybody clarifies what we are these best practices and how they are being followed. Furthermore the incidences history has shown that often the claims themselves are bogus.

This operations security guide is created in a manner that it can assess the security in an objective manner with little room for the interpretation. The assessment process is transparent and open. The guide consists of evaluation points which are easy to verify and have only outcomes "it's secure" or "it's not secure". You either get green light or red light - there is no room for grey area. When you say you have assessed the security based on Operations Security guide you can name the individual facts that were checked.

Learning security
=================

If you are still starting a project, you are new to security to or generally wish to learn more about secure Internet services, this guide can serve you as openreference material. It contains relevant links and past security incidences which are cross-referenced with the evaluation points, building a picture how failing security has caused incidences. With historical background and more hands on examples we hope the guide is more entertaining to study than purely abstract study material.

Self assessment
===============

Self assessment is a procedure where somebody within organization itself goes through the project and evaluates the security principles. This is to harden the system and make sure the project is prepared for developing secure services.

This guide can serve as a base for doing a self assessment. It contains a list of evaluation points a member of the organization can go through and suggest changes to the peers how the issues should be addressed.

Third party assessment
======================

A third party assessment happens when a person who is not a stakeholder in the project is invited to review the project. If the reviewer has no conflict of interest, there is little reason to embellish the results, leading to more objective and accurate assessment.

The results can be published or left as an internal memo. Publishing the results is a trust building tool: if the Internet has a reason to trust the person who did the assessment, the audience learns the organization knows what they are doing and can trust their services.

A third party security assessment example
-----------------------------------------

The following assessment process

* The organization signs NDA with the reviewer

* The reviewer goes through the :doc:`evaluation points <../background/index>` with the representatives of organization

* Each evaluation point is confirmed with manual inspection. If the organization claims the devices are encrypted, the reviewer checks that this is indeed in the case, probably starting from the laptop and mobile phone of the CEO.

* The reviewer gives feedback to address the issues. For example, if a two-factor authentication is not enabled on the hosting provider account, the reviewer and the representative enable it during the assessment.

* If there is sensitive material, like site source code, it is handled only offline, through USB stick. The material is copied only to a specific computer which is reset before and after the assessment. This shields reviewer itself against any potential compromises.

* The report and evaluation point notes are also written offline on the same specific computer. The evaluation point notes are never put online.

* The reviewer gives feedback to the organization including the full evaluation point notes and scores.

Publishing the assessment results
---------------------------------

* The reviewer writes a public statement regarding the service security. The statement includes evaluation point score summaries for each chapter and written letter of recommendation.

* The organization can decide whether the statement is published. The statements are published on operationssecurity.org and the service can use operationssecurity.org badge to link to the results on their website.

* If some of the issues noted during the assessment are too cumbersome to be addresses on the spot, the organization can have the second assessment round. The reviewer comes back and goes through the remaining issues to see they were addresses and the evaluation point clears green.