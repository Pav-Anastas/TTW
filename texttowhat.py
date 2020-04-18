from tkinter import*
import random

# Creating the Window
root = Tk()
root.title("TexttoWhat")


# Creating and adding the Entry log to the grid
e = Entry(root, width=35)
e.grid(row=0, column=0, columnspan=3)



# Saving output to text file command
def saveClick(newstring):
    f = open("output.txt", "w")
    print(newstring, file=f)
    f.close()

# subClick is the first command that gets triggered creating the input and output variables
def subClick():
    intext = e.get()
    newstring = ""
    e.delete(0, END)


# Check for the string conditions
    if not intext.isalpha() and not' ' in intext:
        label = Label(root, text= "Your text contains invalid Characters. (ex. 1, @, _, %)")
        label.grid(row=2, column=0, columnspan=3)
        label.after(3000, label.destroy)
    else:
        # The loop that randomly changes letter Caps
        for a in intext:
            random_bit = random.getrandbits(1)
            if random_bit == 1:
                newstring += (a.lower())
            else:
                newstring += (a.upper())
        # Printing a Label output
        label = Label(root, text=newstring)
        label.grid(row=2, column=0, columnspan=3)
        # Creating save to text Button.
        saveButton = Button(root,text="Save to .text", command=lambda: saveClick(newstring))
        saveButton.grid(row=3, column=1)




# Creating and adding to the grid the submit button
subButton = Button(root, text="Submit", command= subClick)
subButton.grid(row=1, column=1)



root.mainloop()