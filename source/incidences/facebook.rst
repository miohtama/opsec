
.. This is a generated file from data/. DO NOT EDIT.

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

