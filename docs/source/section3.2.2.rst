
.. _section3.2.2:

3.2.2 - Set All Information
=====================


.. _SA:

Action Option -**SA** (-**SetALL**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

creates and modifies all update control, local file, and
remote file records for a given dataset. It combines :ref:`-SC <SC>` (-SetControl),
:ref:`-SL <SL>` (-SetLocalFile), and :ref:`-SR <SR>` (-SetRemoteFile) into a single action.

| **dsupdt** [:ref:`-(DS|Dataset) <DS>`] dNNNNNN -(SA|SetAll) [:ref:`Mode Options <mode3.2.2>`]
|            :ref:`-(IF|InputFile) <IF>` Input Files
|           [:ref:`-(DB|Debug) <DB>` DebugModeInfo]

.. _mode3.2.2:

:ref:`Mode option <section4>` that can be specified for this action:

.. list-table::
   :widths: auto
   :header-rows: 0

   * - :ref:`-(MD|MyDataset) <MD>`
     - sets information into GDEXDB regardless of dataset ownership
   * - :ref:`-(NC|NewControl) <NC>`
     - sets a new update control record into GDEXDB
   * - :ref:`-(NL|NewLocfile) <NL>`
     - sets a new update record into GDEXDB
   * - :ref:`-(RO|ResetOrder) <RO>`
     - resets the executing order indices of the local file records according to the order as they are given per option :ref:`-LF <LF>` (-LocalFile)

At least one input file is required, since section headers can only be
specified in an input file. A convenient way to create one is to run :ref:`-GA <GA>`
(-GetAll) and edit the output file before passing it back with :ref:`-SA <SA>`.



:ref:`Back to Top <section3.2.2>`
:ref:`Back to Table of Contents <index>`
