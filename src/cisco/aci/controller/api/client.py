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

    def get_epgs(self):
        """Get all EndPoint Groups grouped by their tenant

        :return:
        """
        epgs_by_tenant = {}
        tenants = aci.Tenant.get_deep(self._session)

        for tenant in tenants:
            for tenant_child in tenant.get_children():
                if isinstance(tenant_child, aci.AppProfile):
                    for app_profile_child in tenant_child.get_children():
                        if isinstance(app_profile_child, aci.CommonEPG):
                            epgs = epgs_by_tenant.setdefault(tenant.name, [])
                            epgs.append({
                                "name": app_profile_child.name
                            })

        return epgs_by_tenant
