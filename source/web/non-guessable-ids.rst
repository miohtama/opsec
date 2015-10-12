
.. This is a generated file from data/. DO NOT EDIT.

.. _non-guessable-ids:

Non-guessable IDs
==============================================================

**Publicly exposed ids are not guessable?** Yes / No


If the service uses running counters as database primary keys, these IDs should not be exposed to the public.

Knowing the ID sequence allows the attacker to gain knowledge of the item count, weakening service security.

* If HTTP endpoints or pages lack proper permission checks, guessing the ID sequence allows the attacker to scrape private data.

* Sensitive business information, like user count or trade count, is exposed to the public.

Use a random ID generation method like the Universally Unique identifier (UUID) version 4 "random," which provides 122 truly random bits for each ID.



Applies for: Everyone



Related incidences:

- :ref:`purse`




Links:


- `UUID (Wikipedia) <https://en.wikipedia.org/wiki/Universally_unique_identifier#Version_4_.28random.29>`_



- `URL safe UUIDs in the smallest number of characters (StackOverlow) <http://stackoverflow.com/q/11431886/315168>`_



