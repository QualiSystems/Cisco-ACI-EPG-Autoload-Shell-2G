class CiscoACICreateResourcesFlow(object):
    def __init__(self, aci_api_client, resource_config, logger):
        """

        :param aci_api_client:
        :param resource_config:
        :param logger:
        """
        self._aci_api_client = aci_api_client
        self._resource_config = resource_config
        self._logger = logger

    def execute_flow(self, tenant_name, app_profile_name, epg_name, bd_name, bd_ip_address=None, bd_mask=None):
        """

        :param tenant_name:
        :param app_profile_name:
        :param epg_name:
        :param bd_name:
        :param bd_ip_address:
        :param bd_mask:
        :return:
        """
        self._aci_api_client.create_aci_resources(tenant_name=tenant_name,
                                                  app_profile_name=app_profile_name,
                                                  epg_name=epg_name,
                                                  bd_name=bd_name,
                                                  bd_ip_address=bd_ip_address,
                                                  bd_mask=bd_mask)
