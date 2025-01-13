import tkinter as tk
from tkinter import colorchooser

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ZaziPaint")

        # Set up the canvas
        self.canvas = tk.Canvas(root, width=600, height=400, bg="white")
        self.canvas.pack()

        # Set up drawing variables
        self.last_x = None
        self.last_y = None
        self.color = "black"
        self.eraser_mode = False  # Initially, it's in drawing mode

        # Bind mouse events to canvas
        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<ButtonRelease-1>", self.reset)

        # Add buttons for color change and eraser
        self.color_button = tk.Button(root, text="Change Color", command=self.change_color)
        self.color_button.pack(side=tk.LEFT, padx=10)

        self.eraser_button = tk.Button(root, text="Eraser", command=self.toggle_eraser)
        self.eraser_button.pack(side=tk.LEFT)

    def paint(self, event):
        """Function to draw or erase on the canvas."""
        x, y = event.x, event.y
        if self.last_x and self.last_y:
            if self.eraser_mode:
                # Eraser mode: Draw white lines to "erase" content
                self.canvas.create_line(self.last_x, self.last_y, x, y, width=20, fill="white", capstyle=tk.ROUND, smooth=tk.TRUE)
            else:
                # Drawing mode: Draw lines with the selected color
                self.canvas.create_line(self.last_x, self.last_y, x, y, width=2, fill=self.color, capstyle=tk.ROUND, smooth=tk.TRUE)
        self.last_x = x
        self.last_y = y

    def reset(self, event):
        """Reset the last x and y coordinates when the mouse button is released."""
        self.last_x = None
        self.last_y = None

    def change_color(self):
        """Change the drawing color."""
        color = colorchooser.askcolor()[1]
        if color:
            self.color = color

    def toggle_eraser(self):
        """Toggle between drawing and erasing modes."""
        self.eraser_mode = not self.eraser_mode
        if self.eraser_mode:
            self.eraser_button.config(bg="gray")  # Change button color when eraser is active
        else:
            self.eraser_button.config(bg="SystemButtonFace")  # Reset button color when eraser is off

# Set up the main window
root = tk.Tk()
app = DrawingApp(root)

# Start the main event loop
root.mainloop()
