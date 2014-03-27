# -*- coding: utf-8 -*-
"""
/***************************************************************************
 TimestepSelector
                                 A QGIS plugin
 Selects a timestep to display from a netCDF-file
                              -------------------
        begin                : 2014-03-24
        copyright            : (C) 2014 by Morten Sickel
        email                : Morten@sickel.net
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""
# Import the PyQt and QGIS libraries
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from qgis.utils import *
# Initialize Qt resources from file resources.py
import resources_rc
# Import the code for the dialog
from timestepselectordialog import TimestepSelectorDialog
import os.path
# import qgsmessagebar

class TimestepSelector:

    def __init__(self, iface):
        # Save reference to the QGIS interface
        self.iface = iface
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
        self.layerlist=[]
        # initialize locale
        locale = QSettings().value("locale/userLocale")[0:2]
        localePath = os.path.join(self.plugin_dir, 'i18n', 'timestepselector_{}.qm'.format(locale))

        if os.path.exists(localePath):
            self.translator = QTranslator()
            self.translator.load(localePath)

            if qVersion() > '4.3.3':
                QCoreApplication.installTranslator(self.translator)

        # Create the dialog (after translation) and keep reference
        self.dlg = TimestepSelectorDialog()
        # Sets an event handler on the combobox:
        self.dlg.comboBoxLayer.currentIndexChanged.connect(self.getLayerAttributes)
        self.dlg.horizontalTimeSlider.sliderMoved.connect(self.sliderMoved)
            

    def initGui(self):
        # Create action that will start plugin configuration
        self.action = QAction(
            QIcon(":/plugins/timestepselector/icon.png"),
            u"NetCDF timestep", self.iface.mainWindow())
        # connect the action to the run method
        self.action.triggered.connect(self.run)

        # Add toolbar button and menu item
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu(u"&NetCDF timestepselector", self.action)

    def unload(self):
        # Remove the plugin menu item and icon
        self.iface.removePluginMenu(u"&NetCDF timestepselector", self.action)
        self.iface.removeToolBarIcon(self.action)

    # run method that performs all the real work
    def run(self):
        layers=self.iface.legendInterface().layers()
        # Shold be moved somewhere else, this is only initiating when plugin is loaded.
        self.layerlist=[]
        #self.dlg.comboBoxLayer.clear()
        if len(layers) >0:
            for layer in layers:
                # iface.messageBar().pushMessage("Type",layer.name(), level=1, duration=10)
                if type(layer) is QgsRasterLayer and layer.bandCount()>1:
                    self.layerlist.append(layer)
                    self.dlg.comboBoxLayer.addItem(layer.name())
        # Initializes 
        self.getLayerAttributes(0)
        # show the dialog
        self.dlg.show()
        # Run the dialog event loop
        result = self.dlg.exec_()
        # See if OK was pressed
        if result == 1:
            # do something useful (delete the line containing pass and
            # substitute with your code)
            pass
    
    # Eventhandler on layer list combo box:
    def getLayerAttributes(self,comboIndex):
        self.activeLayer=self.layerlist[comboIndex]
        bcnt=self.activeLayer.bandCount()
        #rndr=self.activeLayer.renderer()
        #self.activeLayer.renderer=rndr  
        #iface.messageBar().pushMessage("N bands:",bcnt, level=1, duration=10)
        self.dlg.horizontalTimeSlider.setMaximum(bcnt)
    #    self.dlg.labelStartTime.setText(str(bcnt))
        
    def sliderMoved(self,sldValue):
        self.dlg.labelStartTime.setText(self.activeLayer.bandName(sldValue))
        self.activeLayer.renderer.setGrayBand(sldValue)
        self.activeLayer.triggerRepaint()

