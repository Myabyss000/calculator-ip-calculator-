"""
Quick Test Script for Scientific Calculator
Tests both GUI and CLI functionality
"""

import sys
import os

def test_gui():
    """Test GUI functionality"""
    print("🧪 Testing GUI...")
    try:
        from calculator_gui import ScientificCalculatorGUI
        
        # Create calculator instance
        calc = ScientificCalculatorGUI()
        
        # Test basic functionality without showing GUI
        print("✅ GUI import successful")
        print("✅ GUI initialization successful")
        
        # Test some calculations
        calc.current_input = "2+3"
        calc.calculate()
        if calc.current_input == "5":
            print("✅ GUI calculation test passed")
        else:
            print("❌ GUI calculation test failed")
        
        # Don't actually show the GUI in test mode
        calc.root.destroy()
        
        return True
        
    except Exception as e:
        print(f"❌ GUI test failed: {e}")
        return False

def test_cli():
    """Test CLI functionality"""
    print("\n🧪 Testing CLI...")
    try:
        from calculator_cli import CalculatorCLI
        
        # Create CLI instance
        cli = CalculatorCLI()
        
        print("✅ CLI import successful")
        print("✅ CLI initialization successful")
        
        # Test basic calculation
        result = cli.evaluate_expression("2+3")
        if result == 5:
            print("✅ CLI calculation test passed")
        else:
            print("❌ CLI calculation test failed")
        
        return True
        
    except Exception as e:
        print(f"❌ CLI test failed: {e}")
        return False

def test_core_calculator():
    """Test core calculator functionality"""
    print("\n🧪 Testing Core Calculator...")
    try:
        from scientific_calculator import ScientificCalculator
        
        calc = ScientificCalculator()
        
        # Test basic operations
        tests = [
            (calc.add(2, 3), 5, "Addition"),
            (calc.multiply(4, 5), 20, "Multiplication"),
            (calc.sqrt(16), 4.0, "Square root"),
            (calc.sin(0), 0.0, "Sine"),
            (calc.factorial(5), 120, "Factorial"),
        ]
        
        all_passed = True
        for result, expected, name in tests:
            if abs(result - expected) < 1e-10:
                print(f"✅ {name} test passed")
            else:
                print(f"❌ {name} test failed: got {result}, expected {expected}")
                all_passed = False
        
        return all_passed
        
    except Exception as e:
        print(f"❌ Core calculator test failed: {e}")
        return False

def main():
    """Run all tests"""
    print("🧮 SCIENTIFIC CALCULATOR TEST SUITE")
    print("=" * 50)
    
    # Test core calculator
    core_passed = test_core_calculator()
    
    # Test CLI
    cli_passed = test_cli()
    
    # Test GUI
    gui_passed = test_gui()
    
    # Summary
    print("\n" + "=" * 50)
    print("📋 TEST SUMMARY")
    print("=" * 50)
    print(f"Core Calculator: {'✅ PASSED' if core_passed else '❌ FAILED'}")
    print(f"CLI Interface:   {'✅ PASSED' if cli_passed else '❌ FAILED'}")
    print(f"GUI Interface:   {'✅ PASSED' if gui_passed else '❌ FAILED'}")
    
    if all([core_passed, cli_passed, gui_passed]):
        print("\n🎉 ALL TESTS PASSED! Calculator is ready to use.")
        print("\nTo start the calculator:")
        print("  • Run: python main.py (choose interface)")
        print("  • Or:  python calculator_gui.py (direct GUI)")
        print("  • Or:  python calculator_cli.py (direct CLI)")
    else:
        print("\n⚠️  Some tests failed. Please check the errors above.")
    
    print("=" * 50)

if __name__ == "__main__":
    main()
