import pandas as pd
import pyautogui
import time

#Passo 1 - entrar no sistema da empresa
#Abrindo o google
pyautogui.click(x=36, y=63)
time.sleep(0.5)
#pyautogui.click(x=669, y=504)
time.sleep(0.5)

#Acessando o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#Passo 2 - realizar o login
time.sleep(2)
pyautogui.click(x=487, y=410)
pyautogui.write("emailexemplo@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhadeacessoexemplo")
pyautogui.press("enter")

#Passo 3 - Impoortar a base de dados
tabela = pd.read_csv("produtos.csv")

#Passo 4 - Cadastrar 1 produto
time.sleep(0.5)
pyautogui.press("tab")

codigo = "MOLO000251"
marca = "Logitech"
tipo = "Mouse"
categoria = "1"
preco_unitario = "25.95"
custo = "50"
obs = ""

pyautogui.write(codigo)
pyautogui.press("tab")

pyautogui.write(marca)
pyautogui.press("tab")

pyautogui.write(tipo)
pyautogui.press("tab")

pyautogui.write(categoria)
pyautogui.press("tab")

pyautogui.write(preco_unitario)
pyautogui.press("tab")

pyautogui.write(custo)
pyautogui.press("tab")

pyautogui.write(obs)
pyautogui.press("tab")
pyautogui.press("enter")

print("controle")
#Passo 5 - Repetir para os demais