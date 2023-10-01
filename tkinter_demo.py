from tkinter import ttk, Tk, PhotoImage

root = Tk()
#root.mainloop()
# mainloop() is an infinite loop used to run the application, wait for an event to occur 
# and process the event as long as the window is not closed.

# Using labels:
ttk.Label(root, text="This is a demo label").pack() 
#root.mainloop() -- if you run this this you will see the label in the window.

ttk.Label(root, text="This is the second demo label").pack()


# By creating object:
label1=ttk.Label(text='Demo Label by creating an object') # create a new instance 
label1.pack()
#root.mainloop()

# Using buttons:
# First define a function:

def trigger_func():
    print("You clicked!!")

ttk.Button(root, text="Click me!", command = trigger_func).pack()
#root.mainloop()

# Adding an image as a label:

logo = PhotoImage(file="python_logo.gif")
ttk.Label(root, image=logo).pack()
#root.mainloop()

# Frames -- A frame in Tk lets you organize and group widgets. 
# It works like a container. Its a rectangular area in which widges can be placed.

frame_header = ttk.Frame(root)
frame_header.pack()
ttk.Label(frame_header, text="Label inside a frame").pack()
root.mainloop()
