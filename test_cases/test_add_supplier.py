from page.main_page import MainPage

class TestAddSupplier:

    def setup(self):
        self.main = MainPage()

    def test_add_supplier(self):
        """
        供应商信息
        :return:
        """
        self.main.goto_supplierPage().supplierInfor()