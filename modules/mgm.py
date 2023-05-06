from selenium.webdriver import Chrome


class MGM:

    url = "https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il=__CITY__"

    def __init__(self, driver: Chrome):
        self.driver = driver

    def weather_page(self, city, county=None):
        url = self.url.replace("__CITY__", city)
        if county:
            url += f"&ilce={county}"

        print(url)
        self.driver.get(url)
