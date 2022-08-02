from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://demo.anhtester.com/basic-first-form-demo.html')
driver.implicitly_wait(10)
try:
    print('Fechando o addsense')
    addsense_botao = driver.find_element(By.ID, 'at-cv-lightbox-close')
    addsense_botao.click()
except:
    print('erro ao fechar o addsense')

# selecionando o campo
campo_mensagem = driver.find_element(By.XPATH, '//*[@id="user-message"]')
campo_mensagem.send_keys('Credidio')
sleep(1)
# selecionando o botão
btn_mostra_mensagem = driver.find_element(By.XPATH, '//*[@id="get-input"]/button')
btn_mostra_mensagem.click()
sleep(1)
# exibir mensagem no terminal
mensagem_do_display = driver.find_element(By.ID, 'display').text
print(mensagem_do_display, 'deu tudo certo nosso script de automação')

sleep(5)
driver.quit()