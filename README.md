![](https://github.com/QualiSystems/cloudshell-shells-documentaion-templates/blob/master/cloudshell_logo.png)

# **Cisco ACI EPG Autoload 2G Shell**

Release date: January 2019

Shell version: 1.0.0

Document version: 1.0

# In This Guide

* [Overview](#overview)
* [Downloading the Shell](#downloading-the-shell)
* [Importing and Configuring the Shell](#importing-and-configuring-the-shell)
* [Updating Python Dependencies for Shells](#updating-python-dependencies-for-shells)
* [Typical Workflows](#typical-workflows)
* [References](#references)
* [Release Notes](#release-notes)


# Overview
A shell integrates a device model, application or other technology with CloudShell. A shell consists of a data model that defines how the device and its properties are modeled in CloudShell, along with automation that enables interaction with the device via CloudShell.

### Networking Shells
CloudShell's networking shells provide L2 or L3 connectivity between resources.

### **Cisco ACI EPG Autoload 2G Shell**
The **Cisco ACI EPG Autoload 2G** shell provides you with connectivity and management capabilities such as device structure discovery for the **Cisco ACI**. 

For more information on the **Cisco ACI**, see the official **Cisco** product documentation.

### Standard version
The **Cisco ACI EPG Autoload 2G** shell is based on the Cloudshell Cisco ACI Standard version **1.0.0**.

### Requirements

Release: **Cisco ACI EPG Autoload 2G Shell**

▪ CloudShell version: 8.3 Patch 3, 9.0 Patch 2, 9.1 GA and above

▪ Cisco ACI version: 3.0 and above

**Note:** If your CloudShell version does not support this shell, you should consider upgrading to a later version of CloudShell or contact customer support.

### Data Model

The shell's data model includes all shell metadata, families, and attributes.

#### **Cisco ACI EPG Autoload 2G Shell Families and Models**

The Cisco ACI EPG families and models are listed in the following table:

|Family|Model|Description|
|:---|:---|:---|
|CS_CiscoACIController|Cisco ACI EPG Controller|Generic Cisco ACI EPG Controller 2 Generation |
|CS_CiscoACITenant|CiscoACITenant|Tenants created on the Controller|
|CS_CiscoACIAppProfile|CiscoACIAppProfile|Application Profiles created in the Tenants|
|CS_CiscoACIEndPointGroup|CiscoACIEndPointGroup|EndPoint Groups created in the Application Profiles |

#### **Cisco ACI EPG Autoload 2G Shell Attributes**

#### Cisco ACI EPG Controller

|Attribute Name|Data Type|User input?|Description|Family Attribute?|
|:---|:---|:---|:---|:---|
|User|String|Yes||No|
|Password|Password|Yes||No|
|Model Name|String|No|The Controller model/vendor in a readable format (used by the GUI for display). This information is typically used for abstract resource filtering.|Yes|
|Controller TCP Port|Integer|Yes|Default is 443.|No|
|Scheme|String|Yes|Options include: HTTP, HTTPS|No|

#### Cisco ACI Tenant

|Attribute Name|Data Type|User input?|Description|Family Attribute?|
|:---|:---|:---|:---|:---|
|ACI Name|String|Yes|Tenant name on the ACI Controller|No|


#### Cisco ACI App Profile
|Attribute Name |Data Type |User input?|Description|Family Attribute?|
|:---|:---|:---|:---|:---|
|ACI Name|String|Yes|Application Profile name on the ACI Controller|No|

#### Cisco ACI EndPoint Group

|Attribute Name|Data Type|User input?|Description|Family Attribute?|
|:---|:---|:---|:---|:---|
|ACI Name|String|Yes|EndPoint Group name on the ACI Controller|No|

### Automation
This section describes the automation (drivers) associated with the data model. The shell’s driver is provided as part of the shell package. There are two types of automation processes, Autoload and Resource.  Autoload is executed when creating the resource in the **Inventory** dashboard, while resource commands are run in the sandbox.

The following resource commands are available on the **Cisco ACI EPG Autoload 2G** shell:

* Create ACI Resources
* Remove ACI Resources

# Downloading the Shell
The **Cisco ACI EPG Autoload 2G** shell is available from the [Quali Community Integrations](https://community.quali.com/integrations) page. 

Download the files into a temporary location on your local machine. 

The shell comprises:

|File name|Description|
|:---|:---|
|CiscoAciEpgAutoload.zip|Cisco ACI EPG Autoload shell package|
|cisco-aci-epg-autoload-offline-dependecies-1.0.0.zip|Shell Python dependencies (for offline deployments only)|

# Importing and Configuring the Shell
This section describes how to import the **Cisco ACI EPG Autoload 2G** shell and configure and modify the shell’s devices.

### Importing the shell into CloudShell

**To import the shell into CloudShell:**
  1. Make sure you have the shell’s zip package. If not, download the shell from the [Quali Community's Integrations](https://community.quali.com/integrations) page.
  
  2. In CloudShell Portal, as Global administrator, open the **Manage – Shells** page.
  
  3. Click **Import**.
  
  4. In the dialog box, navigate to the shell's zip package, select it and click **Open**.

The shell is displayed in the **Shells** page and can be used by domain administrators in all CloudShell domains to create new inventory resources, as explained in [Adding Inventory Resources](http://help.quali.com/Online%20Help/9.0/Portal/Content/CSP/INVN/Add-Rsrc-Tmplt.htm?Highlight=adding%20inventory%20resources). 

### Offline installation of a shell

**Note:** Offline installation instructions are relevant only if CloudShell Execution Server has no access to PyPi. You can skip this section if your execution server has access to PyPi. For additional information, see the online help topic on offline dependencies.

In offline mode, import the shell into CloudShell and place any dependencies in the appropriate dependencies folder. The dependencies folder may differ, depending on the CloudShell version you are using:

* For CloudShell version 8.3 and above, see [Adding Shell and script packages to the local PyPi Server repository](#adding-shell-and-script-packages-to-the-local-pypi-server-repository).

* For CloudShell version 8.2, perform the appropriate procedure: [Adding Shell and script packages to the local PyPi Server repository](#adding-shell-and-script-packages-to-the-local-pypi-server-repository) or [Setting the python pythonOfflineRepositoryPath configuration key](#setting-the-python-pythonofflinerepositorypath-configuration-key).

* For CloudShell versions prior to 8.2, see [Setting the python pythonOfflineRepositoryPath configuration key](#setting-the-python-pythonofflinerepositorypath-configuration-key).

### Adding shell and script packages to the local PyPi Server repository
If your Quali Server and/or execution servers work offline, you will need to copy all required Python packages, including the out-of-the-box ones, to the PyPi Server's repository on the Quali Server computer (by default *C:\Program Files (x86)\QualiSystems\CloudShell\Server\Config\Pypi Server Repository*).

For more information, see [Configuring CloudShell to Execute Python Commands in Offline Mode](http://help.quali.com/Online%20Help/9.0/Portal/Content/Admn/Cnfgr-Pyth-Env-Wrk-Offln.htm?Highlight=Configuring%20CloudShell%20to%20Execute%20Python%20Commands%20in%20Offline%20Mode).

**To add Python packages to the local PyPi Server repository:**
  1. If you haven't created and configured the local PyPi Server repository to work with the execution server, perform the steps in [Add Python packages to the local PyPi Server repository (offline mode)](http://help.quali.com/Online%20Help/9.0/Portal/Content/Admn/Cnfgr-Pyth-Env-Wrk-Offln.htm?Highlight=offline%20dependencies#Add). 
  
  2. For each shell or script you add into CloudShell, do one of the following (from an online computer):
      * Connect to the Internet and download each dependency specified in the *requirements.txt* file with the following command: 
`pip download -r requirements.txt`. 
     The shell or script's requirements are downloaded as zip files.

      * In the [Quali Community's Integrations](https://community.quali.com/integrations) page, locate the shell and click the shell's **Download** link. In the page that is displayed, from the Downloads area, extract the dependencies package zip file.

3. Place these zip files in the local PyPi Server repository.
 
### Setting the python PythonOfflineRepositoryPath configuration key
Before PyPi Server was introduced as CloudShell’s python package management mechanism, the `PythonOfflineRepositoryPath` key was used to set the default offline package repository on the Quali Server machine, and could be used on specific Execution Server machines to set a different folder. 

**To set the offline python repository:**
1. Download the *cisco-aci-epg-autoload-offline-dependecies.zip* file, see [Downloading the Shell](#downloading-the-shell).

2. Unzip it to a local repository. Make sure the execution server has access to this folder. 

3.  On the Quali Server machine, in the *~\CloudShell\Server\customer.config* file, add the following key to specify the path to the default python package folder (for all Execution Servers):  
	`<add key="PythonOfflineRepositoryPath" value="repository 
full path"/>`

4. If you want to override the default folder for a specific Execution Server, on the Execution Server machine, in the *~TestShell\Execution Server\customer.config* file, add the following key:  
	`<add key="PythonOfflineRepositoryPath" value="repository 
full path"/>`

5. Restart the Execution Server.

### Configuring a new resource
This section explains how to create a new resource from the shell.

In CloudShell, the component that models the device is called a resource. It is based on the shell that models the device and allows the CloudShell user and API to remotely control the device from CloudShell.

You can also modify existing resources, see [Managing Resources in the Inventory](http://help.quali.com/Online%20Help/9.0/Portal/Content/CSP/INVN/Mng-Rsrc-in-Invnt.htm?Highlight=managing%20resources).

**To create a resource for the device:**
  1. In the CloudShell Portal, in the **Inventory** dashboard, click **Add New**. 
     ![](https://github.com/QualiSystems/cloudshell-shells-documentaion-templates/blob/master/create_a_resource_device.png)
     
  2. From the list, select **Cisco ACI EPG Autoload 2G**.
  
  3. Enter the **Name** and **IP address** of the **Cisco ACI Controller**.
  
  4. Click **Create**.
  
  5. In the **Resource** dialog box, enter the device's settings, see [Cisco ACI EPG Autoload 2G Shell Attributes](#cisco-aci-epg-autoload-2g-shell-attributes).
  
  6. Click **Continue**.

CloudShell validates the device’s settings and updates the new resource with the device’s structure.

# Updating Python Dependencies for Shells
This section explains how to update your Python dependencies folder. This is required when you upgrade a shell that uses new/updated dependencies. It applies to both online and offline dependencies.

### Updating offline Python dependencies
**To update offline Python dependencies:**
1. Download the latest Python dependencies package zip file locally.

2. Extract the zip file to the suitable offline package folder(s). 

3. Terminate the shell’s instance, as explained [here](http://help.quali.com/Online%20Help/9.0/Portal/Content/CSP/MNG/Mng-Exctn-Srv-Exct.htm#Terminat). 

### Updating online Python dependencies
In online mode, the execution server automatically downloads and extracts the appropriate dependencies file to the online Python dependencies repository every time a new instance of the driver or script is created.

**To update online Python dependencies:**
* If there is a live instance of the shell's driver or script, terminate the shell’s instance, as explained [here](http://help.quali.com/Online%20Help/9.0/Portal/Content/CSP/MNG/Mng-Exctn-Srv-Exct.htm#Terminat). If an instance does not exist, the execution server will download the Python dependencies the next time a command of the driver or script runs.

# Typical Workflows 

#### **Workflow 1** - *Create ACI Resources* 
1. In CloudShell Portal, add the **Cisco ACI EPG Autoload** resource to your blueprint and reserve the blueprint.

2. Hover over the resource, select the **Commands** option from the context menu and run the **Create ACI Resources** command.

3. In the command inputs field, enter the following information:
	* **Tenant Name**: Name of the Tenant where the ACI resources will be created.
	* **Application Profile Name**: Name of the Application Profile to be created on the Cisco ACI Controller.
	* **EndPoint Group Name**: Name of the EndPoint Group to be created on the Cisco ACI Controller.
	* **Bridge Domain Name**: Name of the Bridge Domain to be created on the Cisco ACI Controller.
	* **Bridge Domain IP Address**: IP Address to be added to the Bridge Domain.
	* **Bridge Domain Mask**: Subnet Mask to be added to the Bridge Domain.
	
4. Click **Run**.

#### **Workflow 2** - *Remove ACI Resources* 
1. In CloudShell Portal, add the **Cisco ACI EPG Autoload** resource to your blueprint and reserve the blueprint.

2. Hover over the resource, select the **Commands** option from the context menu and run the **Remove ACI Resources** command.

This removes all ACI resources created earlier in the current reservation.

#### **Workflow 3** - *Add Cisco ACI Port to the EndPointGroup*
1. Create a physical connection between the Cisco ACI Port and some DUT/Switch.
    1. In Resource Manager, **Resource Explorer** pane, open the **Cisco ACI Ports Autoload** resource.
    1. Right-click the resource, select **Configuration** from the context menu and click on the **Connections** button at the bottom of the **Resource Configuration** page.
    2. Connect the Cisco ACI Port to some DUT/Switch:
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![](https://github.com/QualiSystems/Cisco-ACI-EPG-Autoload-Shell-2G/blob/master/docs/images/cisco_aci_port_to_dut_phys_connection.png)
    3. Save your changes

2. In CloudShell Portal, add the **Cisco ACI EPG Autoload** resource and the DUT/Switch resource (where you connected the Cisco ACI Ports) to your blueprint.

3. In the diagram view of the blueprint toolbar, click **App/Service>Networking** and drag the **VLAN AUTO** service into the diagram.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![](https://github.com/QualiSystems/Cisco-ACI-EPG-Autoload-Shell-2G/blob/master/docs/images/reservation_with_cisco_aci_epg_dut_and_vlan_service.jpeg)

4. Create a connection between the DUT/Switch port (which you connected earlier to the Cisco ACI Port) and the **Cisco ACI EPG Autoload** resource. Select the EndPoint Group you want to associate with the Cisco ACI Port.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![](https://github.com/QualiSystems/Cisco-ACI-EPG-Autoload-Shell-2G/blob/master/docs/images/cisco_aci_epg_dut_connector.jpeg)

5. Create a connection between the DUT/Switch port and the VLAN Auto Service.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![](https://github.com/QualiSystems/Cisco-ACI-EPG-Autoload-Shell-2G/blob/master/docs/images/cisco_aci_epg_vlan_service_connector.jpeg)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;![](https://github.com/QualiSystems/Cisco-ACI-EPG-Autoload-Shell-2G/blob/master/docs/images/reservation_with_cisco_aci_epg_dut_and_vlan_service_with_connectors.jpeg)

4. Reserve the blueprint.


# References
To download and share integrations, see [Quali Community's Integrations](https://community.quali.com/integrations). 

For instructional training and documentation, see [Quali University](https://www.quali.com/university/).

To suggest an idea for the product, see [Quali's Idea box](https://community.quali.com/ideabox). 

To connect with Quali users and experts from around the world, ask questions and discuss issues, see [Quali's Community forums](https://community.quali.com/forums). 

# Release Notes 

For release updates, see the shell's [GitHub releases page](https://github.com/QualiSystems/Cisco-ACI-EPG-Autoload-Shell-2G/releases).

