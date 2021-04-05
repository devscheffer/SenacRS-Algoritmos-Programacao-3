from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)

from task_2.fn.Auxiliar import fn_leap,fn_days_in_month

class Test_fn_leap:
	def test_leap_true(self):
		assert fn_leap(2020) == True
	def test_leap_false(self):
		assert fn_leap(2021) == False

class Test_fn_days_in_month:
	def test_month_fev(self):
		assert fn_days_in_month(month=2,year=2021)==28
	def test_month_fev_leap(self):
		assert fn_days_in_month(month=2,year=2020)==29
