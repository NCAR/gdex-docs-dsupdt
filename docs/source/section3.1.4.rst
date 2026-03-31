
.. _section3.1.4:

3.1.4 - Get Local Files
=================================


.. _GL:

Action Option -**GL** (-**GetLocalFile**) (Alias: -**GetLocal**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

retrieves local file update records
for a given dataset. If local file indices or names are provided, only those
records are returned.

| **dsupdt** [[:ref:`-(DS|Dataset) <DS>`] dNNNNNN] -(GL|GetLocalFile) [:ref:`Mode Option <mode3.1.4>`]
|           [:ref:`-(FN|FieldNames) <FN>` FieldNameString]
|           [:ref:`-(LI|LocalIndex) <LI>` LocalFileIndices]
|           [:ref:`-(LF|LocalFile) <LF>` LocalFileNames]
|           [:ref:`-(AN|ActionName) <AN>` DSARCHActionName]
|           [:ref:`-(XO|ExecOrder) <XO>` ExecOrderIndex]
|           [:ref:`-(FQ|Frequency) <FQ>` DataFrequencies]
|           [:ref:`-(OF|OutputFile) <OF>` OutputFileName]
|           [:ref:`-(DB|Debug) <DB>` DebugModeInfo]

.. _mode3.1.4:

:ref:`Mode option <section4>` that can be specified for this action:

.. list-table::
   :widths: auto
   :header-rows: 0

   * - :ref:`-(FO|FormatOutput) <FO>`
     - formats each column to a uniform fixed width

Use :ref:`-FN <FN>` (-FieldNames) to specify which local file fields to retrieve. Defaults
to 'LFAIUCOQJNVWZ'. Use :ref:`-FN <FN>` ALL to retrieve all available fields.

Valid field names of local files and their corresponding :ref:`Info option <section5>` names:

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Names
     - :ref:`Info Options <section5>`
     - Descriptions
   * - L
     - :ref:`-(LI|LocalIndex) <LI>`
     - index of update record
   * - F
     - :ref:`-(LF|LocalFile) <LF>`
     - local, original or source file names
   * - A
     - :ref:`-(AN|ActionName) <AN>`
     - Action name for `dsarch <https://gdex-docs-dsarch.readthedocs.io/en/latest/index.html>`_
   * - I
     - :ref:`-(CI|ControlIndex) <CI>`
     - update control indices
   * - P
     - :ref:`-(PI|ParentIndex) <PI>`
     - parent index, refers to a dlupdt.lindex if not 0
   * - U
     - :ref:`-(FA|FileArchived) <FA>`
     - archived file names on GDEX Servers
   * - C
     - :ref:`-(DC|DownloadCommand) <DC>`
     - command for downloading a remote file
   * - O
     - :ref:`-(OP|Options) <OP>`
     - options following the Action
   * - X
     - :ref:`-(XO|ExecOrder) <XO>`
     - order indices for update execution
   * - Q
     - :ref:`-(FQ|Frequency) <FQ>`
     - frequency of data files, i.e., 1W, 1M
   * - E
     - :ref:`-(EP|EndPeriod) <EP>`
     - 0=Sunday/EndMonth if FQ=1W/1M
   * - J
     - :ref:`-(ED|EndDate) <ED>`
     - data end date of next update
   * - K
     - :ref:`-(EH|EndHour) <EH>`
     - data end hour of next update
   * - N
     - :ref:`-(DI|DueInterval) <DI>`
     - data next due period, i.e., 1M2D
   * - V
     - :ref:`-(VI|ValidInterval) <VI>`
     - update valid interval, i.e., 2D, 1M
   * - T
     - :ref:`-(AT|AgeTime) <AT>`
     - remote file age interval, i.e., 2D, 1M
   * - W
     - :ref:`-(WD|WorkDir) <WD>`
     - working directory for processing update
   * - Z
     - :ref:`-(CL|CleanCommand) <CL>`
     - command for removing data files after update
   * - M
     - :ref:`-(MR|MissRemote) <MR>`
     - flag (Y/N) indicating whether a missing remote file is allowed
   * - R
     - :ref:`-(PR|ProcessRemote) <PR>`
     - external utility to process remote files
   * - B
     - :ref:`-(BC|BuildCommand) <BC>`
     - external utility to build local files
   * - S
     - :ref:`-(SN|Specialist) <SN>`
     - DSS specialist who owns the local file record
   * - D
     - :ref:`-(DE|Description) <DE>`
     - File description, include temporal patterns

Specific local files can be filtered by name using :ref:`-LF <LF>` (-LocalFile), which
accepts the '%' wildcard to match any number of characters.

If no dataset number is given, update information is displayed for all available
local files across all datasets owned by the specialist running **dsupdt**.


.. _3.1.4_e4:

**EXAMPLE 4. To retrieve the default local file fields for d744004, local file indices 33 and 34:**

| **dsupdt** d744004 :ref:`GL <GL>` :ref:`-LI <LI>` 33 34

Content of the output:

.. code-block:: none

 Dataset<=>d744004
 LocalIndex<:>LocalFile<:>Action<:>ExecOrder<:>ControlIndex<:>FileArchived<:>DownloadCommand<:>Options<:>Frequency<:>DueInterval<:>EndDate<:>ValidInterval<:>WorkDir<:>CleanCommand<:>
 33<:>uv.<YYYYMM>.bln<:>AW<:>1<:>0<:><:>cp -p /huron/ftp/rossby/upload/morzel/<:>-GI 11 -DF BINARY<:>1M<:><:>2009-08-31<:><:>$UPDTDATA/zji/BLNWIND<:>rm -f __FN__<:>
 34<:>curl.<YYYYMM>.bln<:>Aw<:>2<:>0<:><:>cp -p /huron/ftp/rossby/upload/morzel/<:>-GI 12 -DF BINARY<:>1M<:><:>2009-08-31<:><:>$UPDTDATA/zji/BLNWIND<:>rm -f __FN__<:>



| :ref:`Back to Top <section3.1.4>`
| :ref:`Back to Table of Contents <index>`
