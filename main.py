import time
import pydirectinput
import pyautogui

def loopForShiny():
    shinyWasFound = False
    resetCounter = 0

    while shinyWasFound == False:
        time.sleep(6)
        pydirectinput.press('space')
        time.sleep(1)
        pydirectinput.press('space')
        print('Iniciou o Jogo')

        time.sleep(2)
        pydirectinput.press('x')
        print('Clicou no Continuar')

        time.sleep(3)
        pydirectinput.press('x')
        time.sleep(4)
        pydirectinput.press('x')
        print('Abriu a Maleta')

        time.sleep(1)
        pydirectinput.press('right')
        shouldPressButton('x', 2, 0.5)
        print('Selecionou o Chimchar')

        print('Professor começou a falar')
        time.sleep(3)
        pydirectinput.press('x')
        shouldPressButton('x', 4, 1)
        shouldPressButton('x', 2, 2)
        time.sleep(1)
        pydirectinput.press('x')

        print('Professor se retirou')
        time.sleep(4)
        pydirectinput.press('x')
        time.sleep(1)
        pydirectinput.press('x')

        print('Aluno se retirou')
        time.sleep(4)
        pydirectinput.press('x')
        time.sleep(1)
        pydirectinput.press('x')

        print('Rival se aproxima')
        time.sleep(5)
        pydirectinput.press('x')
        time.sleep(2)
        pydirectinput.press('x')
        time.sleep(0.5)
        pydirectinput.press('x')
        shouldPressButton('x', 3, 1)


        print('Entrando em batalha')
        time.sleep(8)

        print('Verificar se é Shiny')
        normalColor = pyautogui.pixelMatchesColor(200, 201, (199, 109, 44))

        if normalColor:
            pydirectinput.keyDown('l')
            pydirectinput.keyDown('r')
            pydirectinput.keyDown('space')
            pydirectinput.keyDown('tab')
            time.sleep(1)
            pydirectinput.keyUp('l')
            pydirectinput.keyUp('r')
            pydirectinput.keyUp('space')
            pydirectinput.keyUp('tab')

            resetCounter += 1
            print(resetCounter)
        else:
            shinyWasFound = True

def shouldPressButton(button, repetitions, sleepTime):
    for repetition in range(repetitions):
        time.sleep(sleepTime)
        pydirectinput.press(button)

loopForShiny()