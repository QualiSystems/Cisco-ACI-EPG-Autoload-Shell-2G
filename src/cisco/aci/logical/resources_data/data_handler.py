import json
import os


class ResourcesDataHandler(object):
    """

    file_data = {
        "tenants": {
            "Heroes": {
                "app_profiles": ["App Profile 1"],
                "bridge_domains": ["BD 1"]
            }
        }
    }
    """
    ACI_RESOURCE_FILE_NAME_TPL = "created_aci_resources_{reservation_id}.json"
    ACI_RESOURCES_DIR = "created_aci_resources.json"

    def __init__(self, reservation_id):
        """

        :param reservation_id:
        """
        curr_dir = os.path.dirname(os.path.abspath(__file__))  # ~path_to_env/cisco/aci/logical/runners
        self._file_path = os.path.join(curr_dir, self.ACI_RESOURCE_FILE_NAME_TPL.format(reservation_id=reservation_id))
        self._file_data = {
            "tenants": {}
        }

    def __enter__(self):
        """

        :return:
        """
        self.read_data()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """

        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        self.write_data()

    def _get_tenant_data(self, tenant_name):
        """

        :param tenant_name:
        :return:
        """
        default_tenant_data = {"app_profiles": [], "bridge_domains": []}

        return self._file_data["tenants"].setdefault(tenant_name, default_tenant_data)

    def read_data(self):
        """

        :return:
        """
        if os.path.exists(self._file_path):
            with open(self._file_path, "r") as json_file:
                self._file_data = json.load(json_file)

    def write_data(self):
        """

        :return:
        """
        with open(self._file_path, "w") as json_file:
            json.dump(self._file_data, json_file, indent=4)

    def add_app_profile(self, tenant_name, app_profile_name):
        """

        :param tenant_name:
        :param app_profile_name:
        :return:
        """
        tenant_data = self._get_tenant_data(tenant_name)

        if app_profile_name not in tenant_data["app_profiles"]:
            tenant_data["app_profiles"].append(app_profile_name)

    def add_bridge_domain(self, tenant_name, bridge_domain_name):
        """

        :param tenant_name:
        :param bridge_domain_name:
        :return:
        """
        tenant_data = self._get_tenant_data(tenant_name)

        if bridge_domain_name not in tenant_data["bridge_domains"]:
            tenant_data["bridge_domains"].append(bridge_domain_name)

    @property
    def app_profiles_by_tenants(self):
        """

        :return:
        """
        app_profiles = []
        for tenant_name, tenant_data in self._file_data["tenants"].iteritems():
            for app_profile in tenant_data["app_profiles"]:
                app_profiles.append((tenant_name, app_profile))

        return app_profiles

    @property
    def bridge_domains_by_tenants(self):
        """

        :return:
        """
        bridge_domains = []
        for tenant_name, tenant_data in self._file_data["tenants"].iteritems():
            for bridge_domain in tenant_data["bridge_domains"]:
                bridge_domains.append((tenant_name, bridge_domain))

        return bridge_domains

    def remove_data_file(self):
        """

        :return:
        """
        os.remove(self._file_path)
