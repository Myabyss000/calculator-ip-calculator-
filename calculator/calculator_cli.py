"""
Command Line Interface for Scientific Calculator
Interactive calculator with advanced mathematical functions
"""

import sys
import re
from scientific_calculator import ScientificCalculator
import math

class CalculatorCLI:
    def __init__(self):
        self.calc = ScientificCalculator()
        self.running = True
        self.commands = {
            'help': self.show_help,
            'history': self.show_history,
            'clear': self.clear_screen,
            'memory': self.show_memory_commands,
            'constants': self.show_constants,
            'mode': self.change_angle_mode,
            'quit': self.quit_calculator,
            'exit': self.quit_calculator,
        }
    
    def run(self):
        """Main calculator loop"""
        self.show_welcome()
        
        while self.running:
            try:
                user_input = input("\n🧮 Calculator > ").strip()
                
                if not user_input:
                    continue
                
                # Check for special commands
                if user_input.lower() in self.commands:
                    self.commands[user_input.lower()]()
                    continue
                
                # Handle angle mode change
                if user_input.lower().startswith('mode '):
                    mode = user_input.split()[1]
                    self.change_angle_mode(mode)
                    continue
                
                # Evaluate mathematical expression
                result = self.evaluate_expression(user_input)
                if result is not None:
                    print(f"   = {result}")
                    
            except KeyboardInterrupt:
                print("\n\n👋 Calculator closed. Goodbye!")
                break
            except Exception as e:
                print(f"❌ Error: {str(e)}")
    
    def evaluate_expression(self, expression):
        """Evaluate mathematical expression"""
        try:
            # Handle special functions and constants
            expression = self.preprocess_expression(expression)
            
            # Handle memory operations
            if expression.upper() == 'MR':
                return self.calc.memory_recall()
            elif expression.upper() == 'MC':
                self.calc.memory_clear()
                return "Memory cleared"
            elif expression.upper().startswith('MS '):
                value = float(expression[3:])
                self.calc.memory_store(value)
                return f"Stored {value} in memory"
            elif expression.upper().startswith('M+ '):
                value = float(expression[3:])
                self.calc.memory_add(value)
                return f"Added {value} to memory (M = {self.calc.memory})"
            elif expression.upper().startswith('M- '):
                value = float(expression[3:])
                self.calc.memory_subtract(value)
                return f"Subtracted {value} from memory (M = {self.calc.memory})"
            
            # Use eval with restricted namespace for safety
            namespace = self.create_safe_namespace()
            result = eval(expression, namespace)
            
            return result
            
        except Exception as e:
            raise Exception(f"Invalid expression: {str(e)}")
    
    def preprocess_expression(self, expression):
        """Preprocess expression to handle special syntax"""
        # Replace common mathematical notations
        replacements = {
            'π': 'pi',
            '²': '**2',
            '³': '**3',
            '×': '*',
            '÷': '/',
            '√': 'sqrt',
        }
        
        for old, new in replacements.items():
            expression = expression.replace(old, new)
        
        # Handle implicit multiplication (e.g., 2π -> 2*π)
        expression = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expression)
        expression = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', expression)
        expression = re.sub(r'\)(\d)', r')*\1', expression)
        expression = re.sub(r'(\d)\(', r'\1*(', expression)
        
        return expression
    
    def create_safe_namespace(self):
        """Create a safe namespace for eval"""
        namespace = {
            # Basic math functions
            'abs': self.calc.absolute,
            'sqrt': self.calc.sqrt,
            'pow': self.calc.power,
            'exp': self.calc.exp,
            'log': self.calc.log,
            'log10': self.calc.log10,
            'log2': self.calc.log2,
            'ln': self.calc.ln,
            
            # Trigonometric functions
            'sin': self.calc.sin,
            'cos': self.calc.cos,
            'tan': self.calc.tan,
            'asin': self.calc.asin,
            'acos': self.calc.acos,
            'atan': self.calc.atan,
            'atan2': self.calc.atan2,
            
            # Hyperbolic functions
            'sinh': self.calc.sinh,
            'cosh': self.calc.cosh,
            'tanh': self.calc.tanh,
            'asinh': self.calc.asinh,
            'acosh': self.calc.acosh,
            'atanh': self.calc.atanh,
            
            # Other functions
            'ceil': self.calc.ceiling,
            'floor': self.calc.floor,
            'round': self.calc.round_number,
            'factorial': self.calc.factorial,
            'gcd': self.calc.gcd,
            'lcm': self.calc.lcm,
            
            # Constants
            'pi': math.pi,
            'e': math.e,
            'phi': (1 + math.sqrt(5)) / 2,
            
            # Built-in functions we want to allow
            '__builtins__': {},
        }
        return namespace
    
    def show_welcome(self):
        """Display welcome message"""
        print("=" * 60)
        print("🧮 SCIENTIFIC CALCULATOR")
        print("=" * 60)
        print("Welcome to the Advanced Scientific Calculator!")
        print(f"Current angle mode: {self.calc.angle_mode.upper()}")
        print("\nType 'help' for available commands and functions.")
        print("Type 'quit' or 'exit' to close the calculator.")
        print("=" * 60)
    
    def show_help(self):
        """Display help information"""
        help_text = """
📚 HELP - SCIENTIFIC CALCULATOR

🔢 BASIC OPERATIONS:
   +, -, *, /          Basic arithmetic
   ** or ^            Power (e.g., 2**3 or 2^3)
   % or mod           Modulo
   
🔬 SCIENTIFIC FUNCTIONS:
   sqrt(x)            Square root
   exp(x)             e^x
   log(x)             Natural logarithm (ln)
   log10(x)           Common logarithm (base 10)
   log2(x)            Binary logarithm (base 2)
   abs(x)             Absolute value
   ceil(x)            Ceiling function
   floor(x)           Floor function
   round(x, n)        Round to n decimal places
   factorial(n)       n! (factorial)
   gcd(a, b)          Greatest common divisor
   lcm(a, b)          Least common multiple
   
📐 TRIGONOMETRIC FUNCTIONS:
   sin(x), cos(x), tan(x)       Basic trig functions
   asin(x), acos(x), atan(x)    Inverse trig functions
   atan2(y, x)                  Two-argument arctangent
   sinh(x), cosh(x), tanh(x)    Hyperbolic functions
   asinh(x), acosh(x), atanh(x) Inverse hyperbolic functions
   
🔤 CONSTANTS:
   pi or π            Pi (3.14159...)
   e                  Euler's number (2.71828...)
   phi                Golden ratio (1.618...)
   
💾 MEMORY OPERATIONS:
   MS value           Store value in memory
   MR                 Recall memory value
   MC                 Clear memory
   M+ value           Add value to memory
   M- value           Subtract value from memory
   
🎛️  SPECIAL COMMANDS:
   help               Show this help
   history            Show calculation history
   memory             Show memory commands
   constants          Show available constants
   mode degrees       Switch to degree mode
   mode radians       Switch to radian mode
   clear              Clear screen
   quit/exit          Exit calculator
   
📝 EXAMPLES:
   sin(pi/2)          Sine of π/2
   sqrt(16)           Square root of 16
   2**8               2 to the power of 8
   log(e)             Natural log of e
   factorial(5)       5! = 120
   gcd(48, 18)        GCD of 48 and 18
        """
        print(help_text)
    
    def show_history(self):
        """Display calculation history"""
        history = self.calc.get_history()
        if not history:
            print("📝 No calculations in history.")
            return
        
        print("\n📜 CALCULATION HISTORY:")
        print("-" * 40)
        for i, calculation in enumerate(history[-10:], 1):  # Show last 10
            print(f"{i:2d}. {calculation}")
        
        if len(history) > 10:
            print(f"... and {len(history) - 10} more calculations")
    
    def show_memory_commands(self):
        """Display memory commands"""
        print(f"""
💾 MEMORY COMMANDS:
   Current memory value: {self.calc.memory}
   
   MS <value>    Store value in memory
   MR            Recall memory value
   MC            Clear memory  
   M+ <value>    Add value to memory
   M- <value>    Subtract value from memory
   
   Example: MS 42  (stores 42 in memory)
        """)
    
    def show_constants(self):
        """Display available constants"""
        constants = self.calc.get_constants()
        print("\n🔢 MATHEMATICAL CONSTANTS:")
        print("-" * 30)
        for name, value in constants.items():
            print(f"{name:8s} = {value}")
    
    def change_angle_mode(self, mode=None):
        """Change angle mode"""
        if mode is None:
            mode = input("Enter angle mode (degrees/radians): ").strip()
        
        try:
            self.calc.set_angle_mode(mode)
            print(f"✅ Angle mode changed to: {self.calc.angle_mode.upper()}")
        except ValueError as e:
            print(f"❌ {str(e)}")
    
    def clear_screen(self):
        """Clear the screen"""
        import os
        os.system('cls' if os.name == 'nt' else 'clear')
        self.show_welcome()
    
    def quit_calculator(self):
        """Exit the calculator"""
        self.running = False
        print("\n👋 Thank you for using the Scientific Calculator!")
        print("Goodbye! 🧮")

def main():
    """Main function to start the calculator"""
    try:
        calculator = CalculatorCLI()
        calculator.run()
    except KeyboardInterrupt:
        print("\n\n👋 Calculator closed. Goodbye!")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
