
.. _section2.2:

2.2 - Filters and Special Characters in Queries
=================================

For Get-style actions (:ref:`-GC <GC>`, :ref:`-GL <GL>`, :ref:`-GR <GR>`, :ref:`-GA <GA>`), :ref:`Info options <section5>` are interpreted as
query filters. Four characters refine those filters; quote or escape them on
the command line so the shell does not consume them:

.. list-table::
   :widths: auto
   :header-rows: 0

   * - '!'
     - negate the match. Must appear immediately after the option name (may need escaping as '\!' in some shells due to history expansion).
   * - '<'
     - less-than comparison against the next value.
   * - '>'
     - greater-than comparison against the next value.
   * - '<>'
     - range between the next two values (inclusive).

The combination "'!' '<' value" expresses 'greater than or equal to value'.



| :ref:`Back to Top <section2.2>`
| :ref:`Back to Table of Contents <index>`
