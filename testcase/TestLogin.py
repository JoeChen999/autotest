from common import utils
from BaseTestCase import BaseTestCase


class TestLogin(BaseTestCase):
    def init(self):
        device = self.devices[0]
        utils.start_activity(device)
        if utils.is_new_account(device):
            utils.skip_FTE(device)

    def execute(self):
        device = self.devices[0]
        utils.switch_account(device, "999chenbiao@163.com", "joe890819")
        if utils.start_complete(device):
            device.touch_pos(70, 70)
        device.check_saved_pic("user_name")

