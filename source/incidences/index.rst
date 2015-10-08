
.. This is a generated file from data/. DO NOT EDIT.

==============================
Security incidence reference
==============================

This chapter contains references to historical security incidences, why they happened, the implications and what operational security measurements could have been taken to prevent them.

.. attention ::

    *All Internet service incidences listed here could have been avoided by following the security practices presented in this guide.*

Some of the incidences are not directly related to a particular Internet service, e.g. SMS intercepting, but the case reflects the associated security risk it may pose to any Internet service and its user.

Incidences
===================

Number of incidence summaries: **31**

Compromised user accounts: **39.29M**

Lost assets: **457.19M USD**

Bankcrupted companies: **1**

Fired employees: **0**

.. raw :: html

    <table class="table-incidences">
        <thead>
            <tr>
                <th>Name</th>
                <th>Date</th>
                <th>Related security assessment points</th>
            </tr>
        </thead>
        <tbody>
            
                <tr>
                    <td>
                        <a href="icloud.html">Apple iCloud</a>
                    </td>
                    <td class="col-date">
                        2014-09-01
                    </td>
                    <td>
                        
                            <p>
                                <a href="../user/index.html#two-factor-authentication">The service users are encouraged to use two-factor authentication</a>
                            </p>
                        
                            <p>
                                <a href="../user/index.html#brute-force-login-prevention">Service login attempts are throttled in multiple ways</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="ashley-madison.html">Ashley Madison</a>
                    </td>
                    <td class="col-date">
                        2015-07-01
                    </td>
                    <td>
                        
                            <p>
                                <a href="../team/index.html#audited-server-login-keys">A real-time method of maintaining and revoking keys across all servers</a>
                            </p>
                        
                            <p>
                                <a href="../team/index.html#limited-sensitive-data-access">Sensitive data access by administrators is limited</a>
                            </p>
                        
                            <p>
                                <a href="../team/index.html#logged-sensitive-data-access">Sensitive data access by administrators is logged</a>
                            </p>
                        
                            <p>
                                <a href="../team/index.html#data-scrubbing">Data dumps are cleaned from sensitive information</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="chinese-android.html">Asian Android phones</a>
                    </td>
                    <td class="col-date">
                        2015-09-01
                    </td>
                    <td>
                        
                            <p>
                                <a href="../team/index.html#third-party-devices">The team members do not use third party devices for logging in</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="bitly.html">Bitly</a>
                    </td>
                    <td class="col-date">
                        2014-05-08
                    </td>
                    <td>
                        
                            <p>
                                <a href="../team/index.html#two-factor-authentication-on-critical-services">Infrastructure services requires two-factor authentication</a>
                            </p>
                        
                            <p>
                                <a href="../infrastructure/index.html#encrypted-server-data">Data is stored on encrypted partitions</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="bitpay.html">Bitpay</a>
                    </td>
                    <td class="col-date">
                        2015-09-17
                    </td>
                    <td>
                        
                            <p>
                                <a href="../team/index.html#basic-security-practices">The team members follow the basic IT security practices</a>
                            </p>
                        
                            <p>
                                <a href="../team/index.html#minimized-email-usage">Email is not used for internal communications</a>
                            </p>
                        
                            <p>
                                <a href="../team/index.html#two-factor-authentication-on-email">The team member work and personal email accounts require two-factor authentication to log in</a>
                            </p>
                        
                            <p>
                                <a href="../assets/index.html#multisignature-for-major-withdraws">Minimum of two parties are required for a large withdraw</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="bitstamp.html">Bitstamp</a>
                    </td>
                    <td class="col-date">
                        2015-01-04
                    </td>
                    <td>
                        
                            <p>
                                <a href="../team/index.html#dangerous-file-attachments">Potentially dangerous file attachments are handled securely</a>
                            </p>
                        
                            <p>
                                <a href="../team/index.html#two-factor-authentication-on-server-login">The terminal access to the server requires two-factor authentication</a>
                            </p>
                        
                            <p>
                                <a href="../assets/index.html#cold-wallet">Cold wallet maintains most assets offline</a>
                            </p>
                        
                            <p>
                                <a href="../assets/index.html#transaction-verification">Withdraws are verified by heuristics</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="blockchaininfo.html">Blockchain.info</a>
                    </td>
                    <td class="col-date">
                        2015-06-01
                    </td>
                    <td>
                        
                            <p>
                                <a href="../user/index.html#third-factor-authentication">The login process goes through additional check in abnormal circumstances</a>
                            </p>
                        
                            <p>
                                <a href="../user/index.html#re-authentication-on-sensitive-actions">Sensitive actions should prompt for authentication again</a>
                            </p>
                        
                            <p>
                                <a href="../user/index.html#trademark-protection">Is the name of the service trademarked?</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="cloudflare.html">CloudFlare</a>
                    </td>
                    <td class="col-date">
                        2012-06-04
                    </td>
                    <td>
                        
                            <p>
                                <a href="../team/index.html#two-factor-authentication-on-email">The team member work and personal email accounts require two-factor authentication to log in</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="coinbase.html">Coinbase</a>
                    </td>
                    <td class="col-date">
                        2014-04-01
                    </td>
                    <td>
                        
                            <p>
                                <a href="../web/index.html#whitehat-program">The service has a public whitehat or security bounty program</a>
                            </p>
                        
                            <p>
                                <a href="../user/index.html#flood-action-throttle">Actions sending messages to other users are throttled</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="cryptoine.html">Cryptoine</a>
                    </td>
                    <td class="col-date">
                        2015-04-04
                    </td>
                    <td>
                        
                            <p>
                                <a href="../assets/index.html#cold-wallet">Cold wallet maintains most assets offline</a>
                            </p>
                        
                            <p>
                                <a href="../assets/index.html#race-condition-prevention">A systematic development method prevents race conditions</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="facebook.html">Facebook</a>
                    </td>
                    <td class="col-date">
                        2011-04-11
                    </td>
                    <td>
                        
                            <p>
                                <a href="../web/index.html#cross-site-scripting-xss">The software is written in a manner that there is no possibility of cross-site scripting attack</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="hacking-team.html">Hacking Team</a>
                    </td>
                    <td class="col-date">
                        2015-06-05
                    </td>
                    <td>
                        
                            <p>
                                <a href="../team/index.html#password-manager">The team members use password manager</a>
                            </p>
                        
                            <p>
                                <a href="../team/index.html#limited-sensitive-data-access">Sensitive data access by administrators is limited</a>
                            </p>
                        
                            <p>
                                <a href="../web/index.html#password-storage-best-practices">The user passwords and two-factor seeds are hashed and salted against bruteforcing</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="instagram.html">Instagram</a>
                    </td>
                    <td class="col-date">
                        2014-12-08
                    </td>
                    <td>
                        
                            <p>
                                <a href="../user/index.html#account-verification-process">The creation of bogus accounts is prevented</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="lastpass.html">LastPass</a>
                    </td>
                    <td class="col-date">
                        2015-06-10
                    </td>
                    <td>
                        
                            <p>
                                <a href="../team/index.html#password-manager">The team members use password manager</a>
                            </p>
                        
                            <p>
                                <a href="../web/index.html#password-storage-best-practices">The user passwords and two-factor seeds are hashed and salted against bruteforcing</a>
                            </p>
                        
                            <p>
                                <a href="../user/index.html#third-factor-authentication">The login process goes through additional check in abnormal circumstances</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="linode.html">Linode</a>
                    </td>
                    <td class="col-date">
                        2012-03-01
                    </td>
                    <td>
                        
                            <p>
                                <a href="../team/index.html#passphrase-on-server-login-keys">The terminal access to the server requires passphrase protected key</a>
                            </p>
                        
                            <p>
                                <a href="../team/index.html#two-factor-authentication-on-server-login">The terminal access to the server requires two-factor authentication</a>
                            </p>
                        
                            <p>
                                <a href="../infrastructure/index.html#encrypted-server-data">Data is stored on encrypted partitions</a>
                            </p>
                        
                            <p>
                                <a href="../assets/index.html#cold-wallet">Cold wallet maintains most assets offline</a>
                            </p>
                        
                            <p>
                                <a href="../assets/index.html#transaction-verification">Withdraws are verified by heuristics</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="maxcdn.html">MaxCDN</a>
                    </td>
                    <td class="col-date">
                        2013-07-02
                    </td>
                    <td>
                        
                            <p>
                                <a href="../team/index.html#passphrase-on-server-login-keys">The terminal access to the server requires passphrase protected key</a>
                            </p>
                        
                            <p>
                                <a href="../team/index.html#audited-server-login-keys">A real-time method of maintaining and revoking keys across all servers</a>
                            </p>
                        
                            <p>
                                <a href="../web/index.html#https-tls-only">The service is HTTPS-only with security HTTP headers</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="mtgox.html">Mt. Gox</a>
                    </td>
                    <td class="col-date">
                        2014-02-01
                    </td>
                    <td>
                        
                            <p>
                                <a href="../assets/index.html#proof-of-solvency">The service is able to perform Proof-of-solvency</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="nasa.html">NASA</a>
                    </td>
                    <td class="col-date">
                        2012-11-15
                    </td>
                    <td>
                        
                            <p>
                                <a href="../team/index.html#encrypted-computers">The work computers have disk encryption</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="patreon.html">Patreon</a>
                    </td>
                    <td class="col-date">
                        2015-09-01
                    </td>
                    <td>
                        
                            <p>
                                <a href="../team/index.html#limited-sensitive-data-access">Sensitive data access by administrators is limited</a>
                            </p>
                        
                            <p>
                                <a href="../team/index.html#data-scrubbing">Data dumps are cleaned from sensitive information</a>
                            </p>
                        
                            <p>
                                <a href="../web/index.html#non-public-administration-site">The administration site is not accessible or known to public</a>
                            </p>
                        
                            <p>
                                <a href="../infrastructure/index.html#internal-services-not-exposed">Internal servers, services and domains cannot be discovered through public records</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="purse.html">PurseIO</a>
                    </td>
                    <td class="col-date">
                        2015-07-31
                    </td>
                    <td>
                        
                            <p>
                                <a href="../web/index.html#authorization-and-permission-framework">Private pages and data access is protected by authorization framework</a>
                            </p>
                        
                            <p>
                                <a href="../web/index.html#non-guessable-ids">Publicly exposed ids are not guessable</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="sms-malware.html">SMS intercepting trojans</a>
                    </td>
                    <td class="col-date">
                        2015-09-01
                    </td>
                    <td>
                        
                            <p>
                                <a href="../user/index.html#two-factor-authentication">The service users are encouraged to use two-factor authentication</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="sebastian.html">Sebastian</a>
                    </td>
                    <td class="col-date">
                        2013-10-23
                    </td>
                    <td>
                        
                            <p>
                                <a href="../web/index.html#database-injection">The software uses a framework for database queries</a>
                            </p>
                        
                            <p>
                                <a href="../web/index.html#password-storage-best-practices">The user passwords and two-factor seeds are hashed and salted against bruteforcing</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="slack.html">Slack</a>
                    </td>
                    <td class="col-date">
                        2015-03-01
                    </td>
                    <td>
                        
                            <p>
                                <a href="../web/index.html#password-storage-best-practices">The user passwords and two-factor seeds are hashed and salted against bruteforcing</a>
                            </p>
                        
                            <p>
                                <a href="../user/index.html#two-factor-authentication">The service users are encouraged to use two-factor authentication</a>
                            </p>
                        
                            <p>
                                <a href="../user/index.html#effective-session-kill">When the user account is deactivated or changed, the related sessions are dropped</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="soho.html">Soho</a>
                    </td>
                    <td class="col-date">
                        2015-05-16
                    </td>
                    <td>
                        
                            <p>
                                <a href="../web/index.html#https-tls-only">The service is HTTPS-only with security HTTP headers</a>
                            </p>
                        
                            <p>
                                <a href="../web/index.html#cross-site-request-forgery-csrf">The software is written in a manner that it doesn't accept cross-site requests</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="squirrelmail.html">SquirrelMail</a>
                    </td>
                    <td class="col-date">
                        2007-12-18
                    </td>
                    <td>
                        
                            <p>
                                <a href="../team/index.html#software-installation-from-safe-sources">Software is installed from known good sources</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="starbucks.html">Starbucks</a>
                    </td>
                    <td class="col-date">
                        2015-05-21
                    </td>
                    <td>
                        
                            <p>
                                <a href="../web/index.html#whitehat-program">The service has a public whitehat or security bounty program</a>
                            </p>
                        
                            <p>
                                <a href="../assets/index.html#race-condition-prevention">A systematic development method prevents race conditions</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="steam.html">Steam</a>
                    </td>
                    <td class="col-date">
                        2015-07-25
                    </td>
                    <td>
                        
                            <p>
                                <a href="../user/index.html#user-audit-logs">The service retains audit logs of sensitive user actions</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="tor.html">Tor</a>
                    </td>
                    <td class="col-date">
                        2014-01-22
                    </td>
                    <td>
                        
                            <p>
                                <a href="../web/index.html#https-tls-only">The service is HTTPS-only with security HTTP headers</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="twitter.html">Twitter</a>
                    </td>
                    <td class="col-date">
                        2010-09-26
                    </td>
                    <td>
                        
                            <p>
                                <a href="../web/index.html#cross-site-request-forgery-csrf">The software is written in a manner that it doesn't accept cross-site requests</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="veeder-root.html">Veeder-Root</a>
                    </td>
                    <td class="col-date">
                        2015-01-23
                    </td>
                    <td>
                        
                            <p>
                                <a href="../web/index.html#non-public-administration-site">The administration site is not accessible or known to public</a>
                            </p>
                        
                    </td>
                </tr>
            
                <tr>
                    <td>
                        <a href="xcode.html">XCode</a>
                    </td>
                    <td class="col-date">
                        2015-09-17
                    </td>
                    <td>
                        
                            <p>
                                <a href="../team/index.html#software-installation-from-safe-sources">Software is installed from known good sources</a>
                            </p>
                        
                    </td>
                </tr>
            
        </tbody>
    </table>

Indicent index
==============

.. toctree::
    :maxdepth: 2

    icloud

    ashley-madison

    chinese-android

    bitly

    bitpay

    bitstamp

    blockchaininfo

    cloudflare

    coinbase

    cryptoine

    facebook

    hacking-team

    instagram

    lastpass

    linode

    maxcdn

    mtgox

    nasa

    patreon

    purse

    sms-malware

    sebastian

    slack

    soho

    squirrelmail

    starbucks

    steam

    tor

    twitter

    veeder-root

    xcode




