
.. _section5.2:

5.2 - Multi-Value Info Options
=================================

A multi-value Info option passes one or more values for a single Info option
into **dsupdt**. At least one value must follow each multi-value option.


.. _AN:

Info Option -**AN** (-**ActionName**) (Aliases: -**Action**, -**AC**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

the action to run: set in update control
records to drive **dsupdt** processing, and in local file records to drive
`dsarch <https://gdex-docs-dsarch.readthedocs.io/en/latest/index.html>`_ archiving.


.. _AT:

Info Option -**AT** (-**AgeTime**) (Aliases: -**FileAge**, -**FileAgeTime**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

the minimum age a remote
file must have before it is eligible for download. When set, **dsupdt** checks
the file's timestamp on the server and skips the download if the file is
newer than the configured age threshold.


.. _BC:

Info Option -**BC** (-**BuildCommand**) (Alias: -**BuildCmd**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

an external command for building
local files, used in place of the standard tar/compress approach.

The following option values are substituted at call time: :ref:`-LF <LF>`, :ref:`-RF <RF>`, :ref:`-SF <SF>`,
:ref:`-DS <DS>`, :ref:`-ED <ED>`, :ref:`-EH <EH>`, :ref:`-SN <SN>`/LN, and :ref:`-LI <LI>`.

To send a deferred email from within your build command, pass :ref:`-LI <LI>` to obtain
the local file index, then save the email content to the dlupdt.emnote field
of that record. To defer until multiple records complete, pass the index of
the last record. The email is sent only after all included records update
successfully.


.. _BT:

Info Option -**BT** (-**BeginTime**) (Aliases: -**IT**, -**InitialTime**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

specifies the start time when generating multiple remote
file names from a temporal pattern. Used with :ref:`-TI <TI>` (-TimeInterval). Defaults
to 0, meaning the first available time in the period (hour 00 for hourly
updates, the 1st for monthly updates).

To specify non-standard start days per month, provide 12 colon-separated
offset values in the form D:D:D:D:D:D:D:D:D:D:D:D.


.. _CC:

Info Option -**CC** (-**CarbonCopy**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

adds one or more Cc recipients for update notification
emails. Can be set in update control records via :ref:`-SC <SC>` or supplied at run time
on the command line. DSS specialists may use login names; others must provide
full addresses for domains outside 'ucar.edu'.


.. _5.2_e6:

**EXAMPLE 6. To Cc 'schuster@ucar.edu' on update results for d337000:**

| **dsupdt** d337000 :ref:`UF <UF>` :ref:`-MU <MU>` :ref:`-IE <IE>` :ref:`-CC <CC>` schuster


.. _CI:

Info Option -**CI** (-**ControlIndex**) (Alias: -**UpdateControlIndex**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

update control indices for
setting update control records. A single control index can be provided for
updates of multiple local file records. Provide one control index at a time
for any update action.


.. _CL:

Info Option -**CL** (-**CleanCommand**) (Alias: -**CleanFile**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

a command stored in the local file record and run during
data update to clean up temporary files.


.. _CO:

Info Option -**CO** (-**ControlOffset**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

a time offset (e.g., 2D10H, 3H15N) added to the
control frequency to determine the next scheduled run time. For example, with
a monthly frequency and no offset, the next run after completing 2011-09 is
scheduled for 2011-10-01 00:00:00. With an offset of 2D10H30N, it becomes
2011-10-03 10:30:00.


.. _CT:

Info Option -**CT** (-**ControlTime**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

the scheduled run time for an update control record,
in the form YYYY-MM-DD HH:NN:SS. After a successful update, this time is
advanced to the next period based on the control frequency and offset.


.. _DC:

Info Option -**DC** (-**DownloadCommand**) (Aliases: -**Command**, -**Download**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

the command used to
download a remote file, copy a local file, or generate a remote file via local
processing. Can be set in both local and remote file records; used by
:ref:`-DR <DR>` (-DownloadRemote). At run time, the command precedence is:

.. list-table::
   :widths: auto
   :header-rows: 1
 command line > remote file record > local file record.


.. _DB:

Info Option -**DB** (-**Debug**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

enables debug mode with specified detail level. This option
accepts up to 3 values: Debug Level, debug log file path, and debug log file
name. The debug level is required and may be a single integer (e.g., 1000 to
log levels 1 through 1000) or a range (e.g., 200-1000). The default log path
is '$DSSHOME/dssdb/log' and the default log file name is 'mydss.dbg'. Provide
the second and third values to override these defaults.


.. _DE:

Info Option -**DE** (-**Description**) (Aliases: -**Desc**, -**Note**, -**FileDesc**, -**FileDescription**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

a
description for data files. Multi-line descriptions are supported when
supplied via an input file (:ref:`-IF <IF>`).


.. _DO:

Info Option -**DO** (-**DownloadOrder**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

download priority indices for remote file records
when a file is available from multiple servers. The server with index 0 is
tried first, then index 1, and so on.


.. _DT:

Info Option -**DT** (-**DataTime**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

timestamps (YYYY-MM-DD HH:NN:SS) recording how far data
has been updated. Used to manage control record dependencies via
:ref:`-PI <PI>` (-ParentIndex): a control record will not run for a given period until
the parent control record's data time confirms completion.


.. _EC:

Info Option -**EC** (-**ErrorControl**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

a single-letter error handling setting for update
control records:

* I: ignore errors and continue processing all periods (equivalent to :ref:`-IE <IE>`);
* Q: stop immediately on any error (equivalent to :ref:`-QE <QE>`);
* N: normal behavior — stop the current period on error, but continue with other local files under the same control record.


.. _ED:

Info Option -**ED** (-**EndDate**) (Alias: -**UpdateEndDate**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

the data end date of the next update period.


.. _EH:

Info Option -**EH** (-**EndHour**) (Alias: -**UpdateEndHour**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

the data end hour of the next update period. Applicable only
to datasets with sub-daily (hourly) update frequencies.

Local file dependencies are configured via :ref:`-PI <PI>` (-ParentIndex). When set, a
local file record is blocked for a given end date (and hour, if applicable)
until the parent local file record completes that same end date and hour.


.. _EP:

Info Option -**EP** (-**EndPeriod**) (Alias: -**EndPeriodDay**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

the end point of the update period derived from the
frequency set by :ref:`-FQ <FQ>`. A value of 0 (default) means the natural end of the
period — e.g., '2007-03-31' for a monthly record covering March 2007.


.. _ET:

Info Option -**ET** (-**EndTime**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

the end time used when generating multiple remote file names
from a temporal pattern. Used with :ref:`-TI <TI>` (-TimeInterval). Defaults to 0, meaning
the last available time in the period.

To specify non-standard end days per month, provide 12 colon-separated offset
values in the form D:D:D:D:D:D:D:D:D:D:D:D.


.. _FQ:

Info Option -**FQ** (-**Frequency**) (Alias: -**UpdateFrequency**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

the update frequency expressed as NU, where N is an integer
and U is a unit letter: Y (year), M (month), W (week), D (day), H (hour);
e.g., 1W, 5D, 6H. Sub-monthly fractions are supported as NU/F; for example,
1M/3 divides each month into three periods: days 1-10, 11-20, and 21-end
(8 to 11 days depending on the month).


.. _FA:

Info Option -**FA** (-**FileArchived**) (Aliases: -**SF**, -**WF**, -**QF**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

overrides the automatically generated archived file
name for data on the GDEX Server.


.. _GP:

Info Option -**GP** (-**GenericPattern**) (Alias: -**GeneralPattern**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

supplies values for generic
patterns on the command line. The first value replaces '<P0>', the second
'<P1>', and so on.

When two patterns are used (<P0> and <P1>), providing 2n values causes the
substitution to loop n times (n > 0).


.. _HN:

Info Option -**HN** (-**HostName**) (Alias: -**HostMachine**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

one or more host names stored in an update control record
to restrict or allow its associated update actions on specific machines.


.. _HO:

Info Option -**HO** (-**HourOffset**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

a time zone offset in hours used by :ref:`-CN <CN>` (-CheckNewer) to
compare server and local file timestamps. Positive values mean the server is
ahead of local time; negative values mean it is behind. Can be stored in an
update control record via :ref:`-SC <SC>` (-SetControl).


.. _ID:

Info Option -**ID** (-**ControlID**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

a unique descriptive string identifying an update control
record.


.. _IF:

Info Option -**IF** (-**InputFile**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

one or more input file names supplied on the command line.
Each file name must begin with the dataset number in the format 'dNNNNNN.*'
and match the dataset number given by :ref:`-DS <DS>`. This naming rule prevents
accidentally targeting the wrong dataset. Input files contain option names
and their values for passing to **dsupdt**.

In an input file, lines beginning with '#' are treated as comments. Option
names may be given in short, long, or alias form. :ref:`Action <section3>` and :ref:`Mode options <section4>` use
the format OptionName<!>. Single-value assignments use the format
OptionName<=>OptionValue, one per line. The :ref:`Action <section3>`/Mode option sign can be
changed via -AO (-ActOption, default '<!>'); the assignment sign can be changed
via -ES (-EqualSign, default '<=>').  Multi-value assignments are column-
delimited using the separator set by -DV (-Divider, default '<:>'). A column
title line precedes the data rows. Data ends at the end of the file or when a
new column title line or single-value assignment is encountered. If the last
column contains multi-line values, an additional separator must be appended to
each line, including the title line.


.. _KF:

Info Option -**KF** (-**KeepFile**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

controls which files are retained on local disk after a
data update:

* S: keep server files (equivalent to :ref:`-KS <KS>`);
* R: keep remote files after building local files (equivalent to :ref:`-KR <KR>`);
* B: keep both (equivalent to :ref:`-KS <KS>` and :ref:`-KR <KR>` combined);
* N: keep neither.


.. _LF:

Info Option -**LF** (-**LocalFile**) (Alias: -**LocalFileIndex**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

local file names for setting update local file records;
used later for building and archiving local data files onto the GDEX Server.
If temporal patterns are present in the given file names, they are replaced
by times derived from the end date/hour of the update periods.

A different local file name can be provided at the update run time if a local
file index is provided.


.. _LI:

Info Option -**LI** (-**LocalIndex**) (Aliases: -**LocIndex**, -**UpdateIndex**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

indices for setting update local
file records. A local file index may be provided to update an individual
local file record.


.. _MC:

Info Option -**MC** (-**EMailControl**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

controls when notification emails are sent from update
control records:

* E: email only on error (equivalent to :ref:`-EE <EE>`);
* N: no email (equivalent to :ref:`-NE <NE>`);
* S: summary email only (equivalent to :ref:`-SE <SE>`);
* A: always send a detailed email;
* B: summary email, but only on error (equivalent to :ref:`-SE <SE>` + :ref:`-EE <EE>` combined).


.. _MR:

Info Option -**MR** (-**MissRemote**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

when set to 'Y', allows one or more required remote
files to be absent when building a local file. When :ref:`-VI <VI>` (-ValidInterval) is
also set, download attempts continue until the missing files arrive or the
valid interval expires.


.. _DI:

Info Option -**DI** (-**DueInterval**) (Alias: -**NextDue**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

the interval between the data end date/hour and when the
data file is expected to be ready for update, as set in the local file record.
The next update date/hour is calculated by adding this interval to the data
end date/hour.


.. _OP:

Info Option -**OP** (-**Options**) (Alias: -**DsarchOption**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

passes a string of up to 128
characters to `dsarch <https://gdex-docs-dsarch.readthedocs.io/en/latest/index.html>`_ as additional Info and :ref:`Mode options <section4>` for archiving.
Group index or name values can be included, with temporal patterns embedded
to dynamically identify group information at update time.


.. _PD:

Info Option -**PD** (-**PatternDelimiter**) (Aliases: -**TD**, -**TemporalDelimiter**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

the delimiters enclosing temporal or generic
patterns in file names and other text fields. Defaults to '<' and '>'. By
default, patterns are replaced with the data end date/hour. Wrapping a
pattern's content with 'C' (e.g., <CYYYY.MM.DD.HHC>) uses the current
date/hour instead; wrapping with 'B' (e.g., <BYYYY.MM.DD.HHB>) uses the
period's beginning date/hour. For sub-monthly frequencies, <M*M> generates
distinct names per fraction: 'C' for uppercase (A, B, C, ...), 'c' for
lowercase (a, b, c, ...), and 'N' for numeric (1, 2, 3, ...).

Generic patterns are supplied at run time via :ref:`-GP <GP>` (-GenericPattern). For
example, if a local file name contains '<P0>.txt', the replacement value for
'<P0>' must be the first :ref:`-GP <GP>` value; omitting it causes a fatal error.
Additional patterns (<P1>, <P2>, ...) are provided as subsequent :ref:`-GP <GP>` values.


.. _PI:

Info Option -**PI** (-**ParentIndex**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

establishes dependencies between records. Set a parent
control index on an update control record to ensure the parent runs first;
set a parent local index on a local file record to ensure the parent local
file is built and archived first.


.. _PR:

Info Option -**PR** (-**ProcessRemote**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

a specialist-defined command for validating and
converting remote files after download.

The following option values are substituted at call time: :ref:`-LF <LF>`, :ref:`-RF <RF>`, :ref:`-SF <SF>`,
:ref:`-DS <DS>`, :ref:`-ED <ED>`, :ref:`-EH <EH>`, :ref:`-SN <SN>`/LN, and :ref:`-LI <LI>`.

To send a deferred email from within your process command, pass :ref:`-LI <LI>` to obtain
the local file index, then save the email content to the dlupdt.emnote field
of that record. To defer until multiple records complete, pass the index of
the last record. The email is sent only after all included records update
successfully.


.. _QS:

Info Option -**QS** (-**QSubOptions**) (Alias: -**PBSOptions**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

specifies options for executing
**dsupdt** as a batch job via qsub on PBS nodes. Qsub options must be quoted
when provided on the command line, e.g., :ref:`-QS <QS>` '-l walltime=12:00:00'.


.. _RF:

Info Option -**RF** (-**RemoteFile**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

remote file names for setting update remote file records;
used later for downloading remote data files and building local files.
If temporal patterns are present in the given file names, they are replaced
by times derived from the end date/hour of the update periods. Local file
names are used if remote file names are not specified.

When a remote file has the same name as the local file, the local file record
alone is sufficient for data update. A remote file record is needed only when
the remote file differs from the local file, when multiple remote files are
downloaded and tarred into a single local file, or when a single remote file
is available from multiple servers.

Multiple remote files can be provided in a single remote file record by joining
them with '::' as a separator, for example: Rfile1::Rfile2::Rfile3.

A remote file name beginning with '!' is treated as a shell command; its
output is used as the dynamically generated remote file name.


.. _RI:

Info Option -**RI** (-**RetryInterval**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

the wait time (in days or hours) before retrying an
update control process after a failed attempt.


.. _RO:

Mode Option -**RO** (-**ResetOrder**) (Alias: -**Reorder**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

when present, resets the execution
order of the given local files to match the order in which the update records
are provided for action :ref:`-SL <SL>` (-SetLocalFile). Local files can also be reordered
by explicitly providing order index values via Info option :ref:`-XO <XO>` (-ExecOrder).


.. _SF:

Info Option -**SF** (-**ServerFile**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

specifies file names on remote servers when they differ
from the remote file names.


.. _SN:

Info Option -**SN** (-**Specialist**) (Alias: -**SpecialistName**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

the specialist login name stored in GDEXDB for an update
record. Defaults to the current user's login. At run time, the login is
validated against the stored name; a mismatch blocks the update.


.. _TI:

Info Option -**TI** (-**TimeInterval**) (Alias: -**Interval**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

the step size used to generate multiple remote file
names from a temporal pattern within a single update period, stepping from
the beginning time (:ref:`-BT <BT>`) to the data end date/hour.


.. _UC:

Info Option -**UC** (-**UpdateControl**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

a string of single letters pre-configuring :ref:`Mode <section4>`
options in an update control record:

* B: use period begin times for temporal patterns (equivalent to :ref:`-BT <BT>` mode);
* C: allow updates within the current period before the end time is due (equivalent to :ref:`-CP <CP>`);
* E: reset end date/hour when the file timestamp exceeds it by one frequency (equivalent to :ref:`-RE <RE>`);
* F: force at least one update even if not yet due (equivalent to :ref:`-FU <FU>`);
* G: use GMT as controlling time (equivalent to :ref:`-GZ <GZ>`);
* M: process multiple update periods (equivalent to :ref:`-MU <MU>`);
* N: check for changed remote files and update only those (equivalent to :ref:`-CN <CN>`);
* O: process only periods with missing archives (equivalent to :ref:`-MO <MO>`);
* Y: skip February 29 in leap years (equivalent to :ref:`-NY <NY>`);
* Z: treat zero-byte files as valid (equivalent to :ref:`-VS <VS>` 0).


.. _VI:

Info Option -**VI** (-**ValidInterval**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

sets the number of days or hours remote files remain
valid on the server. If the time difference between the current date/time and
the data date/time exceeds the interval configured in GDEXDB by this option,
**dsupdt** will not attempt a download.


.. _WD:

Info Option -**WD** (-**WorkDir**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

the working directory for staging temporary files during
download and archive operations. The root path can be set via the environment
variable $UPDTWKP, which defaults to '/glade/data02/dsswork' on machines with
write access to /glade/data02. For example, '$UPDTWKP/zji/icoads' resolves to
'/glade/data02/dsswork/zji/icoads'. To use a different root path, set the
$UPDTWKP environment variable before running **dsupdt**.


.. _XC:

Info Option -**XC** (-**ExecuteCommand**) (Alias: -**ExecCmd**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

an external command run after a
successful update action for a given update control configuration.


.. _XO:

Info Option -**XO** (-**ExecOrder**) (Alias: -**ExecuteOrder**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

explicit execution order indices for local file records
within a dataset. Ignored when :ref:`-RO <RO>` (-ResetOrder) is present.



| :ref:`Back to Top <section5.2>`
| :ref:`Back to Table of Contents <index>`
