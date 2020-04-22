from tkinter import *
import tkinter.font as tkFont
import os
from subprocess import Popen, PIPE

# FUNCTIONS
def cmdline(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    return process.communicate()[0]


def verifyStatus():
    k_id = getId()
    st = cmdline("xinput | grep AT | cut -d'[' -f 2 | cut -d' ' -f 1").decode('utf-8').strip()
    if st=="slave":
        status = "ativado"
    elif st=="floating":
        status = "desativado"
    t['text'] = f"O teclado de id={k_id} está {status}"
    
def getId():
    return cmdline("xinput | grep AT | cut -d'=' -f 2 | cut -d'[' -f 1").decode('utf-8').strip()

def powerOff( k_id):
    res = cmdline(f"xinput float {k_id}")
    verifyStatus()

def powerOn(k_id):
    res = cmdline(f"xinput reattach {k_id} 3")
    verifyStatus()
    # print(f"xinput reattach {k_id} 3")

# GUI
root = Tk()
root.title("Keyboard Control")
root.geometry("500x200")

fontStyle = tkFont.Font(family="Verdana", size=20)
t = Label(root, text="", font=fontStyle)

t.pack()
status = verifyStatus()
k_id = getId()

btnActivate = Button(root, text="Ativar teclado", command=(lambda : powerOn(k_id)))
btnActivate.pack(side=LEFT)

btnDeactivate = Button(root, text="Desativar teclado", command=(lambda: powerOff(k_id)))
btnDeactivate.pack(side=RIGHT)

# os.system('echo %s' %(k_id))
# wid = frame.winfo_id()
# os.system('xterm -into %d -geometry 40x20 -sb &' % wid)
# os.system('echo %s' %(k_id))

# os.execl("/home/nymphadora/keyboard.sh", " ")

root.mainloop()
