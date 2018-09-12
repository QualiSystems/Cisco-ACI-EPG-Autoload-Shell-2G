# Cisco ACI EPG Autoload Shell 2-nd Generation
<p align="center">
<img src="https://github.com/QualiSystems/devguide_source/raw/master/logo.png"></img>
</p>

## Overview
Shell implements integration of a device model, application or other technology with CloudShell. A shell consists of a data-model that defines how the device and its properties are modeled in CloudShell along with an automation that enables interaction with the device via CloudShell

### About Cisco ACI EPG Autoload Shell
Cisco ACI EPG Autoload Shell 2G provides data model and autoload
functionality

### Standard version
Cisco ACI EPG Autoload Shell 2G is based on the Cloudshell Cisco ACI Standard 1.0.0

### Supported ACI versions
▪ 3.0

### Requirements
▪ CloudShell version 8.2 and above
▪ Cisco ACI version 3.0

### Downloading the Shell
Cisco ACI EPG Autoload Shell 2G is available on the [Quali Download Center](https://support.quali.com/entries/87063688-Solution-Pack-Download-Center).
Download the files into a temporary location on your local machine.
___
**Note:** Registration to the Quali Support Portal is required. If you have not registered,
click this link to register [New registration](http://portal.qualisystems.com/entries/43187197)
___

### Shell comprises:
|File name|Description|
|---|---|
|`Cisco ACI EPG Autoload Shell 2G.zip`|`Cisco ACI EPG Autoload Shell 2nd Generation`|
|`cisco-aci-epg-autoload-offline-dependecies.zip`|`Shell Python dependecies (for offline installation only)`|

### Automation
This section describes the automation (drivers or scripts) associated with the data model. The automation code (either script or driver) is associated with the model and provided as part of the Shell package (in the .zip file). The following commands are associated with a model inside the Shell:

|Command |Description|
|---|---|
|`Autoload`|`Discovers ACI Structure. Add Tenants, Application Profiles and EndPoint Groups to the resource model`|
|`Create ACI Resources`|`Creates ACI Application Profile and Endpoint Group under specific Tenant. Add them to the discovered resource model`|

## Import and Configure Shell
This section describes how to import, configure and modify Cisco ACI EPG Autoload Shell 2G

### Importing the Shell into CloudShell
Use the following procedure to import the downloaded Shell:

**To import the Shell into CloudShell:**
  1. Download the Shell from the Quali Download Center.
  2. Backup your database.
  3. Log in to CloudShell Portal as administrator of the relevant domain.
  4. In the User menu select Import Package
  5. Browse to the location of the downloaded Shell file, select the relevant .zip file and Click Open. Alternatively, drag   the shell’s .zip file into CloudShell Portal.

### Offline installation of a Shell
___
**Note:** Offline installation instructions are relevant only if Cloudshell Execution Server has no access to PyPi. You can skip this section if your execution server has access to Pypi.
___
Cisco ACI EPG Autoload Shell 2G uses a variety of Python packages. To work in offline mode:
  1. Download the cisco-aci-epg-autoload-offline-dependecies.zip file (see "Downloading the Shell" section).
  2. Unzip it into the "C:\Program Files (x86)\QualiSystems\CloudShell\Server\Config\Pypi Server Repository" folder
  3. Restart Execution Server.

### Data Model
Cisco ACI EPG Autoload Shell 2G Families and Models

|Family |Model|
|---|---|
|`CS_CiscoACIController`|`Cisco ACI EPG Controller`|
|`CS_CiscoACITenant`|`Cisco ACI EPG Controller.CiscoACITenant`|
|`CS_CiscoACIAppProfile`|`Cisco ACI EPG Controller.CiscoACIAppProfile`|
|`CS_CiscoACIEndPointGroup`|`Cisco ACI EPG Controller.CiscoACIEndPointGroup`|
