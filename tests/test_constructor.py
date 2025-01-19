from locators import MainPageLocators
from urls import URLS


class TestConstructorPage:
    def test_transition_to_bun_success(self, driver):
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.sauces_btn).click()
        driver.find_element(*MainPageLocators.bun_btn).click()
        bun_class = driver.find_element(*MainPageLocators.active_bun_btn).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in bun_class



    def test_transition_to_sauces_success(self, driver):
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.sauces_btn).click()
        sauces_class = driver.find_element(*MainPageLocators.active_sauces_btn).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in sauces_class

    def test_transition_to_topping_success(self, driver):
        driver.get(URLS.MAIN_PAGE_URL)
        driver.find_element(*MainPageLocators.toppings_btn).click()
        toppings_class = driver.find_element(*MainPageLocators.active_toppings_btn).get_attribute('class')
        assert 'tab_tab_type_current__2BEPc' in toppings_class
