# MitreAttack
Python wrapper for the Mitre ATT&amp;CK framework API

## Methods
```python
from MitreAttack import Attack
att = Attack()

att.findTechnique('credential dumping') # returns a single technique or a list of techniques with displaytext matching the search string
[T1081: Credentials in Files, T1003: Credential Dumping]

att.findGroup('FIN') # returns a single group or a list of groups that have an alias matching the search string
[G0046: Group: FIN7, G0051: Group: FIN10, G0037: Group: FIN6]

att.findSoftware('mimikatz') # returns a single software item or a list of software that has an alias matching the search string
S0002: Software: Mimikatz

# search takes a list of dicts containing a field and a value and searches for matching techniques
# currently searchable fields are data sources, tactics, and displaytitle
att.search([{'field':'data sources','value':'registry'},{'field':'tactics','value':'execution'}])
[T1086: PowerShell, T1035: Service Execution, T1138: Application Shimming, T1117: Regsvr32, T1072: Third-party Software]
```

## Usage Examples
```python
from MitreAttack import Attack
att = Attack()
att.findTechnique('credential dumping').groups
{u'G0004': G0004: Group: Ke3chang, u'G0045': G0045: Group: menuPass, Stone Panda, ..., u'G0040': G0040: Group: Patchwork, Dropping Elephant, Chinastrats, u'G0041': G0041: Group: Strider, ProjectSauron, u'G0003': G0003: Group: Cleaver, Threat Group 2889, TG-2889, u'G0001': G0001: Group: Axiom, Group 72, u'G0006': G0006: Group: APT1, Comment Crew, ..., u'G0007': G0007: Group: APT28, Sednit, ..., u'G0039': G0039: Group: Suckfly, u'G0038': G0038: Group: Stealth Falcon, u'G0037': G0037: Group: FIN6, u'G0021': G0021: Group: Molerats, Gaza cybergang, Operation Molerats, u'G0022': G0022: Group: APT3, Gothic Panda, ..., u'G0033': G0033: Group: Poseidon Group, u'G0027': G0027: Group: Threat Group-3390, TG-3390, ...}

att.findGroup('APT28').techniques
{u'T1091': T1091: Replication Through Removable Media, u'T1090': T1090: Connection Proxy, u'T1001': T1001: Data Obfuscation, u'T1099': T1099: Timestomp, u'T1057': T1057: Process Discovery, u'T1092': T1092: Communication Through Removable Media, u'T1033': T1033: System Owner/User Discovery, u'T1137': T1137: Office Application Startup, u'T1071': T1071: Standard Application Layer Protocol, u'T1070': T1070: Indicator Removal on Host, u'T1075': T1075: Pass the Hash, u'T1074': T1074: Data Staged, u'T1078': T1078: Valid Accounts, u'T1113': T1113: Screen Capture, u'T1082': T1082: System Information Discovery, u'T1083': T1083: File and Directory Discovery, u'T1081': T1081: Credentials in Files, u'T1085': T1085: Rundll32, u'T1134': T1134: Access Token Manipulation, u'T1056': T1056: Input Capture, u'T1025': T1025: Data from Removable Media, u'T1027': T1027: Obfuscated Files or Information, u'T1107': T1107: File Deletion, u'T1068': T1068: Exploitation of Vulnerability, u'T1120': T1120: Peripheral Device Discovery, u'T1105': T1105: Remote File Copy, u'T1122': T1122: Component Object Model Hijacking, u'T1003': T1003: Credential Dumping, u'T1067': T1067: Bootkit}

att.allTechniques['T1122']
T1122: Component Object Model Hijacking

att.allTechniques['T1122'].technical_description
u"The Microsoft Component Object Model (COM) is a system within Windows to enable interaction between software components through the operating system.Microsoft Component Object Model Adversaries can use this system to insert malicious code that can be executed in place of legitimate software through hijacking the COM references and relationships as a means for persistence. Hijacking a COM object requires a change in the Windows Registry to replace a reference to a legitimate system component which may cause that component to not work when executed. When that system component is executed through normal system operation the adversary's code will be executed instead.GDATA COM Hijacking An adversary is likely to hijack objects that are used frequently enough to maintain a consistent level of persistence, but are unlikely to break noticeable functionality within the system as to avoid system instability that could lead to detection."

att.allTechniques['T1122'].data_sources
[u'Windows Registry', u'DLL monitoring', u'Loaded DLLs']
```
