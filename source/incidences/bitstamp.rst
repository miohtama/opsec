
.. This is a generated file from data/. DO NOT EDIT.

.. _bitstamp:

Bitstamp
==============================================================

*Date: 2015-01-04*





Assets stolen: **5M USD**


Bitstamp, one of the largest Bitcoin exchanges, lost 5M USD customer assets due to a breach.

Bitstamp (bitstamp.net) is one of the largest Bitcoin exchanges in the world. Their system was breached 4th January 2015. 18000 Bitcoins, worth of 5M USD by the time, were stolen. After the breach Bitstamp rebuilt their server infrastructure and partnered with BitGo, a transaction policy and clearing party. Bitstamp never commented the cause of the incident in public.

Later a confidential memo by the general counsel of Bitstamp leaked and shed some light on the events. Though the authenticity of the memo is not confirmed by Bitstamp, there is all reasons to believe it is genuine.

Below are some direct questions from this memo.

"On 4 November 2014, Mr Merlak [CTO of Bitstamp] was contacted by Skype account punk.rock.holiday from IP address (94.185.85.171). The gambit for this phishing attack was to offer Mr Merlak free tickets to Punk Rock Holiday 2015. (Merlak is keen on punk rock and has played in a band.) ... Over a period of approximately five weeks, four more Bitstamp employees received similar highly targeted phishing attacks, each tailored to individual interests." (Bitstamp Incident Report)

"On 9 December 2014, Bitstamp’s Systems Administrator, L.K., received a phishing email to his Gmail account. Unlike some of the others targets, K did have access to Bitstamp’s hot wallet. The email header had been spoofed to appear as if it had been sent from konidas@acm[.]org, although it was actually received from a Tor exit node. The sender was offering Mr. K the opportunity ... as part of this offer, the attacker sent a number of attachments. One of these, UPE_application_form.doc, contained obfuscated malicious VBA script. When opened, this script ran automatically and pulled down a malicious file from IP address 185.31.209.145, thereby compromising the machine." (Bitstamp Incident Report)

"On 29 December 2014, SSH logs show that Mr K’s account logged in to X and the Y server at the data centre. On this occasion, Mr K was certain that these log-ins were not made by him, and must therefore have been the attacker. Analysis indicates that the attacker accessed X, where the wallet.dat file was held, and the Y server, where the passphrase for the Bitcoin wallet was stored, before data was transferred out of both servers to IP address 185.31.209.128, which is part of a range owned by a German hosting provider." (Bitstamp Incident Report)

"Two-factor authentication was not required to access the data centre from Mr K laptop while it was logged in to the office network" (Bitstamp Incident Report)

Even though Bitstamp followed high level security procedures, team members and their working devices were vulnerable. By allowing unsafe Office software suite to view an external document instead of a web based viewer, the laptop of a high value victim was compromised. Even though the server required two-factor authentication this was disabled in certain circumstances for the convenience. At the time of the incident Bitstamp did not utilize any kind of fraudulent withdraw detection mechanism. Any of these three factors would have stopped the attacker.

After the incidence Bitstamp rebuild the server infrastructure and opted in to BitGo, a third party Bitcoin transaction verification service. The Bitcoin losses were reimbursed by Bitstamp.



Related evaluation points:

- :ref:`dangerous-file-attachments`

- :ref:`two-factor-authentication-on-server-login`

- :ref:`cold-wallet`

- :ref:`transaction-verification`





Links:

- `Working Link of Leaked Bitstamp Incident Report <https://imgur.com/a/hLt5uQm>`_

- `Hackers steal $5 million from major bitcoin exchange (Fortuna) <http://fortune.com/2015/01/05/bitstamp-bitcoin-freeze-hack/>`_

- `Major Bitcoin Exchange Bitstamp Goes Offline After Possible Hack (WIRED) <http://www.wired.com/2015/01/bitstamp-offline/>`_

- `Bitstamp Incident Report (Office of Inadequate security) <http://www.databreaches.net/bitstamp-incident-report-february-2015/>`_

