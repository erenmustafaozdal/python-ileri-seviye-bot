from modules.excel import Excel
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from settings import linkedin_email, linkedin_password

# Excel dosyasını oluşturalım
xl = Excel("linkedin_posts.xlsx")
xl.write_header([
    "Owner Name",
    "Owner URL",
    "Date",
    "Text",
    "Shared Text",
])

# tarayıcıyı çalıştır ve LinkedIn'e giriş yap
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
# LinkedIn oturum açma sayfasına gidelim
driver.get('https://www.linkedin.com/login')

# Kullanıcı bilgilerimizi yazalım ve giriş yapalım
driver.find_element(By.ID, "username").send_keys(linkedin_email)
driver.find_element(By.ID, "password").send_keys(linkedin_password)
driver.find_element(By.XPATH, "//button[@data-litms-control-urn='login-submit']").click()

# Telefon ekleme ekranı geldi mi?
#   - Evet: Geç tuşuna tıkla
#   - Hayır: LinkedIn girişi başarılı
try:
    add_phone = driver.find_element(By.XPATH, "//div[contains(@class, 'cp-add-phone')]")
    add_phone.find_element(By.XPATH, ".//button[contains(@class, 'secondary-action')]").click()
except:
    print("LinkedIn giriş işlemi başarılı bir şekilde yapıldı.")

sleep(5)

xl.save()
