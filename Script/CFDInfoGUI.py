# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import os
import numpy as np
from Script.Support import *
###########################################################################
## Class SBIR
###########################################################################

class SBIR ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1600,814 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Introduction_Pnl = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Introduction_Pnl.SetFont( wx.Font( 36, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		self.m_notebook1.AddPage( self.Introduction_Pnl, u"Introduction", True )
		self.FlowCondition_Pnl = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.FlowCondition_Pnl.SetFont( wx.Font( 36, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.flowconditiontitle = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, u"Flow Information", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.flowconditiontitle.Wrap( -1 )

		self.flowconditiontitle.SetFont( wx.Font( 48, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer2.Add( self.flowconditiontitle, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer3 = wx.GridSizer( 1, 2, 0, 0 )

		gSizer4 = wx.GridSizer( 5, 3, 0, 0 )

		self.m_staticText15 = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, u"Flow Condition", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		gSizer4.Add( self.m_staticText15, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.empty = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty.Wrap( -1 )

		gSizer4.Add( self.empty, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.empty2 = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty2.Wrap( -1 )

		gSizer4.Add( self.empty2, 0, wx.ALL, 5 )

		self.FlowRate_Chk = wx.CheckBox( self.FlowCondition_Pnl, wx.ID_ANY, u"Flow Rate:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FlowRate_Chk.SetValue(True)
		gSizer4.Add( self.FlowRate_Chk, 0, wx.ALL, 5 )

		self.Q = wx.TextCtrl( self.FlowCondition_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 240,-1 ), 0 )
		gSizer4.Add( self.Q, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.Q_unit = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, u"m^3/s", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Q_unit.Wrap( -1 )

		gSizer4.Add( self.Q_unit, 0, wx.ALL, 5 )

		self.U_Chk = wx.CheckBox( self.FlowCondition_Pnl, wx.ID_ANY, u"Velocity:", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.U_Chk, 0, wx.ALL, 5 )

		self.Ux = wx.TextCtrl( self.FlowCondition_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 240,-1 ), 0 )
		self.Ux.Enable( False )

		gSizer4.Add( self.Ux, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.U_unit = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, u"m/s", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.U_unit.Wrap( -1 )

		gSizer4.Add( self.U_unit, 0, wx.ALL, 5 )

		self.WaterSurfaceElevation = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, u"WSE: ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WaterSurfaceElevation.Wrap( -1 )

		gSizer4.Add( self.WaterSurfaceElevation, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.WSE = wx.TextCtrl( self.FlowCondition_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 240,-1 ), 0 )
		gSizer4.Add( self.WSE, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.WSE_unit = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, u"m", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WSE_unit.Wrap( -1 )

		gSizer4.Add( self.WSE_unit, 0, wx.ALL, 5 )

		self.d50 = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, u"d50:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.d50.Wrap( -1 )

		gSizer4.Add( self.d50, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.d50 = wx.TextCtrl( self.FlowCondition_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 240,-1 ), 0 )
		gSizer4.Add( self.d50, 0, wx.ALL, 5 )

		self.WSE_unit1 = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, u"m", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WSE_unit1.Wrap( -1 )

		gSizer4.Add( self.WSE_unit1, 0, wx.ALL, 5 )


		gSizer3.Add( gSizer4, 1, wx.EXPAND, 5 )

		gSizer5 = wx.GridSizer( 6, 3, 0, 0 )

		self.CFDSetup = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, u"CFD Setup", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CFDSetup.Wrap( -1 )

		gSizer5.Add( self.CFDSetup, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.empty3 = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty3.Wrap( -1 )

		gSizer5.Add( self.empty3, 0, wx.ALL, 5 )

		self.empty4 = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty4.Wrap( -1 )

		gSizer5.Add( self.empty4, 0, wx.ALL, 5 )

		self.PhysicalModel = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, u"    Physical Model:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PhysicalModel.Wrap( -1 )

		gSizer5.Add( self.PhysicalModel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.empty5 = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty5.Wrap( -1 )

		gSizer5.Add( self.empty5, 0, wx.ALL, 5 )

		self.SP_Chk = wx.CheckBox( self.FlowCondition_Pnl, wx.ID_ANY, u"Single Phase   ", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SP_Chk.SetValue(True)
		gSizer5.Add( self.SP_Chk, 0, wx.ALL|wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.empty7 = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty7.Wrap( -1 )

		gSizer5.Add( self.empty7, 0, wx.ALL, 5 )

		self.empty6 = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty6.Wrap( -1 )

		gSizer5.Add( self.empty6, 0, wx.ALL, 5 )

		self.VOF_Chk = wx.CheckBox( self.FlowCondition_Pnl, wx.ID_ANY, u"VOF                 ", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.VOF_Chk, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.TimeStep = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, u"    Time Step:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TimeStep.Wrap( -1 )

		gSizer5.Add( self.TimeStep, 0, wx.ALL, 5 )

		self.empty = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty.Wrap( -1 )

		gSizer5.Add( self.empty, 0, wx.ALL|wx.ALIGN_BOTTOM, 5 )

		gSizer6 = wx.GridSizer( 1, 2, 0, 0 )

		self.dt = wx.TextCtrl( self.FlowCondition_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gSizer6.Add( self.dt, 0, wx.ALL, 5 )

		self.Step_unit = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, u"s", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Step_unit.Wrap( -1 )

		gSizer6.Add( self.Step_unit, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer5.Add( gSizer6, 1, wx.EXPAND, 5 )

		self.PhysicalTime = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, u"    Physical Time:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PhysicalTime.Wrap( -1 )

		gSizer5.Add( self.PhysicalTime, 0, wx.ALL, 5 )

		self.Empty = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Empty.Wrap( -1 )

		gSizer5.Add( self.Empty, 0, wx.ALL, 5 )

		gSizer61 = wx.GridSizer( 1, 2, 0, 0 )

		self.physicalTime = wx.TextCtrl( self.FlowCondition_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )
		gSizer61.Add( self.physicalTime, 0, wx.ALL, 5 )

		self.Time_unit = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, u"s", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Time_unit.Wrap( -1 )

		gSizer61.Add( self.Time_unit, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer5.Add( gSizer61, 1, wx.EXPAND, 5 )

		self.Processor = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, u"    Processor Number:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Processor.Wrap( -1 )

		gSizer5.Add( self.Processor, 0, wx.ALL, 5 )

		self.Empty1 = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Empty1.Wrap( -1 )

		gSizer5.Add( self.Empty1, 0, wx.ALL, 5 )

		gSizer611 = wx.GridSizer( 1, 2, 0, 0 )

		number = '2'
		self.Processor_Number = wx.TextCtrl( self.FlowCondition_Pnl, wx.ID_ANY, number, wx.DefaultPosition, wx.Size( 150,-1 ), 0 )

		gSizer611.Add( self.Processor_Number, 0, wx.ALL, 5 )

		self.Empty = wx.StaticText( self.FlowCondition_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Empty.Wrap( -1 )

		gSizer611.Add( self.Empty, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		gSizer5.Add( gSizer611, 1, wx.EXPAND, 5 )


		gSizer3.Add( gSizer5, 0, wx.EXPAND, 5 )


		bSizer2.Add( gSizer3, 1, wx.EXPAND, 5 )


		self.FlowCondition_Pnl.SetSizer( bSizer2 )
		self.FlowCondition_Pnl.Layout()
		bSizer2.Fit( self.FlowCondition_Pnl )
		self.m_notebook1.AddPage( self.FlowCondition_Pnl, u"Flow Condition", False )
		self.Mesh_Pnl = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.MesgInfo = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, u"Mesh Information", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.MesgInfo.Wrap( -1 )

		self.MesgInfo.SetFont( wx.Font( 48, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer3.Add( self.MesgInfo, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		gSizer13 = wx.GridSizer( 1, 2, 0, 0 )

		gSizer15 = wx.GridSizer( 7, 4, 0, 0 )

		self.BaseMesh = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, u"Base Mesh Information", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BaseMesh.Wrap( -1 )

		self.BaseMesh.SetFont( wx.Font( 40, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer15.Add( self.BaseMesh, 0, wx.ALL, 5 )

		self.empty = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty.Wrap( -1 )

		gSizer15.Add( self.empty, 0, wx.ALL, 5 )

		self.empty = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty.Wrap( -1 )

		gSizer15.Add( self.empty, 0, wx.ALL, 5 )

		self.empty = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty.Wrap( -1 )

		gSizer15.Add( self.empty, 0, wx.ALL, 5 )

		self.BaseSize = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, u"    Base Size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BaseSize.Wrap( -1 )

		self.BaseSize.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer15.Add( self.BaseSize, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.empty1 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty1.Wrap( -1 )

		gSizer15.Add( self.empty1, 0, wx.ALL, 5 )

		self.Base_Size = wx.TextCtrl( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Base_Size.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer15.Add( self.Base_Size, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_RIGHT, 5 )

		self.BsSize_unit = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, u"m", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BsSize_unit.Wrap( -1 )

		self.BsSize_unit.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer15.Add( self.BsSize_unit, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.Layer = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, u"    Prism Layer:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Layer.Wrap( -1 )

		self.Layer.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer15.Add( self.Layer, 0, wx.ALL, 5 )

		self.empty11 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty11.Wrap( -1 )

		gSizer15.Add( self.empty11, 0, wx.ALL, 5 )

		self.empty111 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty111.Wrap( -1 )

		gSizer15.Add( self.empty111, 0, wx.ALL, 5 )

		self.empty112 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty112.Wrap( -1 )

		gSizer15.Add( self.empty112, 0, wx.ALL, 5 )

		self.empty113 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty113.Wrap( -1 )

		gSizer15.Add( self.empty113, 0, wx.ALL, 5 )

		self.BedLayer = wx.CheckBox( self.Mesh_Pnl, wx.ID_ANY, u"Bathymetry Layer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BedLayer.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer15.Add( self.BedLayer, 0, wx.ALL, 5 )

		self.empty114 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty114.Wrap( -1 )

		gSizer15.Add( self.empty114, 0, wx.ALL, 5 )

		self.BedLayerN_Ipt = wx.TextCtrl( self.Mesh_Pnl, wx.ID_ANY, u'0', wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BedLayerN_Ipt.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.BedLayerN_Ipt.Enable( False )

		gSizer15.Add( self.BedLayerN_Ipt, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.empty1131 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty1131.Wrap( -1 )

		gSizer15.Add( self.empty1131, 0, wx.ALL, 5 )

		self.BridgeLayer = wx.CheckBox( self.Mesh_Pnl, wx.ID_ANY, u"Bridge Layer", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BridgeLayer.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer15.Add( self.BridgeLayer, 0, wx.ALL, 5 )

		self.empty1141 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty1141.Wrap( -1 )

		gSizer15.Add( self.empty1141, 0, wx.ALL, 5 )

		self.BridgeLayerN_Ipt = wx.TextCtrl( self.Mesh_Pnl, wx.ID_ANY, u'0', wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BridgeLayerN_Ipt.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.BridgeLayerN_Ipt.Enable( False )

		gSizer15.Add( self.BridgeLayerN_Ipt, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.empty115 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty115.Wrap( -1 )

		gSizer15.Add( self.empty115, 0, wx.ALL, 5 )

		self.Thickness = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, u"First Layer Size:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Thickness.Wrap( -1 )

		self.Thickness.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer15.Add( self.Thickness, 0, wx.ALL, 5 )

		self.empty1151 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty1151.Wrap( -1 )

		gSizer15.Add( self.empty1151, 0, wx.ALL, 5 )

		gSizer16 = wx.GridSizer( 1, 2, 0, 0 )

		self.First_Cell = wx.TextCtrl( self.Mesh_Pnl, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.First_Cell.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer16.Add( self.First_Cell, 0, wx.ALL, 5 )

		self.Layer_unit = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, u"m", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Layer_unit.Wrap( -1 )

		self.Layer_unit.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer16.Add( self.Layer_unit, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		gSizer15.Add( gSizer16, 1, wx.EXPAND, 5 )

		self.empty116 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty116.Wrap( -1 )

		gSizer15.Add( self.empty116, 0, wx.ALL, 5 )

		self.Ration = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, u"Ratio:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Ration.Wrap( -1 )

		self.Ration.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer15.Add( self.Ration, 0, wx.ALL, 5 )

		self.empty8 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty8.Wrap( -1 )

		gSizer15.Add( self.empty8, 0, wx.ALL, 5 )

		self.Ratio = wx.TextCtrl( self.Mesh_Pnl, wx.ID_ANY, u"1.5", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Ratio.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer15.Add( self.Ratio, 0, wx.ALL, 5 )


		gSizer13.Add( gSizer15, 1, wx.EXPAND, 5 )

		gSizer17 = wx.GridSizer( 7, 4, 0, 0 )

		self.AdvancedMeshSetup = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, u"Advanced Mesh Setup", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.AdvancedMeshSetup.Wrap( -1 )

		self.AdvancedMeshSetup.SetFont( wx.Font( 40, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer17.Add( self.AdvancedMeshSetup, 0, wx.ALL, 5 )

		self.empty = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty.Wrap( -1 )

		gSizer17.Add( self.empty, 0, wx.ALL, 5 )

		self.empty9 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty9.Wrap( -1 )

		gSizer17.Add( self.empty9, 0, wx.ALL, 5 )

		self.empty10 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty10.Wrap( -1 )

		gSizer17.Add( self.empty10, 0, wx.ALL, 5 )

		self.SurfaceMesh = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, u"    Surface Mesh:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SurfaceMesh.Wrap( -1 )

		self.SurfaceMesh.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer17.Add( self.SurfaceMesh, 0, wx.ALL, 5 )

		self.empty12 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.empty12.Wrap( -1 )

		gSizer17.Add( self.empty12, 0, wx.ALL, 5 )

		self.Empty = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Empty.Wrap( -1 )

		gSizer17.Add( self.Empty, 0, wx.ALL, 5 )

		self.Empty2 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Empty2.Wrap( -1 )

		gSizer17.Add( self.Empty2, 0, wx.ALL, 5 )

		self.Empty3 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Empty3.Wrap( -1 )

		gSizer17.Add( self.Empty3, 0, wx.ALL, 5 )

		self.BedSurface_Chk = wx.CheckBox( self.Mesh_Pnl, wx.ID_ANY, u"Bathymetry:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BedSurface_Chk.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer17.Add( self.BedSurface_Chk, 0, wx.ALL, 5 )

		self.Empty31 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Empty31.Wrap( -1 )

		gSizer17.Add( self.Empty31, 0, wx.ALL, 5 )

		gSizer18 = wx.GridSizer( 1, 2, 0, 0 )

		self.BedSurface = wx.TextCtrl( self.Mesh_Pnl, wx.ID_ANY, u'0', wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BedSurface.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.BedSurface.Enable( False )

		gSizer18.Add( self.BedSurface, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.SurfaceUnit = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, u"m", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SurfaceUnit.Wrap( -1 )

		self.SurfaceUnit.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer18.Add( self.SurfaceUnit, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		gSizer17.Add( gSizer18, 1, wx.EXPAND, 5 )

		self.Empty32 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Empty32.Wrap( -1 )

		gSizer17.Add( self.Empty32, 0, wx.ALL, 5 )

		self.BridgeSurface_Chk = wx.CheckBox( self.Mesh_Pnl, wx.ID_ANY, u"Bridge:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BridgeSurface_Chk.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer17.Add( self.BridgeSurface_Chk, 0, wx.ALL, 5 )

		self.Empty311 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Empty311.Wrap( -1 )

		gSizer17.Add( self.Empty311, 0, wx.ALL, 5 )

		gSizer181 = wx.GridSizer( 1, 2, 0, 0 )

		self.BridgeSurface = wx.TextCtrl( self.Mesh_Pnl, wx.ID_ANY, u'0', wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BridgeSurface.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.BridgeSurface.Enable( False )

		gSizer181.Add( self.BridgeSurface, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.SurfaceUnit1 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, u"m", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SurfaceUnit1.Wrap( -1 )

		self.SurfaceUnit1.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer181.Add( self.SurfaceUnit1, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		gSizer17.Add( gSizer181, 1, wx.EXPAND, 5 )

		self.RegionMesh = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, u"    Region Mesh:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.RegionMesh.Wrap( -1 )

		self.RegionMesh.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer17.Add( self.RegionMesh, 0, wx.ALL, 5 )

		self.Empty33 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Empty33.Wrap( -1 )

		gSizer17.Add( self.Empty33, 0, wx.ALL, 5 )

		self.Empty34 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Empty34.Wrap( -1 )

		gSizer17.Add( self.Empty34, 0, wx.ALL, 5 )

		self.Empty35 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Empty35.Wrap( -1 )

		gSizer17.Add( self.Empty35, 0, wx.ALL, 5 )

		self.Empty36 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Empty36.Wrap( -1 )

		gSizer17.Add( self.Empty36, 0, wx.ALL, 5 )

		self.BedRegion_Chk = wx.CheckBox( self.Mesh_Pnl, wx.ID_ANY, u"Bathymetry:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BedRegion_Chk.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer17.Add( self.BedRegion_Chk, 0, wx.ALL, 5 )

		self.Empty312 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Empty312.Wrap( -1 )

		gSizer17.Add( self.Empty312, 0, wx.ALL, 5 )

		gSizer182 = wx.GridSizer( 1, 2, 0, 0 )

		self.BedRegion = wx.TextCtrl( self.Mesh_Pnl, wx.ID_ANY, u'0', wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BedRegion.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.BedRegion.Enable( False )

		gSizer182.Add( self.BedRegion, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.SurfaceUnit2 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, u"m", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SurfaceUnit2.Wrap( -1 )

		self.SurfaceUnit2.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer182.Add( self.SurfaceUnit2, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		gSizer17.Add( gSizer182, 1, wx.EXPAND, 5 )

		self.Empty361 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Empty361.Wrap( -1 )

		gSizer17.Add( self.Empty361, 0, wx.ALL, 5 )

		self.BridgeRegion_Chk = wx.CheckBox( self.Mesh_Pnl, wx.ID_ANY, u"Bridge:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BridgeRegion_Chk.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer17.Add( self.BridgeRegion_Chk, 0, wx.ALL, 5 )

		self.Empty3121 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Empty3121.Wrap( -1 )

		gSizer17.Add( self.Empty3121, 0, wx.ALL, 5 )

		gSizer1821 = wx.GridSizer( 1, 2, 0, 0 )

		self.BridgeRegion = wx.TextCtrl( self.Mesh_Pnl, wx.ID_ANY, u'0', wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BridgeRegion.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.BridgeRegion.Enable( False )

		gSizer1821.Add( self.BridgeRegion, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )

		self.SurfaceUnit21 = wx.StaticText( self.Mesh_Pnl, wx.ID_ANY, u"m", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SurfaceUnit21.Wrap( -1 )

		self.SurfaceUnit21.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer1821.Add( self.SurfaceUnit21, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		gSizer17.Add( gSizer1821, 1, wx.EXPAND, 5 )


		gSizer13.Add( gSizer17, 1, wx.EXPAND, 5 )


		bSizer3.Add( gSizer13, 1, wx.EXPAND, 5 )

		self.Mesh_Only = wx.Button( self.Mesh_Pnl, wx.ID_ANY, u"Mesh Only", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Mesh_Only.SetFont( wx.Font( 36, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer3.Add( self.Mesh_Only, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		self.Mesh_Pnl.SetSizer( bSizer3 )
		self.Mesh_Pnl.Layout()
		bSizer3.Fit( self.Mesh_Pnl )
		self.m_notebook1.AddPage( self.Mesh_Pnl, u"Mesh Setup", False )

		bSizer1.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )

		gSizer1 = wx.GridSizer( 1, 2, 0, 0 )

		self.Close_Btn = wx.Button( self, wx.ID_ANY, u"Close", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Close_Btn.SetFont( wx.Font( 36, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer1.Add( self.Close_Btn, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

		self.Run_Btn = wx.Button( self, wx.ID_ANY, u"Run", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Run_Btn.SetFont( wx.Font( 36, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		gSizer1.Add( self.Run_Btn, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer1.Add( gSizer1, 0, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.FlowRate_Chk.Bind( wx.EVT_CHECKBOX, self.FlowRate_Chk_App )
		self.U_Chk.Bind( wx.EVT_CHECKBOX, self.U_Chk_App )
		self.SP_Chk.Bind( wx.EVT_CHECKBOX, self.SP_Chk_App )
		self.VOF_Chk.Bind( wx.EVT_CHECKBOX, self.VOF_Chk_App )
		self.BedLayer.Bind( wx.EVT_CHECKBOX, self.BedLayer_App )
		self.BridgeLayer.Bind( wx.EVT_CHECKBOX, self.BridgeLayer_App )
		self.BedSurface_Chk.Bind( wx.EVT_CHECKBOX, self.BedSurface_Chk_App )
		self.BridgeSurface_Chk.Bind( wx.EVT_CHECKBOX, self.BridgeSurface_Chk_App )
		self.BedRegion_Chk.Bind( wx.EVT_CHECKBOX, self.BedRegion_Chk_App )
		self.BridgeRegion_Chk.Bind( wx.EVT_CHECKBOX, self.BridgeRegion_Chk_App )
		self.Mesh_Only.Bind( wx.EVT_BUTTON, self.MeshOnlyApp )
		self.Close_Btn.Bind( wx.EVT_BUTTON, self.CloseApp )
		self.Run_Btn.Bind( wx.EVT_BUTTON, self.RunApp )

	def __del__( self ):
		pass

	# Virtual event handlers, override them in your derived class

	#Flow rate check
	def FlowRate_Chk_App( self, event):
		if self.FlowRate_Chk.IsChecked( ):
			self.Q.Enable( True )
			self.U_Chk.SetValue( False )
			self.Ux.Enable( False )

		else:
			self.Q.Enable( False )
			self.U_Chk.SetValue( True )
			self.Ux.Enable( True )

	#Velocity rate check
	def U_Chk_App( self, event ):
		if self.U_Chk.IsChecked( ):
			self.Ux.Enable( True )
			self.FlowRate_Chk.SetValue( False )
			self.Q.Enable( False )

		else:
			self.Ux.Enable( False )
			self.FlowRate_Chk.SetValue( True )
			self.Q.Enable( True )

	#Single Phase check
	def SP_Chk_App( self, event ):
		if self.SP_Chk.IsChecked( ):
			self.VOF_Chk.SetValue( False )
		else:
			self.VOF_Chk.SetValue( True )
			self.SP_Chk.SetValue( False )

	#VOF check
	def VOF_Chk_App( self, event ):
		if self.VOF_Chk.IsChecked( ):
			self.SP_Chk.SetValue( False )
		else:
			self.SP_Chk.SetValue( True )
			self.VOF_Chk.SetValue( False )

	#Bed layer number check
	def BedLayer_App( self, event ):
		if self.BedLayer.IsChecked( ):
			self.BedLayerN_Ipt.Enable( True )
		else:
			self.BedLayerN_Ipt.Enable( False )

	#Bridge layer number check
	def BridgeLayer_App( self, event ):
		if self.BridgeLayer.IsChecked( ):
			self.BridgeLayerN_Ipt.Enable( True )
		else:
			self.BridgeLayerN_Ipt.Enable( False )

	#Bed surface mesh setup check
	def BedSurface_Chk_App( self, event ):
		if self.BedSurface_Chk.IsChecked( ):
			self.BedSurface.Enable( True )
		else:
			self.BedSurface.Enable( False )

	#Bridge surface mesh setup check
	def BridgeSurface_Chk_App( self, event ):
		if self.BridgeSurface_Chk.IsChecked( ):
			self.BridgeSurface.Enable( True )
		else:
			self.BridgeSurface.Enable( False )

	#Bed region mesh setup check
	def BedRegion_Chk_App( self, event ):
		if self.BedRegion_Chk.IsChecked( ):
			self.BedRegion.Enable( True )
		else:
			self.BedRegion.Enable( False )

	#Bridge region mesh setup check
	def BridgeRegion_Chk_App( self, event ):
		if self.BridgeRegion_Chk.IsChecked( ):
			self.BridgeRegion.Enable( True )
		else:
			self.BridgeRegion.Enable( False )

	#Only mesh the geometry and show the mesh results, NOT finish
	def MeshOnlyApp( self, event ):
		CFDInfo = {}
		CFDInfo = self.InputInfo()
		Error_Log = "temp/Error_Log.txt"
		if os.path.exists(Error_Log):
			with open (Error_Log, "r") as Error_info :
				f = Error_info.read().strip()
		else:
			f = ''

		if len(f) == 0:
			ConfirmMsg = wx.MessageDialog(None,"Do you accept the current mesh ?", "Mesh Confirmation", wx.YES_NO|wx.ICON_QUESTION)
			if ConfirmMsg.ShowModal() == wx.ID_YES:
				self.Close()

		else:
			ErrMsg = wx.MessageDialog(None, f, 'Error Information!', wx.OK | wx.ICON_QUESTION)
			if ErrMsg.ShowModal() == wx.OK:
				ErrMsg.Destroy()

	#Conduct the simulation
	def RunApp( self, event ):
		CFDInfo = {}
		CFDInfo = self.InputInfo()
		Error_Log = "temp/Error_Log.txt"
		if os.path.exists(Error_Log):
			with open (Error_Log, "r") as Error_info :
				f = Error_info.read().strip()
		else:
			f = ''
		if len(f) == 0:
			self.Destroy()
		else:
			ErrMsg = wx.MessageDialog(None, f, 'Error Information!', wx.OK | wx.ICON_QUESTION)
			if ErrMsg.ShowModal() == wx.OK:
				ErrMsg.Close()

	#Close the GUI window
	def CloseApp( self, event ):
		r = wx.MessageBox("Do you confirm to exit SBIR system ?", "EXIT", wx.CANCEL|wx.OK|wx.ICON_QUESTION)
		if r == wx.OK :
			self.Close()

	#load the input information
	def InputInfo(self):
		CFDInfoFile = 'temp/CFD_Info.txt'
		Error_Log = "temp/Error_Log.txt"
		CFDInfo = {}

		if os.path.exists(CFDInfoFile):
			os.remove(CFDInfoFile)
		if os.path.exists(Error_Log):
			os.remove(Error_Log)

		if self.SP_Chk.IsChecked( ):
			CFDInfo['CFDMode'] = 1
		if self.VOF_Chk.IsChecked( ):
			CFDInfo['CFDMode'] = 2

		CFDInfo['WSE'] = input_check('WSE',self.WSE.GetValue().strip())
		CFDInfo['d50'] = input_check('d50',self.d50.GetValue().strip())

		if self.FlowRate_Chk.IsChecked( ):
			CFDInfo['Q'] = input_check('flow rate',self.Q.GetValue().strip())
			CFDInfo['Ux']  = -2

		if self.U_Chk.IsChecked( ):
			CFDInfo['Ux'] = input_check('Velocity',self.Ux.GetValue().strip())
			CFDInfo['Q']  = -2

		CFDInfo['Base_Size'] = input_check('Base_Size',self.Base_Size.GetValue().strip())
		CFDInfo['First_Cell'] = input_check('First_Cell',self.First_Cell.GetValue().strip())

		if self.BedLayer.IsChecked( ):
			CFDInfo['BedLayerN'] = np.ceil(input_check('BedLayerN',self.BedLayerN_Ipt.GetValue().strip()))
		else:
			CFDInfo['BedLayerN'] = 0

		if self.BridgeLayer.IsChecked( ):
			CFDInfo['BridgeLayerN'] = np.ceil(input_check('BridgeLayerN',self.BridgeLayerN_Ipt.GetValue().strip()))
		else:
			CFDInfo['BridgeLayerN'] = 0

		if self.BedSurface_Chk.IsChecked( ):
			CFDInfo['BedSurface'] = input_check('BedSurface',self.BedSurface.GetValue().strip())
		else:
			CFDInfo['BedSurface'] = CFDInfo['Base_Size']

		if self.BridgeSurface_Chk.IsChecked( ):
			CFDInfo['BridgeSurface'] = input_check('BridgeSurface',self.BridgeSurface.GetValue().strip())
		else:
			CFDInfo['BridgeSurface'] = CFDInfo['Base_Size']

		if self.BedRegion_Chk.IsChecked( ):
			CFDInfo['BedRegion'] = input_check('BedRegion',self.BedRegion.GetValue().strip())
		else:
			CFDInfo['BedRegion'] = 0

		if self.BridgeRegion_Chk.IsChecked( ):
			CFDInfo['BridgeRegion'] = input_check('BridgeRegion',self.BridgeRegion.GetValue().strip())
		else:
			CFDInfo['BridgeRegion'] = 0
		#CFDInfo['']
		CFDInfo['Ratio'] = input_check('Ratio',self.Ratio.GetValue().strip())
		CFDInfo['dt'] = input_check('dt',self.dt.GetValue().strip())
		CFDInfo['physicalTime'] = input_check('physicalTime',self.physicalTime.GetValue().strip())
		CFDInfo['Processor_Number'] = int(input_check('Processor_Number',self.Processor_Number.GetValue().strip()))

		with open(CFDInfoFile,'w') as f:
			for item in CFDInfo.keys():
				content = item + '\t' + str(CFDInfo[item]) + '\n'
				f.write(content)
		return CFDInfo

'''
app = wx.App(False)
frame = SBIR(None)
frame.Show()
app.MainLoop()
del app
'''
