import json
import os

from cisco.aci.logical.flows.create_aci_resource import CiscoACICreateResourcesFlow
from cisco.aci.logical.flows.remove_aci_resource import CiscoACIRemoveResourcesFlow


class CiscoACIResourcesRunner(object):
    CREATED_ACI_RESOURCE_FILE_NAME = "created_aci_resources.json"

    def __init__(self, resource_config, aci_api_client, logger):
        """

        :param resource_config:
        :param aci_api_client:
        :param logger:
        """
        self._resource_config = resource_config
        self._aci_api_client = aci_api_client
        self._logger = logger

    @property
    def create_resources_flow(self):
        return CiscoACICreateResourcesFlow(aci_api_client=self._aci_api_client,
                                           resource_config=self._resource_config,
                                           logger=self._logger)

    @property
    def remove_resources_flow(self):
        return CiscoACIRemoveResourcesFlow(aci_api_client=self._aci_api_client,
                                           resource_config=self._resource_config,
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
        curr_dir = os.path.dirname(os.path.abspath(__file__))  # ~path_to_env/cisco/aci/logical/runners
        file_path = os.path.join(curr_dir, self.CREATED_ACI_RESOURCE_FILE_NAME)

        # file_data = {
        #     "tenants": [
        #         {
        #             "Heroes": {
        #                 "app_profiles": ["App Profile 1"],
        #                 "bridge_domains": ["BD 1"]
        #             }
        #         }
        #     ]
        # }

        # todo: create specific file for each reservation ???

        if os.path.exists(file_path):
            with open(file_path, "r") as json_file:
                file_data = json.load(json_file)
        else:
            file_data = {}

        # we need to add only App Profiles (the root resource) - all nested EPGs will be deleted automatically
        if app_profile_name not in file_data["app_profiles"]:
            file_data["app_profiles"].append(app_profile_name)

        if bd_name not in file_data["bridge_domains"]:
            file_data["bridge_domains"].append(bd_name)

        with open(file_path, "w") as json_file:
            json.dump(file_data, json_file)

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
        curr_dir = os.path.dirname(os.path.abspath(__file__))  # ~path_to_env/cisco/aci/logical/runners
        file_path = os.path.join(curr_dir, self.CREATED_ACI_RESOURCE_FILE_NAME)

        if os.path.exists(file_path):
            with open(file_path, "r") as json_file:
                file_data = json.load(json_file)
            os.remove(file_path)
        else:
            file_data = {"app_profiles": [], "bridge_domains": []}

        return self.remove_resources_flow.execute_flow(app_profiles=file_data["app_profiles"],
                                                       bridge_domains=file_data["bridge_domains"])
