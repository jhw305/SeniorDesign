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
from threading import Thread

running = False
timeUnit = 1000

class SimulationGUI():

    def __init__(self):
        global running
        self.root = tk.Tk()
        self.timeValue = tk.IntVar()
        self.timeValue.set(0)
        self.breakValue = tk.IntVar()
        self.delayValue = tk.IntVar()
        self._initializeLayout()
        self.timerThread = TimerThread()
        self.timerThread.start()

    def _run(self):
        global running
        #Pauses the run if it is running
        if(running):
            running = False
            self.timerThread.pause()
            self._update()
            self._swapButtons()
            print("Run paused")
            return
        
        runDelay =   self.delayEntry.get()
        breakPoint = self.breakEntry.get()
        if(not ( self._verifyInput(runDelay, True) ) or not ( self._verifyInput(breakPoint, False) ) ):
            return
        runDelay = int(runDelay)
        breakPoint = int(breakPoint)
        timeVal = int(self.timeValue.get())

        #Starts run 
        #needs to be moved to the appropriate spot
        running = True

        self._swapButtons()
        self.root.update_idletasks()
        print("Running")

        #Runs simulation according to specified inputs
        if (breakPoint <= timeVal):
            if(runDelay == 0):
                self.timerThread.pause()
                print("Running at no delay")
            else:
                print("Running at delay" + str(runDelay))
                while(running):
                    self._update()
                    print(running)
                    for value in range(0, runDelay):
                        time.sleep(1/timeUnit)
                        self.root.update()

   
    def _killThread(self):
        self.timerThread.stop()

    def _quit(self):
        self._killThread()
        print("Quitting")
        self.root.quit()
    
    def _step(self):
        self._update()
        print("Step")
    
    def _display(self):
        print("Display Statistics")
        self.root.update()    

    def _add(self):
        print("Adding node")

    def _remove(self):
        print("Removing node")

    def _save(self):
        print("Saving")

    def _load(self):
        print("Loading")
    
    def _update(self):
        #Called temporarily instead of SimulationEnvironment.Update()
        self.timeValue.set(self.timerThread.time)
        self.root.update_idletasks()

    def _initializeLayout(self):
        self.quitButton = tk.Button(self.root, text="Quit", fg="red", command=self._quit)
        self.runButton = tk.Button(self.root, text="Run", command=self._run)
        self.stepButton = tk.Button(self.root, text="Step", command=self._step)
        self.displayButton = tk.Button(self.root, text="Display", command=self._display)
        self.addButton = tk.Button(self.root, text="Add", command=self._add)
        self.removeButton = tk.Button(self.root, text="Remove", command=self._remove)
        self.saveButton = tk.Button(self.root, text="Save", command=self._save)
        self.loadButton = tk.Button(self.root, text="Load", command=self._load)
        
        self.delayLabel = tk.Label(self.root, text="Delay:")
        self.delayEntry = tk.Entry(self.root, width = 0, textvariable = self.delayValue)
        
        self.breakLabel = tk.Label(self.root, text="Break at:")
        self.breakEntry = tk.Entry(self.root, width = 0, textvariable = self.breakValue)

        self.timeLabel = tk.Label(self.root, text="Time:")
        self.timeEntry = tk.Label(self.root, width = 0, textvariable = self.timeValue)

        row = col = 0
        self.timeLabel.grid(row=row, column=col, sticky="new")
        self.timeEntry.grid(row=row, column=col+1, sticky="new")
        row += 1
        self.delayLabel.grid(row=row, column=col, sticky="new")
        self.delayEntry.grid(row=row, column=col+1, sticky="new")
        row += 1
        self.breakLabel.grid(row=row, column=col, sticky="new")
        self.breakEntry.grid(row=row, column=col+1, sticky="new")
        row += 1
        self.runButton.grid(row=row, column=col, sticky="new")
        self.stepButton.grid(row=row, column=col+1,sticky="new")
        row += 1
        self.addButton.grid(row=row, column=col, sticky="new")
        self.removeButton.grid(row=row, column=col+1, sticky="new")
        row += 1
        self.saveButton.grid(row=row, column=col, sticky="new")
        self.loadButton.grid(row=row, column=col+1, sticky="new")
        row += 1
        self.displayButton.grid(row=row, column=col, sticky="new")
        self.quitButton.grid(row=row, column=col+1, sticky="new")

        self.root.grid_rowconfigure(10, weight=1)
        self.root.grid_columnconfigure(10, weight=1)
            
    #Verifies both 'Delay' and 'Break at' entries have legal values
    def _verifyInput(self, inputValue, delay):
        valid = True
        if (inputValue.isdigit() == False):
            if(delay):
                print("Invalid argument: Delay contains non-numerical values")
            else:
                print("Invalid argument: Breakpoint contains non-numerical values")
            valid = False
        return valid
    
    def _swapButtons(self):
        if(running):
            #Adjusts visual of the run button and disables step button
            self.runButton['text'] = 'Pause'
            self.stepButton['state'] = 'disabled'
        else:
            #Reenables step button, resets run button's text
            self.stepButton['state'] = 'normal'
            self.runButton['text'] = 'Run'


class TimerThread(Thread):

    def __init__(self):
        super(TimerThread, self).__init__()
        self.startThread = True 
        self.pauseThread = True
        self.time = 0

    def run(self):
        while(self.startThread):
            while(not self.pauseThread):
                self.time+=1
                print (self.time)
                if not self.startThread:
                    return
            time.sleep(.1)

    def pause(self):
        if (self.pauseThread):
            self.pauseThread = False
        else:
            self.pauseThread = True
        
    def stop(self):
        self.startThread = False

if __name__ == "__main__":
    app = SimulationGUI()
    app.root.mainloop()



