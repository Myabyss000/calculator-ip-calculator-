# 🧮 Scientific Calculator

A comprehensive scientific calculator with **Command Line Interface (CLI)**, **Graphical User Interface (GUI)**, and **IP Calculator** written in Python. This all-in-one calculator supports advanced mathematical operations, trigonometry, logarithms, statistics, complex numbers, and network calculations.

## ✨ Features

### 🔢 Basic Operations
- Addition, Subtraction, Multiplication, Division
- Exponentiation and Root operations
- Modulo operations
- Absolute value calculations

### 📐 Trigonometric Functions
- Basic: `sin`, `cos`, `tan`
- Inverse: `asin`, `acos`, `atan`, `atan2`
- Hyperbolic: `sinh`, `cosh`, `tanh`
- Inverse Hyperbolic: `asinh`, `acosh`, `atanh`
- Support for both **degrees** and **radians**

### 📊 Logarithmic & Exponential Functions
- Natural logarithm: `ln(x)`
- Common logarithm: `log10(x)`
- Binary logarithm: `log2(x)`
- Custom base logarithm: `log(x, base)`
- Exponential functions: `e^x`, `10^x`, `2^x`

### 🎯 Advanced Mathematical Functions
- **Factorial**: `n!`
- **Combinations**: `C(n,r)`
- **Permutations**: `P(n,r)`
- **GCD**: Greatest Common Divisor
- **LCM**: Least Common Multiple
- **Floor, Ceiling, Rounding** functions

### 🔢 Complex Number Support
- Basic complex arithmetic
- Magnitude and phase calculations
- Complex exponential functions

### 📡 IP Calculator (NEW!)
- **IP Address Validation**: IPv4 and IPv6 support
- **Network Analysis**: Subnet calculations and splitting
- **Address Conversion**: Binary, decimal, dotted-decimal formats
- **Subnet Planning**: Host calculations and range analysis
- **Common Networks**: RFC standard references and port information
- **Advanced Features**: Wildcard masks, network summarization

### 💾 Memory Operations
- **MS**: Memory Store
- **MR**: Memory Recall  
- **MC**: Memory Clear
- **M+**: Memory Add
- **M-**: Memory Subtract

### 🎛️ Additional Features
- **Calculation History**: Track all calculations
- **Mathematical Constants**: π, e, φ (golden ratio), √2, etc.
- **Angle Mode Selection**: Switch between degrees and radians
- **Error Handling**: Comprehensive error messages
- **High Precision**: Uses Python's decimal module for precision

## 🚀 Getting Started

### Prerequisites
- Python 3.7 or higher
- tkinter (usually comes with Python installation)

### Installation
1. Clone or download this repository:
```bash
git clone <repository-url>
# or download and extract the ZIP file
```

2. Navigate to the calculator directory:
```bash
cd calculator
```

3. No additional packages needed! The calculator uses only Python's standard library.

### Running the Calculator

#### Option 1: Launch Menu (Recommended)
```bash
python main.py
```
Choose from the main menu:
- **1**: 📱 GUI (Graphical User Interface)
- **2**: 💻 CLI (Command Line Interface)
- **3**: 📡 IP Calculator (Network Tools)
- **4**: ❓ Help
- **5**: 🚪 Exit

#### Option 2: Direct Launch
```bash
# For GUI Scientific Calculator
python calculator_gui.py

# For CLI Scientific Calculator
python calculator_cli.py

# For IP Calculator GUI
python ip_calculator_gui.py
```

#### Option 3: Quick Test
```bash
# Run tests to verify everything works
python quick_test.py

# Run IP Calculator demo
python ip_calculator_demo.py
```

## 🖥️ User Interfaces

### GUI (Graphical User Interface)
- **Modern dark theme** with professional color scheme
- **Enhanced display panel** with secondary expression preview
- **Color-coded button layout** for easy function identification:
  - 🔢 **Gray buttons**: Numbers (0-9, decimal point)
  - 🔴 **Red buttons**: Basic operators (+, -, ×, ÷)
  - 🔵 **Blue buttons**: Scientific functions (sin, cos, log, etc.)
  - 🟢 **Green buttons**: Special functions (constants, memory)
  - 🟠 **Orange buttons**: Clear and delete operations
- **Visual button hierarchy** with hover effects and professional styling
- **Memory indicator** showing current memory value with icon
- **Angle mode selector** with visual RAD/DEG indicator
- **Interactive history panel** with scrollable calculations
- **Keyboard shortcuts** support for all operations
- **Responsive design** that adapts to window resizing
- **Enhanced typography** using modern Segoe UI font
- **Mathematical Unicode symbols** for better readability

![GUI Screenshot](gui_screenshot.png)

### CLI (Command Line Interface)
- **Interactive prompt** for direct expression entry
- **Extensive help system** with command reference
- **Command history** tracking
- **Memory operations** with simple commands
- **Multiple output formats** for different number types
- **Error handling** with detailed messages

```bash
🧮 Calculator > sin(pi/2)
   = 1.0

🧮 Calculator > factorial(5)  
   = 120

🧮 Calculator > help
# Shows comprehensive help documentation
```

## 📝 Usage Examples

### Basic Arithmetic
```python
# GUI: Click buttons or type
# CLI: Type directly
2 + 3 * 4        # = 14
(5 + 3) / 2      # = 4.0
2**8             # = 256
sqrt(16)         # = 4.0
```

