# aggregator.py
from trello.client import TrelloClient
import re

class BurndownBoard(TrelloClient):

	def __init__(self, board_id, pin=None):
		self.board_id = board_id
		self.pin = pin

	def get_burndown_totals(self):
		tc = TrelloClient(pin=self.pin)
		visitor = CardVisitor()
		tc.visit_cards(visitor, self.board_id)
		return visitor.get_totals()


class CardVisitor(object):

	def __init__(self):
		self.estimated = 0 
		self.actual = 0

	def visit(self, card):
		est, act = self.parse_counts(card['name'])
		self.estimated += est
		self.actual += act

	def parse_counts(self, name):
		"""
		Pattern finds (#/#) in the beginning of card titles:
		  (#)   - estimated, no work done
		  (#/#) - estimatd, some work done
		  (/#)  - unplanned, work done, estimate = actual work done (burndown "spike") 
		"""

		pattern = r'\((.*?)\)'
		matched = re.findall(pattern, name, re.I)
		# just get first match
		if matched and len(matched) > 0:
			try:
				match = matched[0]
				#print 'match is >> ', match
				if '/' in match:
					# some work done
					est, act = [val.strip() for val in match.split('/')]
					# if an unplanned item, no estimate, estimate = actual (a spikes)
					if est == '': 
						est = act
				else:
					# no work done yet
					est = match.strip()
					act = 0
				return float(est), float(act)

			except:
				print '* could not parse: {}'.format(name)

		return 0, 0

	def get_totals(self):
		return dict(estimated=self.estimated, actual=self.actual)
