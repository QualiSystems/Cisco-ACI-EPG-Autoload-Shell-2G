from cloudshell.core.context.error_handling_context import ErrorHandlingContext
from cloudshell.devices.driver_helper import get_api
from cloudshell.devices.driver_helper import get_logger_with_thread_id
from cloudshell.shell.core.driver_utils import GlobalLock
from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface

from cloudshell.cisco.aci.controller.api.client import CiscoACIControllerHTTPClient

from cloudshell.cisco.aci.controller.configuration_attributes_structure import CiscoACIControllerResourse
from cisco.aci.logical.runners.aci_resources import CiscoACIResourcesRunner
from cisco.aci.logical.runners.autoload import CiscoACIAutoloadRunner


class CiscoAciEpgAutoloadDriver(ResourceDriverInterface):

    SHELL_TYPE = "CS_CiscoACIController"
    SHELL_NAME = "Cisco ACI EPG Controller"

    def __init__(self):
        """
        ctor must be without arguments, it is created with reflection at run time
        """
        pass

    def initialize(self, context):
        """
        Initialize the driver session, this function is called everytime a new instance of the driver is created
        This is a good place to load and cache the driver configuration, initiate sessions etc.
        :param InitCommandContext context: the context the command runs on
        """
        pass

    def cleanup(self):
        """
        Destroy the driver session, this function is called everytime a driver instance is destroyed
        This is a good place to close any open sessions, finish writing to log files
        """
        pass

    @GlobalLock.lock
    def get_inventory(self, context):
        """Discovers the resource structure and attributes.

        :param AutoLoadCommandContext context: the context the command runs on
        :return Attribute and sub-resource information for the Shell resource you can return an AutoLoadDetails object
        :rtype: AutoLoadDetails
        """
        logger = get_logger_with_thread_id(context)
        logger.info("Autoload command started")

        with ErrorHandlingContext(logger):
            resource_config = CiscoACIControllerResourse.from_context(context=context,
                                                                      shell_type=self.SHELL_TYPE,
                                                                      shell_name=self.SHELL_NAME)

            cs_api = get_api(context)
            password = cs_api.DecryptPassword(resource_config.password).Value

            aci_api_client = CiscoACIControllerHTTPClient(logger=logger,
                                                          address=resource_config.address,
                                                          user=resource_config.user,
                                                          password=password,
                                                          scheme=resource_config.scheme,
                                                          port=resource_config.port)

            autoload_runner = CiscoACIAutoloadRunner(aci_api_client=aci_api_client,
                                                     logger=logger,
                                                     resource_config=resource_config)

            autoload_details = autoload_runner.discover()
            logger.info("Autoload command completed")

            return autoload_details

    @GlobalLock.lock
    def create_aci_resources(self, context, tenant_name, app_profile_name, epg_name, bd_name, bd_ip_address, bd_mask):
        """

        :param context:
        :param tenant_name:
        :param app_profile_name:
        :param epg_name:
        :param bd_name:
        :param bd_ip_address:
        :param bd_mask:
        :return:
        """

        logger = get_logger_with_thread_id(context)
        logger.info("Create ACI Resources command started")

        with ErrorHandlingContext(logger):
            resource_config = CiscoACIControllerResourse.from_context(context=context,
                                                                      shell_type=self.SHELL_TYPE,
                                                                      shell_name=self.SHELL_NAME)
            cs_api = get_api(context)
            password = cs_api.DecryptPassword(resource_config.password).Value

            aci_api_client = CiscoACIControllerHTTPClient(logger=logger,
                                                          address=resource_config.address,
                                                          user=resource_config.user,
                                                          password=password,
                                                          scheme=resource_config.scheme,
                                                          port=resource_config.port)

            aci_resources_runner = CiscoACIResourcesRunner(aci_api_client=aci_api_client,
                                                           logger=logger,
                                                           resource_config=resource_config)

            aci_resources_runner.create_resources(tenant_name=tenant_name,
                                                  app_profile_name=app_profile_name,
                                                  epg_name=epg_name,
                                                  bd_name=bd_name,
                                                  bd_ip_address=bd_ip_address,
                                                  bd_mask=bd_mask)

            logger.info("Create ACI Resources command completed")
            logger.info("Executing Autoload to add new resources")
            cs_api.AutoLoad(resource_config.fullname)
            logger.info("Autoload for new resources completed")

    @GlobalLock.lock
    def remove_aci_resources(self, context):
        """

        :param context:
        :return:
        """
        logger = get_logger_with_thread_id(context)
        logger.info("Create ACI Resources command started")

        with ErrorHandlingContext(logger):
            resource_config = CiscoACIControllerResourse.from_context(context=context,
                                                                      shell_type=self.SHELL_TYPE,
                                                                      shell_name=self.SHELL_NAME)
            cs_api = get_api(context)
            password = cs_api.DecryptPassword(resource_config.password).Value

            aci_api_client = CiscoACIControllerHTTPClient(logger=logger,
                                                          address=resource_config.address,
                                                          user=resource_config.user,
                                                          password=password,
                                                          scheme=resource_config.scheme,
                                                          port=resource_config.port)

            aci_resources_runner = CiscoACIResourcesRunner(aci_api_client=aci_api_client,
                                                           logger=logger,
                                                           resource_config=resource_config)

            aci_resources_runner.remove_resources()


