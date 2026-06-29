
.. _section2:

2 - GENERAL DSUPDT USAGE
=================================

| **dsupdt** [[:ref:`-(DS|Dataset) <DS>`] dNNNNNN] [:ref:`Action Option <section3>`] [:ref:`Mode Options <section4>`] [:ref:`Info Options <section5>`]
|        or
| **dsupdt** [:ref:`-(IF|InputFile) <IF>`] InputFileNames

Notation:

.. list-table::
   :widths: auto
   :header-rows: 0

   * - []
     - the enclosed element is optional.
   * - (A|B)
     - either A or B may be used (a short form and a long form).
   * - <OPT>
     - OPT is an option name. Names are case-insensitive; values are not.

Every dsupdt invocation has at most one :ref:`Action option <section3>`, which selects the
task to perform. :ref:`Mode options <section4>` change how the chosen action behaves. :ref:`Info <section5>`
options carry the data the action needs (dataset IDs, file names, dates,
etc.). Each action documents which :ref:`Info options <section5>` are required and which are
optional.

Option :ref:`-DS <DS>` (-Dataset) supplies a dataset number. When it is the first argument
after **dsupdt**, the option name itself may be omitted. Some actions can run
without a dataset number, in which case they apply to all matching update
control or file records across datasets.

Many options have an alias for convenience; both short and long forms are
accepted, and aliases are noted with each option.

.. toctree::
   :maxdepth: 2
   :caption: Table of Contents

   section2.1
   section2.2
   section2.3
   section2.4



| :ref:`Back to Top <section2>`
| :ref:`Back to Table of Contents <index>`
