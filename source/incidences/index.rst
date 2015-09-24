
.. This is a generated file from data/. DO NOT EDIT.

==========
Incidences
==========

This chapter contains references to historical security breaches, their implications and what operational security measurements could have been taken to prevent them.



Bitstamp
==============================================================

Bitstamp lost 5M USD customer assets due to a breach

Bitstamp (bitstamp.net) is one of the largest Bitcoin exchanges in the world. Their system was breached 4th January 2015. 18000 Bitcoins, worth of 5M USD by the time, were stolen. After the breach Bitstamp rebuilt their server infrastructure and partnered with BitGo, a transaction policy and clearing party. Bitstamp never commented the cause of the incident in public.

Later private and confidental memo by the general counsel of Bitstamp, leaked what happened. Though the authenticity of the memo is not confirmed by the authors, it is believed to be genuine.

"On 4 November 2014, Mr Merlak [CTO of Bittamp] was contacted by Skype account punk.rock.holiday from IP address (94.185.85.171). The gambit for this phishing attack was to offer Mr Merlak free tickets to Punk Rock Holiday 2015. (Merlak is keen on punk rock and has played in a band.) ... Over a period of approximately five weeks, four more Bitstamp employees received similar highly targeted phishing attacks, each tailored to individual interests." (Bitstamp Incident Report)

"On 9 December 2014, Bitstamp’s Systems Administrator, L.K., received a phishing email to his Gmail account. Unlike some of the others targets, K did have access to Bitstamp’s hot wallet. The email header had been spoofed to appear as if it had been sent from konidas@acm[.]org, although it was actually received from a Tor exit node. The sender was offering Mr. K the opportunity ... as part of this offer, the attacker sent a number of attachments. One of these, UPE_application_form.doc, contained obfuscated malicious VBA script. When opened, this script ran automatically and pulled down a malicious file from IP address 185.31.209.145, thereby compromising the machine." (Bitstamp Incident Report)

"On 29 December 2014, SSH logs show that Mr K’s account logged in to X and the Y server at the data centre. On this occasion, Mr K was certain that these log-ins were not made by him, and must therefore have been the attacker. Analysis indicates that the attacker accessed X, where the wallet.dat file was held, and the Y server, where the passphrase for the Bitcoin wallet was stored, before data was transferred out of both servers to IP address 185.31.209.128, which is part of a range owned by a German hosting provider." (Bitstamp Incident Report)

"Two-factor authentication was not required to access the data centre from Mr K laptop while it was logged in to the office network" (Bitstamp Incident Report)

Even though Bitstamp followed high level software and infrastructure security procedures, they left team members exposed. By using vulnerable production software suite to view the document instead of a web based viewer, the laptop of a high valued target was compromised. Even though the server required two-factor login, because two-factor was disabled in certain circumstances for the working convenience it didn't stop the attackers this time. Furthermore, during the incident, their Bitcoin transaction system did not use any kind of fraudulent transaction detection mechanism which could have stopped the attacker.




Related evaluation points:

- team, File attachments

- team, Server login requires two-factor authentication

- assets, Cold wallet





Links:

- `Hackers steal $5 million from major bitcoin exchange (Fortuna) <http://fortune.com/2015/01/05/bitstamp-bitcoin-freeze-hack/>`_

- `Major Bitcoin Exchange Bitstamp Goes Offline After Possible Hack (WIRED) <http://www.wired.com/2015/01/bitstamp-offline/>`_

- `Bitstamp Incident Report (Office of Inadequtae security) <http://www.databreaches.net/bitstamp-incident-report-february-2015/>`_





Ashley Madison
==============================================================

Ashley Madison, a service billed as enabling extramarital affairs, comprehensibly compromised. A Canadian, Avid Life Media, was running a dating site for married people.

"In July 2015, a group calling itself "The Impact Team" stole the user data of Ashley Madison, a commercial website billed as enabling extramarital affairs. The group copied personal information about the site's user base, and threatened to release users' names and personally identifying information if Ashley Madison was not immediately shut down. On 18 and 20 August, the group leaked more than 25 gigabytes of company data, including user details." (Wikipedia)

"Because of the site's policy of not deleting users' personal information – including real names, home addresses, search history and credit card transaction records – many users feared being publicly shamed." (Wikipedia)

As the writing of this it is not yet public information how the hacking happened. It is known that a blackhat hacker group called "The Impact Team" distributed the data dumps. What is missing is that how the group get their hands on the data in the first place. However the extend of the data dump, including marketing documents, C-executive emails and and PayPal accounts suggest that this was either an inside job or the hackers spend a lot of time in the internal network.

The CEO of Avid Life Media claims the breach was by an insider who was not an employee.




Related evaluation points:

- team, Backend sensitive data access is limited

- team, Data scrubbing is used





Links:

- `Ashley Madison data breach (Wikipedia) <https://en.wikipedia.org/wiki/Ashley_Madison_data_breach>`_

- `Who Hacked Ashley Madison? (Krebs on Security) <http://krebsonsecurity.com/2015/08/who-hacked-ashley-madison/>`_

- `Second Ashley Madison dump prompts more inside-job speculation (The Register) <http://www.theregister.co.uk/2015/08/21/ashley_madison_inside_job_speculation/>`_

- `Ashley Madison CEO says hack was an inside job (Business Insider) <http://uk.businessinsider.com/ashley-madison-ceo-says-hack-was-an-inside-job-2015-7?r=US&IR=T>`_

- `An Insider Betrayed Ashley Madison (TechNewsWorld) <http://www.technewsworld.com/story/82455.html>`_





Bitly
==============================================================

Bitly unecrypted backups got compromised.

Bitly is a URL shortening service. The users can log in with their Facebook and Twitter accounts. In the incidence, the attacked gained access to offsite unencrypted database backups. It is assumed the database contained (OAuth) tokens to take actions in Facebook and Twitter on behalf of the user.

"On May 8 [2014], the Bitly security team learned of the potential compromise of Bitly user credentials from the security team of another technology company. We immediately began operating under the assumption that we had a breach and started the search for all possible compromise vectors." (More detail)

"They observed that we had an unusually high amount of traffic originating from our offsite database backup storage that was not initiated by Bitly." (More detail)

"We audited the security history for our hosted source code repository that contains the credentials for access to the offsite database backup storage and discovered an unauthorized access on an employee’s account.  We immediately enabled two-factor authentication for all Bitly accounts on the source code repository and began the process of securing the system against any additional vulnerabilities." (More detail)

"Hashed passwords were exposed but plain text passwords were not.  All passwords are salted and hashed.  If you registered, logged in or changed your password after January 8th, 2014, your password was converted to be hashed with BCrypt and HMAC using a unique salt.  Before that, it was salted MD5." (More detail)

The authoritative report "More detail", by Bitly, is now taken down (http://blog.bitly.com/#85169217199).




Related evaluation points:

- team, Two-factor authentication on critical services





Links:

- `Bitly users must change passwords <account credentials might have been compromised>`_

- `More detail (Bitly blog in the Wayback machine) <https://web.archive.org/web/20140515093107/http://blog.bitly.com/>`_




