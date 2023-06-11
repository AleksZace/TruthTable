import tkinter

def logicCircuit(numberOfInputs):
    characterSet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rowNum = numberOfInputs**2
    columnNum = numberOfInputs
    m = tkinter.Tk()
    m.title("Logic Circuit")
    for x in range(numberOfInputs):
        label2 = tkinter.Label(text=characterSet[x])
        label2.grid(row=0, column=x)

    for i in range(2**numberOfInputs):
        binary = bin(i)[2:].zfill(numberOfInputs)
        print(bin(i))
        print(binary)
        for j in range(columnNum):
            label = tkinter.Label(text=binary[j])
            label.grid(column=j, row=i+1)

    m.mainloop()

logicCircuit(5)
