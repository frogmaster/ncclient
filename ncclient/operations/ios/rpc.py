from lxml import etree
from ncclient.xml_ import qualify

import ncclient.operations.retrieve as retrieve
import ncclient.operations.rpc as rpc

IOS_NC_10 = "urn:ietf:params:netconf:base:1.0"


class GetReply(retrieve.GetReply):
    def _parsing_hook(self, root):
        self._data = None
        if not self._errors:
            self._data = root.find(qualify("data", IOS_NC_10))


class Get(retrieve.Get):
    REPLY_CLS = GetReply


class GetConfig(retrieve.GetConfig):
    REPLY_CLS = GetReply


class SaveConfig(rpc.RPC):
    def request(self):
        node = etree.Element(qualify('save-config', IOS_NC_10))
        return self._request(node)
