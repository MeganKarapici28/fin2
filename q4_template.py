# -*- coding: utf-8 -*-

# Enter your candidate ID here: AF23176
# Enter your student ID here: 21210302
# Do NOT enter your name 

import breezypythongui as bpg
from tkinter.filedialog import askopenfilename, asksaveasfilename

class TextEditor(bpg.EasyFrame):
   

    def __init__(self):
        
        bpg.EasyFrame.__init__(self, title="Text Editor", width=700, height=700) #initialize the EasyFrame GUI with title and size
        self.addLabel("Text Editor", 0, 0, columnspan=2)

        self.textArea = self.addTextArea("", 1, 0, columnspan=2, width=60, height=20) #adds a text area where the user input or edit text

        self.addButton("Open", 2, 1, command=self.openFile) #Button to open a file
        self.addButton("Save", 2, 2, command=self.saveFile) #Button to save the current file
        self.addButton("New", 2, 0, command=self.newFile) #Button to create a new file

    def openFile(self):        
        filePath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filePath:
            with open(filePath, "r") as file:
                content = file.read()
            self.textArea.setText(content)  #opens file using file dialog, reads it and gives content in text area of GUI

    def saveFile(self):        
        filePath = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if filePath:
            with open(filePath, "w") as file:
                file.write(self.textArea.getText()) #saves the current text to a file

    def newFile(self):        
        self.textArea.setText("")

def main():    
   #main function runs the TextEditor application
    TextEditor().mainloop()

if __name__ == "__main__":
    main()
