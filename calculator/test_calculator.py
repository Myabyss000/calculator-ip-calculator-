"""
Test Suite for Scientific Calculator
Comprehensive tests for all calculator functions
"""

import unittest
import math
import sys
import os

# Add the parent directory to the path to import our modules
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from scientific_calculator import ScientificCalculator

class TestScientificCalculator(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.calc = ScientificCalculator()
    
    def test_basic_arithmetic(self):
        """Test basic arithmetic operations"""
        # Addition
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-2, 7), 5)
        self.assertEqual(self.calc.add(0, 0), 0)
        
        # Subtraction
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(5, 10), -5)
        
        # Multiplication
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(0, 100), 0)
        
        # Division
        self.assertEqual(self.calc.divide(15, 3), 5)
        self.assertEqual(self.calc.divide(7, 2), 3.5)
        
        # Division by zero
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)
    
    def test_power_and_roots(self):
        """Test power and root operations"""
        # Power
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 2), 25)
        self.assertEqual(self.calc.power(10, 0), 1)
        
        # Square root
        self.assertEqual(self.calc.sqrt(16), 4)
        self.assertEqual(self.calc.sqrt(25), 5)
        self.assertEqual(self.calc.sqrt(0), 0)
        
        # nth root
        self.assertAlmostEqual(self.calc.nth_root(8, 3), 2, places=10)
        self.assertAlmostEqual(self.calc.nth_root(16, 4), 2, places=10)
    
    def test_trigonometric_functions(self):
        """Test trigonometric functions in radians"""
        self.calc.set_angle_mode('radians')
        
        # Basic trig functions
        self.assertAlmostEqual(self.calc.sin(0), 0, places=10)
        self.assertAlmostEqual(self.calc.sin(math.pi/2), 1, places=10)
        self.assertAlmostEqual(self.calc.cos(0), 1, places=10)
        self.assertAlmostEqual(self.calc.cos(math.pi), -1, places=10)
        self.assertAlmostEqual(self.calc.tan(0), 0, places=10)
        self.assertAlmostEqual(self.calc.tan(math.pi/4), 1, places=10)
        
        # Inverse trig functions
        self.assertAlmostEqual(self.calc.asin(0), 0, places=10)
        self.assertAlmostEqual(self.calc.asin(1), math.pi/2, places=10)
        self.assertAlmostEqual(self.calc.acos(1), 0, places=10)
        self.assertAlmostEqual(self.calc.atan(0), 0, places=10)
        self.assertAlmostEqual(self.calc.atan(1), math.pi/4, places=10)
        
        # Test invalid inputs for inverse functions
        with self.assertRaises(ValueError):
            self.calc.asin(2)
        with self.assertRaises(ValueError):
            self.calc.acos(2)
    
    def test_trigonometric_functions_degrees(self):
        """Test trigonometric functions in degrees"""
        self.calc.set_angle_mode('degrees')
        
        self.assertAlmostEqual(self.calc.sin(0), 0, places=10)
        self.assertAlmostEqual(self.calc.sin(90), 1, places=10)
        self.assertAlmostEqual(self.calc.cos(0), 1, places=10)
        self.assertAlmostEqual(self.calc.cos(180), -1, places=10)
        self.assertAlmostEqual(self.calc.tan(45), 1, places=10)
    
    def test_hyperbolic_functions(self):
        """Test hyperbolic functions"""
        self.assertAlmostEqual(self.calc.sinh(0), 0, places=10)
        self.assertAlmostEqual(self.calc.cosh(0), 1, places=10)
        self.assertAlmostEqual(self.calc.tanh(0), 0, places=10)
        
        # Inverse hyperbolic functions
        self.assertAlmostEqual(self.calc.asinh(0), 0, places=10)
        
        # Test invalid inputs
        with self.assertRaises(ValueError):
            self.calc.acosh(0.5)  # Must be >= 1
        with self.assertRaises(ValueError):
            self.calc.atanh(1)    # Must be in (-1, 1)
    
    def test_logarithmic_functions(self):
        """Test logarithmic functions"""
        # Natural logarithm
        self.assertAlmostEqual(self.calc.ln(math.e), 1, places=10)
        self.assertAlmostEqual(self.calc.ln(1), 0, places=10)
        
        # Common logarithm
        self.assertAlmostEqual(self.calc.log10(10), 1, places=10)
        self.assertAlmostEqual(self.calc.log10(100), 2, places=10)
        
        # Binary logarithm
        self.assertAlmostEqual(self.calc.log2(2), 1, places=10)
        self.assertAlmostEqual(self.calc.log2(8), 3, places=10)
        
        # Custom base logarithm
        self.assertAlmostEqual(self.calc.log(8, 2), 3, places=10)
        
        # Test invalid inputs
        with self.assertRaises(ValueError):
            self.calc.ln(0)
        with self.assertRaises(ValueError):
            self.calc.ln(-1)
    
    def test_exponential_functions(self):
        """Test exponential functions"""
        self.assertAlmostEqual(self.calc.exp(0), 1, places=10)
        self.assertAlmostEqual(self.calc.exp(1), math.e, places=10)
        self.assertEqual(self.calc.exp10(2), 100)
        self.assertEqual(self.calc.exp2(3), 8)
    
    def test_statistical_functions(self):
        """Test statistical and combinatorial functions"""
        # Factorial
        self.assertEqual(self.calc.factorial(0), 1)
        self.assertEqual(self.calc.factorial(1), 1)
        self.assertEqual(self.calc.factorial(5), 120)
        
        with self.assertRaises(ValueError):
            self.calc.factorial(-1)
        
        # Combinations
        self.assertEqual(self.calc.combination(5, 2), 10)
        self.assertEqual(self.calc.combination(5, 0), 1)
        self.assertEqual(self.calc.combination(5, 5), 1)
        
        # Permutations
        self.assertEqual(self.calc.permutation(5, 2), 20)
        self.assertEqual(self.calc.permutation(5, 0), 1)
        
        # GCD and LCM
        self.assertEqual(self.calc.gcd(48, 18), 6)
        self.assertEqual(self.calc.gcd(17, 13), 1)
        self.assertEqual(self.calc.lcm(4, 6), 12)
        self.assertEqual(self.calc.lcm(7, 5), 35)
    
    def test_utility_functions(self):
        """Test utility functions"""
        # Absolute value
        self.assertEqual(self.calc.absolute(-5), 5)
        self.assertEqual(self.calc.absolute(5), 5)
        self.assertEqual(self.calc.absolute(0), 0)
        
        # Floor and ceiling
        self.assertEqual(self.calc.floor(3.7), 3)
        self.assertEqual(self.calc.floor(-2.3), -3)
        self.assertEqual(self.calc.ceiling(3.2), 4)
        self.assertEqual(self.calc.ceiling(-2.7), -2)
        
        # Rounding
        self.assertEqual(self.calc.round_number(3.14159, 2), 3.14)
        self.assertEqual(self.calc.round_number(2.5), 2)
        
        # Modulo
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(15, 4), 3)
        
        with self.assertRaises(ZeroDivisionError):
            self.calc.modulo(10, 0)
    
    def test_angle_conversion(self):
        """Test angle conversion functions"""
        self.assertAlmostEqual(
            self.calc.degrees_to_radians(180), math.pi, places=10
        )
        self.assertAlmostEqual(
            self.calc.radians_to_degrees(math.pi), 180, places=10
        )
        self.assertAlmostEqual(
            self.calc.degrees_to_radians(90), math.pi/2, places=10
        )
    
    def test_memory_functions(self):
        """Test memory operations"""
        # Initial memory should be 0
        self.assertEqual(self.calc.memory_recall(), 0)
        
        # Store value
        self.calc.memory_store(42)
        self.assertEqual(self.calc.memory_recall(), 42)
        
        # Add to memory
        self.calc.memory_add(8)
        self.assertEqual(self.calc.memory_recall(), 50)
        
        # Subtract from memory
        self.calc.memory_subtract(15)
        self.assertEqual(self.calc.memory_recall(), 35)
        
        # Clear memory
        self.calc.memory_clear()
        self.assertEqual(self.calc.memory_recall(), 0)
    
    def test_angle_mode_setting(self):
        """Test angle mode setting"""
        # Default should be radians
        self.assertEqual(self.calc.angle_mode, 'radians')
        
        # Change to degrees
        self.calc.set_angle_mode('degrees')
        self.assertEqual(self.calc.angle_mode, 'degrees')
        
        # Change back to radians
        self.calc.set_angle_mode('radians')
        self.assertEqual(self.calc.angle_mode, 'radians')
        
        # Test invalid mode
        with self.assertRaises(ValueError):
            self.calc.set_angle_mode('invalid')
    
    def test_complex_numbers(self):
        """Test complex number operations"""
        z1 = complex(3, 4)
        z2 = complex(1, 2)
        
        # Complex addition
        result = self.calc.complex_add(z1, z2)
        self.assertEqual(result, complex(4, 6))
        
        # Complex multiplication
        result = self.calc.complex_multiply(z1, z2)
        self.assertEqual(result, complex(-5, 10))
        
        # Complex magnitude
        magnitude = self.calc.complex_magnitude(z1)
        self.assertAlmostEqual(magnitude, 5, places=10)
        
        # Complex phase
        phase = self.calc.complex_phase(z1)
        expected_phase = math.atan2(4, 3)
        self.assertAlmostEqual(phase, expected_phase, places=10)
    
    def test_constants(self):
        """Test mathematical constants"""
        constants = self.calc.get_constants()
        
        self.assertAlmostEqual(constants['π'], math.pi, places=10)
        self.assertAlmostEqual(constants['e'], math.e, places=10)
        self.assertAlmostEqual(constants['φ'], (1 + math.sqrt(5))/2, places=10)
        self.assertAlmostEqual(constants['√2'], math.sqrt(2), places=10)
    
    def test_history(self):
        """Test calculation history"""
        # Initially empty
        self.assertEqual(len(self.calc.get_history()), 0)
        
        # Perform some calculations
        self.calc.add(5, 3)
        self.calc.multiply(4, 7)
        
        # Check history
        history = self.calc.get_history()
        self.assertEqual(len(history), 2)
        self.assertIn("5 + 3 = 8", history[0])
        self.assertIn("4 × 7 = 28", history[1])
        
        # Clear history
        self.calc.clear_history()
        self.assertEqual(len(self.calc.get_history()), 0)


