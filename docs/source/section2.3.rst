
.. _section2.3:

2.3 - Input Files
=================================

Every option except :ref:`-IF <IF>` (-InputFile) may be supplied either on the command
line or in an input file. :ref:`-IF <IF>` is itself only valid on the command line. A
single dsupdt invocation may combine command-line options with one or more
input files. If the only options are inside a single input file, the :ref:`-IF <IF>`
prefix may be omitted. See the description of :ref:`-IF <IF>` in Section 5.2 for the
input-file format (comments, action/mode markers, single-value assignments,
and tabular multi-value assignments, including delimiter overrides).

As a safeguard against operating on the wrong dataset, input file names used
for update configuration must begin with the dataset number in the format
'dNNNNNN.*', where '*' matches one or more valid filename characters.



| :ref:`Back to Top <section2.3>`
| :ref:`Back to Table of Contents <index>`
