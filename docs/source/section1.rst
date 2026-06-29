
.. _section1:

1 - INTRODUCTION
=================================

**dsupdt** is a utility for performing periodic dataset updates by calling
`dsarch <https://gdex-docs-dsarch.readthedocs.io>`_ to archive data onto the CISL Geoscience Data Exchange (GDEX) Servers.

The application supports the following capabilities:

* Configure a dataset's update controls, local files, and remote files
* Download or copy data files from remote servers or other local areas
* Invoke specialist-defined routines to validate and convert downloaded data
* Build local files from remote files, applying tar and/or compress operations automatically as needed
* Archive local files onto the GDEX Servers via `dsarch <https://gdex-docs-dsarch.readthedocs.io>`_
* Remove local and temporary files after data files have been archived successfully
* Check availability of files on remote servers
* Initiate update actions through the centralized daemon `dscheck <https://gdex-docs-dscheck.readthedocs.io>`_, via a cron job, or manually

A dataset must already be configured for `dsarch <https://gdex-docs-dsarch.readthedocs.io>`_ before it can be set up for
periodic updates with **dsupdt**. See the `dsarch <https://gdex-docs-dsarch.readthedocs.io>`_ help document for information
on placing a dataset under `dsarch <https://gdex-docs-dsarch.readthedocs.io>`_ control.

Once update information has been configured in GDEXDB, **dsupdt** downloads and
archives data in the following stages:

.. code-block:: none

     Server Files on remote server or other local area --DOWNLOAD/COPY------>
     Remote Files staged in the local working area ------VALIDATE/CONVERT--->
     Remote Files ready to build Local Files ------------TAR/COMPRESS/BUILD->
     Local Files ready for archive ----------------------DSARCH------------->
     Files on the GDEX Servers                                               

If a server file name is not specified explicitly, it defaults to the remote
file name. For one-to-one matches between remote and local files, the remote
file name defaults to the local file name when not otherwise specified.

A local file update record is the minimum configuration required to update
data files for a given dataset. Add remote file configuration records when the
remote file name differs from the local file name, or when several remote
files are needed to build a single local file.

Update control records determine which data-processing computers may run
update actions. Without an update control record, updates must be started
manually or through cron jobs on a specific computer.

To prevent specialists from accidentally updating data files using
configuration records owned by others, only the owning specialist may execute
**dsupdt** against a given update record. Validation is also performed to guard
against configuring the wrong dataset: any input file used for update
configuration must begin with the dataset number in the format 'dNNNNNN.*',
where '*' matches one or more valid filename characters. In addition, **dsupdt**
verifies that the specialist is authorized for the given dataset. Execution
stops if the specialist is not listed as an owner, unless :ref:`Mode option <section4>` :ref:`-MD <MD>`
(-MyDataset) is supplied, which forces **dsupdt** to proceed regardless.

If an error occurs while updating an individual data file, that file's update
is skipped and **dsupdt** continues with the remaining updates. Restarting
**dsupdt** resumes from where it left off for any previously unfinished files.
An email notice is sent to the specialist who initiated the update. By
default, the email contains detailed information on successful updates along
with any error messages.

The **dsupdt** user guide hosted on Read the Docs is generated from this
'dsupdt.usg' file. Opening a pull request that modifies this 'dsupdt.usg'
file in the GitHub repository https://github.com/NCAR/rda-python-dsupdt
triggers an automated workflow that converts the file into the RST source
files, syncs the rda_python_dsupdt version into the documentation, and opens
a new pull request for review in the GitHub repository
https://github.com/NCAR/gdex-docs-dsupdt. Merging that pull request
publishes the user guide as the 'latest' version at
https://gdex-docs-dsupdt.readthedocs.io, and creating a GitHub release
there publishes it as the 'stable' version.

The remainder of this document is organized as follows. Section 2 covers
general usage and conventions. Section 3 describes :ref:`Action options <section3>` grouped
by what they manipulate (configuration records, all-information, and update
processing). Section 4 lists :ref:`Mode options <section4>` that modify how an action behaves.
Section 5 lists Information options that pass values into an action.



| :ref:`Back to Top <section1>`
| :ref:`Back to Table of Contents <index>`
