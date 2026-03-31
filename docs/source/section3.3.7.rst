
.. _section3.3.7:

3.3.7 - Unlock Local Files
=====================


.. _UL:

Action Option -**UL** (-**UnLock**) (Alias: -**UnLockUpdate**) :
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

clears lock information from update
records whose processes terminated abnormally. While a record is being
processed, its PID and hostname are temporarily saved. If the process aborts,
this information may not be cleared, preventing the record from being
reprocessed on another host. Use this action to manually clear those locks.

| **dsupdt** -(UL|UnLockUpdate)
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :ref:`-(CI|ControlIndex) <CI>` UpdateControlIndices
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(DB|Debug) <DB>` DebugModeInfo]
| &nbsp;&nbsp;&nbsp;&nbsp; or

| **dsupdt** -(UL|UnLockUpdate)
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; :ref:`-(LI|LocalIndex) <LI>` LocfileIndices
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [:ref:`-(DB|Debug) <DB>` DebugModeInfo]

A control index is required to unlock a control record; a local file index
is required to unlock a local file record.



:ref:`Back to Top <section3.3.7>`
:ref:`Back to Table of Contents <index>`
