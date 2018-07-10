from cloudshell.devices.autoload.autoload_builder import AutoloadDetailsBuilder

from cisco.aci.logical.autoload import models


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

        tenants_structure = self._aci_api_client.get_tenants_structure()
        tenant_name_gen = UniqueNameGenerator()

        for tenant in tenants_structure:
            unique_tenant_name = tenant_name_gen.get_unique_name(tenant["name"])
            tenant_resource = models.CiscoACITenant(shell_name=self._resource_config.shell_name,
                                                    name=unique_tenant_name,
                                                    unique_id="{}.{}".format(self._resource_config.fullname,
                                                                             unique_tenant_name))
            tenant_resource.aci_name = tenant["name"]
            root_resource.add_sub_resource(hash(unique_tenant_name), tenant_resource)

            app_profile_name_gen = UniqueNameGenerator()

            for app_profile in tenant["app_profiles"]:
                unique_app_profile_name = app_profile_name_gen.get_unique_name(app_profile["name"])
                app_profile_resource = models.CiscoACIAppProfile(shell_name=self._resource_config.shell_name,
                                                                 name=unique_app_profile_name,
                                                                 unique_id="{}.{}.{}"
                                                                 .format(self._resource_config.fullname,
                                                                         unique_tenant_name,
                                                                         unique_app_profile_name))
                app_profile_resource.aci_name = app_profile["name"]
                tenant_resource.add_sub_resource(hash(unique_app_profile_name), app_profile_resource)

                epg_name_gen = UniqueNameGenerator()

                for epg in app_profile["epgs"]:
                    unique_epg_name = epg_name_gen.get_unique_name(epg["name"])
                    epg_resource = models.CiscoACIEndPointGroup(shell_name=self._resource_config.shell_name,
                                                                name=unique_epg_name,
                                                                unique_id="{}.{}.{}.{}".format(
                                                                    self._resource_config.fullname,
                                                                    unique_tenant_name,
                                                                    unique_app_profile_name,
                                                                    unique_epg_name))

                    epg_resource.aci_name = epg["name"]
                    app_profile_resource.add_sub_resource(hash(unique_epg_name), epg_resource)

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

