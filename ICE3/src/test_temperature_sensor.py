import unittest
from temperature_sensor import process_temperatures

# Test Cases
test_cases = [
    [-50],            # Test Case 1: Lower boundary
    [150],            # Test Case 2: Upper boundary
    [-49, 149],       # Test Case 3: Values inside range
    [-60, 20, 160],   # Test Case 4: Out-of-bound values
    [20, "abc", 30],  # Test Case 5: Alphabetic input => Should be "No valid input provided"
    [10, "@", -40],   # Test Case 6: Special character => "No valid input provided"
    [2**31 - 1, -2**31],  # Test Case 7: Very large input => "Out-of-bound values detected" (because of -2**31)
    [50, 50, 50],     # Test Case 8: All inputs are the same
    []                # Test Case 9: Empty list
]

# Run and print each test case
for i, case in enumerate(test_cases, start=1):
    print(f"Test Case {i}: {case}")
    print(process_temperatures(case))
    print("-" * 50)