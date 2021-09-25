import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("OpenUrl")
class BaseClass:
    # drop down utility
    def dropdownselector(self, dropdownlocator, name):
        dd = Select(dropdownlocator)
        dd.select_by_visible_text(name)
