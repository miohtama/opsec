
.. This is a generated file from data/. DO NOT EDIT.

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



