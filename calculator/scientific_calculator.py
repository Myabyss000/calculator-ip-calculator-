"""
Scientific Calculator Module
A comprehensive calculator with basic arithmetic, trigonometric, logarithmic, 
and advanced mathematical functions.
"""

import math
import cmath
from typing import Union, List
from decimal import Decimal, getcontext

# Set precision for decimal calculations
getcontext().prec = 28

class ScientificCalculator:
    """A comprehensive scientific calculator class."""
    
    def __init__(self):
        self.memory = 0
        self.history = []
        self.angle_mode = 'radians'  # 'radians' or 'degrees'
    
    def set_angle_mode(self, mode: str):
        """Set angle mode to 'radians' or 'degrees'."""
        if mode.lower() in ['radians', 'degrees']:
            self.angle_mode = mode.lower()
        else:
            raise ValueError("Angle mode must be 'radians' or 'degrees'")
    
    def _convert_angle(self, angle: float) -> float:
        """Convert angle based on current angle mode."""
        if self.angle_mode == 'degrees':
            return math.radians(angle)
        return angle
    
    def _convert_from_radians(self, angle: float) -> float:
        """Convert angle from radians based on current angle mode."""
        if self.angle_mode == 'degrees':
            return math.degrees(angle)
        return angle
    
    def add_to_history(self, expression: str, result: Union[float, complex]):
        """Add calculation to history."""
        self.history.append(f"{expression} = {result}")
        if len(self.history) > 100:  # Keep only last 100 calculations
            self.history.pop(0)
    
    # Basic Arithmetic Operations
    def add(self, a: float, b: float) -> float:
        """Addition: a + b"""
        result = a + b
        self.add_to_history(f"{a} + {b}", result)
        return result
    
    def subtract(self, a: float, b: float) -> float:
        """Subtraction: a - b"""
        result = a - b
        self.add_to_history(f"{a} - {b}", result)
        return result
    
    def multiply(self, a: float, b: float) -> float:
        """Multiplication: a * b"""
        result = a * b
        self.add_to_history(f"{a} × {b}", result)
        return result
    
    def divide(self, a: float, b: float) -> float:
        """Division: a / b"""
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = a / b
        self.add_to_history(f"{a} ÷ {b}", result)
        return result
    
    def power(self, base: float, exponent: float) -> Union[float, complex]:
        """Power: base^exponent"""
        try:
            result = base ** exponent
            if isinstance(result, complex) and result.imag == 0:
                result = result.real
            self.add_to_history(f"{base}^{exponent}", result)
            return result
        except Exception as e:
            # Handle complex results
            result = complex(base) ** exponent
            self.add_to_history(f"{base}^{exponent}", result)
            return result
    
    def sqrt(self, x: float) -> Union[float, complex]:
        """Square root"""
        if x < 0:
            result = cmath.sqrt(x)
            self.add_to_history(f"√{x}", result)
            return result
        result = math.sqrt(x)
        self.add_to_history(f"√{x}", result)
        return result
    
    def nth_root(self, x: float, n: float) -> Union[float, complex]:
        """nth root of x"""
        return self.power(x, 1/n)
    
    # Trigonometric Functions
    def sin(self, x: float) -> float:
        """Sine function"""
        angle = self._convert_angle(x)
        result = math.sin(angle)
        self.add_to_history(f"sin({x})", result)
        return result
    
    def cos(self, x: float) -> float:
        """Cosine function"""
        angle = self._convert_angle(x)
        result = math.cos(angle)
        self.add_to_history(f"cos({x})", result)
        return result
    
    def tan(self, x: float) -> float:
        """Tangent function"""
        angle = self._convert_angle(x)
        result = math.tan(angle)
        self.add_to_history(f"tan({x})", result)
        return result
    
    def asin(self, x: float) -> float:
        """Arcsine function"""
        if x < -1 or x > 1:
            raise ValueError("Input must be between -1 and 1")
        result = math.asin(x)
        result = self._convert_from_radians(result)
        self.add_to_history(f"arcsin({x})", result)
        return result
    
    def acos(self, x: float) -> float:
        """Arccosine function"""
        if x < -1 or x > 1:
            raise ValueError("Input must be between -1 and 1")
        result = math.acos(x)
        result = self._convert_from_radians(result)
        self.add_to_history(f"arccos({x})", result)
        return result
    
    def atan(self, x: float) -> float:
        """Arctangent function"""
        result = math.atan(x)
        result = self._convert_from_radians(result)
        self.add_to_history(f"arctan({x})", result)
        return result
    
    def atan2(self, y: float, x: float) -> float:
        """Two-argument arctangent function"""
        result = math.atan2(y, x)
        result = self._convert_from_radians(result)
        self.add_to_history(f"atan2({y}, {x})", result)
        return result
    
    # Hyperbolic Functions
    def sinh(self, x: float) -> float:
        """Hyperbolic sine"""
        result = math.sinh(x)
        self.add_to_history(f"sinh({x})", result)
        return result
    
    def cosh(self, x: float) -> float:
        """Hyperbolic cosine"""
        result = math.cosh(x)
        self.add_to_history(f"cosh({x})", result)
        return result
    
    def tanh(self, x: float) -> float:
        """Hyperbolic tangent"""
        result = math.tanh(x)
        self.add_to_history(f"tanh({x})", result)
        return result
    
    def asinh(self, x: float) -> float:
        """Inverse hyperbolic sine"""
        result = math.asinh(x)
        self.add_to_history(f"asinh({x})", result)
        return result
    
    def acosh(self, x: float) -> float:
        """Inverse hyperbolic cosine"""
        if x < 1:
            raise ValueError("Input must be >= 1")
        result = math.acosh(x)
        self.add_to_history(f"acosh({x})", result)
        return result
    
    def atanh(self, x: float) -> float:
        """Inverse hyperbolic tangent"""
        if x <= -1 or x >= 1:
            raise ValueError("Input must be between -1 and 1 (exclusive)")
        result = math.atanh(x)
        self.add_to_history(f"atanh({x})", result)
        return result
    
    # Logarithmic Functions
    def log(self, x: float, base: float = math.e) -> float:
        """Logarithm with specified base (default: natural log)"""
        if x <= 0:
            raise ValueError("Input must be positive")
        if base <= 0 or base == 1:
            raise ValueError("Base must be positive and not equal to 1")
        
        if base == math.e:
            result = math.log(x)
            self.add_to_history(f"ln({x})", result)
        else:
            result = math.log(x, base)
            self.add_to_history(f"log_{base}({x})", result)
        return result
    
    def log10(self, x: float) -> float:
        """Common logarithm (base 10)"""
        if x <= 0:
            raise ValueError("Input must be positive")
        result = math.log10(x)
        self.add_to_history(f"log({x})", result)
        return result
    
    def log2(self, x: float) -> float:
        """Binary logarithm (base 2)"""
        if x <= 0:
            raise ValueError("Input must be positive")
        result = math.log2(x)
        self.add_to_history(f"log₂({x})", result)
        return result
    
    def ln(self, x: float) -> float:
        """Natural logarithm (base e)"""
        return self.log(x)
    
    # Exponential Functions
    def exp(self, x: float) -> float:
        """Exponential function (e^x)"""
        result = math.exp(x)
        self.add_to_history(f"e^{x}", result)
        return result
    
    def exp10(self, x: float) -> float:
        """10^x"""
        result = 10 ** x
        self.add_to_history(f"10^{x}", result)
        return result
    
    def exp2(self, x: float) -> float:
        """2^x"""
        result = 2 ** x
        self.add_to_history(f"2^{x}", result)
        return result
    
    # Statistical Functions
    def factorial(self, n: int) -> int:
        """Factorial of n"""
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        if not isinstance(n, int) and not n.is_integer():
            raise ValueError("Factorial is only defined for integers")
        n = int(n)
        result = math.factorial(n)
        self.add_to_history(f"{n}!", result)
        return result
    
    def combination(self, n: int, r: int) -> int:
        """Combination: C(n,r) = n!/(r!(n-r)!)"""
        if n < 0 or r < 0:
            raise ValueError("n and r must be non-negative")
        if r > n:
            return 0
        result = math.comb(n, r)
        self.add_to_history(f"C({n},{r})", result)
        return result
    
    def permutation(self, n: int, r: int) -> int:
        """Permutation: P(n,r) = n!/(n-r)!"""
        if n < 0 or r < 0:
            raise ValueError("n and r must be non-negative")
        if r > n:
            return 0
        result = math.perm(n, r)
        self.add_to_history(f"P({n},{r})", result)
        return result
    
    def gcd(self, a: int, b: int) -> int:
        """Greatest Common Divisor"""
        result = math.gcd(a, b)
        self.add_to_history(f"gcd({a},{b})", result)
        return result
    
    def lcm(self, a: int, b: int) -> int:
        """Least Common Multiple"""
        result = abs(a * b) // math.gcd(a, b) if a != 0 and b != 0 else 0
        self.add_to_history(f"lcm({a},{b})", result)
        return result
    
    # Other Mathematical Functions
    def absolute(self, x: float) -> float:
        """Absolute value"""
        result = abs(x)
        self.add_to_history(f"|{x}|", result)
        return result
    
    def ceiling(self, x: float) -> int:
        """Ceiling function"""
        result = math.ceil(x)
        self.add_to_history(f"ceil({x})", result)
        return result
    
    def floor(self, x: float) -> int:
        """Floor function"""
        result = math.floor(x)
        self.add_to_history(f"floor({x})", result)
        return result
    
    def round_number(self, x: float, digits: int = 0) -> float:
        """Round to specified decimal places"""
        result = round(x, digits)
        self.add_to_history(f"round({x},{digits})", result)
        return result
    
    def modulo(self, a: float, b: float) -> float:
        """Modulo operation"""
        if b == 0:
            raise ZeroDivisionError("Cannot perform modulo with zero")
        result = a % b
        self.add_to_history(f"{a} mod {b}", result)
        return result
    
    def degrees_to_radians(self, degrees: float) -> float:
        """Convert degrees to radians"""
        result = math.radians(degrees)
        self.add_to_history(f"{degrees}° to rad", result)
        return result
    
    def radians_to_degrees(self, radians: float) -> float:
        """Convert radians to degrees"""
        result = math.degrees(radians)
        self.add_to_history(f"{radians} rad to °", result)
        return result
    
    # Memory Functions
    def memory_store(self, value: float):
        """Store value in memory"""
        self.memory = value
        self.add_to_history(f"M = {value}", "stored")
    
    def memory_recall(self) -> float:
        """Recall value from memory"""
        self.add_to_history("MR", self.memory)
        return self.memory
    
    def memory_clear(self):
        """Clear memory"""
        self.memory = 0
        self.add_to_history("MC", "cleared")
    
    def memory_add(self, value: float):
        """Add value to memory"""
        self.memory += value
        self.add_to_history(f"M+ {value}", self.memory)
    
    def memory_subtract(self, value: float):
        """Subtract value from memory"""
        self.memory -= value
        self.add_to_history(f"M- {value}", self.memory)
    
    # Utility Functions
    def clear_history(self):
        """Clear calculation history"""
        self.history = []
    
    def get_history(self) -> List[str]:
        """Get calculation history"""
        return self.history.copy()
    
    def get_constants(self) -> dict:
        """Get mathematical constants"""
        return {
            'π': math.pi,
            'e': math.e,
            'φ': (1 + math.sqrt(5)) / 2,  # Golden ratio
            '√2': math.sqrt(2),
            '√3': math.sqrt(3),
            '√5': math.sqrt(5),
            'ln(2)': math.log(2),
            'ln(10)': math.log(10),
        }
    
    # Complex number operations
    def complex_add(self, a: complex, b: complex) -> complex:
        """Add complex numbers"""
        result = a + b
        self.add_to_history(f"({a}) + ({b})", result)
        return result
    
    def complex_multiply(self, a: complex, b: complex) -> complex:
        """Multiply complex numbers"""
        result = a * b
        self.add_to_history(f"({a}) × ({b})", result)
        return result
    
    def complex_magnitude(self, z: complex) -> float:
        """Magnitude of complex number"""
        result = abs(z)
        self.add_to_history(f"|{z}|", result)
        return result
    
    def complex_phase(self, z: complex) -> float:
        """Phase of complex number"""
        result = cmath.phase(z)
        result = self._convert_from_radians(result)
        self.add_to_history(f"arg({z})", result)
        return result
