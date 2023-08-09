from page.main_page import MainPage

class TestDeliveryBooking:

    def setup(self):
        self.main = MainPage()

    def test_delivery_booking(self):
        """
        送货预约
        :return:
        """
        self.main.goto_purchase_management().delivery_booking_banb()

