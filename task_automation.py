import pyautogui
import time

# Pequena pausa entre os comandos
pyautogui.PAUSE = 0.5

# Passo 1: Abrir o navegador Chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)

# Passo 2: Acessar o site da GB Wear
pyautogui.write("https://www.gbwear.com.br/")
pyautogui.press("enter")
time.sleep(6)  # espera a página carregar

# Passo 3: Fechar o pop-up clicando no "X"
pyautogui.click(x=1340, y=278)  # Coordenada do botão "X" do pop-up
time.sleep(0.5)

# Passo 4: Passar o mouse sobre "Homens" no menu
pyautogui.moveTo(x=773, y=230)  # Hover sobre "Homens"
time.sleep(0.5)

# Passo 5: Clicar na opção "Kimonos"
pyautogui.click(x=199, y=339)
time.sleep(0.5)

# Passo 6: Scroll para baixo pra mostrar mais produtos
pyautogui.scroll(-900)
time.sleep(0.5)

# Passo 7: Clicar no produto "Kimono Atleta GB V4"
pyautogui.click(x=1306, y=469)
time.sleep(1)  # Espera a página de produto abrir

# Passo 8: Clicar no botão A1 (tamanho)
pyautogui.click(x=1158, y=689)  # Coordenada do botão A1
time.sleep(0.5)

# Passo 9: Clicar no botão "Adicionar ao carrinho"
pyautogui.click(x=1226, y=954)  # Coordenada do botão "Adicionar ao carrinho"
time.sleep(0.5)

# Passo 10: Fechar o navegador (independente do resultado)
pyautogui.hotkey("ctrl", "w")
