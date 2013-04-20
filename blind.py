from aqt import mw
from aqt.overview import Overview
from aqt.reviewer import Reviewer

class BlindOverview(Overview):
	@staticmethod
	def dummy():
		return (1,0,0)

	def _table(self):
		orig = self.mw.col.sched.counts
		self.mw.col.sched.counts = BlindOverview.dummy

		table = Overview._table(self)
		self.mw.col.sched.counts = orig

		return table


class BlindReviewer(Reviewer):
	def _remaining(self):
		return ''

mw.sharedCSS += '''
tr.deck td:nth-child(2), tr.deck td:nth-child(3) {
	font-size:0;
}
'''

mw.overview = BlindOverview(mw)
mw.reviewer = BlindReviewer(mw)