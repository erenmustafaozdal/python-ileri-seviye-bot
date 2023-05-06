from modules.browser import Browser
from modules.mgm import MGM

# tarayıcı oluştur
driver = Browser().get()
# meteroloji genel müdürlüğü işlemleri
mgm = MGM(driver)
mgm.weather_page("ankara")
print(mgm.get_all_value())
