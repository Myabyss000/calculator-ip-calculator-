"""
Scientific Calculator Launcher
Choose between Command Line Interface or Graphical User Interface
"""

import sys
import os

def show_welcome():
    """Display welcome message and options"""
    print("=" * 60)
    print("🧮 SCIENTIFIC CALCULATOR")
    print("=" * 60)
    print("Welcome to the Advanced Scientific Calculator!")
    print("\nChoose your interface:")
    print("1. 📱 GUI (Graphical User Interface)")
    print("2. 💻 CLI (Command Line Interface)")
    print("3. 📡 IP Calculator (Network Tools)")
    print("4. ❓ Help")
    print("5. 🚪 Exit")
    print("=" * 60)

def show_help():
    """Display help information"""
    help_text = """
📚 CALCULATOR FEATURES:

🔢 BASIC OPERATIONS:
   • Addition, Subtraction, Multiplication, Division
   • Exponentiation, Square Root, nth Root
   • Modulo, Absolute Value

📐 TRIGONOMETRIC FUNCTIONS:
   • sin, cos, tan (with degree/radian support)
   • asin, acos, atan (inverse functions)
   • Hyperbolic functions (sinh, cosh, tanh)
   • Inverse hyperbolic functions

📊 LOGARITHMIC & EXPONENTIAL:
   • Natural logarithm (ln), Common log (log10)
   • Binary logarithm (log2), Custom base logarithm
   • Exponential functions (e^x, 10^x, 2^x)

🔬 ADVANCED FUNCTIONS:
   • Factorial, Combinations, Permutations
   • Greatest Common Divisor (GCD)
   • Least Common Multiple (LCM)
   • Floor, Ceiling, Rounding functions

💾 MEMORY OPERATIONS:
   • Store, Recall, Clear, Add, Subtract

📈 COMPLEX NUMBERS:
   • Basic complex arithmetic
   • Magnitude and phase calculations

🎯 INTERFACE OPTIONS:
   1. GUI - Point-and-click interface with buttons
      • Visual button layout
      • History panel
      • Memory indicator
      • Angle mode selection

   2. CLI - Command-line interface for advanced users
      • Type expressions directly
      • Command history
      • Extensive help system
      • Keyboard shortcuts

📝 EXPRESSION EXAMPLES:
   • sin(pi/2)         - Sine of π/2
   • sqrt(16)          - Square root of 16
   • log(e)            - Natural log of e
   • factorial(5)      - 5! = 120
   • 2**8              - 2 to the power of 8
   • gcd(48, 18)       - GCD of 48 and 18

Press Enter to continue...
    """
    print(help_text)
    try:
        input()
    except (EOFError, KeyboardInterrupt):
        pass

def launch_gui():
    """Launch the GUI version"""
    try:
        print("🚀 Starting GUI Calculator...")
        from calculator_gui import ScientificCalculatorGUI
        calculator = ScientificCalculatorGUI()
        calculator.run()
    except ImportError as e:
        print(f"❌ Error importing GUI: {e}")
        print("Make sure calculator_gui.py is in the same directory.")
    except Exception as e:
        print(f"❌ Error starting GUI: {e}")

def launch_cli():
    """Launch the CLI version"""
    try:
        print("🚀 Starting CLI Calculator...")
        from calculator_cli import CalculatorCLI
        calculator = CalculatorCLI()
        calculator.run()
    except ImportError as e:
        print(f"❌ Error importing CLI: {e}")
        print("Make sure calculator_cli.py is in the same directory.")
    except Exception as e:
        print(f"❌ Error starting CLI: {e}")

def launch_ip_calculator():
    """Launch the IP Calculator GUI"""
    try:
        print("🚀 Starting IP Calculator...")
        from ip_calculator_gui import IPCalculatorGUI
        calculator = IPCalculatorGUI()
        calculator.run()
    except ImportError as e:
        print(f"❌ Error importing IP Calculator: {e}")
        print("Make sure ip_calculator_gui.py is in the same directory.")
    except Exception as e:
        print(f"❌ Error starting IP Calculator: {e}")

def main():
    """Main launcher function"""
    while True:
        try:
            # Clear screen
            os.system('cls' if os.name == 'nt' else 'clear')
            
            show_welcome()
            
            try:
                choice = input("\n👆 Enter your choice (1-5): ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\n\n👋 Calculator closed. Goodbye!")
                break
            
            if choice == '1':
                launch_gui()
            elif choice == '2':
                launch_cli()
            elif choice == '3':
                launch_ip_calculator()
            elif choice == '4':
                show_help()
            elif choice == '5':
                print("\n👋 Thank you for using the Scientific Calculator!")
                print("Goodbye! 🧮")
                break
            else:
                print("\n❌ Invalid choice. Please enter 1, 2, 3, 4, or 5.")
                try:
                    input("Press Enter to continue...")
                except (EOFError, KeyboardInterrupt):
                    print("\n\n👋 Calculator closed. Goodbye!")
                    break
                
        except KeyboardInterrupt:
            print("\n\n👋 Calculator closed. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {str(e)}")
            try:
                input("Press Enter to continue...")
            except (EOFError, KeyboardInterrupt):
                print("\n\n👋 Calculator closed. Goodbye!")
                break

if __name__ == "__main__":
    main()
