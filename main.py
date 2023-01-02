import statistics
from tkinter import*
import math
import random
import math
import tkinter as tk
from PIL import Image, ImageTk
import time

# Instructions and import data
print("Create a text file called file1.txt and place in the folder for this program. Enter values to be analyzed each on a separate line")
user_file = open('file1.txt')  # open
input_list = user_file.readlines()  # read file lines into list
newlist = []
intlist = []
for i in input_list:
    newlist.append(i.strip('\n'))


# GUI window defined
#colors
back = "#022126"
box= "#0C2D48"
neon= "#65FC6A"
purple= "#278ED5"

window = Tk(className= "Statistics Calculator")
window.configure(bg= back, padx=30, pady=30)
for i in newlist:
    intlist.append(int(i))
print("Your values were entered as:", intlist)


def calc():
    n = len(intlist)
    mean = sum(intlist) / n
    pv = statistics.pvariance(intlist)
    sd = statistics.stdev(intlist)

    # display calculated values to ui
    t1.delete("1.0", END)
    t1.insert(END, mean)
    t2.delete("1.0", END)
    t2.insert(END, sd)
    t3.delete("1.0", END)
    t3.insert(END, pv)
    s3.delete("1.0", END)
    s3.insert(END, n)

# Statistics
l1= Label(window, bg= back,  fg=purple, text='Statistics',font='Helvetica 11 bold')
# Label Coefficient, x, power
r1 = Label(window, bg= back,  fg=neon, text='Mean')
r2 = Label(window, bg= back,  fg=neon, text='Standard Deviation')
r3 = Label(window, bg= back,  fg=neon, text='Population Variance')
# Widget to display Calculated derivative values
t1 = Text(window, bg= neon,  fg=box, height=1, width=20)
t2 = Text(window, bg= neon,  fg=box, height=1, width=20)
t3 = Text(window, bg= neon,  fg=box, height=1, width=20)
# Space between Calcs
s0 = Label(window, bg= back,  fg=neon, text='')
s1 = Label(window, bg= back,  fg=neon, text='')
s2 = Label(window, bg= back,  fg=neon, text='Based on a population size of:', anchor="center")
s3 = Text(window, bg= neon,  fg=back, height=1, width=20)
s4 = Label(window, bg= back,  fg=neon, text='')


# Button Widgets Calculate
b1 = Button(window,bg= neon,  fg=back, text="Calculate", command=calc)
# TODO: Create launch new window
b3 = Button(window, bg= neon,  fg=back, text="Launch", )

# Grid
# Row 0: Label Statistics
l1.grid(row=0, column=1)
# Row 3: Label mean, x, power
r1.grid(row=3, column=0)
r2.grid(row=3, column=1)
r3.grid(row=3, column=2)
# Row 4: Widget to display Calculated stats
t1.grid(row=4, column=0)
t2.grid(row=4, column=1)
t3.grid(row=4, column=2)
# Add Spacing
s0.grid(row=5, column= 1)
# Calculate Derivative button
b1.grid(row=6, column=1)
s1.grid(row=7, column=1)
# Add Spacing
s2.grid(row=15, column=1)
s3.grid(row=16, column=1)
s4.grid(row=17, column=1)
# Launch Button
b3.grid(row=18, column=1)

# Start the GUI
window.mainloop()