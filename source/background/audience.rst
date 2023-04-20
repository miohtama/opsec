Audience
========

Not all Internet services are equally critical. This guide is aimed for teams who themselves are developing services dealing with private and financial data, though it can be used as a reference for other kind of services. The guide is not geared towards your average company business card website, software product deployments or generic IT administration.

The audience of the guide includes, but is not limited, to

* Website developers

* System administrators and infrastructure operators

* Technology and security officers

* ...and everybody who is responsible for making sure they do not get hacked

The guide assumes the reader has the basic understanding how Internet services are developed and operated. The developers and system administrators can use the guide as a reference when building and :doc:`assessing security of their organizations <../assessment/index>`. Furthermore, with the :doc:`evaluation points <../background/index>` provided by the guide a third party can audit an organization and provide a public track record of the matter.

Sensitive and high value services
=================================

Sensitive services generally include

* **Cryptocurrency services**: gaming industry where players trade with each other, by rules or on blackmarket, is common abuse target. See :ref:`steam`.

* **Hosting services**: Running and managing somebody else's software and data sets you in a privileged position to abuse or to be exploited. See :ref:`linode`.

* **Banking and financial services**: provide access to the assets of the users.See :ref:`bitstamp`.

* **Health services**: sensitive private information which can be used against the users. 

* **Dating service**: sensitive private information which can be used against the users. See :ref:`ashley-madison`.

* **Government and legal**: having government or military service compromised is not good for politics.

* **Critical infrastructure services**: Electricity, gas, fuel, telecom and other modern society services that are a high-value target for cyber warfare.

Even if the service is not a high value target per se, one might host information which is valuable blackmail or cyber reconnaissance material for a nation-state actor. If you are carefree you might even be stamped by an attack which was not especially targeting you. The worst case scenario is that the incident will strip everything of the service and it's unlikely there is an insurance fund which will cover this.
