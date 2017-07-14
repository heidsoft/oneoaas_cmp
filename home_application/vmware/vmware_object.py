# -*- coding: utf-8 -*-
import json


class Capability(object):
    pass

class VirtualMachine(object):
    def __init__(self):
        self.host = None
        self.connectionState = None
        self.powerState = None

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,sort_keys=True, indent=4)