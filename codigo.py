# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui 
import time
import pandas

# pyautogui.write -> escrever um texto
# pyautogui.click -> clicar com o mouse
# pyautogui.press -> apertar uma tecla
# pyautogui.hotkey -> apertar um atalho de teclado (Ctrl, C)
# pyautogui.PAUSE = 1 -> delay

# abrir o navegador
# apertar tecla win
# pyautogui.PAUSE = 0.2
pyautogui.press('win')
pyautogui.write('opera')
pyautogui.press('Enter')

# entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login
time.sleep(1)
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')



# Passo 2: Fazer login
time.sleep(1)
pyautogui.click(x=873, y=359)
pyautogui.write('rodrigueskaua7676@gmail.com')
pyautogui.press('tab')
pyautogui.write('123456')
pyautogui.press('tab')
pyautogui.press('enter')


# Passo 3: Importar base de dados
# linha = 0

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar 1 produto

# para cada linha na minha tabela
for linha in tabela.index:
    pyautogui.click(x=851, y=244)

    #codigo
    codigo = tabela.loc[linha,  'codigo']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    #marca
    marca = tabela.loc[linha, 'marca']
    pyautogui.write(str(marca))
    pyautogui.press('tab')

    #tipo
    tipo = tabela.loc[linha, 'tipo']
    pyautogui.write(str(tipo))
    pyautogui.press('tab')

    #categoria
    categoria = tabela.loc[linha, 'categoria']
    pyautogui.write(str(codigo))
    pyautogui.press('tab')

    #preco
    preco = tabela.loc[linha, 'preco_unitario']
    pyautogui.write(str(preco))
    pyautogui.press('tab')

    #custo
    custo = tabela.loc[linha, 'custo']
    pyautogui.write(str(custo))
    pyautogui.press('tab')

    #obs
    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press('tab')

    pyautogui.press('enter')
    pyautogui.scroll(5000)
    pyautogui.press('tab')
# Passo 5: Repetir o processo de cadastro até acabar os produtos