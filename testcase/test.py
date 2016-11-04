from BaseTestCase import BaseTestCase


class quest(BaseTestCase):
    def init(self):
        self.log.error('1')
        device = self.devices[0]
        device.refresh_ui_data()

    def execute(self):
        self.log.error('2')
