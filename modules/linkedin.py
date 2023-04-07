from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


class LinkedIn:

    # SEÇİCİLER
    # post = //div[contains(@class,'occludable-update')]
    # post_owner_link = //a[contains(@class, 'update-components-actor__container-link')]
    # post_owner = //span[contains(@class, 'update-components-actor__name')]
    # post_date = //span[contains(@class, 'update-components-actor__sub-description')]
    # post_text = //div[contains(@class, 'feed-shared-update-v2__description-wrapper')]
    company_name = "//h1[contains(@class, 'ember-view')]"
    post_title = "//div[contains(@class, 'update-components-actor__meta')]"

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

    def get_company_posts(self, company):
        # Şirketin profiline git
        self.driver.get(f"https://www.linkedin.com/company/{company}/posts")

        # Şirketin adını al
        company_name = self.driver.find_element(By.XPATH, self.company_name).text

        # gönderileri al
        post_titles = self.driver.find_elements(By.XPATH, self.post_title)

        # Gönderiler içinde döngüye girelim
        for title in post_titles:
            pass
            # todo: Gönderinin tarihi seçicisi
            # todo: Gönderinin metni seçicisi

