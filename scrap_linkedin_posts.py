from modules.excel import Excel
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

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
driver.get('https://linkedin.com')

xl.save()
