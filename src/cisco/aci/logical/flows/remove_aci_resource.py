class CiscoACIRemoveResourcesFlow(object):
    def __init__(self, aci_api_client, resource_config, logger):
        """

        :param aci_api_client:
        :param resource_config:
        :param logger:
        """
        self._aci_api_client = aci_api_client
        self._resource_config = resource_config
        self._logger = logger

    def execute_flow(self, app_profiles, bridge_domains):
        """

        :param list[str] app_profiles:
        :return:
        """
        self._logger.info("Remove ACI resources Flow has been started")

        for app_profile in app_profiles:
            self._logger.info("Removing App Profile '{}'...".format(app_profile))
            self._aci_api_client.remove_app_profile(tenant_name="", app_profile_name="")

        for bd_name in bridge_domains:
            self._logger.info("Removing Bridge Domain '{}'...".format(bd_name))
            self._aci_api_client.remove_bridge_domain(tenant_name="", bd_name="")

        self._logger.info("Remove ACI resources Flow has been successfully completed")
