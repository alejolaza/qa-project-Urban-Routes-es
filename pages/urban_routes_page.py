import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR,'.button.round')
    comfort_icon = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    comfort_icon_assert = (By.CSS_SELECTOR, '.tcard.active .tcard-title')
    phone_number_button = (By.CLASS_NAME, 'np-button')
    phone_number_field = (By.ID, 'phone')
    next_button = (By.XPATH, '//button[@class="button full" and text()="Siguiente"]')
    sms_code = (By.CSS_SELECTOR, '#code.input')
    confirm_button = (By.XPATH, '//button[@class="button full" and text()="Confirmar"]')
    pay_button = (By.CSS_SELECTOR, ".pp-button.filled")
    plus_icon = (By.CLASS_NAME, 'pp-plus-container')
    card_number_field = (By.ID, 'number')
    card_code_field = (By.CSS_SELECTOR, '#code.card-input')
    card_modal = (By.CLASS_NAME, 'card-second-row')
    add_button = (By.XPATH, '//button[@class="button full" and text()="Agregar"]')
    card_checkbox = (By.ID, 'card-1')
    close_button = (By.CSS_SELECTOR, '.payment-picker.open .close-button.section-close')
    message_for_driver_field = (By.ID, 'comment')
    order_requirements = (By.CLASS_NAME, 'reqs-arrow')
    blanket_and_scarf_slider = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/input')
    blanket_and_scarf_slider_state = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span')
    counter_plus = (By.CLASS_NAME, 'counter-plus')
    counter_value = (By.XPATH, '//div[@class="counter-value"]')
    modal_request_button = (By.CLASS_NAME, 'smart-button')
    modal_popup = (By.CLASS_NAME, 'order-header-content')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def set_from(self, from_address):
        self.wait.until(
            EC.visibility_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        self.wait.until(
            EC.visibility_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def get_request_taxi_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.request_taxi_button)
        )

    def click_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_icon(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.comfort_icon)
        )

    def click_comfort_icon(self):
        self.get_comfort_icon().click()

    def get_comfort_icon_assert(self):
        return self.wait.until(
            EC.presence_of_element_located(self.comfort_icon_assert)
        )

    def get_phone_number_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.phone_number_button)
        )

    def click_phone_number_button(self):
        self.get_phone_number_button().click()

    def set_phone_number_field(self, phone_number):
        self.wait.until(
            EC.visibility_of_element_located(self.phone_number_field)
        ).send_keys(phone_number)

    def get_phone_number_field(self):
        return self.driver.find_element(*self.phone_number_field).get_property('value')

    def get_next_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.next_button)
        )

    def click_next_button(self):
        self.get_next_button().click()

    def set_sms_code(self, sms_code):
        self.wait.until(
            EC.visibility_of_element_located(self.sms_code)
         ).send_keys(sms_code)

    def get_sms_code(self):
        return self.driver.find_element(*self.sms_code).get_property('value')

    def get_confirm_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.confirm_button)
        )

    def click_confirm_button(self):
        self.get_confirm_button().click()

    def get_pay_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.pay_button)
        )

    def click_pay_button(self):
        self.get_pay_button().click()

    def get_plus_icon(self):
        return self.wait.until(
            EC.presence_of_element_located(self.plus_icon)
        )

    def click_plus_icon(self):
        self.get_plus_icon().click()

    def set_card_number_field(self, card_number):
        self.wait.until(
            EC.visibility_of_element_located(self.card_number_field)
        ).send_keys(card_number)

    def get_card_number_field(self):
        return self.driver.find_element(*self.card_number_field).get_property('value')

    def set_card_code_field(self, card_code):
        self.wait.until(
            EC.visibility_of_element_located(self.card_code_field)
        ).send_keys(card_code)

    def get_card_modal(self):
        return self.wait.until(
            EC.presence_of_element_located(self.card_modal)
        )

    def click_card_modal(self):
        self.get_card_modal().click()

    def get_add_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.add_button)
        )

    def click_add_button(self):
        self.get_add_button().click()

    def get_card_checkbox_state(self):
        return self.driver.find_element(*self.card_checkbox).get_attribute('checked')

    def get_close_button(self):
        return self.wait.until(
            EC.presence_of_element_located(self.close_button)
        )

    def click_close_button(self):
        self.get_close_button().click()

    def set_message_for_driver_field(self, message_for_driver):
        self.wait.until(
            EC.visibility_of_element_located(self.message_for_driver_field)
        ).send_keys(message_for_driver)

    def get_message_for_driver_field(self):
        return self.driver.find_element(*self.message_for_driver_field).get_property('value')

    def get_blanket_and_scarf_slider(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.blanket_and_scarf_slider)
        )

    def click_blanket_and_scarf_slider(self):
        self.get_blanket_and_scarf_slider().click()

    def get_blanket_and_scarf_slider_state(self):
        return self.driver.find_element(*self.blanket_and_scarf_slider_state).is_selected()

    def get_counter_plus(self):
        return self.wait.until(
            EC.presence_of_element_located(self.counter_plus)
        )

    def click_counter_plus(self):
        self.get_counter_plus().click()

    def click_counter_plus_times(self, times):
        for _ in range(times):
            self.click_counter_plus()

    def get_counter_value(self):
        return self.driver.find_element(*self.counter_value).text

    def get_modal_request_button(self):
        return self.wait.until(
            EC.element_to_be_clickable(self.modal_request_button)
        )

    def click_modal_request_button(self):
        self.get_modal_request_button().click()

    def get_modal_popup(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.modal_popup)
        ).is_displayed()



