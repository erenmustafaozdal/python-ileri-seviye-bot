from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MGM:

    url = "https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=__CITY__"

    # SEÇİCİLER
    temp_value = "//div[contains(@class, 'anlik-sicaklik-deger')]"
    temp_icon = "//div[@class='anlik-sicaklik-havadurumu-ikonu']/img"
    temp_humidity = "//div[contains(@class, 'anlik-nem-deger-kac')]"
    temp_wind = "//div[contains(@class, 'anlik-ruzgar-deger-kac')]"

    def __init__(self, driver: Chrome):
        self.driver = driver

    def weather_page(self, city, county=None):
        url = self.url.replace("__CITY__", city)
        if county:
            url += f"&ilce={county}"

        self.driver.get(url)
        # sayfaya gittikten sonra elemanlar yüklenene kadar bekle
        WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located((By.XPATH, self.temp_icon))
        )

    def get_temp_value(self):
        return self.driver.find_element(By.XPATH, self.temp_value).text + "°C"

    def get_temp_icon(self):
        icon = self.driver.find_element(By.XPATH, self.temp_icon)
        return {
            "src": icon.get_attribute("src"),
            "title": icon.get_attribute("title")
        }

    def get_temp_humidity(self):
        return "%" + self.driver.find_element(By.XPATH, self.temp_humidity).text

    def get_temp_wind(self):
        return self.driver.find_element(By.XPATH, self.temp_wind).text + "km/sa"

    def get_all_value(self):
        return {
            "temp": self.get_temp_value(),
            "icon": self.get_temp_icon(),
            "humidity": self.get_temp_humidity(),
            "wind": self.get_temp_wind(),
        }
