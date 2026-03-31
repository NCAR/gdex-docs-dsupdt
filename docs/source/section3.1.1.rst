
.. _section3.1.1:

3.1.1 - Set Update Controls
=====================


.. _SC:

Action Option -**SC** (-**SetControl**) (Alias: -**SetUpdateControl**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

creates or modifies update
control records in GDEXDB for a given dataset. These records schedule data
update actions that are started automatically by the daemon 'dscheck'. One or
more control records may be set per execution.

|  **dsupdt** [[:ref:`-(DS|Dataset) <DS>`] dNNNNNN] -(SC|SetControl) [:ref:`Mode Options <mode3.1.1>`]
|                    :ref:`-(CI|ControlIndex) <CI>` UpdateControlIndices
|                   [:ref:`-(ID|ControlID) <ID>` ControlIdString]
|                   [:ref:`-(SN|Specialist) <SN>` DSSSpecialist]
|                   [:ref:`-(PI|ParentIndex) <PI>` ParentControlIndices]
|                   [:ref:`-(AN|ActionName) <AN>` DSUPDTActionNames]
|                   [:ref:`-(FQ|Frequency) <FQ>` UpdateControlFrequencies]
|                   [:ref:`-(CO|ControlOffset) <CO>` UpdateControlOffsets]
|                   [:ref:`-(CT|ControlTime) <CT>` UpdateControlTimes]
|                   [:ref:`-(RI|RetryInterval) <RI>` ControlRetryInterval]
|                   [:ref:`-(VI|ValidInterval) <VI>` UpdateValidInterval]
|                   [:ref:`-(UC|UpdateControl) <UC>` UpdateControlOptions]
|                   [:ref:`-(MC|EMailControl) <MC>` EmailControlOptions]
|                   [:ref:`-(EC|ErrorControl) <EC>` ErrorControlOptions]
|                   [:ref:`-(KF|KeepFile) <KF>` KeepFileOptions]
|                   [:ref:`-(HO|HourOffset) <HO>` TimeZoneOffsets]
|                   [:ref:`-(DT|DataTime) <DT>` DataUpdatedTimes]
|                   [:ref:`-(HN|HostName) <HN>` HostNames]
|                   [:ref:`-(XC|ExecuteCommand) <XC>` CommandAfterUpdate]
|                   [:ref:`-(CC|CarbonCopy) <CC>` Cc'dEmailAddresses]
|                   [:ref:`-(DB|Debug) <DB>` DebugModeInfo]

.. _mode3.1.1:

:ref:`Mode options <section4>` that can be specified for this action:

.. list-table::
   :widths: auto
   :header-rows: 0

   * - :ref:`-(MD|MyDataset) <MD>`
     - sets information into GDEXDB regardless of dataset ownership
   * - :ref:`-(NC|NewControl) <NC>`
     - adds a new update control record to GDEXDB

If an update control record already exists in GDEXDB, it is modified. A new
record is added only when the control index is 0 and :ref:`Mode option <section4>` :ref:`-NC <NC>`
(-NewControl) is present. The dataset name via :ref:`-DS <DS>` is required only when adding
a new control record.


.. _3.1.1_e1:

**EXAMPLE 1. To set three new update control records for d277000 using input file 'd277000.cntl':**

|  **dsupdt** :ref:`SC <SC>` :ref:`-NC <NC>` :ref:`-IF <IF>` d277000.cntl

Content of input file d277000.cntl:

.. code-block:: none

 Dataset<=>d277000
 ControlIndex<:>Specialist<:>ParentIndex<:>Action<:>Frequency<:>ControlOffset<:>ControlTime<:>RetryInterval<:>UpdateControl<:>EMailControl<:>ErrorControl<:>KeepFile<:>HourOffset<:>
 0<:>zji<:>0<:>UF<:>1W<:>1D9H<:>2011-10-24 09:00:00<:>12H<:><:>A<:>N<:>N<:>0<:>
 0<:>zji<:>0<:>UF<:>1M<:>1D15H<:>2011-11-02 15:00:00<:>1D<:><:>A<:>N<:>N<:>0<:>
 0<:>zji<:>0<:>UF<:>1M<:>2D15H<:>2011-11-03 15:00:00<:>1D<:><:>A<:>N<:>N<:>0<:>



:ref:`Back to Top <section3.1.1>`
:ref:`Back to Table of Contents <index>`
