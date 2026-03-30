
.. _section3.3.5:

3.3.5 - Archive Local Files
=====================


.. _AF:

Action Option -**AF** (-**ArchiveFile**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

an action to archive local files onto the GDEX
Server according to the DSARCH action previously saved in GDEXDB or specified
on the command line via :ref:`Info option <section5>` :ref:`-AN <AN>` (-ActionName).

|  **dsupdt** [[:ref:`-(DS|Dataset) <DS>`] dNNNNNN] -(AF|ArchiveFile) [:ref:`Mode Options <mode3.3.5>`]
|             [:ref:`-(CI|ControlIndex) <CI>` UpdateControlIndex]
|             [:ref:`-(LI|LocalIndex) <LI>` LocalFileIndices]
|             [:ref:`-(LF|LocalFile) <LF>` LocalFileNames]
|             [:ref:`-(XO|ExecOrder) <XO>` ExecOrderIndex]
|             [:ref:`-(ED|EndDate) <ED>` NextDataEndDate]
|             [:ref:`-(EH|EndHour) <EH>` NextDataEndHour]
|             [:ref:`-(GP|GenericPattern) <GP>` GenericPatterns]
|             [:ref:`-(WD|WorkDir) <WD>` WorkingDirectory]
|             [:ref:`-(FQ|Frequency) <FQ>` UpdateFrequency]
|             [:ref:`-(CD|CurrentDate) <CD>` CurrentDate]
|             [:ref:`-(CH|CurrentHour) <CH>` CurrentHour]
|             [:ref:`-(VS|ValidSize) <VS>` MinSizeForValidFile]
|             [:ref:`-(PL|ProcessLimit) <PL>` MaxNumberOfChildProcesses]
|             [:ref:`-(QS|QsubOptions) <QS>`  PBSBatchOptions]
|             [:ref:`-(BP|BatchProcess) <BP>` [BatchProcessHosts]]
|             [:ref:`-(CC|CarbonCopy) <CC>` Cc'dEmailAddresses]
|             [:ref:`-(DB|Debug) <DB>` DebugModeInfo]

.. _mode3.3.5:

:ref:`Mode options <section4>` that can be specified for this action:

.. list-table::
   :widths: auto
   :header-rows: 0

   * - :ref:`-(AW|AnyWhere) <AW>`
     - works with :ref:`Info option <section5>` :ref:`-BP <BP>` (-BatchProcess) to allow the recorded **dsupdt** command to be started anywhere
   * - :ref:`-(BG|BackGround) <BG>`
     - background process; suppresses screen display of standard output and errors
   * - :ref:`-(CP|CurrentPeriod) <CP>`
     - allows the end date/hour to be processed beyond the current date/hour if it falls within the current update period
   * - :ref:`-(EE|ErrorEmail) <EE>`
     - sends email only when an error occurs during archiving
   * - :ref:`-(FU|ForceUpdate) <FU>`
     - if present, forces archive for at least one end date/time, even if the update is not yet due
   * - :ref:`-(GZ|GMTZone) <GZ>`
     - uses GMT dates/times as controlling times
   * - :ref:`-(HU|HourlyUpdate) <HU>`
     - advances time tracking to hours after a successful archive of a local file
   * - :ref:`-(IE|IgnoreError) <IE>`
     - works with :ref:`-MU <MU>` (-MultipleUpdate) to skip archive errors and continue with remaining local files
   * - :ref:`-(MO|MissedOnly) <MO>`
     - archives local file only if it has not been archived yet
   * - :ref:`-(MU|MultipleUpdate) <MU>`
     - archives all available local files across multiple update periods; without this option, only one period is processed
   * - :ref:`-(NE|NoEmail) <NE>`
     - suppresses post-archive email notification
   * - :ref:`-(NY|NoLeapYear) <NY>`
     - skips February 29 for leap years
   * - :ref:`-(RA|RetryArchive) <RA>`
     - forces re-archiving of local files by passing :ref:`-RA <RA>` to `dsarch <https://gdex-docs-dsarch.readthedocs.io/en/latest/index.html>`_
   * - :ref:`-(RE|ResetEndTime) <RE>`
     - resets end date/hour when the file timestamp is newer than the end date/hour plus one update frequency
   * - :ref:`-(SE|SummaryEmail) <SE>`
     - sends a summary-only email after the action, without detailed log information
   * - :ref:`-(UB|UseBeginTime) <UB>`
     - uses the period's beginning time instead of end time when substituting temporal patterns in file names and download commands
   * - :ref:`-(UT|UpdateTime) <UT>`
     - forces an update of the data end time and next due update times regardless of whether archiving succeeds

If a local file is not ready on the local disk, the archive action for this
local file is skipped.



:ref:`Back to Top <section3.3.5>`
:ref:`Back to Table of Contents <index>`
