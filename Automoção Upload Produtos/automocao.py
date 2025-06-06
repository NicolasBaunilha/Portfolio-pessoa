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
time.sleep(0.5)

#Passo 4 - Cadastrar 1 produto
for linha in tabela.index:
    
    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = str(tabela.loc[linha, "categoria"])
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    custo = str(tabela.loc[linha, "custo"])
    obs = str(tabela.loc[linha, "obs"])

    pyautogui.click(x=469, y=288)
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
    
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(100)

print("controle")
#Passo 5 - Repetir para os demais

