
.. This is a generated file from data/. DO NOT EDIT.

===========================================
Digital currencies and securities
===========================================

This chapter discusses the security aspects of storing and handling digital currencies and securities like Bitcoin.

Background
==========


Digital currency services are especially attractive cybercrime targets. Digital currency transactions are anonymous, non-reversible and non-traceable. This makes stealing, laundering and liquidating digital currencies very easy for criminals. The non-reversable transaction mechanism complicates attacks, as often the services can neither chargeback lost assets nor reimburse customer losses.

Traditional credit card, debit card and wire transfer-backed transaction mechanisms are more merciful. Such transactions can be reversed, making it harder to liquidate stolen assets. Anti-money-laundering regulation ensures that it is not possible to move assets without leaving a trace for investigation. Furthermore, the institutions issuing cards and bank accounts have mechanisms to address fraud, co-operate with police and insure funds. For example, the compromise of an e-commerce site poses relatively little risk to its owners and customers unless the site was maintaining a balance in digital currencies.

Thus, services dealing with digital currencies and securities should approach security matters with tremendous seriousness. History shows that companies possessing millions of dollars of funding to address security still fail in basic executio
 (:ref:`bitstamp`, :ref:`bitpay`).





.. _cold-wallet:

Cold wallet
==============================================================

**Cold wallet maintains most assets offline?** Yes / No

Cold wallet is a system in which private keys for digital assets are stored on a computer, not connected to the Internet. To move the assets, somebody has to go to the computer physically and make the transaction.

The opposite of cold wallet is hot wallet, which is continuously running on the server and accessible online. Hot wallet assets are instantly liquid; most customer facing transactions happen in the hot wallet. When the hot wallet gets "too full," assets are moved to the cold wallet to make them safe. On the other hand, when the hot wallet is drying up due to customer withdraws, it must be topped up from the cold wallet.

In case of a service compromise, the attacker can only drain the hot wallet, severely limiting the amount of potentially stolen funds.



Applies for: Everyone



Related incidences:

- :ref:`linode`

- :ref:`bitstamp`

- :ref:`cryptoine`




Links:


- `Cold storage in Bitcoin Wiki <https://en.bitcoin.it/wiki/Cold_storage>`_






.. _race-condition-prevention:

Race condition prevention
==============================================================

**A systematic development method prevents race conditions?** Yes / No

A systematic development method is applied to all financial transactions so that race conditions cannot compromise transaction integrity. Otherwise exploiting the race condition allows the attacker to manipulate account balances.

For all financial transactions:

* Optimistic database-level transaction isolation is applied or...

* Pessimistic application level locks are applied.

The software should be developed in such a manner that there is only one function to make transfers out from the system or within the system. This function has a locking mechanism such that simultaneous transactions from the same account cannot compromise the atomicity, leading to double top up, double withdraw or account overdrawn.





Related incidences:

- :ref:`cryptoine`

- :ref:`starbucks`




Links:


- `Lock (database) (Wikipedia) <https://en.wikipedia.org/wiki/Lock_%28database%29>`_



- `Race condition (Wikipedia) <https://en.wikipedia.org/wiki/Race_condition>`_



- `Atomicity (Wikipedia) <https://en.wikipedia.org/wiki/Atomicity_(database_systems)>`_



- `Transaction Isolation (PostgreSQL) <http://www.postgresql.org/docs/9.1/static/transaction-iso.html>`_



- `How I stole roughly 100 BTC from an exchange and how I could have stolen more <https://www.reddit.com/r/Bitcoin/comments/1wtbiu/how_i_stole_roughly_100_btc_from_an_exchange_and/>`_






.. _transaction-verification:

Transaction verification
==============================================================

**Withdraws are verified by heuristics?** 

Withdraws are verified by heuristics so that unusual outgoing transactions need another round of authorization from the customer or human interaction from the support team.

Outgoing transaction verification provides an additional layer of protection against asset theft:

* Customer withdraws are verified. If the parameters of the transaction do not match prior customer activity and a malicious withdraw is suspected, the customer must reauthorize the transaction (see :ref:`third-factor-authentication`).

* How wallet drain attacks are prevented, as the heuristics would detect such and stop them.

Transaction verification is usually implemented as a multi-signature service with a third party. A third party holds one key required to make the transaction. When a transaction is created, the third-party service checks the transaction parameters against known good rules. If the transaction looks okay, the third-party service signs its part of the transaction. Because the third party is independent and specialized in the transaction verification process, it is unlikely that the attacker would manage to compromise it, too.





Related incidences:

- :ref:`bitstamp`

- :ref:`linode`




Links:


- `BitGo <https://www.bitgo.com/>`_



- `BitGoD (Github) <https://github.com/BitGo/bitgod>`_






.. _multisignature-for-major-withdraws:

Multisignature for major withdraws
==============================================================

**A minimum of two parties are required for a large withdraw?** Yes / No

A sole person alone should not be able to compromise the cold wallet or customer assets. Requiring authorization from two different people makes it less likely that one person disappears with all the customer assets.

Digital currencies provide a multi-signature mechanisms. A withdraw action can be set to require minimum of two different parties to confirm it. Such a mechanism should be used any time a large fraction of assets are moved e.g. topping up the hot wallet from the cold wallet.



Applies for: Medium and large enterprises



Related incidences:

- :ref:`bitpay`




Links:


- `Multisignature (Bitcoin Wiki) <https://en.bitcoin.it/wiki/Multisignature>`_






.. _proof-of-solvency:

Proof of solvency
==============================================================

**The service is able to perform Proof-of-solvency?** Yes / No

Proof of solvency (PoS) is a scheme designed to let users verify the solvency of online websites which accept Bitcoin deposits in a way that doesn't compromise the privacy of users.

Proof of solvency is used as a public proof to verify that the service does not run as a fractional reserve, e.g., some of the customer assets could not be withdrawn on a given moment. It is mostly used by Bitcoin exchanges to prove that they still have the assets that the customers have deposited.

The current proof of solvency schemes usually involves:

* A (merkle tree) hashing scheme

* A third-party auditor

* A public statement

The third party verifies that the exchange was controlled in all given Bitcoin addresses and that they have more unspent Bitcoins than claimed total customer assets.

The service should be able to perform a proof of solvency audit, at least internally.



Applies for: Medium and large enterprises



Related incidences:

- :ref:`mtgox`




Links:


- `Proving Your Bitcoin Reserves (Zak Wilcox) <https://iwilcox.me.uk/2014/proving-bitcoin-reserves>`_



- `Proof of Solvency specification <https://github.com/olalonde/proof-of-solvency>`_



- ` <Bitfinex Passes Stefan Thomas's Proof Of Solvency Audit ()>`_





