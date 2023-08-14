import tkinter as tk
import pywintypes
import win32con
import win32api

root = tk.Tk()
height = root.winfo_screenheight()

devmode = pywintypes.DEVMODEType()

if height == 1080:
    devmode.PelsWidth = 2560
    devmode.PelsHeight =1440
if height == 1440:
    devmode.PelsWidth = 1920
    devmode.PelsHeight = 1080

devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

win32api.ChangeDisplaySettings(devmode, 0)
