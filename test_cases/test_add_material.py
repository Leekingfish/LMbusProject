from page.main_page import MainPage

class TestAddMaterials:

    def setup(self):
        self.main = MainPage()

    def test_add_materials(self):
        """
        料品信息维护
        :return:
        """
        self.main.goto_materialsPage().commodityInfor()