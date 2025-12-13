import unittest
from app import calculate_order, Menu, GST 

class TestOrderCalculations(unittest.TestCase):
    
    def test_sample_order_case(self):
        test_input_order = {
            "Cheeseburger": 2,
            "Soft Drink (Large)": 1
        }
        
        _, result_total, result_gst = calculate_order(test_input_order, Menu, GST)
        
        expected_total = 35.00
        expected_gst = 3.18181818 
        
        self.assertAlmostEqual(result_total, expected_total, places=2)
        self.assertAlmostEqual(result_gst, expected_gst, places=6) 
        

    def test_empty_order(self):
        test_input_order = {}
        
        _, result_total, result_gst = calculate_order(test_input_order, Menu, GST)
        
        self.assertEqual(result_total, 0.00)
        self.assertEqual(result_gst, 0.00)



if __name__ == '__main__':
    unittest.main()