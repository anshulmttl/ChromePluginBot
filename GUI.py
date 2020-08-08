 # @author Anshul Mittal
 # @email anshulmttl@gmail.com
 # @create date 2020-08-05 18:48:09
 # @modify date 2020-08-05 18:48:09
 # @desc [description]
import tkinter

class GUI:
    def __init__(self, master):
        print("GUI")
        self.content = tkinter.StringVar()
        self.CreateUI(master)

    def CreateUI(self,window):
        window.title("Execute Multiple")
        window.minsize(350,250)

        labelNumberRetries = tkinter.Label(window, text="NumberRefreshes").grid(row=1,column=0,padx=(5,5))
        entryNumberRetries = tkinter.Entry(window, bd=5, textvariable=self.content).grid(row=1, column=1,sticky="EW",padx=(5,5))
        btnOpenBrowser = tkinter.Button(window, text="Open Browser", command=self._OpenBrowser).grid(row=0,column=0,sticky="EWNS",padx=(5,5))
        btnCloseSession = tkinter.Button(window, text="Close Browser", command=self._CloseBrowser).grid(row=0,column=1,sticky="EWNS",padx=(5,5))
        btnSetRetries = tkinter.Button(window, text="Set Refreshes", command=self._SetNumberRetries).grid(row=2, column=1,sticky="EWNS",padx=(5,5))
        btnConnectBrowser = tkinter.Button(window, text="Connect Browser", command=self._ConnectBrowser).grid(row=2, column=0,sticky="EWNS",padx=(5,5))
        window.columnconfigure(0,weight=1)
        window.columnconfigure(1, weight=1)
        window.rowconfigure(0,weight=1)
        window.rowconfigure(1,weight=1)
        window.rowconfigure(2,weight=1)

    def GetNumberRetries(self):
        return self.content.get()
        
    def _ConnectBrowser(self):
        self.CallbackConnectBrowser()

    def _OpenBrowser(self):
        self.callbackBrowser()

    def _CloseBrowser(self):
        self.callbackCloseBrowser()

    def _SetNumberRetries(self):
        self.callbackSetNumberRetries()

    def SetCallbacks(self, callBrowser, callCloseBrowser, callNumberRetries, callConnectBrowser):
        self.callbackBrowser = callBrowser
        self.callbackCloseBrowser = callCloseBrowser
        self.callbackSetNumberRetries = callNumberRetries
        self.CallbackConnectBrowser = callConnectBrowser
