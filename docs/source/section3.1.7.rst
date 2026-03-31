
.. _section3.1.7:

3.1.7 - Delete Update Information
=====================


.. _DL:

Action Option -**DL** (-**Delete**) (Aliases: -**RM**, -**Remove**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

deletes one or more update control,
local file, or remote file records from GDEXDB.

| **dsupdt** [[:ref:`-(DS|Dataset) <DS>`] dNNNNNN] -(DL|Delete) [:ref:`Mode Option <mode3.1.7>`]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :ref:`-(CI|ControlIndex) <CI>` UpdateControlIndices
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(DB|Debug) <DB>` DebugModeInfo]
| &nbsp;&nbsp;&nbsp;&nbsp; or

| **dsupdt** [[:ref:`-(DS|Dataset) <DS>`] dNNNNNN] -(DL|Delete) [:ref:`Mode Option <mode3.1.7>`]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :ref:`-(LI|LocalIndex) <LI>` LocalFileIndices
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(DB|Debug) <DB>` DebugModeInfo]
| &nbsp;&nbsp;&nbsp;&nbsp; or

| **dsupdt** [[:ref:`-(DS|Dataset) <DS>`] dNNNNNN] -(DL|Delete) [:ref:`Mode Option <mode3.1.7>`]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :ref:`-(LI|LocalIndex) <LI>` LocalFileIndices
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :ref:`-(RF|RemoteFile) <RF>` RemoteFileNames
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(DO|DownloadOrder) <DO>` DownloadOrderIndices]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(DB|Debug) <DB>` DebugModeInfo]

.. _mode3.1.7:

:ref:`Mode option <section4>` that can be specified for this action:

.. list-table::
   :widths: auto
   :header-rows: 0

   * - :ref:`-(MD|MyDataset) <MD>`
     - deletes records regardless of dataset ownership

Provide a control index to delete an update control record. Provide a local
file index to delete a local file record and all its associated remote file
records. To delete only a specific remote file record, provide both the local
file index and the remote file name.



:ref:`Back to Top <section3.1.7>`
:ref:`Back to Table of Contents <index>`
