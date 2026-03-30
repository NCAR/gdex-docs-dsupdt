
.. _section3.3.4:

3.3.4 - Process Both Files
=====================


.. _PB:

Action Option -**PB** (-**ProcessBoth**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

downloads remote files then validates, converts, and
builds local files in a single action.

|  **dsupdt** [[:ref:`-(DS|Dataset) <DS>`] dNNNNNN] -(PB|ProcessBoth) [:ref:`Mode Options <mode3.3.4>`]
|             [:ref:`-(CI|ControlIndex) <CI>` UpdateControlIndex]
|             [:ref:`-(LI|LocalIndex) <LI>` LocalFileIndices]
|             [:ref:`-(LF|LocalFile) <LF>` LocalFileName]
|             [:ref:`-(XO|ExecOrder) <XO>` ExecOrderIndex]
|             [:ref:`-(RF|RemoteFile) <RF>` RemoteFileNames]
|             [:ref:`-(SF|ServerFile) <SF>` ServerFileNames]
|             [:ref:`-(DO|DownloadOrder) <DO>` DownloadOrderIndices]
|             [:ref:`-(DC|DownloadCommand) <DC>` DownloadCommand]
|             [:ref:`-(PR|ProcessRemote) <PR>` AdditionalRemoteFileProcess]
|             [:ref:`-(BC|BuildCommand) <BC>` CommandBuildLocalFile]
|             [:ref:`-(ED|EndDate) <ED>` NextDataEndDate]
|             [:ref:`-(EH|EndHour) <EH>` NextDataEndHour]
|             [:ref:`-(GP|GenericPattern) <GP>` GenericPatterns]
|             [:ref:`-(WD|WorkDir) <WD>` WorkingDirectory]
|             [:ref:`-(FQ|Frequency) <FQ>` UpdateFrequency]
|             [:ref:`-(MR|MissRemote) <MR>` AllowMissRemoteFile]
|             [:ref:`-(CD|CurrentDate) <CD>` CurrentDate]
|             [:ref:`-(CH|CurrentHour) <CH>` CurrentHour]
|             [:ref:`-(VS|ValidSize) <VS>` MinSizeForValidFile]
|             [:ref:`-(PL|ProcessLimit) <PL>` MaxNumberOfChildProcesses]
|             [:ref:`-(QS|QsubOptions) <QS>`  PBSBatchOptions]
|             [:ref:`-(BP|BatchProcess) <BP>` [BatchProcessHosts]]
|             [:ref:`-(HO|HourOffset) <HO>` TimeZoneHourOffset]
|             [:ref:`-(CC|CarbonCopy) <CC>` Cc'dEmailAddresses]
|             [:ref:`-(DB|Debug) <DB>` DebugModeInfo]

.. _mode3.3.4:

:ref:`Mode options <section4>` that can be specified for this action:

.. list-table::
   :widths: auto
   :header-rows: 0

   * - :ref:`-(AW|AnyWhere) <AW>`
     - works with :ref:`Info option <section5>` :ref:`-BP <BP>` (-BatchProcess) to allow the recorded **dsupdt** command to be started anywhere
   * - :ref:`-(BG|BackGround) <BG>`
     - background process; suppresses screen display of standard output and errors
   * - :ref:`-(CN|CheckNewer) <CN>`
     - when the server file is available locally, checks if it has changed on the server and re-downloads if so
   * - :ref:`-(CP|CurrentPeriod) <CP>`
     - allows the end date/hour to be processed beyond the current date/hour if it falls within the current update period
   * - :ref:`-(EE|ErrorEmail) <EE>`
     - sends email only when an error occurs during remote file retrieval or local file building
   * - :ref:`-(FU|ForceUpdate) <FU>`
     - forces processing for at least one end date/time, even if the update is not yet due
   * - :ref:`-(GZ|GMTZone) <GZ>`
     - uses GMT dates/times as controlling times
   * - :ref:`-(HU|HourlyUpdate) <HU>`
     - advances time tracking to hours after a successful action
   * - :ref:`-(IE|IgnoreError) <IE>`
     - works with :ref:`-MU <MU>` (-MultipleUpdate) to skip errors and continue with remaining remote/local files
   * - :ref:`-(KR|KeepRemote) <KR>`
     - copies rather than moves the remote file to the local file location, preserving the remote file on disk
   * - :ref:`-(KS|KeepServer) <KS>`
     - keeps server file on local disk by copying it to the remote file location instead of moving it
   * - :ref:`-(MO|MissedOnly) <MO>`
     - processes data file only if it has not been archived yet
   * - :ref:`-(LO|LogOn) <LO>`
     - turns on detail logging when option :ref:`-PL <PL>` is present
   * - :ref:`-(MU|MultipleUpdate) <MU>`
     - downloads and builds across all available update periods
   * - :ref:`-(NE|NoEmail) <NE>`
     - suppresses post-action email notification
   * - :ref:`-(NY|NoLeapYear) <NY>`
     - skips February 29 in leap years
   * - :ref:`-(QE|QuitError) <QE>`
     - stops all processing for the dataset on the first error, rather than skipping and continuing
   * - :ref:`-(RD|RetryDownload) <RD>`
     - re-downloads the remote file even if it already exists locally
   * - :ref:`-(SE|SummaryEmail) <SE>`
     - sends a summary-only email after the action, without detailed log information
   * - :ref:`-(UB|UseBeginTime) <UB>`
     - uses the period's beginning time instead of end time when substituting temporal patterns



:ref:`Back to Top <section3.3.4>`
:ref:`Back to Table of Contents <index>`
