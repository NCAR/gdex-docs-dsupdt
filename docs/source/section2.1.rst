
.. _section2.1:

2.1 - Quick Start
=================================

Show the full document, paged through 'more':

.. code-block:: none

   dsupdt

Show the description of a single option:

.. code-block:: none

   dsupdt -h -UF

Retrieve the update control records for a dataset:

.. code-block:: none

   dsupdt d540000 -GC

Retrieve the local file update records for a dataset:

.. code-block:: none

   dsupdt d540000 -GL

Update (download, build, and archive) data files for a dataset:

.. code-block:: none

   dsupdt d540000 -UF

Check whether remote files are available for update:

.. code-block:: none

   dsupdt d540000 -CU



| :ref:`Back to Top <section2.1>`
| :ref:`Back to Table of Contents <index>`
