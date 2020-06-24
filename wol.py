from apama.eplplugin import EPLAction, EPLPluginBase, Correlator, Event, Any
from wakeonlan import send_magic_packet

class WakeOnLanPluginClass(EPLPluginBase):
	"""
	"""
	def __init__(self, init):
		super(WakeOnLanPluginClass, self).__init__(init)

	@EPLAction("action<string>")
	def wakeMAC(self, mac):
		"""
		"""
		send_magic_packet(mac)

