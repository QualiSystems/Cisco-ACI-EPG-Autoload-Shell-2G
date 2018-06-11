from cloudshell.devices.autoload.autoload_builder import AutoloadDetailsBuilder

from cisco.aci.controller.autoload import models


class CiscoACIAutoloadFlow(object):
    def __init__(self, aci_api_client, resource_config, logger):
        """

        :param aci_api_client:
        :param resource_config:
        :param logger:
        """
        self._aci_api_client = aci_api_client
        self._resource_config = resource_config
        self._logger = logger

    def execute_flow(self):
        """

        :return:
        """
        root_resource = models.CiscoACIEPGController(shell_name=self._resource_config.shell_name,
                                                     name="Cisco ACI EPG Controller",
                                                     unique_id=self._resource_config.fullname)

        epgs_by_tenant = self._aci_api_client.get_epgs()

        for tenant_idx, (tenant, epgs) in enumerate(epgs_by_tenant.iteritems(), start=1):
            tenant_resource = models.CiscoACITenant(shell_name=self._resource_config.shell_name,
                                                    name="{} {}".format(tenant, tenant_idx),
                                                    unique_id="{}.{}.{}".format(self._resource_config.fullname,
                                                                                tenant, tenant_idx))

            root_resource.add_sub_resource(tenant_idx, tenant_resource)

            for epg_idx, epg in enumerate(epgs, start=1):
                epg_resource = models.CiscoACIEndPointGroup(shell_name=self._resource_config.shell_name,
                                                            name="{} {}".format(epg["name"], epg_idx),
                                                            unique_id="{}.{}.{}.{}.{}".format(
                                                                self._resource_config.fullname,
                                                                tenant, tenant_idx, epg["name"], epg_idx))
                tenant_resource.add_sub_resource(epg_idx, epg_resource)

        return AutoloadDetailsBuilder(root_resource).autoload_details()
