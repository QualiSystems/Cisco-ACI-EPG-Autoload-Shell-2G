class CiscoACIRemoveResourcesFlow(object):
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

    def execute_flow(self):
        """

        :return:
        """
        self._logger.info("Remove ACI resources Flow has been started")

        with self._resources_data_handler as resources_data_handler:
            for tenant_name, app_profile in resources_data_handler.app_profiles_by_tenants:
                self._logger.info("Removing App Profile '{}'...".format(app_profile))
                try:
                    self._aci_api_client.remove_app_profile(tenant_name=tenant_name, app_profile_name=app_profile)
                except Exception:  # todo: catch specific API Client exception
                    self._logger.warning("Unable to remove Application Profile '{}' due to exception:"
                                         .format(app_profile), exc_info=True)

            for tenant_name, bd_name in resources_data_handler.bridge_domains_by_tenants:
                self._logger.info("Removing Bridge Domain '{}'...".format(bd_name))
                try:
                    self._aci_api_client.remove_bridge_domain(tenant_name=tenant_name, bd_name=bd_name)
                except Exception:  # todo: catch specific API Client exception
                    self._logger.warning("Unable to remove Bridge Domain '{}' due to exception:"
                                         .format(bd_name), exc_info=True)

        self._logger.info("Removing JSON data file...")
        self._resources_data_handler.remove_data_file()

        self._logger.info("Remove ACI resources Flow has been successfully completed")
