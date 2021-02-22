'''
Here, graphical user interface is used by python-tkinter
'''


from tkinter import *
# root=Tk()

# First you need to create a label widget

#mylabel=Label(root,text="Hello World!")

# Showing onto the screen
#mylabel.pack()

# Main loop of the program
#root.mainloop()



# Positioning with Tkinter's sytem

'''
If you want to position your labels you need to use grid function instead of pack function! 
'''

#root=Tk()

# First you need to create a label widget

#mylabel=Label(root,text="Hello World!")
#mylabel2=Label(root,text="My name is Ali!")

# Showing onto the screen
#mylabel.grid(row=0,column=0)
#mylabel2.grid(row=1,column=0)

# Main loop of the program
#root.mainloop()



# LECTURE 3

# Creating Buttons!
#root=Tk()
'''
To make this button, to do something, you need to create a function, then tell the Button function
to execute it, using command variable 
'''
#def add():
 #   x=5
  #  y=6
   # mylabel=Label(root,text="The result= {}".format(x+y))
    #mylabel.pack()

#  Create  a Button
'''
You can change the button font ground color or back ground color!
bg, or fg

'''
#myButton=Button(root,text="Click Me!",padx=10,pady=5,fg="yellow",bg="red",command=add) # To change the size of the button, you can use padx and pady

#Let's pack it

#myButton.pack()
# Main loop of the program
#root.mainloop()


# LECTURE 4 / CREATE INPUT BOXES

root=Tk()

'''
To create an entery widget, you need to use Entery widget!
'''
e= Entry(root,width=30,bg="green",fg="white",borderwidth=2) # Change entery widget's size= width, you can also change colors and border width
e.pack()

# To get user input, you need to get it with "get" function
'''
If you want to add some text in your entery widget, you need to use insert function.
'''

e.insert(0,"Enter your name man: ")



def add():
    x=5
    y=6
    mylabel=Label(root,text="The result= {}".format(e.get()))
    mylabel.pack()

#  Create  a Button
'''
You can change the button font ground color or back ground color!
bg, or fg

'''
myButton=Button(root,text="Click Me!",padx=10,pady=5,fg="yellow",bg="red",command=add) # To change the size of the button, you can use padx and pady

#Let's pack it

myButton.pack()
# Main loop of the program
root.mainloop()


print(float('2.0'))