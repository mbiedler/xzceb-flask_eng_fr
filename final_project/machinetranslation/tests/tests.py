import unittest

from translator import frenchtoenglish, englishtofrench

class Testfrenchtoenglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchtoenglish(''), '') 
        self.assertEqual(frenchtoenglish('Bonjour'), 'Hello')  
    
        

class Testenglishtofrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishtofrench(''),'') # test when 2 is given as input the output is 4.
        self.assertEqual(englishtofrench('Hello'),'Bonjour') # test when 2 is given as input the output is 4.
        
unittest.main()