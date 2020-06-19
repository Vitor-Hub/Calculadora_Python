"""

Nome: Vitor Santos Pereira
Matrícula: 201510170911
02/12/2018

"""

from tkinter import*
i = Tk()

    # Display
display = Label(i,width=20, text="0", font= ("Times",15, "bold"))
display.grid(row = 0 ,columnspan = 4)

resul = Label(i,width=20, text="", font= ("Times",15, "bold"))
resul.grid(row = 1 ,  columnspan = 4)


    # Botões
but1 = Button(i, text = "1",bg = "#19193C", fg = "white" ,width = 5, bd = 3, padx = 10, pady = 10, font= ("Times",15, "bold"), command = lambda: Botao(but1))
but1.grid( row = 5, column = 0)

but2 = Button(i, text = "2",bg = "#19193C", fg = "white" ,width = 5, bd = 3, padx = 10, pady = 10, font= ("Times",15, "bold"), command = lambda: Botao(but2))
but2.grid(row = 5, column = 1)

but3 = Button(i, text = "3",bg = "#19193C", fg = "white" ,width = 5, bd = 3, padx = 10, pady = 10, font= ("Times",15, "bold"), command = lambda:Botao(but3))
but3.grid(row = 5, column = 2)

but4 = Button(i, text = "4",bg = "#19193C", fg = "white" ,width = 5, bd = 3, padx = 10, pady = 10, font= ("Times",15, "bold"), command = lambda:Botao(but4))
but4.grid(row = 4, column = 0)

but5 = Button(i, text = "5",bg = "#19193C", fg = "white" ,width = 5, bd = 3, padx = 10, pady = 10, font= ("Times",15, "bold"), command = lambda:Botao(but5))
but5.grid(row = 4, column = 1)

but6 = Button(i, text="6", bg="#19193C", fg="white", width=5, bd=3, padx = 10, pady = 10, font= ("Times",15, "bold"), command = lambda:Botao(but6))
but6.grid(row=4, column=2)

but7 = Button(i, text="7", bg="#19193C", fg="white", width=5, bd=3, padx = 10, pady = 10, font= ("Times",15, "bold"), command = lambda:Botao(but7))
but7.grid(row=3, column=0)

but8 = Button(i, text="8", bg="#19193C", fg="white", width=5, bd=3, padx = 10, pady = 10, font= ("Times",15, "bold"), command = lambda:Botao(but8))
but8.grid(row=3, column=1)

but9 = Button(i, text="9", bg="#19193C", fg="white", width=5, bd=3, padx = 10, pady = 10, font= ("Times",15, "bold"), command = lambda:Botao(but9))
but9.grid(row=3, column=2)

but0 = Button(i, text="0", bg="#19193C", fg="white", width=5, bd=3, padx=10, pady=10,font=("Times", 15, "bold"), command = lambda:Botao(but0))
but0.grid(row=6, column=0)

butv = Button(i, text=".", bg="#19193C", fg="white", width=5, bd=3, padx=10, pady=10,font=("Times", 15, "bold"), command = lambda:Botao(butv))
butv.grid(row=6, column=1)

buti = Button(i, text="=", bg="#1E90FF", fg="white", width=5, bd=3, padx=10, pady=10,font=("Times", 15, "bold"), command = lambda:Botao(buti))
buti.grid(row=6, column=2)

butdiv = Button(i, text="/", bg="#2F4F4F", fg="white", width=5, bd=3, padx=10, pady=10,font=("Times", 15, "bold"), command = lambda:Botao(butdiv))
butdiv.grid(row=3, column=3)

butvez = Button(i, text="*", bg="#2F4F4F", fg="white", width=5, bd=3, padx=10, pady=10,font=("Times", 15, "bold"), command = lambda:Botao(butvez))
butvez.grid(row=4, column=3)

butme = Button(i, text="-", bg="#2F4F4F", fg="white", width=5, bd=3, padx=10, pady=10,font=("Times", 15, "bold"), command = lambda:Botao(butme))
butme.grid(row=5, column=3)

butma = Button(i, text="+", bg="#2F4F4F", fg="white", width=5, bd=3, padx=10, pady=10,font=("Times", 15, "bold"), command = lambda:Botao(butma))
butma.grid(row=6, column=3)

butexp = Button(i, text="^", bg="#2F4F4F", fg="white", width=5, bd=3, padx=10, pady=10,font=("Times", 15, "bold"), command = lambda:Botao(butexp))
butexp.grid(row=2, column=3)

butC = Button(i, text="C", bg="#4682B4", fg="white", width=5, bd=3, padx=10, pady=10,font=("Times", 15, "bold"), command = lambda:Botao(butC))
butC.grid(row = 2,  columnspan = 2, sticky = W + N + E + S)

butCE = Button(i, text="CE", bg="#4682B4", fg="white", width=5, bd=3, padx=10, pady=10,font=("Times", 15, "bold"), command = lambda:Botao(butCE))
butCE.grid(row=2, column=2)

infistr = ''
k=1
infix = []

def Botao(btn):
    global infistr, infix, k, prioridade, pos

    if btn["text"] == "=":
       if k ==0:
            infix = infistr.split()
            infistr = ''
            calcula_posfixa()
            k +=1
            resul['text'] = calcula_posfixa()
            print(calcula_posfixa())

    elif btn["text"] == "C":
        infistr = ''
        infix = []
        k += 1

    elif btn["text"] == "CE":
        if len(infistr) != 0:
            if infistr[-1] == ' ' :
                pass
            else:
                infistr = infistr[:len(infistr)-1]
                if len(infistr) == 0:
                    k += 1
    elif btn["text"] == ".":
        if k == 0:
            infistr += btn["text"]
            k += 1
    elif btn["text"] in ['*', '+', '-', '/', '^']:
        if k == 0:
            infistr = infistr + ' ' + btn["text"] + ' '
            k += 1
    else:
        infistr += btn["text"]
        k = 0
    print(infistr)
    display['text'] = infistr



#Programa para Calcular Posfixa

def calcula_posfixa():
    pilha = []
    posfix = []
    prioridade = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operacao = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y,
                '^': lambda x, y: x ** y}
    for b in infix:

        if b in ['*', '+', '-', '/', '^']:
            while True:

                if not pilha:
                    pilha.append(b)
                    break

                if prioridade[b] <= prioridade[pilha[-1]]:
                    posfix.append(pilha.pop())

                else:
                    pilha.append(b)
                    break

        else:
            posfix.append(b)

    while len(pilha) != 0:
        posfix.append(pilha.pop())


    resultado = []

    for b in posfix:
        if b in ['*', '+', '-', '/', '^']:
            op2 = pilha.pop()
            op1 = pilha.pop()

            if b == '/':
                if op2 == 0:
                    resul['text'] = "ERRO DIV POR 0"
                else:
                    resultado = operacao[b](op1, op2)
                    pilha.append(resultado)
            else:
                resultado = operacao[b](op1, op2)
                pilha.append(resultado)

        else:
            pilha.append(float(b))
    return resultado
    del infix[:]

i.grid()

i.title("Calculadora")

i.resizable(width = False, height = False)

i.mainloop()


