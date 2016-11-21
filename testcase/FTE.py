from BaseTestCase import BaseTestCase
from common import utils


class FTE(BaseTestCase):
    def init(self):
        device = self.devices[0]
        if not utils.is_new_account(device):
            self.log.info("old account")
            if utils.start_complete(device):
                self.log.info("start complete")
                utils.switch_account(device)
                self.log.info("switch account complete")
                if not utils.is_new_account(device):
                    device.screen_shot_to_fault(check_num=99)
                    self.success = False

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
