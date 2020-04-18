import unittest
from testing import eat, nap

class ActivityTest(unittest.TestCase):

    # setUp function help to define some code before runnig the test. This code will be run before each test function.
    # Eg for creating an instance of a class and avoid creatig it in each function when testig class methods

    def test_eating_health(self):
        """ eat should have a possitive message for healthy eating """
        self.assertEqual(
            eat('broccoli', is_healthy = True),
            'I am eating broccoli, because my body is a temple'
        )
    
    def test_eating_unhealth(self):
        """ eat should have a negative message for unhealthy eating """
        self.assertEqual(
            eat('pizza', is_healthy = False),
            'I am eating pizza, because YOLO'
        )

    def test_long_nap(self):
        """ nap should have a won't sleep well message for hours be greater or equal than 2 """
        self.assertEqual(nap(3), 'I sleept 3 hours, I wont sleep well tonight')

    def test_short_nap(self):
        """ nap should have a will sleep well message for hours be lower than 2 """
        self.assertEqual(nap(1), 'I sleept just 1 hour, I am fresh and probably I will sleep well enought tonight')

    # tearDown function helps for removing instances or data created in the setUP function. This is useful in case you need to
    # add some data in the database before running tests

if __name__ == '__main__':
    unittest.main()