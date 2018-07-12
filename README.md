# Cisco ACI EPG Autoload Shell 2-nd Generation
<p align="center">
<img src="https://github.com/QualiSystems/devguide_source/raw/master/logo.png"></img>
</p>

## Overview
The Cisco ACI EPG Autoload shell provides CloudShell Resource Manager with the capability to communicate with switches that are part of the CloudShell inventory.

End users will be able to create routes, configure port settings, and read values from the switch using the CloudShell Portal, Resource Manager client, or the CloudShell API.

### The Cisco ACI EPG Autoload Shell includes:

|File name|Description|
|---|---|
|`APCON_CLI4.exe`|Driver used by CloudShell Server|
|`APCON_CLI4_RuntimeConfig.yml`|YML file enabling additional configuration interface for the driver|
|`APCON_CLI4_ResourceConfiguration.xml`|An XML file holding all attribute and capabilities of the L1 switches of the same vendor|

### Requirements
The driver is compatible with the following CloudShell versions:
- 7.0 and above

### Supported Devices/Firmwares
The driver has been verified with the following devices and software versions:
- ACI-3036-XR-AC - 5.1.3

### Installation

Follow the instructions in the link below for installation:
http://help.quali.com/Online%20Help/7.0.0.0/Portal/Content/Admn/Cnct-Ctrl-L1-Swch.htm

In step 7 at the above guide, you will need to copy only one exe file, and instead of the runtimeConfig.xml file please copy the `APCON_CLI4_RuntimeConfig.yml` file.

### Supported Functionality

| Feature | Description |
| ------ | ------ |
| `AutoLoad` | Creates the sub-resources of the L1 switch |
| `MapBidi` | Creates a bi-directional connection between two ports |
| `MapUni` | Creates a uni-directional connection between two ports |
| `MapClear` | Clears any connection ending in this port |
| `MapClearTo` | Clears a uni-directional connection between two ports |

### Configuration

| Feature | Description |
| ------ | ------ |
| CLI.TYPE | Session type list i.e. [SSH, TELNET] |
| CLI.PORT | Session Port used to establish connection, i.e. SSH: 22 |
| LOGGING.LEVEL | Logging level, by default - INFO. To get more info change to DEBUG |

### Known Issues
-

