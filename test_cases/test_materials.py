from page.main_page import MainPage

class TestDeliveryBooking:

    def setup(self):
        self.main = MainPage()

    def test_delivery_booking(self):
        """
        料品信息维护
        :return:
        """
        self.main.goto_commodity_infor().commodityInfor()