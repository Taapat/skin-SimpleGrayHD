#######################################################################
#
#    Renderer for Enigma2
#    Based on code from shamann (c)2011
#    Updatet by Taapat (c)2018
#
#    This program is free software; you can redistribute it and/or
#    modify it under the terms of the GNU General Public License
#    as published by the Free Software Foundation; either version 2
#    of the License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#    See the GNU General Public License for more details.
#    
#######################################################################

from Renderer import Renderer
from enigma import eLabel
from enigma import eDVBVolumecontrol, eTimer
from Components.VariableText import VariableText


class SDVolume(VariableText, Renderer):
	def __init__(self):
		Renderer.__init__(self)
		VariableText.__init__(self)
		self.vTimer = eTimer()
		self.vTimer.callback.append(self.showVolume)

	GUI_WIDGET = eLabel

	def showVolume(self):
		self.text = str(eDVBVolumecontrol.getInstance().getVolume()) + '%'

	def onShow(self):
		self.showVolume()
		self.vTimer.start(200)

	def onHide(self):
		self.vTimer.stop()

