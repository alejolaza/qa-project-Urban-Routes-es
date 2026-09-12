from Utils.retrieve_phone_code import retrieve_phone_code
from data import data
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.urban_routes_page import UrbanRoutesPage

class TestUrbanRoutes:

    def setup_method(self):
        options = Options()
        options.set_capability("goog:loggingPrefs",{'performance': 'ALL'})
        self.driver = webdriver.Chrome(service=Service(),options=options)
        self.driver.maximize_window()
        self.driver.get(data.urban_routes_url)
        self.routes_page = UrbanRoutesPage(self.driver)

    def test_1_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    def test_2_select_comfort_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        comfort_tariff = self.routes_page.get_comfort_icon_assert().text
        assert comfort_tariff == 'Comfort'

    def test_3_fill_phone_number(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_phone_number_button()
        phone_number = data.phone_number
        self.routes_page.set_phone_number_field(phone_number)
        self.routes_page.click_next_button()
        sms_code = retrieve_phone_code(self.driver)
        self.routes_page.set_sms_code(sms_code)
        self.routes_page.click_confirm_button()
        assert self.routes_page.get_phone_number_field() == phone_number

    def test_4_add_credit_card(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_pay_button()
        self.routes_page.click_plus_icon()
        card_number = data.card_number
        card_code = data.card_code
        self.routes_page.set_card_number_field(card_number)
        self.routes_page.set_card_code_field(card_code)
        self.routes_page.click_card_modal()
        self.routes_page.click_add_button()
        assert self.routes_page.get_card_checkbox_state() == 'true'
        self.routes_page.click_close_button()

    def test_5_write_message_for_driver(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        message_for_driver= data.message_for_driver
        self.routes_page.set_message_for_driver_field(message_for_driver)
        assert  self.routes_page.get_message_for_driver_field() == message_for_driver

    def test_6_request_blanket_and_scarf(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_blanket_and_scarf_slider()
        assert self.routes_page.get_blanket_and_scarf_slider_state().is_selected()

    def test_7_request_two_ice_cream(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_counter_plus_times(2)
        assert self.routes_page.get_counter_value() == "2"

    def test_8_request_taxi_modal_is_visible(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        self.routes_page.click_phone_number_button()
        phone_number = data.phone_number
        self.routes_page.set_phone_number_field(phone_number)
        self.routes_page.click_next_button()
        sms_code = retrieve_phone_code(self.driver)
        self.routes_page.set_sms_code(sms_code)
        self.routes_page.click_confirm_button()
        self.routes_page.click_pay_button()
        self.routes_page.click_plus_icon()
        card_number = data.card_number
        card_code = data.card_code
        self.routes_page.set_card_number_field(card_number)
        self.routes_page.set_card_code_field(card_code)
        self.routes_page.click_card_modal()
        self.routes_page.click_add_button()
        self.routes_page.click_close_button()
        self.routes_page.click_modal_request_button()
        assert self.routes_page.get_modal_popup() is True

    def teardown_method(self):
        self.driver.quit()