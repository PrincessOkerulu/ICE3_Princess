from ICE3.src.temperature_sensor import process_temperatures
import unittest
# Test Cases
class TestTemperatureSensor(unittest.TestCase):
    def test_temperature_sensor(self):
        self.assertEqual(process_temperatures([-50]), "Min: -50.0°C, Max: -50.0°C, Avg: -50.0°C")
        self.assertEqual(process_temperatures([150]),    "Min: 150.0°C, Max: 150.0°C, Avg: 150.0°C")
        self.assertEqual(process_temperatures([-49, 149]),   "Min: -49.0°C, Max: 149.0°C, Avg: 50.0°C")
     # Test Case 3: Values inside range
        self.assertEqual(process_temperatures( [-60, 20, 160]),   "Error: Out-of-bound values detected.")
# Test Case 4: Out-of-bound values
        self.assertEqual(process_temperatures([20, "abc", 30]),  "Error: No valid input provided.")
        # Test Case 5: Alphabetic input => Should be "No valid input provided"
        self.assertEqual(process_temperatures([10, "@", -40]),  "Error: No valid input provided.")
 # Test Case 6: Special character => "No valid input provided"
        self.assertEqual(process_temperatures( [2**31 - 1, -2**31]), "Error: Out-of-bound values detected.") # Test Case 7: Very large input => "Out-of-bound values detected" (because of -2**31)

        self.assertEqual(process_temperatures( [50, 50, 50]),  "Min: 50.0°C, Max: 50.0°C, Avg: 50.0°C")
  # Test Case 8: All inputs are the same
        self.assertEqual(process_temperatures( [] ),      "Error: No input provided.")          # Test Case 9: Empty
