from Tkinter import *
root = Tk()

drawpad = Canvas(root, width=800,height=600, background='white')
opponent = drawpad.create_rectangle(490,580,410,600, fill="red")
player = drawpad.create_rectangle(390,580,410,600, fill="blue")

# Create your "enemies" here, before the class


class MyApp:
	def __init__(self, parent):
       	    global drawpad
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.up = Button(self.myContainer1)
       	    self.up.configure(text="up", background= "green")
       	    self.up.grid(row=0,column=0)
       	    # Bind an event to the first button
       	    self.up.bind("<Button-1>", self.upClicked)
       	    
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.down = Button(self.myContainer1)
       	    self.down.configure(text="Down", background= "Blue")
       	    self.down.grid(row=0,column=1)
       	    # Bind an event to the first button
       	    self.down.bind("<Button-1>", self.downClicked)
       	    
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.right = Button(self.myContainer1)
       	    self.right.configure(text="right", background= "Red")
       	    self.right.grid(row=0,column=1)
       	    # Bind an event to the first button
       	    self.right.bind("<Button-1>", self.rightClicked)
       	    
       	    self.myParent = parent  
       	    self.myContainer1 = Frame(parent)
       	    self.myContainer1.pack()
       	    self.left = Button(self.myContainer1)
       	    self.left.configure(text="left", background= "purple")
       	    self.left.grid(row=0,column=1)
       	    # Bind an event to the first button
       	    self.left.bind("<Button-1>", self.leftClicked)
       	    
       	    # No need to edit this - just includes the drawpad into our frame
       	    drawpad.pack(side=BOTTOM)
	
	def animate(self):
	    global drawpad
	    global player
	    # Remember to include your "enemies" with "global"
	    	
		
	def upClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,-20)

        def downClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,0,20)
	 
        def rightClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,20,0)
	
	def leftClicked(self, event):   
	   global oval
	   global player
	   drawpad.move(player,-20,0)
		
		
app = MyApp(root)
root.mainloop()
