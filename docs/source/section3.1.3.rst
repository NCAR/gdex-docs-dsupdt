
.. _section3.1.3:

3.1.3 - Set Local Files
=================================


.. _SL:

Action Option -**SL** (-**SetLocalFile**) (Alias: -**SetLocal**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

creates or modifies local file update
records in GDEXDB for a given dataset. One or more records may be processed per
execution.

| **dsupdt** [[:ref:`-(DS|Dataset) <DS>`] dNNNNNN] -(SL|SetLocalFile) [:ref:`Mode Options <mode3.1.3>`]
|            :ref:`-(LI|LocalIndex) <LI>` LocalFileIndices
|           [:ref:`-(LF|LocalFile) <LF>` LocalFileNames]
|           [:ref:`-(CI|ControlIndex) <CI>` UpdateControlIndices]
|           [:ref:`-(PI|ParentIndex) <PI>` ParentLocalIndices]
|           [:ref:`-(FA|FileArchived) <FA>` ArchivedFileNames]
|           [:ref:`-(DC|DownloadCommand) <DC>` DownloadCommand]
|           [:ref:`-(AN|ActionName) <AN>` DSARCHActionNames]
|           [:ref:`-(OP|Options) <OP>` DSARCHOptions]
|           [:ref:`-(XO|ExecOrder) <XO>` ExecuteOrderIndices]
|           [:ref:`-(FQ|Frequency) <FQ>` DataFrequencies]
|           [:ref:`-(EP|EndPeriod) <EP>` PeriodEndAt]
|           [:ref:`-(DI|DueInterval) <DI>` DataDueInterval]
|           [:ref:`-(ED|EndDate) <ED>` NextDataEndDate]
|           [:ref:`-(EH|EndHour) <EH>` NextDataEndHour]
|           [:ref:`-(VI|ValidInterval) <VI>` UpdateValidInterval]
|           [:ref:`-(AT|AgeTime) <AT>` RemoteFileAgeTime]
|           [:ref:`-(WD|WorkDir) <WD>` WorkingDirectory]
|           [:ref:`-(CL|CleanCommand) <CL>` FileCleaningCommand]
|           [:ref:`-(MR|MissRemote) <MR>` AllowMissRemote]
|           [:ref:`-(PR|ProcessRemote) <PR>` AdditionalRemoteFileProcess]
|           [:ref:`-(BC|BuildCommand) <BC>` CommandBuildLocalFile]
|           [:ref:`-(SN|Specialist) <SN>` DSSSpecialist]
|           [:ref:`-(DE|Description) <DE>` FileDescription]
|           [:ref:`-(DB|Debug) <DB>` DebugModeInfo]

.. _mode3.1.3:

:ref:`Mode options <section4>` that can be specified for this action:

.. list-table::
   :widths: auto
   :header-rows: 0

   * - :ref:`-(MD|MyDataset) <MD>`
     - sets information into GDEXDB regardless of dataset ownership
   * - :ref:`-(NL|NewLocfile) <NL>`
     - adds a new local file update record to GDEXDB
   * - :ref:`-(RO|ResetOrder) <RO>`
     - resets execution order indices to match the order in which records are provided

If a local file record already exists in GDEXDB for the given index, it is
modified. A new record is created when the index is 0 and :ref:`-NL <NL>` (-NewLocfile)
is present. The dataset name via :ref:`-DS <DS>` is required only when adding a new record.

Temporal or generic patterns enclosed by delimiters (default '<' and '>') may
be embedded in local file names (:ref:`-LF <LF>`), remote file names (:ref:`-RF <RF>`), download
commands (:ref:`-DC <DC>`), and file descriptions (:ref:`-DE <DE>`). Delimiters can be changed via
:ref:`-PD <PD>` (-PatternDelimiter). Patterns act as placeholders substituted with real
values at update time. For example, <YYYYMM> represents a 4-digit year and
2-digit month. A file named 'filename.<YYYYMM>.ext' updated to end date
2007-10-31 becomes 'filename.200710.ext'.

Linking a local file record to an update control record (via :ref:`-CI <CI>`) causes the
control record's scheduled action to run automatically against that local file.


.. _3.1.3_e3:

**EXAMPLE 3. To set update information for two new local files of d744004 via input file 'd744004.loc':**

| **dsupdt** :ref:`SL <SL>` :ref:`-NL <NL>` :ref:`-IF <IF>` d744004.loc

Content of input file d744004.loc:

.. code-block:: none

 Dataset<=>d744004
 LocalIndex<:>LocalFile<:>Action<:>ExecOrder<:>ControlIndex<:>FileArchived<:>DownloadCommand<:>Options<:>Frequency<:>DueInterval<:>EndDate<:>ValidInterval<:>WorkDir<:>CleanCommand<:>
 0<:>uv.<YYYYMM>.bln<:>AW<:>1<:>0<:><:>cp -p /huron/ftp/rossby/upload/morzel/<:>-GI 11 -DF BINARY<:>1M<:><:>2009-08-31<:><:>$UPDTDATA/zji/BLNWIND<:>rm -f __FN__<:>
 0<:>curl.<YYYYMM>.bln<:>AB<:>2<:>0<:><:>cp -p /huron/ftp/rossby/upload/morzel/<:>-GI 12 -DF BINARY<:>1M<:><:>2009-08-31<:><:>$UPDTDATA/zji/BLNWIND<:>rm -f __FN__<:>



| :ref:`Back to Top <section3.1.3>`
| :ref:`Back to Table of Contents <index>`
