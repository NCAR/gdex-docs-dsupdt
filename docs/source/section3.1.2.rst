
.. _section3.1.2:

3.1.2 - Get Update Controls
===========================


.. _GC:

Action Option -**GC** (-**GetControl**) (Alias: -**GetUpdateControl**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

retrieves update control
records for a given dataset.

| **dsupdt** [[:ref:`-(DS|Dataset) <DS>`] dNNNNNN] -(GC|GetControl) [:ref:`Mode Option <mode3.1.2>`]
|           [:ref:`-(FN|FieldNames) <FN>` FieldNameString]
|           [:ref:`-(CI|ControlIndex) <CI>` UpdateControlIndices]
|           [:ref:`-(ID|ControlID) <ID>` ControlIdString]
|           [:ref:`-(SN|Specialist) <SN>` DSSSpecialist]
|           [:ref:`-(PI|ParentIndex) <PI>` ParentControlIndices]
|           [:ref:`-(AN|ActionName) <AN>` DSUPDTActionNames]
|           [:ref:`-(FQ|Frequency) <FQ>` UpdateControlFrequencies]
|           [:ref:`-(CO|ControlOffset) <CO>` UpdateControlOffsets]
|           [:ref:`-(CT|ControlTime) <CT>` UpdateControlTimes]
|           [:ref:`-(OF|OutputFile) <OF>` OutputFileName]
|           [:ref:`-(DB|Debug) <DB>` DebugModeInfo]

.. _mode3.1.2:

:ref:`Mode option <section4>` that can be specified for this action:

.. list-table::
   :widths: auto
   :header-rows: 0

   * - :ref:`-(FO|FormatOutput) <FO>`
     - formats each column to a uniform fixed width

Use :ref:`Info option <section5>` :ref:`-FN <FN>` (-FieldNames) to specify which control fields to
retrieve. It defaults to 'CLNPAFOTRVUJEKZ' if option :ref:`-FN <FN>` is not provided.
Update information of all available fields is retrieved if :ref:`-FN <FN>` ALL is given.

Valid field names of update controls and their corresponding :ref:`Info option <section5>` names:

.. list-table::
   :widths: auto
   :header-rows: 1

   * - Names
     - :ref:`Info Options <section5>`
     - Descriptions
   * - C
     - :ref:`-(CI|ControlIndex) <CI>`
     - index of update control record
   * - L
     - :ref:`-(ID|ControlID) <ID>`
     - descriptive id for a control record
   * - N
     - :ref:`-(SN|Specialist) <SN>`
     - DSS specialist who owns the control record
   * - P
     - :ref:`-(PI|ParentIndex) <PI>`
     - parent index, refers to a dcupdt.cindex if not 0
   * - A
     - :ref:`-(AN|ActionName) <AN>`
     - update action name for **dsupdt**
   * - F
     - :ref:`-(FQ|Frequency) <FQ>`
     - frequency of update control, i.e., 1W, 1M
   * - O
     - :ref:`-(CO|ControlOffset) <CO>`
     - time offset for next process, i.e., 2D10H, 3H15N
   * - T
     - :ref:`-(CT|ControlTime) <CT>`
     - time to run dsupdt, format: YYYY-MM-DD HH:NN:SS
   * - R
     - :ref:`-(RI|RetryInterval) <RI>`
     - retry interval for failed dsupdt, i.e., 1M2D, 2H
   * - V
     - :ref:`-(VI|ValidInterval) <VI>`
     - update valid interval, i.e., 2D, 1M
   * - U
     - :ref:`-(UC|UpdateControl) <UC>`
     - any of B-Begin, C-Current, E-Reset End Date/Time, F-Future, G-GMT, M-Multi, N-New, O-Miss, Y-Skip Feb. 29, Z-Allow Zero Filesize
   * - J
     - :ref:`-(MC|EMailControl) <MC>`
     - one of A-All, E-Error, N-No, S-Summary, B-Summary when Error
   * - E
     - :ref:`-(EC|ErrorControl) <EC>`
     - one of I-Ignore Error, Q-Quit on Error, N-Neither
   * - K
     - :ref:`-(KF|KeepFile) <KF>`
     - one of S-Server File, R-Remote File, B-Keep Both, N-Neither
   * - Z
     - :ref:`-(HO|HourOffset) <HO>`
     - time zone hour offset, hours ahead of local time
   * - D
     - :ref:`-(DT|DataTime) <DT>`
     - time data updated to, format: YYYY-MM-DD HH:NN:SS
   * - H
     - :ref:`-(HN|HostName) <HN>`
     - hostnames on which this control index can or cannot be processed
   * - Q
     - :ref:`-(QS|QsubOptions) <QS>`
     - additional PBS qsub options
   * - Y
     - :ref:`-(CC|CarbonCopy) <CC>`
     - carbon copies for additional email addresses
   * - X
     - :ref:`-(XC|ExecuteCommand) <XC>`
     - Command to be executed after successful update

If no dataset number is given, update control information is displayed for all
available control records across all datasets owned by the specialist running
**dsupdt**.


.. _3.1.2_e2:

**EXAMPLE 2. To retrieve the default update control fields for d277000:**

| **dsupdt** d277000 GC

Content of the output:

.. code-block:: none

 Dataset<=>d277000
 ControlIndex<:>Specialist<:>ParentIndex<:>Action<:>Frequency<:>ControlOffset<:>ControlTime<:>RetryInterval<:>UpdateControl<:>EMailControl<:>ErrorControl<:>KeepFile<:>HourOffset<:>
 1<:>zji<:>0<:>UF<:>1W<:>1D9H<:>2011-10-24 09:00:00<:>12H<:><:>A<:>N<:>N<:>0<:>
 2<:>zji<:>0<:>UF<:>1M<:>1D15H<:>2011-11-02 15:00:00<:>1D<:><:>A<:>N<:>N<:>0<:>
 3<:>zji<:>0<:>UF<:>1M<:>2D15H<:>2011-11-03 15:00:00<:>1D<:><:>A<:>N<:>N<:>0<:>



| :ref:`Back to Top <section3.1.2>`
| :ref:`Back to Table of Contents <index>`
