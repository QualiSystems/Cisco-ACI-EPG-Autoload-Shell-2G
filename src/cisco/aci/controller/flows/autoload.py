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

        tenant_name_gen = UniqueNameGenerator()

        for tenant_idx, (tenant, epgs) in enumerate(epgs_by_tenant.iteritems(), start=1):
            tenant_name = tenant_name_gen.get_unique_name(tenant)
            tenant_resource = models.CiscoACITenant(shell_name=self._resource_config.shell_name,
                                                    name=tenant_name,
                                                    unique_id="{}.{}".format(self._resource_config.fullname,
                                                                             tenant_name))
            tenant_resource.aci_name = tenant
            root_resource.add_sub_resource(tenant_idx, tenant_resource)

            epg_name_gen = UniqueNameGenerator()

            for epg_idx, epg in enumerate(epgs, start=1):
                epg_name = epg_name_gen.get_unique_name(epg["name"])
                epg_resource = models.CiscoACIEndPointGroup(shell_name=self._resource_config.shell_name,
                                                            name=epg_name,
                                                            unique_id="{}.{}.{}".format(
                                                                self._resource_config.fullname,
                                                                tenant_name,
                                                                epg_name))

                epg_resource.aci_name = epg["name"]
                tenant_resource.add_sub_resource(epg_idx, epg_resource)

        return AutoloadDetailsBuilder(root_resource).autoload_details()


class UniqueNameGenerator(object):
    def __init__(self):
        """"""
        self._used_names = []

    def get_unique_name(self, name):
        """

        :param str name:
        :return:
        """
        name = name.lower()

        while name in self._used_names:
            name = "{}-1".format(name)

        self._used_names.append(name)
        return name

