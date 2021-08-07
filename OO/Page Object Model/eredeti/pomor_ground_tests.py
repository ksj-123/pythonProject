from training_playground_page import TrainingPlaygroundPage

tpPage = TrainingPlaygroundPage()
tpPage = None
def get_page():
    global tpPage
    if tpPage == None:
        tpPage = TrainingPlaygroundPage()

def ipt1_empty_by_default_test():
    """ipt1 filed should be empty"""
    tpPage = TrainingPlaygroundPage()
    # runs global tpPage instance
    get_page()
    tpPage.setup()
    assert tpPage.get_input_1().text == ''
    tpPage.tier_down()

def ipt1_fill_with_text_test():
    """ipt1 send keys to fill"""
    # runs global tpPage instance
    get_page()
    tpPage.setup()
    test_string = "sdfssfdsfd"
    tpPage.type_into_input_1(test_string)
    assert test_string == tpPage.get_input_1().get_attribute("value")
    tpPage.tier_down()
