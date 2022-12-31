from tkinter import *
import socket
from pythonping import ping


# f=open("Diabetes.txt",'r')
# f.read()
def click():
    # Getting the text info as an int() & Error handling
    try:
        text_info_1 = str(text1.get())
    except Exception as e:
        text1.delete(0, END)
        text3.delete(0, END)
        text3.insert(0, f'Error: {e}')
        return
    # actual part of the func
    text3.delete(0, END)
    text3.insert(0, text_info_1)
    text_info_1 = str(text1.get())

    f=open(text_info_1,'r')
    fileData=f.read()
    fileData=fileData.replace(" ", "")
    IPline='LabeledRecCfg_override.agentsIPs",'
    print(fileData)
    if IPline in fileData:
        print('string exist')
        print(fileData.find(IPline)+44)
        print(fileData[fileData.find(IPline)+44])
    else:
        print('string does not exist')
    f.close()


hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

# ping('192.168.0.115', verbose=True)
# print(local_ip)
# def click func


# Gui Config
root = Tk()
root.geometry('500x400')
root.title('Window')

# The actual gui
label1 = Label(root, text='Enter path for ui_params!')
label1.pack()

spacing1 = Label(root)
spacing1.pack()

text1 = Entry(root)
text1.pack(ipadx=20)

spacing2 = Label(root, text='+')
spacing2.pack()

button = Button(root, text='Click me!', command=click)
button.pack()

spacing4 = Label(root)
spacing4.pack()

text3 = Entry(root)
text3.pack(ipadx=60)

# Making the gui run
root.mainloop()
