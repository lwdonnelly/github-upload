import unittest
import mc

class TestMarkov(unittest.TestCase):
    def test_get_table(self):
        res = mc.get_table('ab')
        self.assertEqual(res, {'a':{'b':1}})

    def test_get_table2(self):
        res = mc.get_table('abacab')
        self.assertEqual(res, {'a': {'b': 2, 'c': 1}, 'b': {'a': 1}, 'c': {'a': 1}})

    def test_get_table3(self):
        res = mc.get_table('abc', size = 2)
        self.assertEqual(res, {'ab':{'c':1}})
        
    def test_predict(self):
        m = mc.Markov('ab')
        res = m.predict('a')
        self.assertEqual(res, 'b')

    def test_predict2(self):
        m = mc.Markov('abc', size = 2)
        res = m.predict('ab')
        self.assertEqual(res, 'c')

if __name__ == '__main__':
    #executing this file
    unittest.main()
else:
    print('loading')
    
