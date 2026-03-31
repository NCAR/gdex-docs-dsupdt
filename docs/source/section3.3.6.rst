
.. _section3.3.6:

3.3.6 - Clean Temporary Files
=====================


.. _CF:

Action Option -**CF** (-**CleanFile**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

removes temporary files from the local working area,
including files that have already been archived or have become outdated.

| **dsupdt** [[:ref:`-(DS|Dataset) <DS>`] dNNNNNN] -(CF|CleanFile) [:ref:`Mode Options <mode3.3.6>`]
|           [:ref:`-(LI|LocalIndex) <LI>` LocalFileIndices]
|           [:ref:`-(LF|LocalFile) <LF>` LocalFileNames]
|           [:ref:`-(XO|ExecOrder) <XO>` ExecOrderIndex]
|           [:ref:`-(ED|EndDate) <ED>` NextDataEndDate]
|           [:ref:`-(EH|EndHour) <EH>` NextDataEndHour]
|           [:ref:`-(GP|GenericPattern) <GP>` GenericPatterns]
|           [:ref:`-(WD|WorkDir) <WD>` WorkingDirectory]
|           [:ref:`-(FQ|Frequency) <FQ>` UpdateFrequency]
|           [:ref:`-(CD|CurrentDate) <CD>` CurrentDate]
|           [:ref:`-(CH|CurrentHour) <CH>` CurrentHour]
|           [:ref:`-(PL|ProcessLimit) <PL>` MaxNumberOfChildProcesses]
|           [:ref:`-(QS|QsubOptions) <QS>`  PBSBatchOptions]
|           [:ref:`-(BP|BatchProcess) <BP>` [BatchProcessHosts]]
|           [:ref:`-(CC|CarbonCopy) <CC>` Cc'dEmailAddresses]
|           [:ref:`-(DB|Debug) <DB>` DebugModeInfo]

.. _mode3.3.6:

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
     - sends email only when an error occurs during local file cleaning
   * - :ref:`-(FU|ForceUpdate) <FU>`
     - if present, forces clean for at least one end date/time, even if the update is not yet due
   * - :ref:`-(GZ|GMTZone) <GZ>`
     - uses GMT dates/times as controlling times
   * - :ref:`-(HU|HourlyUpdate) <HU>`
     - advances time tracking to hours after a successful clean action
   * - :ref:`-(MU|MultipleUpdate) <MU>`
     - cleans temporary files across all available update periods
   * - :ref:`-(NE|NoEmail) <NE>`
     - suppresses post-clean email notification
   * - :ref:`-(NY|NoLeapYear) <NY>`
     - skips February 29 in leap years
   * - :ref:`-(SE|SummaryEmail) <SE>`
     - sends a summary-only email after the action, without detailed log information
   * - :ref:`-(UB|UseBeginTime) <UB>`
     - uses the period's beginning time instead of end time when substituting temporal patterns in file names and clean commands

If a temporary file is not found in the local working area, the cleaning
action is skipped.



:ref:`Back to Top <section3.3.6>`
:ref:`Back to Table of Contents <index>`
