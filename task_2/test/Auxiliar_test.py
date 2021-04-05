from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)

from task_2.fn.Auxiliar import fn_leap

class Test_leap:
	def test_leap_true(self):
		assert fn_leap(2020) == True
	def test_leap_false(self):
		assert fn_leap(2021) == False
