
.. _section3.3.2:

3.3.2 - Download Remote Files
=====================


.. _DR:

Action Option -**DR** (-**DownloadRemote**) (Alias: -**DownloadRemoteFile**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

downloads or copies server
files to local working disk, or generates new data files via local processing.
The resulting files are called remote files and are later validated and
converted to local files by :ref:`-BL <BL>` (-BuildLocal).

|  **dsupdt** [[:ref:`-(DS|Dataset) <DS>`] dNNNNNN] -(DR|DownloadRemote) [:ref:`Mode Options <mode3.3.2>`]
|             [:ref:`-(CI|ControlIndex) <CI>` UpdateControlIndex]
|             [:ref:`-(LI|LocalIndex) <LI>` LocalFileIndices]
|             [:ref:`-(LF|LocalFile) <LF>` LocalFileNames]
|             [:ref:`-(RF|RemoteFile) <RF>` RemoteFileNames]
|             [:ref:`-(SF|ServerFile) <SF>` ServerFileNames]
|             [:ref:`-(DO|DownloadOrder) <DO>` DownloadOrderIndices]
|             [:ref:`-(XO|ExecOrder) <XO>` ExecOrderIndex]
|             [:ref:`-(DC|DownloadCommand) <DC>` DownloadCommand]
|             [:ref:`-(PR|ProcessRemote) <PR>` AdditionalRemoteFileProcess]
|             [:ref:`-(ED|EndDate) <ED>` NextDataEndDate]
|             [:ref:`-(EH|EndHour) <EH>` NextDataEndHour]
|             [:ref:`-(GP|GenericPattern) <GP>` GenericPatterns]
|             [:ref:`-(WD|WorkDir) <WD>` WorkingDirectory]
|             [:ref:`-(MR|MissRemote) <MR>` AllowMissRemoteFile]
|             [:ref:`-(FQ|Frequency) <FQ>` UpdateFrequency]
|             [:ref:`-(CD|CurrentDate) <CD>` CurrentDate]
|             [:ref:`-(CH|CurrentHour) <CH>` CurrentHour]
|             [:ref:`-(VS|ValidSize) <VS>` MinSizeForValidFile]
|             [:ref:`-(PL|ProcessLimit) <PL>` MaxNumberOfChildProcesses]
|             [:ref:`-(HO|HourOffset) <HO>` TimeZoneHourOffset]
|             [:ref:`-(QS|QsubOptions) <QS>`  PBSBatchOptions]
|             [:ref:`-(BP|BatchProcess) <BP>` [BatchProcessHosts]]
|             [:ref:`-(CC|CarbonCopy) <CC>` Cc'dEmailAddresses]
|             [:ref:`-(DB|Debug) <DB>` DebugModeInfo]

.. _mode3.3.2:

:ref:`Mode options <section4>` that can be specified for this action:

.. list-table::
   :widths: auto
   :header-rows: 0

   * - :ref:`-(AW|AnyWhere) <AW>`
     - works with :ref:`-BP <BP>` (-BatchProcess) to allow the recorded **dsupdt** command to start from any directory
   * - :ref:`-(BG|BackGround) <BG>`
     - runs in background; suppresses screen output and errors
   * - :ref:`-(CN|CheckNewer) <CN>`
     - when the server file is available locally, checks if the file has changed on the server and re-downloads it if so
   * - :ref:`-(CP|CurrentPeriod) <CP>`
     - allows the end date/hour to be processed beyond the current date/hour if it falls within the current update period
   * - :ref:`-(EE|ErrorEmail) <EE>`
     - sends email only when an error occurs during retrieval of remote files
   * - :ref:`-(FU|ForceUpdate) <FU>`
     - forces download for at least one end date/time, even if the update is not yet due
   * - :ref:`-(GZ|GMTZone) <GZ>`
     - uses GMT dates/times as controlling times
   * - :ref:`-(HU|HourlyUpdate) <HU>`
     - advances time tracking to hours after a successful remote file download
   * - :ref:`-(IE|IgnoreError) <IE>`
     - works with :ref:`-MU <MU>` (-MultipleUpdate) to skip download errors and continue with remaining remote files
   * - :ref:`-(KS|KeepServer) <KS>`
     - keeps server file on local disk by copying it to the remote file location instead of moving it
   * - :ref:`-(LO|LogOn) <LO>`
     - turns on detail logging when option :ref:`-PL <PL>` is present
   * - :ref:`-(MO|MissedOnly) <MO>`
     - downloads remote file only if it has not been archived yet
   * - :ref:`-(MU|MultipleUpdate) <MU>`
     - downloads across all available update periods; without this option, only one period is processed
   * - :ref:`-(NE|NoEmail) <NE>`
     - suppresses post-download email notification
   * - :ref:`-(NY|NoLeapYear) <NY>`
     - skips February 29 for leap years
   * - :ref:`-(QE|QuitError) <QE>`
     - stops all downloads for the dataset on the first error, rather than skipping and continuing
   * - :ref:`-(RD|RetryDownload) <RD>`
     - re-downloads the remote file even if it already exists locally
   * - :ref:`-(SE|SummaryEmail) <SE>`
     - sends a summary-only email after the action, without detailed log information
   * - :ref:`-(UB|UseBeginTime) <UB>`
     - uses the period's beginning time instead of end time when substituting temporal patterns

If a remote file already exists on local disk, the download action is skipped.
To re-download, either remove the existing file manually or use :ref:`Mode <section4>` option
:ref:`-RD <RD>` (-RetryDownload).

A server file is the original file on the remote server. Specify it only
when its name differs from the remote file name.



:ref:`Back to Top <section3.3.2>`
:ref:`Back to Table of Contents <index>`
