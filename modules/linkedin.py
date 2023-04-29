from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from time import sleep


class LinkedIn:

    # SEÇİCİLER
    post = "//div[contains(@class,'occludable-update')]"
    post_owner_link = ".//a[contains(@class, 'update-components-actor__container-link')]"
    post_owner = ".//span[contains(@class, 'update-components-actor__name')]"
    post_date = ".//span[contains(@class, 'update-components-actor__sub-description')]"
    post_text = ".//div[contains(@class, 'feed-shared-update-v2__description-wrapper')]//div[contains(@class, 'update-components-text')]"
    load_button = "//button[contains(@class, 'scaffold-finite-scroll__load-button')]"

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

    def infinite_scroll_get_posts(self):
        posts_count = 0
        while True:
            # daha fazla yükle tuşu olduğu sürece tıkla, yoksa devam et
            try:
                self.driver.find_element(By.XPATH, self.load_button).click()
            except:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            sleep(5)

            posts = self.driver.find_elements(By.XPATH, self.post)
            print(f"Toplam gönderi sayısı: {posts_count}")

            if posts_count == len(posts):
                break

            posts_count = len(posts)

        return posts

    def get_company_posts(self, company):
        # Şirketin profiline git
        self.driver.get(f"https://www.linkedin.com/company/{company}/posts")

        # gönderileri al
        posts = self.infinite_scroll_get_posts()

        # Gönderiler içinde döngüye girelim
        result = []
        for post in posts:
            # Gönderileri reklamlardan ayırmak için gönderi sahibi linki
            # var mı diye kontrol edelim. Eğer yoksa continue ile adımı atlayalım
            try:
                post_link = post.find_element(By.XPATH, self.post_owner_link).get_attribute("href")
                post_owner_name = post.find_element(By.XPATH, self.post_owner).text
                post_date = post.find_element(By.XPATH, self.post_date).text
                post_text = post.find_element(By.XPATH, self.post_text).text
            except:
                continue

            # dict key'ler düzeltilecek dict.values ile excel'e yazılacak
            result.append({
                "A": post_owner_name.split("\n")[0],
                "B": post_link.split("?")[0],
                "C": post_date.split(' • ')[0],
                "D": post_text
            })

        return result
