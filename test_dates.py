import unittest
import datetime
from transaction import TodoList
from tracker import *

class TestValidateDate(unittest.TestCase):
    def test_validate_date(self):
        # Test flow_path = 0 (day)
        # Valid date
        self.assertEqual(validate_date(0), "15")
        # Invalid date
        with self.assertRaises(ValueError):
            validate_date(0)

        # Test flow_path = 1 (month)
        # Valid date
        self.assertEqual(validate_date(1), "5")
        # Invalid date
        with self.assertRaises(ValueError):
            validate_date(1)

        # Test flow_path = 2 (year)
        # Valid date
        self.assertEqual(validate_date(2), "2022")
        # Invalid date
        with self.assertRaises(ValueError):
            validate_date(2)

        # Test invalid flow_path
        with self.assertRaises(IllegalDateField):
            validate_date(3)

if __name__ == '__main__':
    unittest.main(exit=False, defaultTest='TestValidateDate', argv=['-s'])
