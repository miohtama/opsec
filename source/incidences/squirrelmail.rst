
.. This is a generated file from data/. DO NOT EDIT.

.. _squirrelmail:

SquirrelMail
==============================================================

*Date: 2007-12-18*






SquirrelMail, a popular self-hosted web email platform, had its source code repository poisoned.

SquirrelMail was a popular self-hosted web email application during 00s. The attacked managed to compromise the download repository and modify the packaged application. The distributed package was modified to include a remote file inclusion bug allowing the attackers to execute arbitrary code on any compromised SquirrelMail installation, leading to the compromise of the server running SquirrelMail.

The attack was detected due to mismatching package MD5 signatures.

The compromise is believed to happen through a hacked maintainers account, but it is not known how it was hacked in the first place.



Related evaluation points:

- :ref:`software-installation-from-safe-sources`





Links:

- `SquirrelMail Repository Poisoned with Critical flaw (Sûnnet Beskerming) <http://www.beskerming.com/commentary/2007/12/19/313/SquirrelMail_Repository_Poisoned_with_Critical_flaw>`_

- `SquirrelMail Repository Poisoned <http://it.slashdot.org/story/07/12/18/1847233/squirrelmail-repository-poisoned>`_

