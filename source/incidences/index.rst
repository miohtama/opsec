
.. This is a generated file from data/. DO NOT EDIT.

==========
Incidences
==========

This chapter contains references to historical security breaches, their implications and what operational security measurements could have been taken to prevent them.



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

- :ref:`unsafe-file-attachments`

- :ref:`two-factor-authentication-on-server-login`

- :ref:`cold-wallet`

- :ref:`transaction-verification`





Links:

- `Hackers steal $5 million from major bitcoin exchange (Fortuna) <http://fortune.com/2015/01/05/bitstamp-bitcoin-freeze-hack/>`_

- `Major Bitcoin Exchange Bitstamp Goes Offline After Possible Hack (WIRED) <http://www.wired.com/2015/01/bitstamp-offline/>`_

- `Bitstamp Incident Report (Office of Inadequtae security) <http://www.databreaches.net/bitstamp-incident-report-february-2015/>`_





.. _ashley-madison:

Ashley Madison
==============================================================

*Date: 2015-07-01*

Ashley Madison, a service billed as enabling extramarital affairs, got comprehensibly compromised. A Canadian, Avid Life Media, was running a dating site for married people.

"In July 2015, a group calling itself "The Impact Team" stole the user data of Ashley Madison, a commercial website billed as enabling extramarital affairs. The group copied personal information about the site's user base, and threatened to release users' names and personally identifying information if Ashley Madison was not immediately shut down. On 18 and 20 August, the group leaked more than 25 gigabytes of company data, including user details." (Wikipedia)

"Because of the site's policy of not deleting users' personal information – including real names, home addresses, search history and credit card transaction records – many users feared being publicly shamed." (Wikipedia)

As the writing of this it is not yet public information how the hacking happened. It is known that a blackhat hacker group called "The Impact Team" distributed the data dumps. What is missing is that how the group get their hands on the data in the first place. However the extend of the data dump, including marketing documents, C-executive emails and and PayPal accounts suggest that this was either an inside job or the hackers spend a lot of time in the internal network.

The CEO of Avid Life Media claims the breach was by an insider who was not an employee.



Related evaluation points:

- :ref:`sensitive-data-access-limitations`

- :ref:`sensitive-data-access-logs`

- :ref:`data-scrubbing`





Links:

- `Ashley Madison data breach (Wikipedia) <https://en.wikipedia.org/wiki/Ashley_Madison_data_breach>`_

- `Who Hacked Ashley Madison? (Krebs on Security) <http://krebsonsecurity.com/2015/08/who-hacked-ashley-madison/>`_

- `Second Ashley Madison dump prompts more inside-job speculation (The Register) <http://www.theregister.co.uk/2015/08/21/ashley_madison_inside_job_speculation/>`_

- `Ashley Madison CEO says hack was an inside job (Business Insider) <http://uk.businessinsider.com/ashley-madison-ceo-says-hack-was-an-inside-job-2015-7?r=US&IR=T>`_

- `An Insider Betrayed Ashley Madison (TechNewsWorld) <http://www.technewsworld.com/story/82455.html>`_





.. _bitly:

Bitly
==============================================================

*Date: 2014-05-08*

Bitly unecrypted backups got compromised.

Bitly is a URL shortening service. The users can log in with their Facebook and Twitter accounts. In the incidence, the attacked gained access to offsite unencrypted database backups. It is assumed the database contained (OAuth) tokens to take actions in Facebook and Twitter on behalf of the user.

"On May 8 [2014], the Bitly security team learned of the potential compromise of Bitly user credentials from the security team of another technology company. We immediately began operating under the assumption that we had a breach and started the search for all possible compromise vectors." (More detail)

"They observed that we had an unusually high amount of traffic originating from our offsite database backup storage that was not initiated by Bitly." (More detail)

"We audited the security history for our hosted source code repository that contains the credentials for access to the offsite database backup storage and discovered an unauthorized access on an employee’s account.  We immediately enabled two-factor authentication for all Bitly accounts on the source code repository and began the process of securing the system against any additional vulnerabilities." (More detail)

"Hashed passwords were exposed but plain text passwords were not.  All passwords are salted and hashed.  If you registered, logged in or changed your password after January 8th, 2014, your password was converted to be hashed with BCrypt and HMAC using a unique salt.  Before that, it was salted MD5." (More detail)

