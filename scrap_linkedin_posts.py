from modules.excel import Excel
from modules.browser import Browser
from modules.linkedin import LinkedIn
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
driver = Browser().get()
# LinkedIn oturum açma sayfasına gidelim
linkedin = LinkedIn(driver)
linkedin.login(linkedin_email, linkedin_password)

# Şirket kullanıcı adı verildiğinde gönderilerini al
posts = linkedin.get_company_posts("servicenow")

sleep(5)

xl.save()
