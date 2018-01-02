# -*- coding: utf-8 -*-

#******************************************************************************
#
# QTiles
# ---------------------------------------------------------
# Generates tiles from QGIS project
#
# Copyright (C) 2012-2014 NextGIS (info@nextgis.org)
#
# This source is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 2 of the License, or (at your option)
# any later version.
#
# This code is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# A copy of the GNU General Public License is available on the World Wide Web
# at <http://www.gnu.org/licenses/>. You can also obtain it by writing
# to the Free Software Foundation, 51 Franklin Street, Suite 500 Boston,
# MA 02110-1335 USA.
#
#******************************************************************************


from qgis.PyQt.QtCore import *

from qgis.core import QgsMapLayer, QgsProject


def getMapLayers():
    layerMap = QgsProject.instance().mapLayers()
    layers = dict()
    for name, layer in layerMap.items():
        if layer.type() == QgsMapLayer.VectorLayer:
            if layer.id() not in list(layers.keys()):
                layers[layer.id()] = str(layer.name())
        if layer.type() == QgsMapLayer.RasterLayer and layer.providerType() == 'gdal':
            if layer.id() not in list(layers.keys()):
                layers[layer.id()] = str(layer.name())
    return layers


def getLayerById(layerId):
    layerMap = QgsProject.instance().mapLayers()
    for name, layer in layerMap.items():
        if layer.id() == layerId:
            if layer.isValid():
                return layer
            else:
                return None


def getLayerGroup(layer_id):
    treeNode = QgsProject.instance().layerTreeRoot().findLayer(layer_id)
    if treeNode is not None:
        groupNode = treeNode.parent()
        if groupNode is not None:
            return groupNode.name()
    return None
