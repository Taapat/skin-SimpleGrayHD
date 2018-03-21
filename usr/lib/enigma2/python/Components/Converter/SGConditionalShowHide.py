from Converter import Converter

class SGConditionalShowHide(Converter, object):
	def __init__(self, argstr):
		Converter.__init__(self, argstr)

	def connectDownstream(self, downstream):
		Converter.connectDownstream(self, downstream)
		if hasattr(self.source, 'boolean'):
			vis = self.source.boolean
		else:
			vis = bool(self.source.text)
		if vis is None:
			vis = False
		downstream.visible = vis
