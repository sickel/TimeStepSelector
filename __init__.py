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
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
    # load TimestepSelector class from file TimestepSelector
    from timestepselector import TimestepSelector
    return TimestepSelector(iface)
