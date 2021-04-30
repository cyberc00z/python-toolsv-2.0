# pinging servers in python

from pythonping import ping

ping('0.0.0.0',verbose=True,count=1000, timeout=50)


#from tkinter import *
#from pythonping import ping

#def get_ping():
 #   response = ping(e.get(), verbose=True, count=30, timeout=5, df=True )
   #  res.set(response)

   #let's tkinter

   #master = Tk()
   #master.configure(bg='light grey')

   # variable class in tkinter
   #res = StringVar()

   #creating label for each information
   #name using widget Label

   #Label(master, text="Enter the target's URL or IP : ", bg='white').grid(row=0,sticky=W)
   #Label(master, text="", textvariable=res, bg="light grey").grid(row=1,column=1,sticky= W)

   #e = Entry(master)
   #e.grid(row=0, column=1)

   #creating a button using the widget
   #button that will call the submit function
   #b = Button(master, text="Show", command=get_ping)
   #b.grid(row=0,column=2,columnspan=2, rowspan=2,padx=5,pady=5)

   #mainloop()



