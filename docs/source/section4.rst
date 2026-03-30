
.. _section4:

4 - MODE OPTIONS
=====================

Mode options modify the behavior of :ref:`Action options <section3>`. All Mode options are
optional and do not accept values.


.. _AW:

Mode Option -**AW** (-**AnyWhere**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

works with :ref:`Info option <section5>` :ref:`-BP <BP>` (-BatchProcess) to use an empty
working directory so that the recorded **dsupdt** command can be executed from
any directory, rather than only from the directory where it was originally
recorded.


.. _BG:

Mode Option -**BG** (-**BackGround**) (Alias: -**b**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

background process. When present, screen
display is suppressed for both standard output and errors.


.. _CA:

Mode Option -**CA** (-**CheckAll**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

if present, allows check update actions :ref:`-CU <CU>` (-CheckUpdate)
to verify availability of all remote files. Without it, checking stops after
the first unavailable file.


.. _CN:

Mode Option -**CN** (-**CheckNewer**) (Alias: -**CheckNewFile**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

when the server file is available
locally, checks if it has changed on the server and re-downloads it if so.
This option is ignored if :ref:`-RD <RD>` is present. A local copy of the data file is
required for the comparison. This copy is normally the local copy of the server
file, but may also be an existing remote or local file with identical content,
even if the name differs.

For this option to work correctly, specialists must maintain a valid local
copy of the data file and a download command capable of checking the server
for changes. Suitable commands include 'cp', 'mv', and 'tar' for local files,
and 'scp', 'wget', and 'ncftpget' for remote files. Custom download commands
must include built-in logic for detecting server-side changes.

If the server and local time zones differ, provide :ref:`-HO <HO>` (-HourOffset) with the
hour difference so that local and remote file timestamps can be compared
correctly.


.. _CP:

Mode Option -**CP** (-**CurrentPeriod**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

if present, allows update actions when the current
date/hour falls within the current update period, even if the data end
date/hour is not yet due.


.. _EE:

Mode Option -**EE** (-**ErrorEmail**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

sends an email notification only when an error occurs
during the update action.


.. _FO:

Mode Option -**FO** (-**FormatOutput**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

formats the output of GET actions so that all values
in a given field share the same dynamically calculated column width.


.. _FU:

Mode Option -**FU** (-**FutureUpdate**) (Alias: -**ForceUpdate**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

if present, forces update for at least one end date/time,
even if the update is not yet due.


.. _GZ:

Mode Option -**GZ** (-**GMTZone**) (Aliases: -**GMT**, -**GreenwichZone**, -**UTC**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

uses GMT rather than
local time as the reference for update action scheduling.


.. _HU:

Mode Option -**HU** (-**HourlyUpdate**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

forces time tracking to advance in hourly steps after
a successful data file archive.


.. _IE:

Mode Option -**IE** (-**IgnoreError**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

used with :ref:`-MU <MU>` (-MultipleUpdate) to skip failed updates
and continue processing subsequent periods. For records with a valid interval
defined, **dsupdt** also looks back over that interval to re-archive any
missing data.


.. _KR:

Mode Option -**KR** (-**KeepRemote**) (Alias: -**KeepRemoteFile**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

preserves the remote file on
disk by copying it to the local file location rather than moving it.


.. _KS:

Mode Option -**KS** (-**KeepServer**) (Alias: -**KeepServerFile**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

preserves the server file on
disk by copying it to the remote file location rather than moving it.


.. _LO:

Mode Option -**LO** (-**LogOn**) (Alias: -**LoggingOn**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

turns on detail logging when :ref:`Info <section5>` option
:ref:`-PL <PL>` (-ProcessLimit) is present for update actions.


.. _MD:

Mode Option -**MD** (-**MyDataset**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

allows a specialist to add or modify update records for
a dataset owned by another specialist.


.. _MO:

Mode Option -**MO** (-**MissedOnly**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

skips files that are already archived. Typically used
with :ref:`-MU <MU>` (-MultipleUpdate). Ignored when :ref:`-RA <RA>`, :ref:`-RD <RD>`, or :ref:`-CN <CN>` is present.


.. _MU:

Mode Option -**MU** (-**MultipleUpdate**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

processes all available elapsed update periods.
Without this option, only the most recent period is processed.


.. _NC:

Mode Option -**NC** (-**NewControl**) (Alias: -**NewUpdateControl**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

required when adding a new update control record via
:ref:`-SC <SC>` (-SetControl) with a control index of 0. Guards against unintentional
record creation.


.. _NE:

Mode Option -**NE** (-**NoEmail**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

suppresses all post-update email notifications.


.. _NL:

Mode Option -**NL** (-**NewLocfile**) (Alias: -**NewLocalFile**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

required when adding a new local file record via
:ref:`-SL <SL>` (-SetLocalFile) with a local file index of 0. Guards against unintentional
record creation.


.. _NY:

Mode Option -**NY** (-**NoLeapYear**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

skips February 29 for leap years.


.. _QE:

Mode Option -**QE** (-**QuitError**) (Alias: -**QuitOnError**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

stops all update processing for the
dataset on the first error, rather than skipping the failed file and
continuing.


.. _RA:

Mode Option -**RA** (-**RetryArchive**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

forces re-archiving of local files by passing :ref:`-RA <RA>`
to `dsarch <https://gdex-docs-dsarch.readthedocs.io/en/latest/index.html>`_.


.. _RD:

Mode Option -**RD** (-**RetryDownload**) (Alias: -**Redownload**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

retries downloading the remote
file if it already exists locally, for :ref:`Action <section3>` :ref:`-DR <DR>` (-DownloadRemote).


.. _RE:

Mode Option -**RE** (-**ResetEndTime**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

if present, resets the end date/hour when the file
timestamp is newer than the end date/hour plus one update frequency.


.. _RO:

Mode Option -**RO** (-**ResetOrder**) (Alias: -**Reorder**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

when present, resets the execution
order of the given local files to match the order in which the update records
are provided for action :ref:`-SL <SL>` (-SetLocalFile). Local files can also be reordered
by explicitly providing order index values via :ref:`Info option <section5>` :ref:`-XO <XO>` (-ExecOrder).


.. _SE:

Mode Option -**SE** (-**SummaryEmail**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

sends a brief summary email after the update action,
omitting detailed log information.


.. _UB:

Mode Option -**UB** (-**UseBeginTime**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

when present, uses the beginning time of the update
period to replace temporal patterns in file names, download commands, and
other fields.


.. _UT:

Mode Option -**UT** (-**UpdateTime**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

when present, forces an update of the data end time and
next due update times in local file records, regardless of whether the update
actions succeed.



:ref:`Back to Top <section4>`
:ref:`Back to Table of Contents <index>`
