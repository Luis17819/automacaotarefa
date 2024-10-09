import pyautogui # type: ignore
import time
import pandas # type: ignore
# pyautogui.write - escrever um texto
# pyautogui.click - clicar com o mouse
# pyautogui.press - apertar uma tecla
# pyautogui.hotkey - apertar um atalho de teclado Ex: Ctrl + C 
# pyautogui.PAUSE - pausa em segundo

pyautogui.PAUSE = 0.3

# Passo 1: Entrar no sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login

# abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Passo 2: Fazer login
    
time.sleep(3)
# clicar no campo email
pyautogui.click(x=-1196, y=637)
pyautogui.write("teste.email@gmail.com")
# passar para o próximo campo
pyautogui.press("tab")
pyautogui.write("teste123")
# entra no sistema
pyautogui.press("enter")

# Clica no Ok aviso google
time.sleep(2)
pyautogui.press("enter")

# Passo 3: Importar a base de dados
tabela = pandas.read_csv("p.csv")
print(tabela)

# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o processo de cadastro até acabar os produtos
for linha in tabela.index:
    pyautogui.click(x=-1207, y=527)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    pyautogui.press("enter")

    pyautogui.scroll(1000)

