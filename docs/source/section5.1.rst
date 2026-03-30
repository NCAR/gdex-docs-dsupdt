
.. _section5.1:

5.1 - Single-Value Info Options
=====================

A single-value Info option passes exactly one value into this application.
Exactly one value must follow each such option; providing no value or more
than one value will result in an error.


.. _BP:

Info Option -**BP** (-**BatchProcess**) (Aliases: -**d**, -**DelayedMode**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

delayed mode execution. When
present, the **dsupdt** command is not executed immediately; instead, the command
information is recorded in GDEXDB and executed later by the daemon 'dscheck'.
One or more host names may be specified after :ref:`-BP <BP>` to restrict execution to
specific hosts (or exclude them if prefixed with '!'). For example, '-d PBS'
restricts execution to Portable Batch System (PBS) hosts. An upper limit on
retry attempts (1 to 99) can also be specified; for example, '-d 2' limits
retries to 2. If not specified, the default retry count is 1.


.. _CD:

Info Option -**CD** (-**CurrentDate**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

provides an alternative current date for update actions.
This allows specialists to rerun an update for re-archiving or recovering a
deleted update action.


.. _CH:

Info Option -**CH** (-**CurrentHour**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

provides an alternative current hour for update actions.
This allows specialists to rerun an update for re-archiving or recovering a
deleted update action.


.. _DS:

Info Option -**DS** (-**Dataset**) (Aliases: -**Dsid**, -**DatasetID**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

the dataset ID in the format [a-z]NNNNNN.


.. _DV:

Info Option -**DV** (-**Divider**) (Aliases: -**Delimiter**, -**Separator**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

delimiter for separating
column values of multi-value Info options in input files. Defaults to '<:>'.


.. _ES:

Info Option -**ES** (-**EqualSign**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

sets the delimiter used to assign values to options in
input files. Defaults to '<=>'.


.. _FN:

Info Option -**FN** (-**FieldNames**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

a string of single-letter field names specifying which
fields to retrieve via :ref:`-GL <GL>` (-GetLocalFile) or :ref:`-GR <GR>` (-GetRemoteFile). Omitting
this option returns the default fields. Valid names are listed in each
action's section.


.. _LN:

Info Option -**LN** (-**LoginName**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

the login name of the executing specialist. Defaults to
the current user. Set this option to run **dsupdt** on behalf of another
specialist. If the provided name differs from the actual login, :ref:`-MD <MD>` is
automatically applied when calling `dsarch <https://gdex-docs-dsarch.readthedocs.io/en/latest/index.html>`_.


.. _OF:

Info Option -**OF** (-**OutputFile**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

specifies an output file name into which this application
writes its results. The output format matches the input file format. If not
specified, results are displayed on screen.


.. _ON:

Info Option -**ON** (-**OrderNames**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

a string of single-letter field names that determines the
sort order of GET action results (:ref:`-GC <GC>`, :ref:`-GL <GL>`, :ref:`-GR <GR>`). Uppercase letters sort
ascending; lowercase sort descending.


.. _PL:

Info Option -**PL** (-**ProcessLimit**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

defaults to 1. When set to a value greater than 1,
**dsupdt** spawns that many child processes, each handling one update record in
parallel. The parent process exits once all records are handled. Useful for
datasets with many independent, time-consuming update records.


.. _AO:

Info Option -**AO** (-**ActOption**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

sets the marker used to designate :ref:`Action <section3>` and :ref:`Mode <section4>` options
in input files. Defaults to '<!>'.


.. _VS:

Info Option -**VS** (-**ValidSize**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

the minimum file size considered valid for archiving.
Defaults to 100 bytes. Can be overridden on the command line at run time.



:ref:`Back to Top <section5.1>`
:ref:`Back to Table of Contents <index>`
