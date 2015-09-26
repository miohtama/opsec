
.. This is a generated file from data/. DO NOT EDIT.

===========================================
Digital currencies and securities
===========================================

This chapter discusses about storing digital securities on the behalf of a customer. The securities here refer to crypto securities, assets and digital currencies, like Bitcoin. Usually these protocols have only non-reversable transaction mechanism.

Background
==========


The services serving high amount of crypto securities are especially valuable cybercrime targets. The securities transactions are non-reversible and non-traceable, making stealing the securities, laundering and liquiding them an easy operation.

Traditional credit and debit card backed transaction mechanism are usually reversible. Furthermore the institutions maintaining the balances have mechanism to address the stolen assets and the user funds are insured. Thus, the traditional transaction mechanism do not have the same issues to deal with.





.. _cold-wallet:

Cold wallet
==============================================================

**Cold wallet maintains the most of assets offline?** Yes / No

In the case of the compromised service, the attacker cannot get access to all assets and only can steal minor part of them, severely limiting the damage. Most of the assets are stored offline, in a non-connected computer, which has only physical offline access in a safe location. Thus, the attack taking all the assets would need a physical access to this device, making over-the-internet attacks impossible.


Applies for: Everyone



Related incidences:

- :ref:`bitstamp`




Links:


- `Cold storage in Bitcoin Wiki <https://en.bitcoin.it/wiki/Cold_storage>`_






.. _transaction-verification:

Transaction verification
==============================================================

**Outgoing transactions are verified by heurestics?** 

Outgoing transactions are verified by heurestics, so that unusual transactions need manual verification or other human interaction.
This prevents emptying the hot wallet in the case private keys or hot wallet API access is compromised.
TODO




Related incidences:

- :ref:`bitstamp`




Links:


- `BitGo <https://www.bitgo.com/>`_



- `BitGoD (Github) <https://github.com/BitGo/bitgod>`_






.. _multisignature-for-major-transactions:

Multisignature for major transactions
==============================================================

**Minimum of two parties are required to make major a customer assets transfer?** Yes / No

A sole person alone should not be able to embezzle the customer assets.

Digital currencies provide a multisignature mechanisms needing the approvement of at least two different parties to sign the transfer of the assets. Such a mechanism should be used any time a large fraction of customer assets are moved e.g. topping up the hot wallet from the cold wallet. This decreases the risk of corruption or blackmail attacks.



Applies for: Medium and large enterprises





Links:


- `Multisignature (Bitcoin Wiki) <https://en.bitcoin.it/wiki/Multisignature>`_





