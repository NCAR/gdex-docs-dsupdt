
.. _section3.1.5:

3.1.5 - Set Remote Files
=====================


.. _SR:

Action Option -**SR** (-**SetRemoteFile**) (Alias: -**SetRemote**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

creates or modifies remote file
update records in GDEXDB for a given dataset and local file. One or more
remote file records may be processed per execution.

|  **dsupdt** [:ref:`-(DS|Dataset) <DS>`] dNNNNNN -(SR|SetRemoteFile) [:ref:`Mode Option <mode3.1.5>`]
|              :ref:`-(LI|LocalIndex) <LI>` LocalFileIndices
|              :ref:`-(RF|RemoteFile) <RF>` RemoteFileNames
|             [:ref:`-(DO|DownloadOrder) <DO>` DownloadOrderIndices]
|             [:ref:`-(DC|DownloadCommand) <DC>` DownloadCommand]
|             [:ref:`-(SF|ServerFile) <SF>` FileNamesOnRemoteServer]
|             [:ref:`-(BT|BeginTime) <BT>` BeginningDay/Hour]
|             [:ref:`-(ET|EndTime) <ET>` EndingDay/Hour]
|             [:ref:`-(TI|TimeInterval) <TI>` TimeInterval]
|             [:ref:`-(DB|Debug) <DB>` DebugModeInfo]

.. _mode3.1.5:

:ref:`Mode option <section4>` that can be specified for this action:

.. list-table::
   :widths: auto
   :header-rows: 0

   * - :ref:`-(MD|MyDataset) <MD>`
     - sets information into GDEXDB regardless of dataset ownership

Configure remote file update information only when needed. When remote and
local file names are identical, the local file record alone is sufficient for
data update. A remote file record is required only when the remote file differs
from the local file, when multiple remote files are downloaded and tarred into
a single local file, or when a single remote file is available from multiple
servers.

Local file indices and remote file names must be provided per options :ref:`-LI <LI>`
(-LocalIndex) and :ref:`-RF <RF>` (-RemoteFile), respectively, for this action to work.

If :ref:`-DC <DC>` (-DownloadCommand) is set in the remote file record, it takes
precedence over the download command in the local file record.

Use :ref:`-SF <SF>` (-ServerFile) to specify the file's name on the remote server when
it differs from the remote file name. If not set, the server file name is
assumed to match the remote file name.

Files downloaded from a server or generated locally are staged on disk as
remote files until they are validated and converted into local files.

If a remote file is available from multiple servers, use :ref:`-DO <DO>` (-DownloadOrder)
to set download order indices. The server with the lowest index is tried first;
if it fails, servers are tried in ascending index order until one succeeds.



:ref:`Back to Top <section3.1.5>`
:ref:`Back to Table of Contents <index>`
