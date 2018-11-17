class CiscoACICreateResourcesFlow(object):
    def __init__(self, aci_api_client, resource_config, resources_data_handler, logger):
        """

        :param aci_api_client:
        :param resource_config:
        :param resources_data_handler
        :param logger:
        """
        self._aci_api_client = aci_api_client
        self._resource_config = resource_config
        self._resources_data_handler = resources_data_handler
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
        self._logger.info("Create ACI resources Flow has been started")

        with self._resources_data_handler as resources_data_handler:
            self._logger.info("Adding Application Profile '{}' to the JSON file".format(app_profile_name))
            resources_data_handler.add_app_profile(tenant_name=tenant_name, app_profile_name=app_profile_name)

            if bd_name is not None:
                self._logger.info("Adding Bridge Domain '{}' to the JSON file".format(bd_name))
                resources_data_handler.add_bridge_domain(tenant_name=tenant_name, bridge_domain_name=bd_name)

        self._logger.info("Creating resources on the ACI")
        self._aci_api_client.create_aci_resources(tenant_name=tenant_name,
                                                  app_profile_name=app_profile_name,
                                                  epg_name=epg_name,
                                                  bd_name=bd_name,
                                                  bd_ip_address=bd_ip_address,
                                                  bd_mask=bd_mask)

        self._logger.info("Create ACI resources Flow has been successfully completed")
