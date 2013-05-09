"""
SimpleGUI is the graphics module for CodeSkulptor, the in-browser Python 
developed by Scott Rixner of Rice university for the course, "Introduction to Interactive 
Programming in Python", that is now being offered on Coursera. 

This module is a wrapper that allows SimpleGUI programs to be run outside of
CodeSkulptor using the Tkinter module, which comes standard with Python. This version of the
module requires Python 2.7. Much of the function documentation is from http:/www.codeskulptor.org.

author: Shang-Lin Chen
created: May 5, 2013 
"""


import Tkinter

class Frame:
    """
    A SimpleGUI frame.
    """
    def __init__(self, root, canvas_width, canvas_height, control_width):
        """
        Constructor. Creates a Tkinter Frame with a canvas and an area for controls
        """
        #print root.geometry()
        self.tk_frame = Tkinter.Frame(root, width = canvas_width + control_width, height = canvas_height)
        self.tk_frame.grid()
        
        # Current row in the controls section.
        self.control_row = 0
        
        self.canvas = Tkinter.Canvas(root, width = canvas_width, height = canvas_height, bg = "black")
        self.canvas.grid(row = 0, column = 1)
        
    def set_canvas_background(color):
        pass
    def start(self):
        Tkinter.mainloop()
    def get_canvas_textwidth(self):
        pass
   
    def add_label(self, text):
        """ Adds a text label to the control panel. The label can be changed. """
        pass
    def add_button(self, text, button_handler, width):
        """ 
        Adds a button to the control panel with the given text label. The width of the button 
        defaults to the width of the given text, but can be specified in pixels. If the provided 
        width is less than that of the text, the text overflows the button. The label can be 
        changed. 
        """
        button = Tkinter.Button(self.tk_frame, text = text, width = width, command = button_handler)  
        button.grid(row = self.control_row, column = 0)
        self.control_row += 1
        
    def add_input(self, text, input_handler, width):
        """
        Adds a text input field to the control panel with the given text label. The input 
        field has the given width in pixels. The label can be changed.
        """
        pass
    def set_keydown_handler(self, key_handler):
        pass
    def set_keyup_handler(self, key_handler):
        pass
    def set_mouseclick_handler(self, mouse_handler):
        pass
    def set_mousedrag_handler(self, mouse_handler):
        pass
        
def create_frame(title, canvas_width, canvas_height, control_width = 200):
    """
    Creates a new frame for interactive programs. The frame has the given title, a string. 
    It contains a control panel with the optionally-specified width and the same height as the
    canvas. It contains a canvas of the specified dimensions.
    """
    root = Tkinter.Tk()
    if title is not None:
        root.wm_title(title)
    geometry = str(canvas_width) + "x" + str(canvas_height) + "+0+0"
    #print geometry
    root.geometry(geometry)
    #print root.geometry()
    #print canvas_width, canvas_height, control_width
    frame = Frame(root, canvas_width, canvas_height, control_width)
    
    print root.geometry()
    return frame
    
if __name__ == "__main__":
    frame = create_frame("Test", 300, 200)
    frame.start()
    