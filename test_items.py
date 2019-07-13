import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_items(browser):
    browser.get(link)
    time.sleep (30)
    button = browser.find_element_by_id("add_to_basket_form")
    assert len (button) == 1, "Something wrong with our button"
