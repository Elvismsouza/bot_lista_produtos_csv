import pyautogui
import time
import pandas

# pyautogui.click - clicar com mouse
# pyautogui.write - escrever um texto
# pyautogui.press - apertar 1 tecla
# pyautogui.scroll - rolar a tela para cima ou para baixo

pyautogui.PAUSE = 0.5

# Entrar no sistema 
# Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(504, 429, duration=1)

# Entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press('enter')
time.sleep(5)
pyautogui.click(397, 377, duration=1)
time.sleep(1)
pyautogui.write("elvismsouza18@gmail.com")
time.sleep(1)
pyautogui.click(395, 472, duration=1)
time.sleep(1)
pyautogui.write("102030bia")
time.sleep(1)
pyautogui.click(677, 532, duration=1)
time.sleep(3)

# Ler tabela de produtos
tabela = pandas.read_csv("produtos.csv")

print(tabela)

# Cadastrar produtos
# Para cada linha da tabela:
for linha in tabela.index:
    pyautogui.click(x=442, y=260)

    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco_unitario)

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.press("tab")
        pyautogui.write(obs)

    pyautogui.press("enter")
    
    # Rolar para cima
    pyautogui.scroll(5000)
    
    # Clicar no primeiro campo
    pyautogui.click(410, 260, duration=1)
    
    time.sleep(15)
