from cloudshell.devices.standards.base import AbstractResource
from cloudshell.devices.standards.validators import attr_length_validator


AVAILABLE_SHELL_TYPES = ["CS_CiscoACIController", "CS_CiscoACITenant", "CS_CiscoACIEndPointGroup"]


class CiscoACIEPGController(AbstractResource):
    RESOURCE_MODEL = "Cisco ACI EPG Controller"
    RELATIVE_PATH_TEMPLATE = ""

    def __init__(self, shell_name, name, unique_id, shell_type="CS_CiscoACIController"):
        super(CiscoACIEPGController, self).__init__(shell_name, name, unique_id)

        if shell_name:
            self.shell_name = "{}.".format(shell_name)
            if shell_type in AVAILABLE_SHELL_TYPES:
                self.shell_type = "{}.".format(shell_type)
            else:
                raise Exception(self.__class__.__name__, "Unavailable shell type {shell_type}."
                                                         "Shell type should be one of: {avail}"
                                .format(shell_type=shell_type, avail=", ".join(AVAILABLE_SHELL_TYPES)))
        else:
            self.shell_name = ""
            self.shell_type = ""


class CiscoACITenant(AbstractResource):
    RESOURCE_MODEL = "Cisco ACI Tenant"
    RELATIVE_PATH_TEMPLATE = "T"

    def __init__(self, shell_name, name, unique_id, shell_type="CS_CiscoACITenant"):
        super(CiscoACITenant, self).__init__(shell_name, name, unique_id)

        if shell_name:
            if shell_type in AVAILABLE_SHELL_TYPES:
                self.shell_type = "{}.".format(shell_type)
            else:
                raise Exception(self.__class__.__name__, "Unavailable shell type {shell_type}."
                                                         "Shell type should be one of: {avail}"
                                .format(shell_type=shell_type, avail=", ".join(AVAILABLE_SHELL_TYPES)))
        else:
            self.shell_name = ""
            self.shell_type = ""

    @property
    def aci_name(self):
        """ Return the name of a contact registered in the device """

        return self.attributes.get("{}ACI Name".format(self.namespace), None)

    @aci_name.setter
    @attr_length_validator
    def aci_name(self, value):
        """ Set the name of a contact registered in the device """
        self.attributes["{}ACI Name".format(self.namespace)] = value


class CiscoACIEndPointGroup(AbstractResource):
    RESOURCE_MODEL = "Cisco ACI EndPointGroup"
    RELATIVE_PATH_TEMPLATE = "EPG"

    def __init__(self, shell_name, name, unique_id, shell_type="CS_CiscoACIEndPointGroup"):
        super(CiscoACIEndPointGroup, self).__init__(shell_name, name, unique_id)

        if shell_name:
            if shell_type in AVAILABLE_SHELL_TYPES:
                self.shell_type = "{}.".format(shell_type)
            else:
                raise Exception(self.__class__.__name__, "Unavailable shell type {shell_type}."
                                                         "Shell type should be one of: {avail}"
                                .format(shell_type=shell_type, avail=", ".join(AVAILABLE_SHELL_TYPES)))
        else:
            self.shell_name = ""
            self.shell_type = ""

    @property
    def aci_name(self):
        """ Return the name of a contact registered in the device """

        return self.attributes.get("{}ACI Name".format(self.namespace), None)

    @aci_name.setter
    @attr_length_validator
    def aci_name(self, value):
        """ Set the name of a contact registered in the device """
        self.attributes["{}ACI Name".format(self.namespace)] = value
