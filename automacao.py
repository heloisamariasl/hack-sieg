from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://talkabit-z3eg.onrender.com")

botao = driver.find_element("xpath", "//button[contains(., 'Entrar no portal')]")

botao.click()

login = "STARWARS-RMJQZ"
senha = "talkabit"

campo_login = driver.find_element("xpath", "//input[@placeholder='Login']")
campo_login.send_keys(login)

campo_senha = driver.find_element("xpath", "//input[@placeholder='Senha']")
campo_senha.send_keys(senha)
