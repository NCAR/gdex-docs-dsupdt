
.. _section3.3.1:

3.3.1 - Update Data Files
=====================


.. _UF:

Action Option -**UF** (-**UpdateFile**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

a comprehensive action that downloads and copies server
files, validates and converts them into remote files, builds local files from
the available remote files, archives local files to the GDEX server, and cleans
up temporary data files generated during the update procedure.

| **dsupdt** [[:ref:`-(DS|Dataset) <DS>`] dNNNNNN] -(UF|UpdateFile) [:ref:`Mode Options <mode3.3.1>`]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(CI|ControlIndex) <CI>` UpdateControlIndex]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(LI|LocalIndex) <LI>` LocalFileIndices]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(LF|LocalFile) <LF>` LocalFileNames]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(XO|ExecOrder) <XO>` ExecOrderIndex]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(RF|RemoteFile) <RF>` RemoteFileNames]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(SF|ServerFile) <SF>` ServerFileNames]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(DO|DownloadOrder) <DO>` DownloadOrderIndices]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(DC|DownloadCommand) <DC>` DownloadCommand]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(ED|EndDate) <ED>` NextDataEndDate]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(EH|EndHour) <EH>` NextDataEndHour]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(GP|GenericPattern) <GP>` GenericPatterns]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(WD|WorkDir) <WD>` WorkingDirectory]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(MR|MissRemote) <MR>` AllowMissRemoteFile]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(FQ|Frequency) <FQ>` DataFrequency]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(PR|ProcessRemote) <PR>` AdditionalRemoteFileProcess]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(BC|BuildCommand) <BC>` CommandBuildLocalFile]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(CD|CurrentDate) <CD>` CurrentDate]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(CH|CurrentHour) <CH>` CurrentHour]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(VS|ValidSize) <VS>` MinSizeForValidFile]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(PL|ProcessLimit) <PL>` MaxNumberOfChildProcesses]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(HO|HourOffset) <HO>` TimeZoneHourOffset]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(QS|QsubOptions) <QS>`  PBSBatchOptions]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(BP|BatchProcess) <BP>` [BatchProcessHosts]]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(CC|CarbonCopy) <CC>` Cc'dEmailAddresses]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(DB|Debug) <DB>` DebugModeInfo]

.. _mode3.3.1:

:ref:`Mode options <section4>` that can be specified for this action:

.. list-table::
   :widths: auto
   :header-rows: 0

   * - :ref:`-(AW|AnyWhere) <AW>`
     - works with :ref:`-BP <BP>` (-BatchProcess) to allow the recorded **dsupdt** command to start from any directory
   * - :ref:`-(BG|BackGround) <BG>`
     - runs in background; suppresses screen output and errors
   * - :ref:`-(CN|CheckNewer) <CN>`
     - when the server file is available locally, checks if it has changed on the server and re-downloads if so
   * - :ref:`-(CP|CurrentPeriod) <CP>`
     - allows the end date/hour to be processed even if it falls within the current update period
   * - :ref:`-(EE|ErrorEmail) <EE>`
     - sends email only when an error occurs during updates
   * - :ref:`-(FU|ForceUpdate) <FU>`
     - forces update for at least one end date/time, even if the update is not yet due
   * - :ref:`-(HU|HourlyUpdate) <HU>`
     - advances time tracking to hours after a successful file update
   * - :ref:`-(IE|IgnoreError) <IE>`
     - works with :ref:`Mode option <section4>` :ref:`-MU <MU>` (-MultipleUpdate) to skip failed updates and continue processing the remaining updates
   * - :ref:`-(KR|KeepRemote) <KR>`
     - copies rather than moves the remote file to the local file location, preserving the remote file on disk
   * - :ref:`-(KS|KeepServer) <KS>`
     - copies rather than moves the server file to the remote file location, preserving the server file on disk
   * - :ref:`-(LO|LogOn) <LO>`
     - enables detailed logging when :ref:`-PL <PL>` is present
   * - :ref:`-(MO|MissedOnly) <MO>`
     - processes only files that have not yet been archived
   * - :ref:`-(MU|MultipleUpdate) <MU>`
     - processes all available update periods; without this option, only the most recent period is processed
   * - :ref:`-(NE|NoEmail) <NE>`
     - suppresses post-update email notification
   * - :ref:`-(NY|NoLeapYear) <NY>`
     - skips February 29 in leap years
   * - :ref:`-(QE|QuitError) <QE>`
     - stops all update processing for the dataset on the first error, rather than skipping and continuing
   * - :ref:`-(RA|RetryArchive) <RA>`
     - forces re-archiving by passing :ref:`-RA <RA>` to `dsarch <https://gdex-docs-dsarch.readthedocs.io/en/latest/index.html>`_
   * - :ref:`-(RD|RetryDownload) <RD>`
     - re-downloads the remote file even if it already exists locally
   * - :ref:`-(RE|ResetEndTime) <RE>`
     - if present, resets end date/hour based on the local file timestamp
   * - :ref:`-(SE|SummaryEmail) <SE>`
     - send a summary email to the specialist after update without detail logging information
   * - :ref:`-(UB|UseBeginTime) <UB>`
     - uses the period's beginning time instead of end time when substituting temporal patterns
   * - :ref:`-(UT|UpdateTime) <UT>`
     - forces an update of the data end time and next due update times

Provide a dataset number via :ref:`-DS <DS>` to restrict updates to a single dataset.
Runtime :ref:`Info options <section5>` can identify specific records or override GDEXDB values.
:ref:`-CD <CD>` (-CurrentDate) and :ref:`-CH <CH>` (-CurrentHour) are runtime-only options that
substitute a different date or hour for the system default.

When :ref:`-MU <MU>` (-MultipleUpdate) is present, all elapsed update periods between
the data end date/hour and the current date/hour are processed.

As noted in the introduction, an error during an individual file's update
stops that file's processing. However, remote file download errors are tolerated
when :ref:`-MR <MR>` (-MissRemote) is 'Y' for records where a local file is built from
multiple remote files, permitting a partial update. If :ref:`-VI <VI>` (-ValidInterval) is
also set, the partial update is held open until the missing files arrive or
the valid period expires.

If :ref:`Info option <section5>` :ref:`-PL <PL>` is set to a value greater than 1, **dsupdt** forks multiple
child processes, each handling one update record. This improves performance
for datasets with many time-consuming independent update records.

Additional notification recipients can be added via :ref:`-CC <CC>` (-CarbonCopy).
DSS specialists may use login names directly, e.g., ':ref:`-CC <CC>` zji schuster'.

:ref:`-UF <UF>` can be run from the command line, via cron job, or through the daemon
'dscheck' when local file records are linked to an update control record.
Rather than supplying :ref:`Mode options <section4>` at run time, most can be pre-configured
in the update control record.

Alternatively, the individual actions :ref:`-DR <DR>` (-DownloadRemote), :ref:`-BL <BL>` (-BuildLocal),
:ref:`-AF <AF>` (-ArchiveFile), and :ref:`-CF <CF>` (-CleanFile) can be used to step through the
download/archive procedure. Their command-line syntax is similar to :ref:`-UF <UF>`
(-UpdateFile) and is described in the following sections.



:ref:`Back to Top <section3.3.1>`
:ref:`Back to Table of Contents <index>`
