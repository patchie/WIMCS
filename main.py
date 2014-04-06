#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx           #Imports the wx library for gui interface
import main_gui     #Imports the python file with the gui
import wmi          #Imports the python Windows Management Instrumentation library

#---------------------------------------------------------------
#| MISC                                                        |
#---------------------------------------------------------------
def prettify_kb(kbytes):              #Convert bytes to the correct unit
    kbytes = float(kbytes)
    if kbytes >= 1073741824:
        size = '%.1fTiB' % (kbytes / 1073741824)
    elif kbytes >= 1048576:
        size = '%.1fGiB' % (kbytes / 1048576)
    elif kbytes >= 1024:
        size = '%.1fMiB' % (kbytes / 1024)
    else:
        size = '%.1fKiB' % kbytes
    return size

#---------------------------------------------------------------
#| GUI STUFF                                                   |
#---------------------------------------------------------------
class Main_gui_window(main_gui.MainFrame):
    def __init__(self, parent):
        main_gui.MainFrame.__init__(self,parent)

    def Menu_Refresh(self, event):
        WIMCS.SetTitle("test22222222")
        WIMCS.SetStatusText("hehehe22222222222")
        Computer_Scan()


#---------------------------------------------------------------
#| Starting the scan                                           |
#---------------------------------------------------------------
def Computer_Scan():
    c = wmi.WMI()   #Running scan on local computer
    
    for os in c.Win32_OperatingSystem():
        for disk in c.Win32_LogicalDisk(["FreeSpace", "Size", "DriveType"], DriveType=3, DeviceID=os.SystemDrive):
            HdTotalValue = prettify_kb(float(disk.Size)/1024)                               #The disk.Size value comes in bytes, converts to kb before sending 
            HdFreeValue = prettify_kb(float(disk.Freespace)/1024)                           #The disk.Freespace value comes in bytes, converts to kb before sending
            HdUsedValue = prettify_kb(float(disk.Size)/1024 - float(disk.Freespace)/1024)   #The disk.Size value comes in bytes, converts to kb before sending
        MemoryPhysicalValue = prettify_kb(os.TotalVisibleMemorySize)                        #Memory cards installed (visible for the OS)
        MemoryVirtualValue = prettify_kb(os.SizeStoredInPagingFiles)
        MemoryTotalValue = prettify_kb(float(os.SizeStoredInPagingFiles) + float(os.TotalVisibleMemorySize))    #Total cards and swap(HDD)
        MemoryTotalfreeValue = prettify_kb(float(os.FreePhysicalMemory) + float(os.FreeSpaceInPagingFiles))     #Total free memory in cards and swap(HDD)
        MemoryTotalusedValue = prettify_kb((float(os.SizeStoredInPagingFiles) + float(os.TotalVisibleMemorySize)) - (float(os.FreePhysicalMemory) + float(os.FreeSpaceInPagingFiles)))

        #Checking if you use more swap memory then you have free physical memory. This can cause a slow computer.
        swapusedkb = float(os.SizeStoredInPagingFiles) - float(os.FreeSpaceInPagingFiles)
            #print "swapusedkb: ", prettify_kb(float(os.SizeStoredInPagingFiles) - float(os.FreeSpaceInPagingFiles))
        ramfreekb = float(os.FreePhysicalMemory) * 2
            #print "freeramkb*2: ", prettify_kb(float(os.FreePhysicalMemory) * 2)
        ramtotalkb = float(os.TotalVisibleMemorySize)
            #print "ramtotalkb: ", prettify_kb(float(os.TotalVisibleMemorySize))
        if ((swapusedkb > (ramfreekb*2)) and (swapusedkb > (ramtotalkb/100))):
            print "hehe"
        wx.MessageBox('You use more swap memory then free physical memory.\nThis can cause a slow computer.\n\nYou can solve this problem by closing programs and releasing more memory.', 'Swap memory error!', wx.OK | wx.ICON_ERROR)



    WIMCS.m_staticText_HdTotalValue.SetLabel(HdTotalValue)  #m_staticText_HdTotalValue
    WIMCS.m_staticText_HdFreeValue.SetLabel(HdFreeValue)    #m_staticText_HdFreeValue
    WIMCS.m_staticText_HdUsedValue.SetLabel(HdUsedValue)    #m_staticText_HdUsedValue
    #WIMCS.m_staticText_HdFragmentedValue.SetLabel()    #m_staticText_HdFragmentedValue
    WIMCS.m_staticText_MemoryPhysicalValue.SetLabel(MemoryPhysicalValue)    #m_staticText_MemoryPhysicalValue
    WIMCS.m_staticText_MemoryVirtualValue.SetLabel(MemoryVirtualValue)    #m_staticText_MemoryVirtualValue
    WIMCS.m_staticText_MemoryTotalValue.SetLabel(MemoryTotalValue)    #m_staticText_MemoryTotalValue
    WIMCS.m_staticText_MemoryTotalfreeValue.SetLabel(MemoryTotalfreeValue)    #m_staticText_MemoryTotalfreeValue
    WIMCS.m_staticText_MemoryTotalusedValue.SetLabel(MemoryTotalusedValue)    #m_staticText_MemoryTotalusedValue
    #WIMCS.m_staticText_CPUTypeValue.SetLabel()    #m_staticText_CPUTypeValue
    #WIMCS.m_staticText_CPUSpeedValue.SetLabel()    #m_staticText_CPUSpeedValue
    #WIMCS.m_staticText_CPULoadValue.SetLabel()    #m_staticText_CPULoadValue
    #WIMCS.m_staticText_CPUTempValue.SetLabel()    #m_staticText_CPUTempValue

        
    



#---------------------------------------------------------------
#| Initialize                                                  |
#---------------------------------------------------------------
if __name__ == '__main__':
    app = wx.App()
    WIMCS = Main_gui_window(None)
    WIMCS.SetTitle("WIMCS v0.01 Alpha")
    WIMCS.SetStatusText("Scanning computer...")
    WIMCS.Show()                    #Shows the window
    app.MainLoop()                  #Starts the application loop

