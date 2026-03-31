
.. _section3.3.3:

3.3.3 - Build Local Files
=====================


.. _BL:

Action Option -**BL** (-**BuildLocal**) (Alias: -**BuildLocalfile**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

an action to validate and convert
remote files and build local files.

| **dsupdt** [[:ref:`-(DS|Dataset) <DS>`] dNNNNNN] -(BL|BuildLocal) [:ref:`Mode Options <mode3.3.3>`]
|           [:ref:`-(CI|ControlIndex) <CI>` UpdateControlIndex]
|           [:ref:`-(LI|LocalIndex) <LI>` LocalFileIndices]
|           [:ref:`-(LF|LocalFile) <LF>` LocalFileNames]
|           [:ref:`-(XO|ExecOrder) <XO>` ExecOrderIndex]
|           [:ref:`-(RF|RemoteFile) <RF>` RemoteFileNames]
|           [:ref:`-(BC|BuildCommand) <BC>` CommandBuildLocalFile]
|           [:ref:`-(ED|EndDate) <ED>` NextDataEndDate]
|           [:ref:`-(EH|EndHour) <EH>` NextDataEndHour]
|           [:ref:`-(GP|GenericPattern) <GP>` GenericPatterns]
|           [:ref:`-(WD|WorkDir) <WD>` WorkingDirectory]
|           [:ref:`-(FQ|Frequency) <FQ>` UpdateFrequency]
|           [:ref:`-(CD|CurrentDate) <CD>` CurrentDate]
|           [:ref:`-(CH|CurrentHour) <CH>` CurrentHour]
|           [:ref:`-(VS|ValidSize) <VS>` MinSizeForValidFile]
|           [:ref:`-(PL|ProcessLimit) <PL>` MaxNumberOfChildProcesses]
|           [:ref:`-(QS|QsubOptions) <QS>`  PBSBatchOptions]
|           [:ref:`-(BP|BatchProcess) <BP>` [BatchProcessHosts]]
|           [:ref:`-(CC|CarbonCopy) <CC>` Cc'dEmailAddresses]
|           [:ref:`-(DB|Debug) <DB>` DebugModeInfo]

.. _mode3.3.3:

:ref:`Mode options <section4>` that can be specified for this action:

.. list-table::
   :widths: auto
   :header-rows: 0

   * - :ref:`-(AW|AnyWhere) <AW>`
     - works with :ref:`-BP <BP>` (-BatchProcess) to allow the recorded **dsupdt** command to start from any directory
   * - :ref:`-(BG|BackGround) <BG>`
     - runs in background; suppresses screen output and errors
   * - :ref:`-(CP|CurrentPeriod) <CP>`
     - allows the end date/hour to be processed even if it falls within the current update period
   * - :ref:`-(EE|ErrorEmail) <EE>`
     - sends email only when an error occurs during local file building
   * - :ref:`-(FU|ForceUpdate) <FU>`
     - if present, forces build for at least one end date/time, even if the update is not yet due
   * - :ref:`-(GZ|GMTZone) <GZ>`
     - uses GMT dates/times as controlling times
   * - :ref:`-(HU|HourlyUpdate) <HU>`
     - advances time tracking to hours after a successful local file build
   * - :ref:`-(IE|IgnoreError) <IE>`
     - works with :ref:`-MU <MU>` (-MultipleUpdate) to skip build errors and continue with remaining local files
   * - :ref:`-(KR|KeepRemote) <KR>`
     - copies rather than moves the remote file to the local file location, preserving the remote file on disk
   * - :ref:`-(LO|LogOn) <LO>`
     - enables detailed logging when :ref:`-PL <PL>` is present
   * - :ref:`-(MO|MissedOnly) <MO>`
     - builds only files that have not yet been archived
   * - :ref:`-(MU|MultipleUpdate) <MU>`
     - builds across all available update periods; without this option, only one period is processed
   * - :ref:`-(NE|NoEmail) <NE>`
     - suppresses post-build email notification
   * - :ref:`-(NY|NoLeapYear) <NY>`
     - skips February 29 in leap years
   * - :ref:`-(QE|QuitError) <QE>`
     - stops all builds for the dataset on the first error, rather than skipping and continuing
   * - :ref:`-(UB|UseBeginTime) <UB>`
     - uses the period's beginning time instead of end time when substituting temporal patterns

If specialist-defined validation and conversion routines are configured, this
action invokes them. If local and remote files are identical, no action is
taken. Otherwise, standard compress/uncompress and tar/untar utilities handle
one-to-one, many-to-one, or one-to-many conversions. Local files are the
final, archive-ready output.

If a local file already exists on disk, the build action for that file is
skipped. To rebuild, remove the existing local file manually.



:ref:`Back to Top <section3.3.3>`
:ref:`Back to Table of Contents <index>`
