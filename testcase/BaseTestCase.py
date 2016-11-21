from common import Log
from common.Color import Color


class BaseTestCase:
    def __init__(self, devices, test_suite, test_case):
        self.devices = devices
        self.log = Log.Log(test_suite)
        self.success = True
        self.case_name = test_case
        self.test_suite = test_suite

    def set_up(self):
        for d in self.devices:
            d.set_case_name(suite=self.test_suite, name=self.case_name)
        for d in self.devices:
            d.start_activity()

    def init(self):
        pass

    def execute(self):
        pass

    def dispose(self):
        if self.success:
            self.log.info("test case [%s] execute success" % self.case_name)
        else:
            self.log.error("test case [%s] execute failed" % self.case_name)
        for d in self.devices:
            d.stop_activity()
        pass
