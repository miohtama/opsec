
.. This is a generated file from data/. DO NOT EDIT.

.. _bitstamp:

Bitstamp
==============================================================

*Date: 2015-01-04*

Bitstamp lost 5M USD customer assets due to a breach

Bitstamp (bitstamp.net) is one of the largest Bitcoin exchanges in the world. Their system was breached 4th January 2015. 18000 Bitcoins, worth of 5M USD by the time, were stolen. After the breach Bitstamp rebuilt their server infrastructure and partnered with BitGo, a transaction policy and clearing party. Bitstamp never commented the cause of the incident in public.

Later private and confidental memo by the general counsel of Bitstamp, leaked what happened. Though the authenticity of the memo is not confirmed by the authors, it is believed to be genuine.

"On 4 November 2014, Mr Merlak [CTO of Bittamp] was contacted by Skype account punk.rock.holiday from IP address (94.185.85.171). The gambit for this phishing attack was to offer Mr Merlak free tickets to Punk Rock Holiday 2015. (Merlak is keen on punk rock and has played in a band.) ... Over a period of approximately five weeks, four more Bitstamp employees received similar highly targeted phishing attacks, each tailored to individual interests." (Bitstamp Incident Report)

"On 9 December 2014, Bitstamp’s Systems Administrator, L.K., received a phishing email to his Gmail account. Unlike some of the others targets, K did have access to Bitstamp’s hot wallet. The email header had been spoofed to appear as if it had been sent from konidas@acm[.]org, although it was actually received from a Tor exit node. The sender was offering Mr. K the opportunity ... as part of this offer, the attacker sent a number of attachments. One of these, UPE_application_form.doc, contained obfuscated malicious VBA script. When opened, this script ran automatically and pulled down a malicious file from IP address 185.31.209.145, thereby compromising the machine." (Bitstamp Incident Report)

"On 29 December 2014, SSH logs show that Mr K’s account logged in to X and the Y server at the data centre. On this occasion, Mr K was certain that these log-ins were not made by him, and must therefore have been the attacker. Analysis indicates that the attacker accessed X, where the wallet.dat file was held, and the Y server, where the passphrase for the Bitcoin wallet was stored, before data was transferred out of both servers to IP address 185.31.209.128, which is part of a range owned by a German hosting provider." (Bitstamp Incident Report)

"Two-factor authentication was not required to access the data centre from Mr K laptop while it was logged in to the office network" (Bitstamp Incident Report)

Even though Bitstamp followed high level software and infrastructure security procedures, they left team members exposed. By using vulnerable production software suite to view the document instead of a web based viewer, the laptop of a high valued target was compromised. Even though the server required two-factor login, because two-factor was disabled in certain circumstances for the working convenience it didn't stop the attackers this time. Furthermore, during the incident, their Bitcoin transaction system did not use any kind of fraudulent transaction detection mechanism which could have stopped the attacker.



Related evaluation points:

- :ref:`basic-security-practices`

- :ref:`dangerous-file-attachments`

- :ref:`two-factor-authentication-on-server-login`

- :ref:`cold-wallet`

- :ref:`transaction-verification`





Links:

- `Hackers steal $5 million from major bitcoin exchange (Fortuna) <http://fortune.com/2015/01/05/bitstamp-bitcoin-freeze-hack/>`_

- `Major Bitcoin Exchange Bitstamp Goes Offline After Possible Hack (WIRED) <http://www.wired.com/2015/01/bitstamp-offline/>`_

- `Bitstamp Incident Report (Office of Inadequtae security) <http://www.databreaches.net/bitstamp-incident-report-february-2015/>`_

