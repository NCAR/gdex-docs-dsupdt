
.. _section3.3.8:

3.3.8 - Check Update Status
=====================


.. _CU:

Action Option -**CU** (-**CheckUpdate**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

checks whether remote files are available for retrieval.
This is useful when remote data files become available irregularly but are
organized into files covering regular temporal periods.

| **dsupdt** [[:ref:`-(DS|Dataset) <DS>`] dNNNNNN] -(CU|CheckUpdate) [:ref:`Mode Options <mode3.3.8>`]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(LI|LocalIndex) <LI>` LocalFileIndices]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(LF|LocalFile) <LF>` LocalFileNames]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(CI|ControlIndex) <CI>` UpdateControlIndices]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(XO|ExecOrder) <XO>` ExecOrderIndex]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(RF|RemoteFile) <RF>` RemoteFileNames]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(SF|ServerFile) <SF>` ServerFileNames]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(DO|DownloadOrder) <DO>` DownloadOrderIndices]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(DC|DownloadCommand) <DC>` DownloadCommand]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(ED|EndDate) <ED>` NextDataEndDate]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(EH|EndHour) <EH>` NextDataEndHour]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(GP|GenericPattern) <GP>` GenericPatterns]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(WD|WorkDir) <WD>` WorkingDirectory]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(MR|MissRemote) <MR>` AllowMissRemoteFile]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(FQ|Frequency) <FQ>` UpdateFrequencies]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(CD|CurrentDate) <CD>` CurrentDate]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(CH|CurrentHour) <CH>` CurrentHour]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(HO|HourOffset) <HO>` TimeZoneHourOffset]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(CC|CarbonCopy) <CC>` Cc'dEmailAddresses]
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(DB|Debug) <DB>` DebugModeInfo]

.. _mode3.3.8:

:ref:`Mode options <section4>` that can be specified for this action:

.. list-table::
   :widths: auto
   :header-rows: 0

   * - :ref:`-(CA|CheckAll) <CA>`
     - checks all remote files rather than stopping at the first unavailable one
   * - :ref:`-(EE|ErrorEmail) <EE>`
     - sends email only when an error occurs during checking
   * - :ref:`-(MU|MultipleUpdate) <MU>`
     - checks files across multiple update periods
   * - :ref:`-(NE|NoEmail) <NE>`
     - suppresses post-check email notification
   * - :ref:`-(NY|NoLeapYear) <NY>`
     - skips February 29 in leap years
   * - :ref:`-(SE|SummaryEmail) <SE>`
     - sends a summary-only email with update status, without detailed log information
   * - :ref:`-(UB|UseBeginTime) <UB>`
     - uses the period's beginning time instead of end time when substituting temporal patterns

When executed without additional conditions, all datasets due for updates are
checked for update status.



:ref:`Back to Top <section3.3.8>`
:ref:`Back to Table of Contents <index>`
