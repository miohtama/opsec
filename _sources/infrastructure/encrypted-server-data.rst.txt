
.. This is a generated file from data/. DO NOT EDIT.

.. _encrypted-server-data:

Encrypted server data
==============================================================

**Data is stored on encrypted partitions?** 

All data should be stored on encrypted partitions or files. In the case of unauthorized physical access or unauthorized reboot, the data cannot be compromised. Encryption should also apply for backups and other offsite files.

Data on encrypted partitions protect against:

* Hosting provider attacks or social engineering attacks against the hosting provider in which the root password is reset through single-user mode reboot

* Law enforcement attacks in which the servers are physically confiscated

Disk encryption protects data when the server is offline. All sensitive databases should reside on the partitions which are not accessible if the physical machine is compromised.

If the server is rebooted without authorization, the server should ask for a passphrase to decrypt the data partitions. The easiest way to achieve this is to have separate partitions for boot volume and data volume. By having separate "high" and "low" states, the server cannot enter into the state with access to data unless an authorized person enters a passphrase through a terminal.

All unaccounted reboots should be suspicious, as when the server is offline the boot mechanism can be compromised to record the data decryption keys.

.. note ::

  Virtual machines, like those provided by Amazon EC2 or Digital Ocean, are ultimately unsafe. It's possible to make a silent copy of a virtual machine and its disk, even if encrypted, without the authorization of the server owner. If the adversaries include law enforcement agencies and nation state actors, it is recommended to use physical servers with chassis removal detection in a locked rack.





Related incidences:

- :ref:`bitly`

- :ref:`linode`




Links:


- `How To Use DM-Crypt to Create an Encrypted Volume on an Ubuntu (Digital Ocean) <https://www.digitalocean.com/community/tutorials/how-to-use-dm-crypt-to-create-an-encrypted-volume-on-an-ubuntu-vps>`_



- `Duplicity, encrypting backup utility <http://duplicity.nongnu.org/>`_



