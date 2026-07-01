
.. _section3.1.5:

3.1.5 - Set Remote Files
=================================


.. _SR:

Action Option -**SR** (-**SetRemoteFile**) (Alias: -**SetRemote**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

(Alias: -SetRemote) creates or modifies remote file
update records in GDEXDB for a given dataset and local file. One or more
remote file records may be processed per execution.

| **dsupdt** [:ref:`-(DS|Dataset) <DS>`] dNNNNNN -(SR|SetRemoteFile) [:ref:`Mode Option <mode3.1.5>`]
|            :ref:`-(LI|LocalIndex) <LI>` LocalFileIndices
|            :ref:`-(RF|RemoteFile) <RF>` RemoteFileNames
|           [:ref:`-(DO|DownloadOrder) <DO>` DownloadOrderIndices]
|           [:ref:`-(DC|DownloadCommand) <DC>` DownloadCommand]
|           [:ref:`-(SF|ServerFile) <SF>` FileNamesOnRemoteServer]
|           [:ref:`-(BT|BeginTime) <BT>` BeginningDay/Hour]
|           [:ref:`-(ET|EndTime) <ET>` EndingDay/Hour]
|           [:ref:`-(TI|TimeInterval) <TI>` TimeInterval]
|           [:ref:`-(DB|Debug) <DB>` DebugModeInfo]

Available :ref:`Mode option <section4>`:

.. list-table::
   :widths: auto
   :header-rows: 0

   * - :ref:`-(MD|MyDataset) <MD>`
     - sets information into GDEXDB regardless of dataset ownership

Configure remote file update information only when needed. When the remote
and local file names are identical, the local file record alone is enough
to drive the update. A remote file record is required only when the
remote file differs from the local file, when multiple remote files are
downloaded and tarred into a single local file, or when a single remote
file is available from multiple servers.

Local file indices and remote file names must be provided via :ref:`-LI <LI>`
(-LocalIndex) and :ref:`-RF <RF>` (-RemoteFile), respectively, for this action to work.

When :ref:`-DC <DC>` (-DownloadCommand) is set in the remote file record, it takes
precedence over the download command in the local file record.

Use :ref:`-SF <SF>` (-ServerFile) to specify the file's name on the remote server
when it differs from the remote file name. If not set, the server file
name is assumed to match the remote file name.

Files downloaded from a server or generated locally are staged on disk as
remote files until they are validated and converted into local files.

A downloaded file lands in the working directory (:ref:`-WD <WD>`) under its remote file
name (:ref:`-RF <RF>`). Whenever the server file (:ref:`-SF <SF>`) or download command (:ref:`-DC <DC>`) carries
date information (i.e., <DDMMYYYY> in the server path) that is not captured by
the remote file name (i.e., only <HH> is in the name), the working directory
must be made dynamic to hold that missing date information; otherwise files
retrieved for different dates share the same working path and overwrite each
other before archiving, causing wrong-date files to be archived. Both :ref:`-SR <SR>` and
:ref:`-SL <SL>` (and :ref:`-SA <SA>`) reject a record when a required date pattern is present neither
in the remote file name nor in the working directory.

Use :ref:`-TI <TI>` (-TimeInterval) to generate one remote file name per sub-period
within an update window; it must be a single count with a unit of Y, M, W,
D, or H (i.e., 6H, 5D). :ref:`-BT <BT>` (-BeginTime) and :ref:`-ET <ET>` (-EndTime) bound that range
and are used only when :ref:`-TI <TI>` is set; setting :ref:`-BT <BT>` or :ref:`-ET <ET>` without :ref:`-TI <TI>` is rejected
because they would otherwise be ignored.

When a remote file is available from multiple servers, use
:ref:`-DO <DO>` (-DownloadOrder) to set download order indices. The server with the
lowest index is tried first; if it fails, the next is tried in ascending
index order until one succeeds.



| :ref:`Back to Top <section3.1.5>`
| :ref:`Back to Table of Contents <index>`
