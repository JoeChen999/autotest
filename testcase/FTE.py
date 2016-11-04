from BaseTestCase import BaseTestCase
from common import checkpic
from common import utils


class FTE(BaseTestCase):
    def init(self):
        device = self.devices[0]
        if not utils.is_new_account(device):
            if utils.start_complete(device):
                utils.switch_account(device)
                assert utils.is_new_account(device)

    def execute(self):
        device = self.devices[0]
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280, 10)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280, 5)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280, 5)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280)
        device.touch_pos(720, 1280, 5)
        device.touch_pos(720, 1280)
        if not device.check_pic(50, 2100, 280, 60):
            self.success = False
            return 
