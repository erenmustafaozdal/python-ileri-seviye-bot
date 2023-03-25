from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class LinkedIn:

    def __init__(self, driver: Chrome):
        self.driver = driver

    def login(self, email, password):
        self.driver.get('https://www.linkedin.com/login')

        # Kullanıcı bilgilerimizi yazalım ve giriş yapalım
        self.driver.find_element(By.ID, "username").send_keys(email)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[@data-litms-control-urn='login-submit']").click()

        # Telefon ekleme ekranı geldi mi?
        #   - Evet: Geç tuşuna tıkla
        #   - Hayır: LinkedIn girişi başarılı
        try:
            add_phone = self.driver.find_element(By.XPATH, "//div[contains(@class, 'cp-add-phone')]")
            add_phone.find_element(By.XPATH, ".//button[contains(@class, 'secondary-action')]").click()
        except:
            print("LinkedIn giriş işlemi başarılı.")
