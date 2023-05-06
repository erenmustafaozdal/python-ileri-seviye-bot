from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class MGM:

    url = "https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=__CITY__"

    # SEÇİCİLER
    temp_value = "//div[contains(@class, 'anlik-sicaklik-deger')]"

    def __init__(self, driver: Chrome):
        self.driver = driver

    def weather_page(self, city, county=None):
        url = self.url.replace("__CITY__", city)
        if county:
            url += f"&ilce={county}"

        self.driver.get(url)

    def get_temp_value(self):
        return self.driver.find_element(By.XPATH, self.temp_value).text + "°C"
