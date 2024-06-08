from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from time import sleep

#definir browser
driver = webdriver.Firefox()

#timeout implicito
driver.set_page_load_timeout(5)

#try e except na página
try:
    driver.get("http://localhost:8501")
    sleep(5)
    print("Acessou a Página com sucesso")
except:
    print("Tempo de carregamento da página excedeu o limite")
finally:
    driver.quit()