### Trigonometry
```python
sin(pi/2)        # = 1.0 (radians mode)
sin(90)          # = 1.0 (degrees mode)  
cos(0)           # = 1.0
tan(pi/4)        # = 1.0
asin(0.5)        # = 0.5236 (radians) or 30° (degrees)
```

### Logarithms & Exponentials
```python
ln(e)            # = 1.0
log10(100)       # = 2.0
log2(8)          # = 3.0
exp(1)           # = 2.718...
10**(2)          # = 100
```

### Advanced Functions
```python
factorial(5)     # = 120
gcd(48, 18)      # = 6
lcm(4, 6)        # = 12
combination(5,2) # = 10
permutation(5,2) # = 20
```

### Memory Operations
```python
# CLI commands
MS 42            # Store 42 in memory
MR               # Recall memory (returns 42)
M+ 8             # Add 8 to memory (now 50)
M- 15            # Subtract 15 from memory (now 35)  
MC               # Clear memory

# GUI: Use M buttons
```

## 🎛️ Commands Reference

### CLI Special Commands
| Command | Description |
|---------|-------------|
| `help` | Show comprehensive help |
| `history` | Display calculation history |
| `memory` | Show memory commands |
| `constants` | Display mathematical constants |
| `mode degrees` | Switch to degree mode |
| `mode radians` | Switch to radian mode |
| `clear` | Clear screen |
| `quit` / `exit` | Exit calculator |

### Mathematical Constants
| Symbol | Value | Description |
|--------|-------|-------------|
| `π` or `pi` | 3.14159... | Pi |
| `e` | 2.71828... | Euler's number |
| `φ` or `phi` | 1.61803... | Golden ratio |

## 🧪 Testing

Run the comprehensive test suite to verify all functions work correctly:

```bash
python test_calculator.py
```

The test suite includes:
- ✅ Basic arithmetic operations
- ✅ Trigonometric functions (degrees/radians)
- ✅ Logarithmic and exponential functions
- ✅ Statistical functions
- ✅ Memory operations
- ✅ Complex number operations
- ✅ Edge cases and error handling
- ✅ Precision and accuracy tests

## 📁 Project Structure
```
calculator/
│
├── 🚀 main.py                    # Main launcher (choose GUI/CLI/IP Calc)
├── 🧮 scientific_calculator.py   # Core calculator engine  
├── 🖥️ calculator_gui.py          # GUI interface (tkinter)
├── 💻 calculator_cli.py          # CLI interface
├── 📡 ip_calculator.py           # IP/Network calculation engine
├── 🌐 ip_calculator_gui.py       # IP Calculator GUI interface
├── � ip_calculator_demo.py      # IP Calculator demonstration
├── 📘 IP_CALCULATOR_GUIDE.md     # IP Calculator documentation
├── 🧪 test_calculator.py         # Comprehensive test suite
├── ⚡ quick_test.py              # Quick functionality test
├── 📋 requirements.txt           # Dependencies (Python stdlib only)
├── 📖 README.md                  # Complete documentation
└── 📜 LICENSE                    # MIT License
```

## 🔧 Customization

### Adding New Functions
1. Add the mathematical function to `ScientificCalculator` class
2. Update the GUI buttons in `calculator_gui.py`
3. Add CLI support in `calculator_cli.py`
4. Write tests in `test_calculator.py`

### Modifying the GUI
- Edit `calculator_gui.py`
- Modify button layout in `create_button_frame()`
- Adjust colors in the `colors` dictionary
- Add new functionality to button callbacks

### Extending the CLI
- Edit `calculator_cli.py`
- Add new commands to the `commands` dictionary
- Extend the `preprocess_expression()` function for new syntax
- Update the help documentation

## 🐛 Error Handling

The calculator includes comprehensive error handling for:
- **Division by zero**: Clear error messages
- **Invalid inputs**: Type validation and range checking
- **Mathematical domain errors**: e.g., sqrt of negative numbers
- **Overflow/Underflow**: Large number handling
- **Invalid expressions**: Syntax error detection
- **Memory operations**: Safe memory access

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature-name`
3. **Add tests** for new functionality
4. **Ensure** all tests pass: `python test_calculator.py`
5. **Update** documentation as needed
6. **Submit** a pull request

### Areas for Enhancement
- [ ] **Graphing capabilities** for function plotting
- [ ] **Equation solver** for algebraic equations
- [ ] **Unit conversions** (length, weight, temperature)
- [ ] **Financial calculations** (interest, loans, etc.)
- [ ] **Matrix operations** (determinant, inverse, etc.)
- [ ] **Statistical analysis** (mean, median, standard deviation)
- [ ] **Export functionality** (save history to file)
- [ ] **Themes** for GUI customization

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Built using **Python's standard library** only
- **tkinter** for the graphical interface  
- **math** and **cmath** modules for mathematical functions
- **unittest** framework for testing
- Inspired by scientific calculators and the need for a comprehensive Python-based solution

## 📞 Support

If you encounter any issues or have questions:

1. **Check** the help documentation (`help` command in CLI)
2. **Run** the test suite to verify installation
3. **Review** error messages for troubleshooting hints
4. **Create** an issue in the repository for bugs or feature requests

---

**Happy Calculating!** 🧮✨

*Made with ❤️ in Python*
