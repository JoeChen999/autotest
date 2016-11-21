from BaseTestCase import BaseTestCase
from common import utils


class Quest(BaseTestCase):
    def init(self):
        device = self.devices[0]
        if utils.is_new_account(device):
            utils.skip_FTE(device)
        if not utils.start_complete(device):
            device.screen_shot_to_fault(check_num=99)
            self.success = False
        utils.switch_account(device, "999chenbiao@163.com", "joe890819")
        if not utils.start_complete(device):
            device.screen_shot_to_fault(check_num=98)
            self.success = False
        pass

    def execute(self):
        if not self.success:
            return
        device = self.devices[0]
        device.touch_pos(460, 2450)
        if not device.check_pic(50, 800, 1300, 400):
            self.success = False
            return
        device.touch_pos(600, 1000)
        if not device.check_pic(80, 370, 1280, 1730):
            self.success = False
            return
        device.press_back()
        device.touch_pos(600, 1600)
        if not device.check_pic(80, 370, 1280, 1730):
            self.success = False
            return



