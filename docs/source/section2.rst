
.. _section2:

2 - GENERAL DSUPDT USAGE
=====================

|  **dsupdt** [[:ref:`-(DS|Dataset) <DS>`] dNNNNNN] [:ref:`Action Option <section3>`] [:ref:`Mode Options <section4>`] [:ref:`Info Options <section5>`]
|          or
|  **dsupdt** [:ref:`-(IF|InputFile) <IF>`] InputFileNames

Brackets [] indicate optional elements. A pipe '|' within parentheses, as in
(A|B), means either A or B may be used. Options are divided into three
categories:

.. list-table::
   :widths: auto
   :header-rows: 0

   * - :ref:`Action options <section3>`
     - specify what task to execute
   * - :ref:`Mode options <section4>`
     - modify how an action behaves
   * - :ref:`Info options <section5>`
     - supply values to the action

Each option may be given in either its short or long form (e.g., :ref:`-DS <DS>` or -Dataset).
Some options have alias names for convenience. Option names are case-insensitive,
but the values following :ref:`Info options <section5>` are case-sensitive.

Option :ref:`-DS <DS>` specifies a dataset number. If provided as the first argument
following **dsupdt**, the :ref:`-DS <DS>` (-Dataset) option name may be omitted. Some actions
can run without a dataset number, in which case they apply to all available
update control or file records across all datasets.

Specify exactly one :ref:`Action option <section3>` per execution. Depending on the chosen :ref:`Action <section3>`,
certain :ref:`Info options <section5>` are mandatory, others are optional, and specific :ref:`Mode <section4>` options
may be applied to alter the action's behavior.

All options except :ref:`-IF <IF>` (-InputFile) may be provided either on the command line
or in input files. Input file names are specified via :ref:`-IF <IF>` and can only be given
on the command line. See the :ref:`-IF <IF>` option description for details on how to
format options in input files. One or more input files may be combined with
command-line options. The :ref:`-IF <IF>` option name itself may be omitted when a single
input file is given on the command line and all action and option information is
contained within that file.

:ref:`Info options <section5>` used with GET actions serve as query filters. Four special
characters enable more precise filtering — they must be quoted or escaped
on the command line to prevent shell interpretation:

.. list-table::
   :widths: auto
   :header-rows: 0

   * - '!'
     - exclude matches; must appear immediately after the option name
   * - '<'
     - less-than comparison on the following value
   * - '>'
     - greater-than comparison on the following value
   * - '<>'
     - range between two values

Combining '!' and '<' as "'!' '<' OptionValue" expresses a 'greater than or
equal to OptionValue' condition.

The description of an individual option is displayed when **dsupdt** is run as

| **dsupdt** [Option] -(h|help) [Option]

The description is shown for the option placed either before or after -(h|help).
If no option is given, or **dsupdt** is run without arguments, the full document
is displayed using the UNIX 'more' utility. A printed copy of this document is
available at $DSSHOME/dssdb/prog_usage/dsupdt.usg, where $DSSHOME is the
environment variable for the DSS home directory.



:ref:`Back to Top <section2>`
:ref:`Back to Table of Contents <index>`
