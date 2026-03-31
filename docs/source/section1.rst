
.. _section1:

1 - INTRODUCTION
=================================

**dsupdt** is a utility for performing periodic dataset updates by calling `dsarch <https://gdex-docs-dsarch.readthedocs.io/en/latest/index.html>`_
to archive data onto CISL Geoscience Data Exchange (GDEX) Servers.

This application supports the following functions:

* Configure update information for a dataset's update controls, local files, and remote files
* Download or retrieve data files from remote servers or other local machines
* Call specialist-defined routines to validate and convert downloaded remote data files
* Build local files from remote files, applying tar and/or compress operations automatically as needed
* Archive local files onto GDEX Servers by calling `dsarch <https://gdex-docs-dsarch.readthedocs.io/en/latest/index.html>`_
* Remove local and temporary files after data files have been archived successfully
* Check availability of files on remote servers
* Initiate update actions via the centralized daemon 'dscheck', via cron job, or manually

A dataset must be configured to work with `dsarch <https://gdex-docs-dsarch.readthedocs.io/en/latest/index.html>`_ before it can be set up for
periodic updates by **dsupdt**. See the `dsarch <https://gdex-docs-dsarch.readthedocs.io/en/latest/index.html>`_ help document for information
on placing a dataset under `dsarch <https://gdex-docs-dsarch.readthedocs.io/en/latest/index.html>`_ control.

Once update information is configured in GDEXDB, **dsupdt** downloads and archives
data in the following steps:

|  Server Files on remote server or at other local area ===DOWNLOAD/COPY=>
|  Remote Files at local working area ==================VALIDATE/CONVERT=>
|  Remote Files ready for building Local Files =======TAR/COMPRESS/BUILD=>
|  Local Files ready for archive =================================DSARCH=>
|  Files on GDEX Servers

If not specified explicitly, the server file name defaults to the remote file name.
For one-to-one matches between remote and local files, the remote file name
defaults to the local file name if not otherwise specified.

A local file update record is the minimum configuration required to update data
files for a given dataset. Add remote file configuration records when the remote
file name differs from the local file name, or when multiple remote files are
needed to build a single local file.

Update control records determine which data processing computers may run update
actions. Without an update control record, updates must be started manually or
via cron jobs on a specific computer.

To prevent specialists from accidentally updating data files using configuration
records owned by others, only the owning specialist can execute **dsupdt** against
a given update record. Validation is also performed to prevent configuration on
the wrong dataset: any input file used for update configuration must begin with
the dataset number in the format 'dNNNNNN.*', where '*' matches one or more
valid filename characters. Additionally, **dsupdt** verifies that the specialist
is authorized for the given dataset. Execution stops if the specialist is not
listed as an owner, unless :ref:`Mode option <section4>` :ref:`-MD <MD>` (-MyDataset) is present, which forces
**dsupdt** to proceed with the action regardless.

If an error occurs while updating an individual data file, that file's update is
skipped and **dsupdt** continues with the remaining updates. Restarting **dsupdt**
resumes from where it left off for any previously unfinished files. An email
notice is sent to the specialist who initiated the update. By default, the email
includes detailed information on successful updates along with any error messages.

The following sections first describe general usage of **dsupdt**, then provide
detailed descriptions of each option, with examples interspersed throughout.



| :ref:`Back to Top <section1>`
| :ref:`Back to Table of Contents <index>`
