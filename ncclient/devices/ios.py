"""
Handler for Cisco IOS device specific information.

Note that for proper import, the classname has to be:

    "<Devicename>DeviceHandler"

...where <Devicename> is something like "Default", "Nexus", etc.

All device-specific handlers derive from the DefaultDeviceHandler,
which implements the generic information needed for interaction
with a Netconf server.

"""


from .default import DefaultDeviceHandler

import ncclient.operations.third_party.ios.rpc as ios_rpc


IOS_NC_10 = "urn:ietf:params:netconf:base:1.0"


def ios_unknown_host_cb(host, fingerprint):
    # This will ignore the unknown host check when connecting to CSR devices
    return True


class IosDeviceHandler(DefaultDeviceHandler):
    """
    Cisco IOS handler for device specific information.


    """
    def __init__(self, device_params):
        super(IosDeviceHandler, self).__init__(device_params)

    def add_additional_operations(self):
        operations = dict(
            save_config=ios_rpc.SaveConfig,
            get=ios_rpc.Get,
            get_config=ios_rpc.GetConfig,
        )
        return operations

    def add_additional_ssh_connect_params(self, kwargs):
        kwargs['allow_agent'] = False
        kwargs['look_for_keys'] = False
        kwargs['unknown_host_cb'] = ios_unknown_host_cb

    def perform_qualify_check(self):
        return False

    def get_xml_base_namespace_dict(self):
        return {None: IOS_NC_10}
