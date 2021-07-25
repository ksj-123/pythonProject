from traing_playground_page import get_input_1, type_into_input_1, setup, tier_down

def ipt1_empty_by_default_test():
    """ipt1 filed should be empty"""
    setup()
    assert get_input_1().text == ''
    tier_down()

def ipt1_fill_with_text_test():
    """ipt1 send keys to fill"""
    setup()
    test_string = "sdfssfdsfd"
    ipt1_element = get_input_1()
    type_into_input_1(test_string)
    assert test_string == ipt1_element.text
    tier_down()


# if __name__ == "__main__":
#     setup()