if __name__ == "__main__":
    import mock
    from cloudshell.shell.core.driver_context import ResourceCommandContext, ResourceContextDetails, ReservationContextDetails

    # TEST ENV
    address = "sandboxapicdc.cisco.com"
    user = "admin"
    password = "ciscopsdt"
    port = 443
    scheme = "https"

    # PROD ENV
    # address = "192.168.85.28"
    # user = "aci-dev-cali"
    # password = "Cisco.123!"
    # port = 8888
    # scheme = "https"

    auth_key = 'h8WRxvHoWkmH8rLQz+Z/pg=='
    api_port = 8029

    context = ResourceCommandContext(*(None, ) * 4)
    context.resource = ResourceContextDetails(*(None, ) * 13)
    context.resource.name = 'Cisco ACI EPG Structure'
    context.resource.fullname = 'Cisco ACI EPG Structure'
    context.reservation = ReservationContextDetails(*(None, ) * 7)
    context.reservation.reservation_id = '0cc17f8c-75ba-495f-aeb5-df5f0f9a0e97'
    context.resource.attributes = {}
    context.resource.attributes['{}.Scheme'.format(CiscoAciEpgAutoloadDriver.SHELL_NAME)] = "HTTPS"
    context.resource.attributes['{}.Controller TCP Port'.format(CiscoAciEpgAutoloadDriver.SHELL_NAME)] = port
    context.resource.attributes['{}.User'.format(CiscoAciEpgAutoloadDriver.SHELL_NAME)] = user
    context.resource.attributes['{}.Password'.format(CiscoAciEpgAutoloadDriver.SHELL_NAME)] = password
    context.resource.address = address

    context.connectivity = mock.MagicMock()
    context.connectivity.server_address = "192.168.85.28"

    dr = CiscoAciEpgAutoloadDriver()
    dr.initialize(context)

    with mock.patch('__main__.get_api') as get_api:
        get_api.return_value = type('api', (object,), {
            'DecryptPassword': lambda self, pw: type('Password', (object,), {'Value': pw})(),
            'AutoLoad': lambda self, pw: type('Password', (object,), {'Value': pw})()
        })()

        # result = dr.create_aci_resources(context=context,
        #                                  tenant_name="Heroes",
        #                                  app_profile_name="App_Profile_222",
        #                                  epg_name="epg_2",
        #                                  bd_name="bd_22222",
        #                                  bd_ip_address="40.40.10.10",
        #                                  bd_mask="24")
        #
        result = dr.remove_aci_resources(context=context)

        print result
