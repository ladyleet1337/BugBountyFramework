import re
import subprocess
import config
from concurrent.futures import ThreadPoolExecutor,as_completed
class dirb():
	def __init__(self):
		self.wordlist = config.FILE_LIST
		self.urls = []
	def start(self,domain):
		output = subprocess.check_output('dirb http://'+domain+' \"'+self.wordlist+'\" -S', shell=True)
		for i in re.findall(r'\+ (.*?) \(C',output):
			self.urls.append(i)
	def run(self,domains):
	print '[+]Running dirb with wordlist: '+config.FILE_LIST
		tpool = ThreadPoolExecutor(config.DIRB_THREADS)
		futures = [tpool.submit(self.start,d) for d in domains]
	tpool.shutdown(True)
	print self.urls
#
#