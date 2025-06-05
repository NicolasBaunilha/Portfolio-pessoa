import pandas as pd
import pyautogui
import time

#Passo 1 - entrar no sistema da empresa
#Abrindo o google
pyautogui.click(x=36, y=63)
time.sleep(0.5)
pyautogui.click(x=669, y=504)
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
#Passo 5 - Repetir para os demais