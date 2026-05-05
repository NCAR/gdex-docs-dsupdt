
.. _section3:

3 - ACTION OPTIONS
=================================

Action options specify the tasks that **dsupdt** will execute. No values follow
Action options. Depending on the chosen Action, multiple tasks may be
processed in a single execution. Some comprehensive actions automatically
include simpler actions by default; others include additional actions when
certain :ref:`Mode options <section4>` are present. Only one Action option may be specified per
execution; supplying multiple Action options simultaneously is not permitted.

Some actions write information to GDEXDB; others retrieve it. Most actions
target a single dataset, but some can operate across all datasets when no
dataset number is provided.

Actions are organized into three categories based on the type of information
they handle:

.. list-table::
   :widths: auto
   :header-rows: 0

   * - :ref:`Configuration Actions <section3.1>`
     - create, delete, modify, and retrieve information for update controls, local files, and remote files in GDEXDB for a specified dataset
   * - :ref:`All Information Actions <section3.2>`
     - retrieve and modify all update control, local file, and remote file records for a specified dataset in a single operation
   * - :ref:`Update Actions <section3.3>`
     - download remote files, build local files, archive local files onto the GDEX Servers, clean temporary data files, check the update status of files on remote servers, and unlock update controls or local files held by aborted update processes

.. toctree::
   :maxdepth: 2
   :caption: Table of Contents

   section3.1
   section3.2
   section3.3

**Appendix A: List of Examples**

- :ref:`A.1. Action Option -SC (-SetControl) <3.1.1_e1>`
- :ref:`A.2. Action Option -GC (-GetControl) <3.1.2_e2>`
- :ref:`A.3. Action Option -SL (-SetLocalFile) <3.1.3_e3>`
- :ref:`A.4. Action Option -GL (-GetLocalFile) <3.1.4_e4>`
- :ref:`A.5. Action Option -GA (-GetALL) <3.2.1_e5>`



| :ref:`Back to Top <section3>`
| :ref:`Back to Table of Contents <index>`
