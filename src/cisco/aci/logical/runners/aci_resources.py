from cisco.aci.logical.flows.create_aci_resource import CiscoACICreateResourcesFlow
from cisco.aci.logical.flows.remove_aci_resource import CiscoACIRemoveResourcesFlow
from cisco.aci.logical.resources_data.data_handler import ResourcesDataHandler


class CiscoACIResourcesRunner(object):
    def __init__(self, resource_config, aci_api_client, reservation_id, logger):
        """

        :param resource_config:
        :param aci_api_client:
        :param reservation_id:
        :param logger:
        """
        self._resource_config = resource_config
        self._aci_api_client = aci_api_client
        self._resources_data_handler = ResourcesDataHandler(reservation_id=reservation_id)
        self._logger = logger

    @property
    def create_resources_flow(self):
        return CiscoACICreateResourcesFlow(aci_api_client=self._aci_api_client,
                                           resource_config=self._resource_config,
                                           resources_data_handler=self._resources_data_handler,
                                           logger=self._logger)

    @property
    def remove_resources_flow(self):
        return CiscoACIRemoveResourcesFlow(aci_api_client=self._aci_api_client,
                                           resource_config=self._resource_config,
                                           resources_data_handler=self._resources_data_handler,
                                           logger=self._logger)

    def create_resources(self, tenant_name, app_profile_name, epg_name, bd_name, bd_ip_address=None, bd_mask=None):
        """

        :param tenant_name:
        :param app_profile_name:
        :param epg_name:
        :param bd_name:
        :param bd_ip_address:
        :param bd_mask:
        :return:
        """
        return self.create_resources_flow.execute_flow(tenant_name=tenant_name,
                                                       app_profile_name=app_profile_name,
                                                       epg_name=epg_name,
                                                       bd_name=bd_name,
                                                       bd_ip_address=bd_ip_address,
                                                       bd_mask=bd_mask)

    def remove_resources(self):
        """

        :return: AutoLoadDetails object
        """
        return self.remove_resources_flow.execute_flow()
