import unittest

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from cron_parser.cron_parse import expression_parser

class TestExpressionParse(unittest.TestCase):

    def test_correct(self):
        excepted = [13]
        result = expression_parser('13', 60)
        self.assertEqual(excepted, result)
    
    def test_modulo(self):
        excepted = [0, 30]
        for x in range(0, len(excepted)):
            excepted[x] = int(excepted[x])
        
        result = expression_parser('*/30', 60)
        self.assertEqual(excepted, result)
    
    def test_range(self):
        excepted = [2, 3, 4]
        for x in range(0, len(excepted)):
            excepted[x] = int(excepted[x])
        
        result = expression_parser('2-4', 60)
        self.assertEqual(excepted, result)
    
    def test_star(self):
        excepted = [1, 2, 3, 4, 5, 6, 7]
        
        result = expression_parser('*', 8, 1)
        self.assertEqual(excepted, result)
    
    def test_comma(self):
        excepted = [1, 3, 7]
        
        result = expression_parser('1,3,7', 8)
        self.assertEqual(excepted, result)
    
    def test_greater_than_max(self):
        self.assertRaises(ValueError, expression_parser, '9', 8)
    
    def test_lower_than_min(self):
        self.assertRaises(ValueError, expression_parser, '1', 8, 2)
    
    def test_invalid_modulo(self):
        self.assertRaises(ValueError, expression_parser, '/60', 60)
    
    def test_invalid_range(self):
        self.assertRaises(ValueError, expression_parser, '-3', 60)
    
    def test_invalid_star(self):
        self.assertRaises(ValueError, expression_parser, '*3', 60)
    
    def test_invalid_comma(self):
        self.assertRaises(ValueError, expression_parser, '4,', 60)
    
    def test_range_out_of_range(self):
        self.assertRaises(ValueError, expression_parser, '1-8', 8)
    
    def test_comma_out_of_range(self):
        self.assertRaises(ValueError, expression_parser, '1,9', 8)

if __name__ == '__main__':
    unittest.main()