The authoritative report "More detail", by Bitly, is now taken down (http://blog.bitly.com/#85169217199).



Related evaluation points:

- :ref:`two-factor-authentication-on-critical-services`

- :ref:`encrypted-server-data`





Links:

- `Bitly users must change passwords, account credentials might have been compromised <http://www.techtimes.com/articles/6773/20140510/bitly-users-must-change-passwords-account-credentials-might-have-been-compromised.htm>`_

- `More detail (Bitly blog in the Wayback machine) <https://web.archive.org/web/20140515093107/http://blog.bitly.com/>`_





.. _cloudflare:

CloudFlare
==============================================================

*Date: 2012-06-04*

Matthew Prince, the CEO of CloudFlare, a security proxy service company, had his personal Google email account hacked. The account was protected by two-factor authentication.

Google offers two-factor authentication on their web based email a.k.a. GMail. Two-factor authentication should protect against cases where the attacked somehow gains access to the password. In this case, the two-factor authentication is believed to be reset through social engineering AT&T customer support. Prince’s voicemail message was modified by the attacker in order to receive and record an automated phone call from Google with a audible code that could be used to reset his account.

The personal email account of Prince was the recovery email for Google Apps for Business. After gaining the access to Apps, the attacker could read some transaction email traffic, including password reset emails, which was BCC'ed to CloudFlare team. BCC feature was mostly for error diagnostics. The attacker performed password reset on 4Chan.org account, grabbed the password reset email, logged in to 4Chan account and then was able to redirect all 4Chan.org traffic to a page under the control of the attacker.



Related evaluation points:

- :ref:`two-factor-authentication-on-email`





Links:

- `The Four Critical Security Flaws that Resulted in Last Friday's Hack (CloudFlare) <https://blog.cloudflare.com/the-four-critical-security-flaws-that-resulte/>`_

- `Google Two-Factor Authentication Flaw Exposed Google Apps Customers (SecurityWeek) <http://www.securityweek.com/exclusive-google-two-factor-authentication-flaw-exposed-google-apps-customers>`_





.. _xcode:

XCode
==============================================================

*Date: 2015-09-17*

XCode is Apple's development tool for building iOS and OSX applications. A pirated version was distributed with an ability to infect all applications created with the pirated versions. Many official Chinese applications in App Store got rigged. The high valued targets included the official application of Baidu, a large Chinese search engine.

Apple's App Store review policies did not caught the malware and rigged applications passed the review.

The reason why Chinese developers used the pirated XCode in the first place is that the development tool is large (3GB) and downloading it from official Apple sources takes forever in China.



Related evaluation points:

- :ref:`software-comes-from-secure-sources`





Links:

- `Novel Malware XcodeGhost Modifies Xcode, Infects Apple iOS Apps and Hits App Store (PaloAlto Networks) <http://researchcenter.paloaltonetworks.com/2015/09/novel-malware-xcodeghost-modifies-xcode-infects-apple-ios-apps-and-hits-app-store/#>`_

- `Apple will host Xcode on Chinese servers following malware attack <http://mashable.com/2015/09/24/apple-xcode-china/>`_





.. _slack:

Slack
==============================================================

*Date: 2015-03-01*

Slack is a popular team communication tool among software companies and in US. The database of Slack got compromised, leading to the exposure of salted passwords.

After the breach Slack detected suspicious activity targetting some of its customers. Slack reseted the passwords for these customers. Furthermore, after the incident, Slack enabled two-factor authentication and kill switch as options for its users. Two-factor authentication was not an option before Slack got hacked.

Whether two-factor authentication effectively stops the attackers in the case of database breach is a subject to discussion. If the salted passwords are compromised you usually also lose the two-factor authentication tokens stored in the same database.



Related evaluation points:

- :ref:`password-storage-best-practices`

- :ref:`two-factor-authentication`

- :ref:`effective-session-kill`





Links:

- `March 2015 Security Incident and the Launch of Two Factor Authentication <http://slackhq.com/post/114696167740/march-2015-security-incident-and-launch-of-2fa>`_

- `Slack enables two-factor authentication following security breach <http://www.theverge.com/2015/3/27/8301031/slack-office-app-two-factor-authentication-secure>`_





.. _lastpass:

LastPass
==============================================================

*Date: 2015-06-10*

A popular password management service, LastPass, got compromised.

LastPass account email addresses, password reminders, server per user salts, and authentication hashes were compromised.

The salted user master passwords where exposed to the attacker. A weak master password could lead to the compromise of the whole password vault of a user. All users were prompted to change their master passwords. LastPass does third factor authentication on its users, claiming this could have protected the potential victims.



Related evaluation points:

- :ref:`password-manager`

- :ref:`password-storage-best-practices`

- :ref:`third-factor-authentication`





Links:

- `LastPass Security Notice <https://blog.lastpass.com/2015/06/lastpass-security-notice.html/>`_

- `Hack Brief: Password Manager LastPass Got Breached Hard <http://www.wired.com/2015/06/hack-brief-password-manager-lastpass-got-breached-hard/>`_





.. _chinese-android:

Asian Android phones
==============================================================

*Date: 2015-09-01*

Various (low budget) Asian Android phones ship with malware preinstalled. This includes brands available in western markets, like Huawei, Lenovo and Xiaomi.

G DATA security experts discovered over 26 Android phone models which are sold having malware preinstalled. Supply chain companies, operators or manufacturers themselves are suspected of planting the malware. The attacker siphons the user data and then resells it on the black markets to substitute the phone price. The malware is usually hidden in a legitimate app which is manipulated to contain malware as an add-on.



Related evaluation points:

- :ref:`third-party-devices`





Links:

- `G DATA Releases Mobile Malware Report for the Second Quarter of 2015 <https://www.gdata-software.com/g-data/newsroom/news/article/g-data-releases-mobile-malware-report-for-the-second-quarter-of-2015>`_

- `Chinese Android smartphones now shipping with pre-installed malware <http://www.scmagazineuk.com/chinese-android-smartphones-now-shipping-with-pre-installed-malware/article/436631/>`_





.. _nasa:

NASA
==============================================================

*Date: 2012-11-15*

NASA lost a laptop containing data on 10,000 users.

Personally identifiable information of at least 10,000 NASA employees and contractors remained at risk of compromise.

The laptop did not have whole disk encryption, making it possible for the thief to access all the data.

The incident prompted an immediate agency-wide initiative to implement full disk encryption on all NASA laptops.



Related evaluation points:

- :ref:`encrypted-computers`





Links:

- `NASA breach update: Stolen laptop had data on 10,000 users <http://www.computerworld.com/article/2493084/security0/nasa-breach-update--stolen-laptop-had-data-on-10-000-users.html>`_





.. _tor:

Tor
==============================================================

*Date: 2014-01-22*

Security researches detected Tor exit nodes performing man-in-the-middle attack on the traffic.

Tor is a layered network to obfuscate the source of the traffic i.e. hide your tracks. It is used by criminals, privacy advocates and security researchers. Tor relies on *exit nodes* where the traffic comes out from Tor network and connects to normal Internet.

Malicious Tor exit nodes where intercepting the traffic. They performed HTTP traffic snooping, HTTP -> HTTPS redirection interception and HTTPS man-in-the-middle with self-signed certificate. There are recorded cases where the victim accepted the invalid HTTPS certificate even though Firefox-based Tor browser presented a red warning screen with difficult options to proceed beyond it.



Related evaluation points:

- :ref:`https-tls-only`





Links:

- `What the "Spoiled Onions" paper means for Tor users <https://blog.torproject.org/blog/what-spoiled-onions-paper-means-tor-users>`_

- `Scientists detect “spoiled onions” trying to sabotage Tor privacy network <http://arstechnica.com/security/2014/01/scientists-detect-spoiled-onions-trying-to-sabotage-tor-privacy-network/>`_





.. _soho:

Soho
==============================================================

*Date: 2015-05-16*

Hackers hijack 300,000 SOHO routers with man-in-the-middle attacks.

SOHO routers were infected via drive-by download attacks and malvertising on popular websites. The initial drive-by attack exploited a CSRF flaw in the router administration page. When a victim behind the router visited a malicious site, a JavaScript payload reconfigured the routers.

The attackers modified the routers DNS settings so that everybody from the router network could be redirected to a malicious site. This puts all sensitive transactions made from the network to risk.



Related evaluation points:

- :ref:`https-tls-only`





Links:

- `Malware don't need Coffee <http://malware.dontneedcoffee.com/2015/05/an-exploit-kit-dedicated-to-csrf.html>`_

- `Exploit Kit Using CSRF to Redirect SOHO Router DNS Settings <https://threatpost.com/exploit-kit-using-csrf-to-redirect-soho-router-dns-settings/112993/#sthash.GRLJ8k7N.dpuf>`_

- `Hackers hijack 300,000 SOHO routers with man-in-the-middle attacks <http://www.v3.co.uk/v3-uk/news/2331953/hackers-hijack-300-000-soho-routers-with-man-in-the-middle-attacks>`_





.. _twitter:

Twitter
==============================================================

*Date: 2010-09-26*

Twitter allowed to post a tweet using a HTTP GET request.

The attacker created a worm which posted itself on behalf of the user when the users clicked a link they saw in their friends feed.



Related evaluation points:

- :ref:`cross-site-request-forgery-csrf`





Links:

- `CSRF attack strikes Twitter <https://nacin.com/2010/09/26/csrf-twitter/>`_

- `Don't Click The WTF Link On Twitter Unless You DO Like Sex With Goats <http://techcrunch.com/2010/09/26/dont-click-the-wtf-link-on-twitter-unless-you-do-like-sex-with-goats/>`_





.. _sebastian:

Sebastian
==============================================================

*Date: 2013-10-23*

A hacker group TeamBerserk claimed to have stolen more than 100k USD via SQL injeciton injection from Sebastian, a Californian based ISP.

Through SQL injection, the attackers downloaded the list of ISP's customers, their usernames and passwords in clear text.
The attackers exploited the fact the users recycle the same password and used usernames and passwords login GMail, PayPal, CitiBank, etc. The attack was demostrated on a video uploaded to MEGA (now defunct).

Tom Dominico, marketing and business development manager for Sebastian, told “We are aware of the claims that our system has been compromised. We have checked with our service providers and their records indicate that no such attack has occurred. We take the security of our customer's personal information very seriously and are constantly working to keep them safe from online threats.”



Related evaluation points:

- :ref:`database-injection`

- :ref:`password-storage-best-practices`





Links:

- `Hacker group claims to have looted $100k via SQL injection attack (SC Magazine) <http://www.scmagazine.com/hacker-group-claims-to-have-looted-100k-via-sql-injection-attack/article/317412/>`_

- `Hacker stole $100,000 from Users of California based ISP using SQL Injection (The Hacker News) <http://thehackernews.com/2013/10/hacker-stole-100000-from-users-of.html>`_





.. _facebook:

Facebook
==============================================================

*Date: 2011-04-11*

Facebook status update functionality did not properly escape parameters.

It was possible to post HTML content which was not properly sanitized which further loaded JavaScript. The loaded JavaScript then took actions on the behalf of the user.
This allowed the attacker to create a worm which propagated through Facebook walls.

The root cause was is that PHP's built-in `parse_url()` function does not properly check for malformed URLs. The issue still exists in PHP today and is only addresses in the documentation.



Related evaluation points:

- :ref:`cross-site-scripting-xss`





Links:

- `Recent Facebook XSS Attacks Show Increasing Sophistication <http://theharmonyguy.com/oldsite/2011/04/21/recent-facebook-xss-attacks-show-increasing-sophistication/>`_

- `Bug #54600 <https://bugs.php.net/bug.php?id=54600>`_





.. _veeder-root:

Veeder-Root
==============================================================

*Date: 2015-01-23*

Gas stations use automated tank gauges (ATGs) for remote control and diagnostics. Automated tank gauges were exposed to Internet through serial port servers that map ATG serial interfaces to the Internet-accessible TCP port.

Most of ATGs were manufactured bt Veeder-Root, a petroleum equipment service company. The system allows maximum of six letters password, but often the password is not set.

The attacker could change the calibration and make the tank report full or empty. Worst case the attacker could shut down the pumps.



Related evaluation points:

- :ref:`non-public-administration-site`





Links:

- `Internet attack could shut down US gas stations <http://arstechnica.com/security/2015/01/internet-attack-could-shut-down-us-gasoline-stations/>`_

- `Thousands of U.S. gas stations exposed to Internet attacks <http://www.csoonline.com/article/2874230/cybercrime-hacking/thousands-of-us-gas-stations-exposed-to-internet-attacks.html>`_

- `Mideast Hackers May Be Attacking US Gas Stations <http://bit.ly/1eVcSCD>`_





.. _icloud:

Apple iCloud
==============================================================

*Date: 2014-09-01*

Apple iCloud service was subject to login brute force attack leading to the compromise of several celebrity accounts.

Apple did not follow the security best practices to prevent brute forced login attempts. Find my iPhone, a part of iCloud services, allowed unthrottled login attempts.

Later the private photos of victims, most of them being celebrities, were leaked in Internet, causing harm to these people.

Apple did not apologize.



Related evaluation points:

- :ref:`two-factor-authentication-on-critical-services`

- :ref:`two-factor-authentication`

- :ref:`brute-force-login-prevention`





Links:

- `Apple Media Advisory - Update to Celebrity Photo Investigation <http://www.apple.com/pr/library/2014/09/02Apple-Media-Advisory.html>`_

- `Apple patches 'Find My iPhone' exploit (ZDNet) <http://www.zdnet.com/article/apple-patches-find-my-iphone-exploit/>`_

- `Find My iPhone exploit may be to blame for celebrity photo hacks (Engadget) <http://www.engadget.com/2014/09/01/find-my-iphone-exploit/>`_

- `Was iCloud vulnerable... (Quora) <https://www.quora.com/Was-iCloud-vulnerable-patched-9-1-14-to-a-brute-force-attack-because-unlimited-password-attempts-were-allowed-and-if-so-is-Apple-responsible-for-the-Fappening>`_





.. _sms-malware:

SMS intercepting trojans
==============================================================

*Date: 2015-09-01*


Multiple malware and trojan programs are observed to steal SMS two-factor authentication codes. These mostly target banks and popular services. Malware is mostly Android ecosystem issue, though other operating systems, especially jailbroken ones, can be infected.

When the user receives two-factor authentication codes over SMS they are forwared to the attacker. Furthermore the malware intercepts logins and passwords to popular services.



Related evaluation points:

- :ref:`two-factor-authentication`





Links:

- `New Banking Trojan Targets Android, Steals SMS <https://threatpost.com/new-banking-trojan-targets-android-steals-sms/110819/>`_

- `Zeus Banking Trojan Hits Android Phones <http://www.informationweek.com/mobile/zeus-banking-trojan-hits-android-phones/d/d-id/1098909?>`_





.. _instagram:

Instagram
==============================================================

*Date: 2014-12-08*

Instagram deleted millions of accounts.

Due to lax account creation process, A large proportion of Instagram accounts were fake and automatically created robot accounts. The fake accounts can be exploited as fake followers or to send spam. Social media PR companies may buy fake followers to inflate their campaign success rates.

It can be speculated that even if being aware of the severity of the issue Instagram was not in rush to delete the fake accounts before acquisition by Facebook to inflate their market value.

Some celebrities lost up to 90% of their followers. Instagram's own Instagram account lost 30% of its followers.



Related evaluation points:

- :ref:`account-verification-process`





Links:

- `Instagram mass-deletes spam accounts, users freak out <http://www.digitaltrends.com/social-media/instagram-mass-deletes-spam-accounts-users-freak/>`_

- `Chaos Ensues As Instagram Deletes Millions Of Accounts <http://uk.businessinsider.com/chaos-ensues-as-instagram-deletes-millions-of-accounts-2014-12?r=US&IR=T>`_





.. _steam:

Steam
==============================================================

*Date: 2015-07-25*

A flaw in password reset procedure allowed login to any Steam account without two-factor authentication.

A bug in Steam, a popular gaming platform and store by Valve, allowed to reset the password of the user without entering the verification token send to the email. User accounts with two-factor authentication enabled were protected.

One could submit empty ("") verification code and it passed as valid.

Valve forced the users with suspected malicious password reset to go through additional password reset procedure.



Related evaluation points:

- :ref:`user-audit-logs`





Links:

- `Steam accounts hacked during security lapse "bug" (TrustedReviews) <http://www.trustedreviews.com/news/steam-accounts-hacked-during-security-lapse-bug#Jih1G6ugCR2SeEOV.99>`_

- `Valve patches huge password reset hole that allowed anyone to hijack Steam accounts (ComputerWorld) <http://www.computerworld.com/article/2953016/cybercrime-hacking/valve-patches-huge-password-reset-hole-that-allowed-anyone-to-hijack-steam-accounts.html>`_





.. _hacking-team:

Hacking Team
==============================================================

*Date: 2015-06-05*

Hacking Team was a company selling offensive intrusion and surveillance capabilities to governments. Hacking Team got compromised, all 400GB of internal data leaked.

All the stolen information was likely accessed via the compromised computers of Christian Pozzi and Mauro Romeo, two Hacking Team’s sysadmins.

The leaked data demostrated Hacking Team operations security standards were not high. Weak password policies, lack of sensitive data access limitations and bad software development practices. For example, the customer software contained a hidden switch to disable it. This switch was exposed in the leak, forcing all the customers to stop using the software.

As the writing of this the attacker is still not known.



Related evaluation points:

- :ref:`password-manager`

- :ref:`sensitive-data-access-limitations`

- :ref:`password-storage-best-practices`





Links:

- `Hacking Team (Wikipedia) <https://en.wikipedia.org/wiki/Hacking_Team>`_

- `Hacking Team hacked, attackers claim 400GB in dumped data (CSO Online) <http://www.csoonline.com/article/2943968/data-breach/hacking-team-hacked-attackers-claim-400gb-in-dumped-data.html>`_

- `Hacking Team goes to war against former employees, suspects some helped hackers (Ars Technica) <http://arstechnica.com/security/2015/07/italian-prosecutors-investigate-former-hacking-team-employees-for-role-in-hack/>`_

- `Hacking Team’s KillSwitch – Disabling the Galileo RCS remotely and silently (4Armed) <https://www.4armed.com/blog/hacking-teams-killswitch-disabling-galileo-rcs-remotely-silently/>`_





.. _cryptoine:

Cryptoine
==============================================================

*Date: 2015-04-04*

A race condition existed in the software of Cryptoine, now defunct Bitcoin exchange.

The race condition allowed the attacker to drain all hot wallets.

This damage caused the closure of the exchange.



Related evaluation points:

- :ref:`cold-wallet`

- :ref:`race-condition-prevention`





Links:

- `Cryptoine.com HACKED [race condition bug] [exchange closed] (BitcoinTalk) <https://bitcointalk.org/index.php?topic=1001408.0>`_

- `Bitcoin exchange Cryptoine hacked (ZDNet) <http://www.zdnet.com/article/bitcoin-exchange-cryptoine-hacked/>`_





.. _starbucks:

Starbucks
==============================================================

*Date: 2015-05-21*

A researcher was able to steal money from Starbucks by exploiting a race condition in its gift card value-transfer protocol.

By doing two gift card value transfers at the same time, the researcher was able to duplicate the transfer and duplicate the balance on the accounts of the researcher.

The researched disclosed the exploit to Starbucks who did not thank the researcher for his efforts.



Related evaluation points:

- :ref:`race-condition-prevention`





Links:

- `Hacking Starbucks for unlimited coffee (Egor Homakov) <http://sakurity.com/blog/2015/05/21/starbucks.html>`_

- `Race Condition Exploit in Starbucks Gift Cards (Schneier on Security) <https://www.schneier.com/blog/archives/2015/05/race_condition_.html>`_





.. _purse:

PurseIO
==============================================================

*Date: 2015-07-31*

Guessable ids allowed the researcher to scrape private orders from PurseIO service.

PurseIO is a service where one can pay in Bitcoin for somebody to ask him or her to make an Amazon order on the behalf of the payer.

PurseIO AJAX call endpoint had guessable id sequence, allowing the researcher to scrape semi-private data.



Related evaluation points:

- :ref:`authorization-and-permission-framework`

- :ref:`non-guessable-ids`





Links:

- `Purse.io Data Spelunking <https://gist.github.com/ummjackson/e0abc55bdbe3d5ae9a03>`_





.. _coinbase:

Coinbase
==============================================================

*Date: 2014-04-01*

Coinbase has a Request money feature which sends email to a third party through Coinbase service.

Coinbase did not throttle this feature allowing anyone to send infinite number of emails through Coinbase.
Furthermore the feature exposed if any email had an account on Coinbase or not.

The security researcher reported the issue to Coinbase, who marked the issue as "WONTFIX" one month later. It was not until the publicly demostrated exploit when Coinbase took action.

Coinbase started to throttle the feature. Coinbase took a PR hit because the community did not find the initial response of Coinbase sufficient. The community questioned the security integrity of Coinbase as a whole.



Related evaluation points:

- :ref:`whitehat-program`

- :ref:`flood-action-throttle`





Links:

- `Coinbase design allows for mass, targeted phishing of its users (Shubham Shah) <http://blog.shubh.am/full-disclosure-coinbase-security/>`_

- `Coinbase denies security breach, defends spamming-friendly features (Help Net Security) <http://www.net-security.org/secworld.php?id=16628>`_

- `Update on Coinbase Data Security <https://blog.coinbase.com/2014/04/01/update-on-coinbase-data-security/>`_




