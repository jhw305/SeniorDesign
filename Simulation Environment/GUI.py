#This program displays the locations of each anchor and node as has the following
#options for interaction:
#   Run (speed)
#   Step
#   Quit
#   Run until (time)
#   Display statistics (node)
#   Add node
#   Remove node
#   Save
#   Load

import tkinter as tk
import time

running = False
timeUnit = 1000

def Run():
    #Pauses the run if it is running
    global running
    if (running):
        running = False
        #Reenables step button, resets run button's text
        stepButton['state'] = 'normal'
        runButton['text'] = 'Run'
        print("Run paused")
        return
    #Verifies both 'Delay' and 'Break at' entries have legal values
    runDelay = delayEntry.get()
    if (runDelay.isdigit() == False):
        print("Invalid argument: Delay contains non-numerical values")
        return
    runDelay = int(runDelay)
    breakPoint = breakEntry.get()
    if (breakPoint.isdigit() == False):
        print("Invalid argument: Breakpoint contains non-numerical values")
        return
    breakPoint = int(breakPoint)
    timeVal = int(timeValue.get())
    #Adjusts visual of the run button and disables step button
    runButton['text'] = 'Pause'
    stepButton['state'] = 'disabled'
    #Runs simulation according to specified inputs
    running = True
    if (breakPoint <= timeVal):
        if (runDelay == 0):
            print("Running at no delay")
            while (running):
                Update()
                root.update()
        else:
            print("Running at delay %s" % (runDelay))
            while (running):
                Update()
                for value in range(0, runDelay):
                    time.sleep(1/timeUnit)
                    root.update()
    else:
        if (runDelay == 0):
            print("Running at no delay until time %s" % (breakPoint))
            while (running and int(timeValue.get()) < breakPoint):
                Update()
                root.update()
        else:
            print("Running at delay %s until time %s" % (runDelay, breakPoint))
            while (running and int(timeValue.get()) < breakPoint):
                Update()
                for value in range(0, runDelay):
                    time.sleep(1/timeUnit)
                    root.update()
        stepButton['state'] = 'normal'
        runButton['text'] = 'Run'
        running = False

def Step():
    Update()

def Display():
    print("Display Statistics")

def Add():
    print("Add node")

def Remove():
    print("Removing node")

def Save():
    print("Saving")

def Load():
    print("Loading")

def Quit():
    print("Quitting")
    quit()

def Update():
    #Called temporarily instead of SimulationEnvironment.Update()
    timeValue.set(timeValue.get() + 1)

def Initialize():
    global running
    running = False
    timeValue.set("0")
    #delete nodelist, anchorlist
    #new simulationEnvironment loading values from path
    
root = tk.Tk()
breakValue = tk.IntVar()
delayValue = tk.IntVar()
timeValue = tk.IntVar()

quitButton = tk.Button(root, 
                   text="QUIT", 
                   fg="red",
                   command=Quit)
runButton = tk.Button(root,
                   text="Run",
                   command=Run)
stepButton = tk.Button(root,
                   text="Step",
                   command=Step)
displayButton = tk.Button(root,
                   text="Display",
                   command=Display)
addButton = tk.Button(root,
                   text="Add",
                   command=Add)
removeButton = tk.Button(root,
                   text="Remove",
                   command=Remove)
saveButton = tk.Button(root,
                   text="Save",
                   command=Save)
loadButton = tk.Button(root,
                   text="Load",
                   command=Load)
delayLabel = tk.Label(root,
                      text="Delay:")
delayEntry = tk.Entry(root,
                      width = 0,
                      textvariable = delayValue)
breakLabel = tk.Label(root,
                      text="Break at:")
breakEntry = tk.Entry(root,
                      width = 0,
                      textvariable = breakValue)
timeLabel = tk.Label(root,
                     text="Time:")
timeEntry = tk.Label(root,
                     textvariable = timeValue)
                     
row = col = 0
timeLabel.grid(row=row, column=col, sticky="new")
timeEntry.grid(row=row, column=col+1, sticky="new")
row += 1
delayLabel.grid(row=row, column=col, sticky="new")
delayEntry.grid(row=row, column=col+1, sticky="new")
row += 1
breakLabel.grid(row=row, column=col, sticky="new")
breakEntry.grid(row=row, column=col+1, sticky="new")
row += 1
runButton.grid(row=row, column=col, sticky="new")
stepButton.grid(row=row, column=col+1,sticky="new")
row += 1
addButton.grid(row=row, column=col, sticky="new")
removeButton.grid(row=row, column=col+1, sticky="new")
row += 1
saveButton.grid(row=row, column=col, sticky="new")
loadButton.grid(row=row, column=col+1, sticky="new")
row += 1
displayButton.grid(row=row, column=col, sticky="new")
quitButton.grid(row=row, column=col+1, sticky="new")

root.grid_rowconfigure(10, weight=1)
root.grid_columnconfigure(10, weight=1)

root.mainloop()
