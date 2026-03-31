
.. _section3.2.1:

3.2.1 - Get All Information
===========================


.. _GA:

Action Option -**GA** (-**GetALL**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

retrieves all update control, local file, and remote file
records for a given dataset. It combines :ref:`-GC <GC>` (-GetControl), :ref:`-GL <GL>` (-GetLocalFile),
and :ref:`-GR <GR>` (-GetRemoteFile) into a single action.

| **dsupdt** [[:ref:`-(DS|Dataset) <DS>`] dNNNNNN] -(GA|GetAll) [:ref:`Mode Option <mode3.2.1>`]
|           [:ref:`-(CI|ControlIndex) <CI>` UpdateControlIndices]
|           [:ref:`-(LI|LocalIndex) <LI>` LocalFileIndices]
|           [:ref:`-(LF|LocalFile) <LF>` LocalFileNames]
|           [:ref:`-(RF|RemoteFile) <RF>` RemoteFileNames]
|           [:ref:`-(OF|OutputFile) <OF>` OutputFileName]
|           [:ref:`-(DB|Debug) <DB>` DebugModeInfo]

.. _mode3.2.1:

:ref:`Mode option <section4>` that can be specified for this action:

.. list-table::
   :widths: auto
   :header-rows: 0

   * - :ref:`-(FO|FormatOutput) <FO>`
     - formats each column to a uniform fixed width

Output is sectioned under [DCUPDT] for update controls, [DLUPDT] for local
files, and [DRUPDT] for remote files.

Use :ref:`-OF <OF>` (-OutputFile) to save the retrieved information to a file. Without
it, results are printed to screen. The output file can be edited and fed back
into **dsupdt** via :ref:`-SA <SA>` (-SetAll) to apply changes to GDEXDB.


.. _3.2.1_e5:

**EXAMPLE 5. To retrieve all update control, local file, and remote file information for d277000 at control index 2:**

| **dsupdt** d277000 :ref:`GA <GA>` :ref:`-CI <CI>` 2 :ref:`-OF <OF>` d277000.c1

Content of output file d277000.c1:

.. code-block:: none

 Dataset<=>d277000
 [DCUPDT]
 ControlIndex<:>Specialist<:>ParentIndex<:>Action<:>Frequency<:>ControlOffset<:>ControlTime<:>RetryInterval<:>UpdateControl<:>EMailControl<:>ErrorControl<:>KeepFile<:>HourOffset<:>DataTime<:>HostName<:>
 1<:>zji<:>0<:>UF<:>1W<:>1D9H<:>2011-10-24 09:00:00<:>12H<:><:>A<:>N<:>N<:>0<:><:><:>
 [DLUPDT]
 LocalIndex<:>LocalFile<:>Action<:>ExecOrder<:>ControlIndex<:>FileArchived<:>DownloadCommand<:>Options<:>Frequency<:>EndPeriod<:>DueInterval<:>EndDate<:>EndHour<:>RetryInterval<:>ValidInterval<:>AgeTime<:>WorkDir<:>MissRemote<:>ProcessRemote<:>BuildCommand<:>CleanCommand<:>Specialist<:>Description<:>
 51<:>oisst.<YYYY>.asc.gz<:>AB<:>1<:>1<:><:>ncftpget ftp://ftp.emc.ncep.noaa.gov/cmb/sst/oisst_v2/ASCII_UPDATE/<:>-GI 1 -AF GZ -DF ASCII<:>1W<:>6<:><:>2011-10-22<:><:><:><:><:>$UPDTDATA/zji/NCEPSST<:>N<:><:><:>rm -f -LF<:>zji<:><YYYY/MM/DD>-<YYYY/MM/DD><:>
 [DRUPDT]
 LocalIndex<:>LocalFile<:>RemoteFile<:>ExecOrder<:>DownloadOrder<:>ServerFile<:>DownloadCommand<:>BeginTime<:>EndTime<:>TimeInterval<:>
 51<:>oisst.<YYYY>.asc.gz<:>oisst.<YYYY>.asc.Z<:>1<:>0<:><:><:><:><:><:>

This example shows a weekly update of a local file with remote file name
different from the local file name.



| :ref:`Back to Top <section3.2.1>`
| :ref:`Back to Table of Contents <index>`
