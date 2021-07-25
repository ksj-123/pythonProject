import unittest
from unittest import TestCase
from traing_playground_page import TrainingPlaygroundPage
tpPage = None
def get_page():
    global tpPage
    if tpPage == None:
        tpPage = TrainingPlaygroundPage()


class TrainingGroundTests(TestCase):
    def setUp(self):
        get_page()

    def test_ipt1_empty_by_default(self):
        """ipt1 filed should be empty"""
        # tpPage = TrainingPlaygroundPage()
        # runs global tpPage instance
        get_page()
        tpPage.setup()
        # self.assertTrue(tpPage.get_input_1().text == '')
        self.assertTrue(tpPage.get_input("input_1").get_attribute(value) == '')
        # tpPage.tier_down()

    def test_ipt1_fill_with_text(self):
        """ipt1 send keys to fill"""
        # runs global tpPage instance
        get_page()
        tpPage.setup()
        test_string = "sdfssfdsfd"
        # tpPage.type_into_input_1(test_string)
        tpPage.type_into("input_1", test_string)
        self.assertTrue(test_string == tpPage.get_input_1().get_attribute("value"))
        # tpPage.tier_down()