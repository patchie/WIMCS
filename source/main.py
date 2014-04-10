#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import wx           # Imports the wx library for gui interface
import main_gui     # Imports the python file with the gui
import wmi          # Imports the python Windows Management Instrumentation library

#---------------------------------------------------------------
#| VARIABLES                                                   |
#---------------------------------------------------------------
version = "v0.01 Alpha"

#---------------------------------------------------------------
#| MISC FUNCTIONS                                              |
#---------------------------------------------------------------
def prettify_kb(kbytes):                # Convert bytes to the correct unit

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
class Main_gui_window(main_gui.MainFrame):                                  # MAIN
    def __init__(self, parent):
        main_gui.MainFrame.__init__(self, parent)


    def menu_refresh(self, event):
        #WIMCS.SetTitle("test22222222")
        #WIMCS.SetStatusText("hehehe22222222222")
        computer_scan()

    def menu_exit(self, event):
        close_answer = wx.MessageBox("Quit program?", "Confirm", wx.YES_NO)
        if close_answer == wx.YES:
            self.Close()

    def menu_about(self, parent):
        WIMCS_about = About_Gui_Window(None)
        WIMCS_about.Show()

class About_Gui_Window(main_gui.MyDialog_About):                            # ABOUT
    def __init__(self, parent):
         main_gui.MyDialog_About.__init__(self, parent)

    def About_Ok(self, parent):
        self.Close()

#---------------------------------------------------------------
#| THE SCAN                                                    |
#---------------------------------------------------------------
def computer_scan():
    c = wmi.WMI()   # Retrieving information from VMI
    for os in c.Win32_OperatingSystem():            # Fetching WMI information from the OS
        for disk in c.Win32_LogicalDisk(["FreeSpace", "Size", "DriveType"], DriveType=3, DeviceID=os.SystemDrive):
            HdTotalValue = prettify_kb(float(disk.Size)/1024)                               # The disk.Size value comes in bytes, converts to kb before sending
            WIMCS.m_staticText_HdTotalValue.SetLabel(HdTotalValue)

            HdFreeValue = prettify_kb(float(disk.Freespace)/1024)                           # The disk.Freespace value comes in bytes, converts to kb before sending
            WIMCS.m_staticText_HdFreeValue.SetLabel(HdFreeValue)

            HdUsedValue = prettify_kb(float(disk.Size)/1024 - float(disk.Freespace)/1024)   # The disk.Size value comes in bytes, converts to kb before sending
            WIMCS.m_staticText_HdUsedValue.SetLabel(HdUsedValue)

            #WIMCS.m_staticText_HdFragmentedValue.SetLabel()                                # I need to fix this one. Its only supposed to disk defragment if its a HDD, and not a SSD

        MemoryPhysicalValue = prettify_kb(os.TotalVisibleMemorySize)                        # Memory cards installed (visible for the OS)
        WIMCS.m_staticText_MemoryPhysicalValue.SetLabel(MemoryPhysicalValue)

        MemoryVirtualValue = prettify_kb(os.SizeStoredInPagingFiles)                        # This is the pagefile
        WIMCS.m_staticText_MemoryVirtualValue.SetLabel(MemoryVirtualValue)

        MemoryTotalValue = prettify_kb(float(os.SizeStoredInPagingFiles) + float(os.TotalVisibleMemorySize))    # Total cards and swap(HDD)
        WIMCS.m_staticText_MemoryTotalValue.SetLabel(MemoryTotalValue)

        MemoryTotalFreeValue = prettify_kb(float(os.FreePhysicalMemory) + float(os.FreeSpaceInPagingFiles))     # Total free memory in cards and swap(HDD)
        WIMCS.m_staticText_MemoryTotalFreeValue.SetLabel(MemoryTotalFreeValue)

        MemoryTotalUsedValue = prettify_kb((float(os.SizeStoredInPagingFiles) + float(os.TotalVisibleMemorySize)) - (float(os.FreePhysicalMemory) + float(os.FreeSpaceInPagingFiles)))
        WIMCS.m_staticText_MemoryTotalUsedValue.SetLabel(MemoryTotalUsedValue)

    for Processor in c.Win32_Processor():           # Fetching WMI information from the Processor
        CpuTypeValue = Processor.Name                                                       # Showing the CPU name
        WIMCS.m_staticText_CpuTypeValue.SetLabel(CpuTypeValue)

        CpuSpeedValue = str(Processor.CurrentClockSpeed) + "Mhz"                            # Showing current CPU speed
        WIMCS.m_staticText_CpuSpeedValue.SetLabel(CpuSpeedValue)

        CpuLoadValue = str(Processor.LoadPercentage) + " %"                                 # Showing the current CPU load
        WIMCS.m_staticText_CpuLoadValue.SetLabel(CpuLoadValue)

        #WIMCS.m_staticText_CpuTempValue.SetLabel()    # m_staticText_CPUTempValue

#---------------------------------------------------------------
#| NOTIFICATION SERVICE                                        |
#---------------------------------------------------------------
def notification_service():

        # Checking if you use more swap memory then you have free physical memory. This can cause a slow computer.
        swapusedkb = float(os.SizeStoredInPagingFiles) - float(os.FreeSpaceInPagingFiles)
            #print "swapusedkb: ", prettify_kb(float(os.SizeStoredInPagingFiles) - float(os.FreeSpaceInPagingFiles))
        ramfreekb = float(os.FreePhysicalMemory) * 2
            #print "freeramkb*2: ", prettify_kb(float(os.FreePhysicalMemory) * 2)
        ramtotalkb = float(os.TotalVisibleMemorySize)
            #print "ramtotalkb: ", prettify_kb(float(os.TotalVisibleMemorySize))
        if (swapusedkb > (ramfreekb*2)) and (swapusedkb > (ramtotalkb/100)):
            print "hehe"
        wx.MessageBox('You use more swap memory then free physical memory.\nThis can cause a slow computer.\n\nYou can solve this problem by closing programs and releasing more memory.', 'Swap memory error!', wx.OK | wx.ICON_ERROR)


#---------------------------------------------------------------
#| INITIALIZE                                                  |
#---------------------------------------------------------------
if __name__ == '__main__':
    app = wx.App()
    WIMCS = Main_gui_window(None)
    WIMCS.SetTitle("WIMCS " + version)
    WIMCS.SetStatusText("none..")
    computer_scan()                 # Start the computer scan
    WIMCS.Show()                    # Shows the window
    app.MainLoop()                  # Starts the application loop