from apama.eplplugin import EPLAction, EPLPluginBase, Correlator, Event, Any
from wakeonlan import send_magic_packet
from ping3 import ping
import threading, queue

class Job(object):
	"""
		Jobs to be executed asynchronously
		@param fn a functor to execute
	"""
	def __init__(self, fn):
		self.fn = fn

def iothread(plugin):
	"""
		Background thread to execute async jobs on.
	"""
	plugin.getLogger().debug("Starting background IO thread for asynchronous jobs")
	while plugin.running:
		try:
			job = plugin.queue.get(timeout=1.0)
			job.fn()
		except queue.Empty:
			pass

	plugin.getLogger().info("iothread done")


class WakeOnLanPluginClass(EPLPluginBase):
	"""
	"""
	def __init__(self, init):
		super(WakeOnLanPluginClass, self).__init__(init)
		self.running = True
		self.queue = queue.SimpleQueue()
		self.thread = threading.Thread(target=iothread, args=[self], name='Apama WakeOnLanPluginClass io thread')
		self.thread.start()

	def _sendResponseEvent(self, channel, eventType, body):
		Correlator.sendTo(channel, Event(eventType, body))

	@EPLAction("action<string>")
	def wakeMAC(self, mac):
		"""
		"""
		self.getLogger().info("Waking up machine with address %s"%mac)
		send_magic_packet(mac)
	
	@EPLAction("action<string, integer, string>")
	def ping(self, host, requestId, channel):
		self.queue.put(Job(
			lambda: self._sendResponseEvent(channel, "com.apamax.Ping", {
				"requestId":requestId,
				"host": host,
				"state": True if ping(host) else False,
			})
		))
		
	@EPLAction("action<>")
	def shutdown(self):
		"""
			Plug-in function to shutdown the background thread.
		"""
		self.getLogger().debug(f"Shutting down Kasa plug-in")
		self.running = False
		self.thread.join()



