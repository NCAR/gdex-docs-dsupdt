
.. _appendixA:

============================
Appendix A: List of Examples
============================

- :ref:`A.1. Action Option -SC (-SetControl): To set three new update control records for d277000 from input file 'd277000.cntl' <3.1.1_e1>`
- :ref:`A.2. Action Option -GC (-GetControl): To retrieve the default update control fields for d277000 <3.1.2_e2>`
- :ref:`A.3. Action Option -SL (-SetLocalFile): -WD '$UPDTWKP/zji/ds084.1/<YYYYMMDD>' resolves to '$UPDTWKP/zji/ds084.1/20071031' for end date 2007-10-31, keeping each day's download and build isolated. Linking a local file record to an update control record (via -CI) causes the control record's scheduled action to run automatically against that local file. <3.1.3_e3>`
- :ref:`A.4. Action Option -SL (-SetLocalFile): To set update information for two new local files of d744004 via input file 'd744004.loc' <3.1.3_e4>`
- :ref:`A.5. Action Option -GL (-GetLocalFile): To retrieve the default local file fields for d744004, local file indices 33 and 34 <3.1.4_e5>`
- :ref:`A.6. Action Option -GA (-GetALL): To retrieve all update control, local file, and remote file information for d277000 at control index 2 <3.2.1_e6>`
- :ref:`A.7. Info Option -CC (-CarbonCopy): To Cc 'schuster@ucar.edu' on update results for d337000 <5.2_e7>`
- :ref:`A.8. Info Option -PD (-PatternDelimiter): When a local file name contains '<P0>.txt', the replacement value for '<P0>' must be the first -GP value; omitting it causes a fatal error. Additional patterns (<P1>, <P2>, ...) are provided as subsequent -GP values. A serial pattern '<Sstart:endS>' (or '<Sstart:end:stepS>' with an explicit step, defaulting to 1) embedded in a local file name (-LF) or remote file name (-RF) expands that single name into a list of names, one per integer from 'start' to 'end' inclusive. Each value is zero-padded to the digit width of 'start'. For example, 'file.<S01:03S>' expands to 'file.01', 'file.02', and 'file.03', while 'file.<S0:6:2S>' expands to 'file.0', 'file.2', 'file.4', and 'file.6'. <5.2_e8>`


| :ref:`Back to Table of Contents <index>`