class TestCalculatorEdgeCases(unittest.TestCase):
    """Test edge cases and error conditions"""
    
    def setUp(self):
        self.calc = ScientificCalculator()
    
    def test_large_numbers(self):
        """Test with very large numbers"""
        large_num = 10**100
        result = self.calc.add(large_num, large_num)
        self.assertEqual(result, 2 * large_num)
    
    def test_very_small_numbers(self):
        """Test with very small numbers"""
        small_num = 10**-100
        result = self.calc.multiply(small_num, 2)
        self.assertEqual(result, 2 * small_num)
    
    def test_infinity_and_nan(self):
        """Test infinity and NaN handling"""
        # These should not raise exceptions but may return inf or nan
        result = self.calc.divide(1, 0.0)  # Should handle gracefully
        
    def test_precision_limits(self):
        """Test precision limits"""
        # Test that results are reasonably precise
        result = self.calc.divide(1, 3)
        self.assertAlmostEqual(result * 3, 1, places=10)


def run_tests():
    """Run all tests and display results"""
    print("=" * 60)
    print("🧪 RUNNING SCIENTIFIC CALCULATOR TESTS")
    print("=" * 60)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add test classes
    suite.addTests(loader.loadTestsFromTestCase(TestScientificCalculator))
    suite.addTests(loader.loadTestsFromTestCase(TestCalculatorEdgeCases))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 60)
    print("🏆 TEST RESULTS SUMMARY")
    print("=" * 60)
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.wasSuccessful():
        print("✅ ALL TESTS PASSED!")
    else:
        print("❌ SOME TESTS FAILED")
        if result.failures:
            print("\nFailures:")
            for test, traceback in result.failures:
                print(f"  - {test}: {traceback}")
        if result.errors:
            print("\nErrors:")
            for test, traceback in result.errors:
                print(f"  - {test}: {traceback}")
    
    print("=" * 60)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
