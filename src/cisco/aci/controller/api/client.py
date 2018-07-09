import acitoolkit.acitoolkit as aci


class CiscoACIControllerHTTPClient(object):
    def __init__(self, logger, address, user=None, password=None, scheme="https", port=443):
        """

        :param logging.Logger logger:
        :param str address: controller IP address
        :param str user: controller username
        :param str password: controller password
        :param str scheme: protocol (http|https)
        :param int port: controller port
        """
        full_url = "{}://{}:{}".format(scheme.lower(), address, port)
        self._logger = logger
        self._logger.info("APIC full URL: {}".format(full_url))
        self._session = aci.Session(url=full_url, uid=user, pwd=password)
        self._login()

    def _login(self):
        """

        :return:
        """
        resp = self._session.login()

        if not resp.ok:
            self._logger.error("Unable to login to the ACI Controller. HTTP Status code: {} Response: {}"
                               .format(resp.status_code, resp.content))
            raise Exception("Unable to login to the ACI Controller")

    def get_tenants_structure(self):
        """Get all Tenants structure in the next format:

        [{"name": "tenant_1", "app_profiles": [{"name": "app_profile_1", "epgs": [{"name": "EPG_1"}]}]}]
        :rtype: list[dict]
        """
        tenants_structure = []
        tenants = aci.Tenant.get_deep(self._session)
        self._logger.info("Tenants info from the APIC: {}".format(tenants))

        for tenant in tenants:
            app_profiles = []
            tenants_structure.append({
                "name": tenant.name,
                "app_profiles": app_profiles
            })
            for tenant_child in tenant.get_children():
                if isinstance(tenant_child, aci.AppProfile):
                    epgs = []
                    app_profiles.append({
                        "name": tenant_child.name,
                        "epgs": epgs
                    })

                    for app_profile_child in tenant_child.get_children():
                        if isinstance(app_profile_child, aci.CommonEPG):
                            epgs.append({
                                "name": app_profile_child.name
                            })

        self._logger.info("Parsed Tenants structure: {}".format(tenants_structure))
        return tenants_structure
