# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 26 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"WIMCS", pos = wx.DefaultPosition, size = wx.Size( 538,473 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		self.m_menubar = wx.MenuBar( 0 )
		self.m_menu_File = wx.Menu()
		self.m_menuItem_Refresh = wx.MenuItem( self.m_menu_File, wx.ID_ANY, u"Refresh"+ u"\t" + u"F5", u"This option refreshes the data", wx.ITEM_NORMAL )
		self.m_menu_File.AppendItem( self.m_menuItem_Refresh )
		
		self.m_menu_File.AppendSeparator()
		
		self.m_menuItem_Exit = wx.MenuItem( self.m_menu_File, wx.ID_ANY, u"Exit", u"Close application", wx.ITEM_NORMAL )
		self.m_menu_File.AppendItem( self.m_menuItem_Exit )
		
		self.m_menubar.Append( self.m_menu_File, u"File" ) 
		
		self.m_menu_Edit = wx.Menu()
		self.m_menuItem_Preferences = wx.MenuItem( self.m_menu_Edit, wx.ID_ANY, u"Preferences", u"Edit settings for this application", wx.ITEM_NORMAL )
		self.m_menu_Edit.AppendItem( self.m_menuItem_Preferences )
		
		self.m_menubar.Append( self.m_menu_Edit, u"Edit" ) 
		
		self.m_menu_Help = wx.Menu()
		self.m_menuItem_HelpContents = wx.MenuItem( self.m_menu_Help, wx.ID_ANY, u"Help Contents"+ u"\t" + u"F1", u"Read our helpfile", wx.ITEM_NORMAL )
		self.m_menu_Help.AppendItem( self.m_menuItem_HelpContents )
		
		self.m_menu_Help.AppendSeparator()
		
		self.m_menuItem_About = wx.MenuItem( self.m_menu_Help, wx.ID_ANY, u"About", u"Want to know more about us?", wx.ITEM_NORMAL )
		self.m_menu_Help.AppendItem( self.m_menuItem_About )
		
		self.m_menubar.Append( self.m_menu_Help, u"Help" ) 
		
		self.SetMenuBar( self.m_menubar )
		
		self.m_statusBar = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer1 = wx.FlexGridSizer( 4, 1, 0, 0 )
		fgSizer1.AddGrowableCol( 0 )
		fgSizer1.AddGrowableRow( 2 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_staticText_Topic = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Why Is My Computer Slow?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Topic.Wrap( -1 )
		self.m_staticText_Topic.SetFont( wx.Font( 12, 74, 90, 92, False, wx.EmptyString ) )
		
		fgSizer1.Add( self.m_staticText_Topic, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		fgSizer2 = wx.FlexGridSizer( 0, 7, 0, 0 )
		fgSizer2.AddGrowableCol( 0 )
		fgSizer2.AddGrowableRow( 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		sbSizer_HD = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"HD" ), wx.VERTICAL )
		
		gSizer1 = wx.GridSizer( 4, 2, 0, 0 )
		
		self.m_static_HdTotal = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Total :", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_static_HdTotal.Wrap( -1 )
		gSizer1.Add( self.m_static_HdTotal, 0, wx.ALL, 5 )
		
		self.m_staticText_HdTotalValue = wx.StaticText( self.m_panel1, wx.ID_ANY, u"xxx GB", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_HdTotalValue.Wrap( -1 )
		gSizer1.Add( self.m_staticText_HdTotalValue, 0, wx.ALL, 5 )
		
		self.m_staticText_HdFree = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Free:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_HdFree.Wrap( -1 )
		gSizer1.Add( self.m_staticText_HdFree, 0, wx.ALL, 5 )
		
		self.m_staticText_HdFreeValue = wx.StaticText( self.m_panel1, wx.ID_ANY, u"xxx GB", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_HdFreeValue.Wrap( -1 )
		gSizer1.Add( self.m_staticText_HdFreeValue, 0, wx.ALL, 5 )
		
		self.m_staticText_HdUsed = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Used:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_HdUsed.Wrap( -1 )
		gSizer1.Add( self.m_staticText_HdUsed, 0, wx.ALL, 5 )
		
		self.m_staticText_HdUsedValue = wx.StaticText( self.m_panel1, wx.ID_ANY, u"xxx GB", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_HdUsedValue.Wrap( -1 )
		gSizer1.Add( self.m_staticText_HdUsedValue, 0, wx.ALL, 5 )
		
		self.m_staticText_HdFragmented = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Fragmented:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_HdFragmented.Wrap( -1 )
		gSizer1.Add( self.m_staticText_HdFragmented, 0, wx.ALL, 5 )
		
		self.m_staticText_HdFragmentedValue = wx.StaticText( self.m_panel1, wx.ID_ANY, u"xx %", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_HdFragmentedValue.Wrap( -1 )
		gSizer1.Add( self.m_staticText_HdFragmentedValue, 0, wx.ALL, 5 )
		
		
		sbSizer_HD.Add( gSizer1, 1, wx.EXPAND, 5 )
		
		
		fgSizer2.Add( sbSizer_HD, 1, wx.EXPAND, 5 )
		
		sbSizer_Memory = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"Memory" ), wx.VERTICAL )
		
		gSizer2 = wx.GridSizer( 5, 2, 0, 0 )
		
		self.m_staticText_MemoryPhysical = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Physical:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_MemoryPhysical.Wrap( -1 )
		gSizer2.Add( self.m_staticText_MemoryPhysical, 0, wx.ALL, 5 )
		
		self.m_staticText_MemoryPhysicalValue = wx.StaticText( self.m_panel1, wx.ID_ANY, u"xxx GB", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_MemoryPhysicalValue.Wrap( -1 )
		gSizer2.Add( self.m_staticText_MemoryPhysicalValue, 0, wx.ALL, 5 )
		
		self.m_staticText_MemoryVirtual = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Virtual:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_MemoryVirtual.Wrap( -1 )
		gSizer2.Add( self.m_staticText_MemoryVirtual, 0, wx.ALL, 5 )
		
		self.m_staticText_MemoryVirtualValue = wx.StaticText( self.m_panel1, wx.ID_ANY, u"xxx GB", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_MemoryVirtualValue.Wrap( -1 )
		gSizer2.Add( self.m_staticText_MemoryVirtualValue, 0, wx.ALL, 5 )
		
		self.m_staticText_MemoryTotal = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Total:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_MemoryTotal.Wrap( -1 )
		gSizer2.Add( self.m_staticText_MemoryTotal, 0, wx.ALL, 5 )
		
		self.m_staticText_MemoryTotalValue = wx.StaticText( self.m_panel1, wx.ID_ANY, u"xxx GB", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_MemoryTotalValue.Wrap( -1 )
		gSizer2.Add( self.m_staticText_MemoryTotalValue, 0, wx.ALL, 5 )
		
		self.m_staticText_MemoryTotalFree = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Total Free:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_MemoryTotalFree.Wrap( -1 )
		gSizer2.Add( self.m_staticText_MemoryTotalFree, 0, wx.ALL, 5 )
		
		self.m_staticText_MemoryTotalFreeValue = wx.StaticText( self.m_panel1, wx.ID_ANY, u"xxx GB", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_MemoryTotalFreeValue.Wrap( -1 )
		gSizer2.Add( self.m_staticText_MemoryTotalFreeValue, 0, wx.ALL, 5 )
		
		self.m_staticText_MemoryTotalUsed = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Total Used:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_MemoryTotalUsed.Wrap( -1 )
		gSizer2.Add( self.m_staticText_MemoryTotalUsed, 0, wx.ALL, 5 )
		
		self.m_staticText_MemoryTotalUsedValue = wx.StaticText( self.m_panel1, wx.ID_ANY, u"xxx GB", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_MemoryTotalUsedValue.Wrap( -1 )
		gSizer2.Add( self.m_staticText_MemoryTotalUsedValue, 0, wx.ALL, 5 )
		
		
		sbSizer_Memory.Add( gSizer2, 1, wx.EXPAND, 5 )
		
		
		fgSizer2.Add( sbSizer_Memory, 1, wx.EXPAND, 5 )
		
		sbSizer_Cpu = wx.StaticBoxSizer( wx.StaticBox( self.m_panel1, wx.ID_ANY, u"CPU" ), wx.VERTICAL )
		
		gSizer3 = wx.GridSizer( 5, 2, 0, 0 )
		
		self.m_staticText_CpuType = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Type:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_CpuType.Wrap( -1 )
		gSizer3.Add( self.m_staticText_CpuType, 0, wx.ALL, 5 )
		
		self.m_staticText_CpuTypeValue = wx.StaticText( self.m_panel1, wx.ID_ANY, u"xxx", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_CpuTypeValue.Wrap( -1 )
		gSizer3.Add( self.m_staticText_CpuTypeValue, 0, wx.ALL, 5 )
		
		self.m_staticText_CpuSpeed = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Speed:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_CpuSpeed.Wrap( -1 )
		gSizer3.Add( self.m_staticText_CpuSpeed, 0, wx.ALL, 5 )
		
		self.m_staticText_CpuSpeedValue = wx.StaticText( self.m_panel1, wx.ID_ANY, u"xxx ghz", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_CpuSpeedValue.Wrap( -1 )
		gSizer3.Add( self.m_staticText_CpuSpeedValue, 0, wx.ALL, 5 )
		
		self.m_staticText_CpuLoad = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Load:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_CpuLoad.Wrap( -1 )
		gSizer3.Add( self.m_staticText_CpuLoad, 0, wx.ALL, 5 )
		
		self.m_staticText_CpuLoadValue = wx.StaticText( self.m_panel1, wx.ID_ANY, u"xx %", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_CpuLoadValue.Wrap( -1 )
		gSizer3.Add( self.m_staticText_CpuLoadValue, 0, wx.ALL, 5 )
		
		self.m_staticText_CpuTemp = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Temp:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_CpuTemp.Wrap( -1 )
		gSizer3.Add( self.m_staticText_CpuTemp, 0, wx.ALL, 5 )
		
		self.m_staticText_CpuTempValue = wx.StaticText( self.m_panel1, wx.ID_ANY, u"xx C", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_CpuTempValue.Wrap( -1 )
		gSizer3.Add( self.m_staticText_CpuTempValue, 0, wx.ALL, 5 )
		
		
		gSizer3.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		sbSizer_Cpu.Add( gSizer3, 1, wx.EXPAND, 5 )
		
		
		fgSizer2.Add( sbSizer_Cpu, 1, wx.EXPAND, 5 )
		
		
		fgSizer2.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		
		fgSizer1.Add( fgSizer2, 1, 0, 5 )
		
		self.m_notebook1 = wx.Notebook( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel_Status = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook1.AddPage( self.m_panel_Status, u"Status", False )
		self.m_panel_Processes = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer3 = wx.FlexGridSizer( 1, 1, 0, 0 )
		fgSizer3.AddGrowableCol( 0 )
		fgSizer3.AddGrowableRow( 0 )
		fgSizer3.SetFlexibleDirection( wx.BOTH )
		fgSizer3.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_listCtrl_Processes = wx.ListCtrl( self.m_panel_Processes, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.SIMPLE_BORDER )
		fgSizer3.Add( self.m_listCtrl_Processes, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel_Processes.SetSizer( fgSizer3 )
		self.m_panel_Processes.Layout()
		fgSizer3.Fit( self.m_panel_Processes )
		self.m_notebook1.AddPage( self.m_panel_Processes, u"Processes", False )
		self.m_panel_Services = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer4 = wx.FlexGridSizer( 1, 1, 0, 0 )
		fgSizer4.AddGrowableCol( 0 )
		fgSizer4.AddGrowableRow( 0 )
		fgSizer4.SetFlexibleDirection( wx.BOTH )
		fgSizer4.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_listCtrl_Services = wx.ListCtrl( self.m_panel_Services, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.SIMPLE_BORDER )
		fgSizer4.Add( self.m_listCtrl_Services, 0, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel_Services.SetSizer( fgSizer4 )
		self.m_panel_Services.Layout()
		fgSizer4.Fit( self.m_panel_Services )
		self.m_notebook1.AddPage( self.m_panel_Services, u"Services", False )
		self.m_panel_Startup = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer5 = wx.FlexGridSizer( 1, 1, 0, 0 )
		fgSizer5.AddGrowableCol( 0 )
		fgSizer5.AddGrowableRow( 0 )
		fgSizer5.SetFlexibleDirection( wx.BOTH )
		fgSizer5.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.m_listCtrl_Startup = wx.ListCtrl( self.m_panel_Startup, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LC_REPORT|wx.SIMPLE_BORDER )
		fgSizer5.Add( self.m_listCtrl_Startup, 0, wx.EXPAND|wx.ALL, 5 )
		
		
		self.m_panel_Startup.SetSizer( fgSizer5 )
		self.m_panel_Startup.Layout()
		fgSizer5.Fit( self.m_panel_Startup )
		self.m_notebook1.AddPage( self.m_panel_Startup, u"Startup", False )
		
		fgSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText_Version = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Version 0.01 by Patchie", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText_Version.Wrap( -1 )
		bSizer2.Add( self.m_staticText_Version, 0, wx.ALL, 5 )
		
		
		fgSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( fgSizer1 )
		self.m_panel1.Layout()
		fgSizer1.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_MENU, self.menu_refresh, id = self.m_menuItem_Refresh.GetId() )
		self.Bind( wx.EVT_MENU, self.menu_exit, id = self.m_menuItem_Exit.GetId() )
		self.Bind( wx.EVT_MENU, self.menu_preferences, id = self.m_menuItem_Preferences.GetId() )
		self.Bind( wx.EVT_MENU, self.menu_help, id = self.m_menuItem_HelpContents.GetId() )
		self.Bind( wx.EVT_MENU, self.menu_about, id = self.m_menuItem_About.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def menu_refresh( self, event ):
		event.Skip()
	
	def menu_exit( self, event ):
		event.Skip()
	
	def menu_preferences( self, event ):
		event.Skip()
	
	def menu_help( self, event ):
		event.Skip()
	
	def menu_about( self, event ):
		event.Skip()
	

###########################################################################
## Class MyDialog_About
###########################################################################

class MyDialog_About ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"About", pos = wx.DefaultPosition, size = wx.Size( 331,247 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel6 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer6 = wx.FlexGridSizer( 5, 1, 0, 0 )
		fgSizer6.AddGrowableRow( 3 )
		fgSizer6.SetFlexibleDirection( wx.BOTH )
		fgSizer6.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_ALL )
		
		self.m_bitmap1 = wx.StaticBitmap( self.m_panel6, wx.ID_ANY, wx.Bitmap( u"../Resources/Icon/Large_icon.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.m_staticText30 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Why Is My Computer Slow?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )
		self.m_staticText30.SetFont( wx.Font( 16, 74, 90, 92, False, "Arial" ) )
		
		fgSizer6.Add( self.m_staticText30, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_staticText31 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"Version x.x", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText31.Wrap( -1 )
		fgSizer6.Add( self.m_staticText31, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.BOTTOM|wx.LEFT|wx.RIGHT, 5 )
		
		self.m_staticText32 = wx.StaticText( self.m_panel6, wx.ID_ANY, u"This application's main focus is to tell the user why his/her computer is slow. By showing the user statistics, graphs, and data about all the resources and how much is in use while running the program.", wx.DefaultPosition, wx.Size( 300,-1 ), 0 )
		self.m_staticText32.Wrap( 300 )
		fgSizer6.Add( self.m_staticText32, 0, wx.ALL, 5 )
		
		self.m_button_AboutOk = wx.Button( self.m_panel6, wx.ID_ANY, u"OK", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer6.Add( self.m_button_AboutOk, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		self.m_panel6.SetSizer( fgSizer6 )
		self.m_panel6.Layout()
		fgSizer6.Fit( self.m_panel6 )
		bSizer3.Add( self.m_panel6, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer3 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button_AboutOk.Bind( wx.EVT_BUTTON, self.About_Ok )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def About_Ok( self, event ):
		event.Skip()
	

