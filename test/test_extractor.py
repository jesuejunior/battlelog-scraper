import unittest
from core.action.extractor import _extract

__author__ = 'jesuejunior'

class ExtractorTest(unittest.TestCase):

    def test_extract_to_integer(self):

        self.assertEquals(_extract('5'), 5)
        self.assertEquals(_extract('\n 545 \n'), 545)
        self.assertEquals(_extract('188 m '), 188)
        self.assertEquals(_extract('30%'), 30)
        self.assertEquals(_extract('16,000'), 16000)
        self.assertEquals(_extract('1.04'), 1.04)