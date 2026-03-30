
.. _section3.1.6:

3.1.6 - Get Remote Files
=====================


.. _GR:

Action Option -**GR** (-**GetRemoteFile**) (Alias: -**GetRemote**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

retrieves remote file update
records matching the specified conditions.

|  **dsupdt** [[:ref:`-(DS|Dataset) <DS>`] dNNNNNN] -(GR|GetRemoteFile) [:ref:`Mode Option <mode3.1.6>`]
|             [:ref:`-(FN|FieldNames) <FN>` FieldNameString]
|             [:ref:`-(LI|LocalIndex) <LI>` LocalFileIndices]
|             [:ref:`-(LF|LocalFile) <LF>` LocalFileNames]
|             [:ref:`-(RF|RemoteFile) <RF>` RemoteFileNames]
|             [:ref:`-(DO|DownloadOrder) <DO>` DownloadOrderIndices]
|             [:ref:`-(SF|ServerFile) <SF>` ServerFileNames]
|             [:ref:`-(OF|OutputFile) <OF>` OutputFileName]
|             [:ref:`-(DB|Debug) <DB>` DebugModeInfo]

.. _mode3.1.6:

:ref:`Mode option <section4>` that can be specified for this action:

.. list-table::
   :widths: auto
   :header-rows: 0

   * - :ref:`-(FO|FormatOutput) <FO>`
     - formats each column to a uniform fixed width

Use :ref:`-FN <FN>` (-FieldNames) to specify which remote file fields to retrieve.
Defaults to 'LFDSCBET'.

Valid remote file field names and their corresponding :ref:`Info options <section5>`:

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Names
     - :ref:`Info Options <section5>`
     - Descriptions
   * - L
     - :ref:`-(LI|LocalIndex) <LI>`
     - indices of records
   * - F
     - :ref:`-(RF|RemoteFile) <RF>`
     - remote file names
   * - D
     - :ref:`-(DO|DownloadOrder) <DO>`
     - download order indices
   * - S
     - :ref:`-(SF|ServerFile) <SF>`
     - file names on remote server
   * - C
     - :ref:`-(DC|DownloadCommand) <DC>`
     - command for downloading a remote file
   * - B
     - :ref:`-(BT|BeginTime) <BT>`
     - for remote file names, 0 - the first day/hour
   * - E
     - :ref:`-(ET|EndTime) <ET>`
     - for remote file names, 0 - the last day/hour
   * - T
     - :ref:`-(TI|TimeInterval) <TI>`
     - for remote file names, i.e., 2H, 5D

If no dataset number is given, remote file update information for all datasets
owned by the specialist running **dsupdt** is displayed.



:ref:`Back to Top <section3.1.6>`
:ref:`Back to Table of Contents <index>`
