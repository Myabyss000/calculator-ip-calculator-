"""
Scientific Calculator Demo
Showcase various calculator capabilities
"""

from scientific_calculator import ScientificCalculator
import math

def demonstrate_calculator():
    """Demonstrate calculator capabilities"""
    calc = ScientificCalculator()
    
    print("🧮 SCIENTIFIC CALCULATOR DEMONSTRATION")
    print("=" * 60)
    
    # Basic Operations
    print("\n📊 BASIC OPERATIONS:")
    print(f"Addition: 15 + 27 = {calc.add(15, 27)}")
    print(f"Subtraction: 100 - 37 = {calc.subtract(100, 37)}")
    print(f"Multiplication: 12 × 8 = {calc.multiply(12, 8)}")
    print(f"Division: 144 ÷ 12 = {calc.divide(144, 12)}")
    print(f"Power: 2^10 = {calc.power(2, 10)}")
    print(f"Square Root: √169 = {calc.sqrt(169)}")
    
    # Trigonometric Functions
    print("\n📐 TRIGONOMETRIC FUNCTIONS (Radians):")
    calc.set_angle_mode('radians')
    print(f"sin(π/2) = {calc.sin(math.pi/2)}")
    print(f"cos(π) = {calc.cos(math.pi)}")
    print(f"tan(π/4) = {calc.tan(math.pi/4)}")
    
    print("\n📐 TRIGONOMETRIC FUNCTIONS (Degrees):")
    calc.set_angle_mode('degrees')
    print(f"sin(90°) = {calc.sin(90)}")
    print(f"cos(180°) = {calc.cos(180)}")
    print(f"tan(45°) = {calc.tan(45)}")
    
    # Logarithmic Functions
    print("\n📈 LOGARITHMIC & EXPONENTIAL FUNCTIONS:")
    print(f"Natural log: ln(e) = {calc.ln(math.e)}")
    print(f"Common log: log₁₀(1000) = {calc.log10(1000)}")
    print(f"Binary log: log₂(256) = {calc.log2(256)}")
    print(f"Exponential: e^2 = {calc.exp(2)}")
    print(f"Power of 10: 10^3 = {calc.exp10(3)}")
    
    # Advanced Functions
    print("\n🎯 ADVANCED MATHEMATICAL FUNCTIONS:")
    print(f"Factorial: 7! = {calc.factorial(7)}")
    print(f"Combinations: C(10,3) = {calc.combination(10, 3)}")
    print(f"Permutations: P(10,3) = {calc.permutation(10, 3)}")
    print(f"GCD: gcd(48, 18) = {calc.gcd(48, 18)}")
    print(f"LCM: lcm(12, 18) = {calc.lcm(12, 18)}")
    
    # Hyperbolic Functions
    print("\n🌊 HYPERBOLIC FUNCTIONS:")
    print(f"sinh(1) = {calc.sinh(1):.6f}")
    print(f"cosh(1) = {calc.cosh(1):.6f}")
    print(f"tanh(1) = {calc.tanh(1):.6f}")
    
    # Utility Functions
    print("\n🔧 UTILITY FUNCTIONS:")
    print(f"Absolute: |−42| = {calc.absolute(-42)}")
    print(f"Ceiling: ceil(3.14) = {calc.ceiling(3.14)}")
    print(f"Floor: floor(3.14) = {calc.floor(3.14)}")
    print(f"Round: round(3.14159, 3) = {calc.round_number(3.14159, 3)}")
    
    # Memory Operations
    print("\n💾 MEMORY OPERATIONS:")
    calc.memory_store(42)
    print(f"Stored 42 in memory")
    calc.memory_add(8)
    print(f"Added 8 to memory: {calc.memory_recall()}")
    calc.memory_subtract(15)
    print(f"Subtracted 15 from memory: {calc.memory_recall()}")
    
    # Complex Numbers
    print("\n🔢 COMPLEX NUMBER OPERATIONS:")
    z1 = complex(3, 4)
    z2 = complex(1, 2)
    print(f"z1 = {z1}, z2 = {z2}")
    print(f"z1 + z2 = {calc.complex_add(z1, z2)}")
    print(f"z1 × z2 = {calc.complex_multiply(z1, z2)}")
    print(f"|z1| = {calc.complex_magnitude(z1)}")
    
    # Constants
    print("\n🔤 MATHEMATICAL CONSTANTS:")
    constants = calc.get_constants()
    for name, value in constants.items():
        if len(name) <= 5:  # Show shorter constant names
            print(f"{name} = {value:.10g}")
    
    # History
    print(f"\n📜 CALCULATION HISTORY (last 5):")
    history = calc.get_history()
    for calculation in history[-5:]:
        print(f"  {calculation}")
    
    print("\n" + "=" * 60)
    print("✨ Demonstration complete!")
    print("Run 'python main.py' to start the interactive calculator.")
    print("Choose between GUI and CLI interfaces.")

if __name__ == "__main__":
    demonstrate_calculator()
