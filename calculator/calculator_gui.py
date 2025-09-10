"""
GUI Scientific Calculator using tkinter
A comprehensive graphical calculator with advanced mathematical functions
"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import math
from scientific_calculator import ScientificCalculator
from ip_calculator_gui import IPCalculatorGUI

class ScientificCalculatorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.calc = ScientificCalculator()
        self.current_input = ""
        self.result_displayed = False
        
        # Theme settings
        self.themes = {
            'dark': {
                'bg_primary': '#1a1a1a',
                'bg_secondary': '#2d2d2d', 
                'bg_tertiary': '#404040',
                'text_primary': '#ffffff',
                'text_secondary': '#888888',
                'accent_green': '#00d4aa',
                'accent_red': '#ff6b6b',
                'accent_blue': '#4ecdc4',
                'accent_orange': '#ff8a65',
                'accent_purple': '#a8e6cf'
            },
            'light': {
                'bg_primary': '#f5f5f5',
                'bg_secondary': '#ffffff',
                'bg_tertiary': '#e0e0e0',
                'text_primary': '#333333',
                'text_secondary': '#666666',
                'accent_green': '#00a693',
                'accent_red': '#d32f2f',
                'accent_blue': '#00acc1',
                'accent_orange': '#ff5722',
                'accent_purple': '#7cb342'
            }
        }
        self.current_theme = 'dark'
        
        self.setup_window()
        self.create_variables()
        self.create_widgets()
        self.setup_bindings()
    
    def setup_window(self):
        """Setup main window properties"""
        self.root.title("🧮 Scientific Calculator Pro")
        self.root.geometry("900x750")
        self.root.resizable(True, True)
        self.root.configure(bg='#1a1a1a')  # Darker, more modern background
        self.root.minsize(800, 650)
        
        # Set icon and styling
        try:
            self.root.iconname("Calculator")
        except:
            pass
        
        # Center the window
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
        # Configure style for ttk widgets
        self.style = ttk.Style()
        self.style.theme_use('clam')
    
    def create_variables(self):
        """Create tkinter variables"""
        self.display_var = tk.StringVar(value="0")
        self.angle_mode_var = tk.StringVar(value="Radians")
        self.memory_var = tk.StringVar(value="M: 0")
    
    def create_widgets(self):
        """Create all GUI widgets"""
        self.create_display()
        self.create_mode_frame()
        self.create_button_frame()
        self.create_history_frame()
    
    def create_display(self):
        """Create the display area"""
        # Main display container with gradient-like effect
        display_container = tk.Frame(self.root, bg='#1a1a1a', pady=15)
        display_container.pack(fill=tk.X, padx=15)
        
        # Display frame with rounded corner effect
        display_frame = tk.Frame(
            display_container, 
            bg='#2d2d2d', 
            bd=2, 
            relief=tk.GROOVE,
            pady=15,
            padx=15
        )
        display_frame.pack(fill=tk.X)
        
        # Secondary display for expression/history
        self.secondary_display = tk.Label(
            display_frame,
            text="",
            font=('Segoe UI', 11),
            bg='#2d2d2d',
            fg='#888888',
            anchor='e',
            justify='right'
        )
        self.secondary_display.pack(fill=tk.X, pady=(0, 5))
        
        # Main display with better styling
        self.display = tk.Entry(
            display_frame,
            textvariable=self.display_var,
            font=('Segoe UI', 22, 'bold'),
            justify='right',
            state='readonly',
            bg='#2d2d2d',
            fg='#ffffff',
            bd=0,
            relief=tk.FLAT,
            readonlybackground='#2d2d2d',
            selectbackground='#404040',
            selectforeground='#ffffff'
        )
        self.display.pack(fill=tk.X, pady=(0, 10), ipady=8)
        
        # Status bar with memory and mode info
        status_frame = tk.Frame(display_frame, bg='#2d2d2d')
        status_frame.pack(fill=tk.X, pady=(5, 0))
        
        # Memory indicator with icon
        self.memory_label = tk.Label(
            status_frame,
            textvariable=self.memory_var,
            font=('Segoe UI', 10, 'bold'),
            bg='#2d2d2d',
            fg='#00d4aa',
            anchor='w'
        )
        self.memory_label.pack(side=tk.LEFT)
        
        # Mode indicator
        self.mode_label = tk.Label(
            status_frame,
            text="RAD",
            font=('Segoe UI', 10, 'bold'),
            bg='#2d2d2d',
            fg='#ff6b6b',
            anchor='e'
        )
        self.mode_label.pack(side=tk.RIGHT)
    
    def create_mode_frame(self):
        """Create mode selection frame"""
        mode_frame = tk.Frame(self.root, bg='#1a1a1a', pady=5)
        mode_frame.pack(fill=tk.X, padx=15)
        
        # Create a styled frame for the mode selector
        mode_container = tk.Frame(
            mode_frame, 
            bg='#2d2d2d', 
            bd=1, 
            relief=tk.SOLID,
            padx=15,
            pady=10
        )
        mode_container.pack(fill=tk.X)
        
        # Angle mode label with icon
        mode_icon = tk.Label(
            mode_container,
            text="🎯",
            font=('Segoe UI', 12),
            bg='#2d2d2d',
            fg='#ffffff'
        )
        mode_icon.pack(side=tk.LEFT, padx=(0, 8))
        
        tk.Label(
            mode_container,
            text="Angle Mode:",
            font=('Segoe UI', 11, 'bold'),
            bg='#2d2d2d',
            fg='#ffffff'
        ).pack(side=tk.LEFT)
        
        # Style the combobox
        self.style.configure(
            'Mode.TCombobox',
            fieldbackground='#404040',
            background='#404040',
            foreground='#ffffff',
            borderwidth=1,
            focuscolor='#00d4aa',
            selectbackground='#00d4aa',
            selectforeground='#ffffff'
        )
        
        mode_menu = ttk.Combobox(
            mode_container,
            textvariable=self.angle_mode_var,
            values=['Radians', 'Degrees'],
            state='readonly',
            width=12,
            font=('Segoe UI', 10),
            style='Mode.TCombobox'
        )
        mode_menu.pack(side=tk.LEFT, padx=(10, 0))
        mode_menu.bind('<<ComboboxSelected>>', self.change_angle_mode)
        
        # Add IP Calculator button
        ip_calc_btn = tk.Button(
            mode_container,
            text="📡 IP Calculator",
            font=('Segoe UI', 10, 'bold'),
            bg='#00d4aa',
            fg='#ffffff',
            bd=0,
            padx=15,
            pady=5,
            cursor='hand2',
            command=self.launch_ip_calculator,
            relief=tk.FLAT,
            activebackground='#00a693',
            activeforeground='#ffffff'
        )
        ip_calc_btn.pack(side=tk.RIGHT, padx=(10, 0))
        
        # Add hover effects to IP Calculator button
        def on_enter(e):
            ip_calc_btn.config(bg='#00a693')
        
        def on_leave(e):
            ip_calc_btn.config(bg='#00d4aa')
        
        ip_calc_btn.bind('<Enter>', on_enter)
        ip_calc_btn.bind('<Leave>', on_leave)
    
    def create_button_frame(self):
        """Create the button layout with modern styling"""
        button_frame = tk.Frame(self.root, bg='#1a1a1a', pady=10)
        button_frame.pack(fill=tk.BOTH, expand=True, padx=15)
        
        # Enhanced button configurations with modern styling
        btn_config = {
            'font': ('Segoe UI', 12, 'bold'),
            'bd': 0,
            'relief': tk.FLAT,
            'height': 2,
            'width': 8,
            'cursor': 'hand2'
        }
        
        # Modern color schemes with gradients and hover effects
        colors = {
            'number': {
                'bg': '#404040', 
                'fg': '#ffffff', 
                'activebackground': '#525252',
                'activeforeground': '#ffffff'
            },
            'operator': {
                'bg': '#ff6b6b', 
                'fg': '#ffffff', 
                'activebackground': '#ff5252',
                'activeforeground': '#ffffff'
            },
            'function': {
                'bg': '#4ecdc4', 
                'fg': '#ffffff', 
                'activebackground': '#42b8b3',
                'activeforeground': '#ffffff'
            },
            'special': {
                'bg': '#a8e6cf', 
                'fg': '#2d4a3e', 
                'activebackground': '#95d5b2',
                'activeforeground': '#2d4a3e'
            },
            'clear': {
                'bg': '#ff8a65', 
                'fg': '#ffffff', 
                'activebackground': '#ff7043',
                'activeforeground': '#ffffff'
            },
            'equals': {
                'bg': '#00d4aa', 
                'fg': '#ffffff', 
                'activebackground': '#00c49a',
                'activeforeground': '#ffffff'
            }
        }
        
        # Enhanced button layout with better organization
        buttons = [
            # Row 1 - Memory and Clear operations
            (0, 0, 'MC', lambda: self.memory_clear(), 'special', '🗑️ MC'),
            (0, 1, 'MR', lambda: self.memory_recall(), 'special', '📥 MR'),
            (0, 2, 'M+', lambda: self.memory_add(), 'special', '➕ M+'),
            (0, 3, 'M-', lambda: self.memory_subtract(), 'special', '➖ M-'),
            (0, 4, 'MS', lambda: self.memory_store(), 'special', '💾 MS'),
            (0, 5, 'AC', lambda: self.all_clear(), 'clear', '🧹 AC'),
            (0, 6, 'C', lambda: self.clear_entry(), 'clear', '⌫ C'),
            (0, 7, '←', lambda: self.backspace(), 'clear', '←'),
            
            # Row 2 - Primary trigonometric functions
            (1, 0, 'sin', lambda: self.add_function('sin('), 'function', 'sin'),
            (1, 1, 'cos', lambda: self.add_function('cos('), 'function', 'cos'),
            (1, 2, 'tan', lambda: self.add_function('tan('), 'function', 'tan'),
            (1, 3, 'ln', lambda: self.add_function('ln('), 'function', 'ln'),
            (1, 4, 'log', lambda: self.add_function('log10('), 'function', 'log₁₀'),
            (1, 5, 'eˣ', lambda: self.add_function('exp('), 'function', 'eˣ'),
            (1, 6, 'x²', lambda: self.add_text('²'), 'function', 'x²'),
            (1, 7, 'x³', lambda: self.add_text('³'), 'function', 'x³'),
            
            # Row 3 - Inverse trigonometric functions
            (2, 0, 'sin⁻¹', lambda: self.add_function('asin('), 'function', 'sin⁻¹'),
            (2, 1, 'cos⁻¹', lambda: self.add_function('acos('), 'function', 'cos⁻¹'),
            (2, 2, 'tan⁻¹', lambda: self.add_function('atan('), 'function', 'tan⁻¹'),
            (2, 3, '√x', lambda: self.add_function('sqrt('), 'function', '√x'),
            (2, 4, 'xʸ', lambda: self.add_text('**'), 'operator', 'xʸ'),
            (2, 5, '10ˣ', lambda: self.add_function('10**('), 'function', '10ˣ'),
            (2, 6, '1/x', lambda: self.reciprocal(), 'function', '1/x'),
            (2, 7, 'n!', lambda: self.factorial(), 'function', 'n!'),
            
            # Row 4 - Constants and basic operations
            (3, 0, 'π', lambda: self.add_text('π'), 'special', 'π'),
            (3, 1, 'e', lambda: self.add_text('e'), 'special', 'e'),
            (3, 2, '(', lambda: self.add_text('('), 'operator', '('),
            (3, 3, ')', lambda: self.add_text(')'), 'operator', ')'),
            (3, 4, 'mod', lambda: self.add_text('%'), 'operator', 'mod'),
            (3, 5, '|x|', lambda: self.add_function('abs('), 'function', '|x|'),
            (3, 6, '±', lambda: self.toggle_sign(), 'operator', '±'),
            (3, 7, '÷', lambda: self.add_text('/'), 'operator', '÷'),
            
            # Row 5 - Numbers 7,8,9 and multiplication
            (4, 0, '7', lambda: self.add_number('7'), 'number', '7'),
            (4, 1, '8', lambda: self.add_number('8'), 'number', '8'),
            (4, 2, '9', lambda: self.add_number('9'), 'number', '9'),
            (4, 3, '×', lambda: self.add_text('*'), 'operator', '×'),
            (4, 4, 'sinh', lambda: self.add_function('sinh('), 'function', 'sinh'),
            (4, 5, 'cosh', lambda: self.add_function('cosh('), 'function', 'cosh'),
            (4, 6, 'tanh', lambda: self.add_function('tanh('), 'function', 'tanh'),
            (4, 7, 'log₂', lambda: self.add_function('log2('), 'function', 'log₂'),
            
            # Row 6 - Numbers 4,5,6 and subtraction
            (5, 0, '4', lambda: self.add_number('4'), 'number', '4'),
            (5, 1, '5', lambda: self.add_number('5'), 'number', '5'),
            (5, 2, '6', lambda: self.add_number('6'), 'number', '6'),
            (5, 3, '−', lambda: self.add_text('-'), 'operator', '−'),
            (5, 4, 'sinh⁻¹', lambda: self.add_function('asinh('), 'function', 'sinh⁻¹'),
            (5, 5, 'cosh⁻¹', lambda: self.add_function('acosh('), 'function', 'cosh⁻¹'),
            (5, 6, 'tanh⁻¹', lambda: self.add_function('atanh('), 'function', 'tanh⁻¹'),
            (5, 7, '⌈x⌉', lambda: self.add_function('ceil('), 'function', '⌈x⌉'),
            
            # Row 7 - Numbers 1,2,3 and addition
            (6, 0, '1', lambda: self.add_number('1'), 'number', '1'),
            (6, 1, '2', lambda: self.add_number('2'), 'number', '2'),
            (6, 2, '3', lambda: self.add_number('3'), 'number', '3'),
            (6, 3, '+', lambda: self.add_text('+'), 'operator', '+'),
            (6, 4, 'gcd', lambda: self.add_function('gcd('), 'function', 'gcd'),
            (6, 5, 'lcm', lambda: self.add_function('lcm('), 'function', 'lcm'),
            (6, 6, '⌊x⌋', lambda: self.add_function('floor('), 'function', '⌊x⌋'),
            (6, 7, 'round', lambda: self.add_function('round('), 'function', '≈'),
            
            # Row 8 - Zero, decimal and equals
            (7, 0, '0', lambda: self.add_number('0'), 'number', '0'),
            (7, 1, '00', lambda: self.add_number('00'), 'number', '00'),
            (7, 2, '.', lambda: self.add_text('.'), 'number', '•'),
            (7, 3, '=', lambda: self.calculate(), 'equals', '='),
            (7, 4, '', None, 'number', ''),  # Empty
            (7, 5, '', None, 'number', ''),  # Empty
            (7, 6, '', None, 'number', ''),  # Empty
            (7, 7, '', None, 'number', ''),  # Empty
        ]
        
        # Create buttons with enhanced styling
        self.button_widgets = {}  # Store button references for potential hover effects
        
        for row, col, text, command, color_type, display_text in buttons:
            if text and command:  # Skip empty buttons
                btn = tk.Button(
                    button_frame,
                    text=display_text or text,
                    command=command,
                    **btn_config,
                    **colors[color_type]
                )
                
                # Add subtle border effect
                btn.configure(highlightthickness=1, highlightcolor='#666666')
                
                # Store reference and bind hover effects
                self.button_widgets[f"{row},{col}"] = btn
                self.bind_hover_effects(btn, colors[color_type])
                
                btn.grid(row=row, column=col, padx=3, pady=3, sticky='nsew')
        
        # Configure grid weights for responsive design
        for i in range(8):
            button_frame.grid_rowconfigure(i, weight=1)
        for i in range(8):
            button_frame.grid_columnconfigure(i, weight=1)
    
    def bind_hover_effects(self, button, colors):
        """Add hover effects to buttons"""
        def on_enter(e):
            button.configure(bg=colors['activebackground'])
            
        def on_leave(e):
            button.configure(bg=colors['bg'])
            
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
    
    def create_history_frame(self):
        """Create history display frame with modern styling"""
        # Main history container
        history_container = tk.Frame(self.root, bg='#1a1a1a', pady=10)
        history_container.pack(fill=tk.BOTH, expand=False, padx=15)
        
        # History header with icon
        header_frame = tk.Frame(history_container, bg='#2d2d2d', pady=8, padx=15)
        header_frame.pack(fill=tk.X, pady=(0, 5))
        
        # History icon and title
        history_icon = tk.Label(
            header_frame,
            text="📜",
            font=('Segoe UI', 12),
            bg='#2d2d2d',
            fg='#ffffff'
        )
        history_icon.pack(side=tk.LEFT, padx=(0, 8))
        
        history_title = tk.Label(
            header_frame,
            text="Calculation History",
            font=('Segoe UI', 12, 'bold'),
            bg='#2d2d2d',
            fg='#ffffff'
        )
        history_title.pack(side=tk.LEFT)
        
        # Clear history button in header
        clear_btn = tk.Button(
            header_frame,
            text="🗑️ Clear",
            command=self.clear_history,
            font=('Segoe UI', 9, 'bold'),
            bg='#ff6b6b',
            fg='#ffffff',
            bd=0,
            relief=tk.FLAT,
            cursor='hand2',
            activebackground='#ff5252',
            activeforeground='#ffffff'
        )
        clear_btn.pack(side=tk.RIGHT)
        
        # History content frame
        content_frame = tk.Frame(
            history_container, 
            bg='#2d2d2d', 
            bd=1, 
            relief=tk.SOLID
        )
        content_frame.pack(fill=tk.BOTH, expand=True)
        
        # Enhanced scrolled text widget
        self.history_text = scrolledtext.ScrolledText(
            content_frame,
            height=6,
            width=80,
            font=('Consolas', 10),
            bg='#2d2d2d',
            fg='#ffffff',
            state=tk.DISABLED,
            wrap=tk.WORD,
            bd=0,
            relief=tk.FLAT,
            selectbackground='#404040',
            selectforeground='#ffffff',
            insertbackground='#ffffff'
        )
        self.history_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Configure scrollbar styling
        try:
            scrollbar = self.history_text.vbar
            scrollbar.configure(
                bg='#404040',
                troughcolor='#2d2d2d',
                activebackground='#606060'
            )
        except:
            pass
    
    def setup_bindings(self):
        """Setup keyboard bindings"""
        self.root.bind('<Key>', self.key_pressed)
        self.root.focus_set()
    
    def key_pressed(self, event):
        """Handle keyboard input"""
        key = event.char
        
        if key.isdigit():
            self.add_number(key)
        elif key in '+-*/':
            self.add_text(key)
        elif key in '().':
            self.add_text(key)
        elif key == '\r' or key == '=':  # Enter or equals
            self.calculate()
        elif key == '\x08':  # Backspace
            self.backspace()
        elif key.lower() == 'c':
            self.clear_entry()
    
    def add_number(self, number):
        """Add number to current input"""
        if self.result_displayed:
            self.current_input = ""
            self.result_displayed = False
        
        self.current_input += number
        self.display_var.set(self.current_input)
    
    def add_text(self, text):
        """Add text to current input"""
        if self.result_displayed:
            if text in '+-*/':
                # Continue calculation with result
                pass
            else:
                self.current_input = ""
            self.result_displayed = False
        
        self.current_input += text
        self.display_var.set(self.current_input)
    
    def add_function(self, func):
        """Add function to current input"""
        if self.result_displayed:
            self.current_input = ""
            self.result_displayed = False
        
        self.current_input += func
        self.display_var.set(self.current_input)
    
    def calculate(self):
        """Calculate the current expression with enhanced display"""
        try:
            if not self.current_input:
                return
            
            # Show the expression in secondary display
            self.update_secondary_display(f"{self.current_input} =")
            
            # Preprocess the expression
            expression = self.preprocess_expression(self.current_input)
            
            # Create safe namespace
            namespace = self.create_safe_namespace()
            
            # Calculate result
            result = eval(expression, namespace)
            
            # Format result
            if isinstance(result, complex):
                if result.imag == 0:
                    result = result.real
                else:
                    formatted_result = f"{result.real:.10g}+{result.imag:.10g}i"
                    formatted_result = formatted_result.replace("+-", "-")
                    self.display_var.set(formatted_result)
                    self.add_to_history(self.current_input, formatted_result)
                    self.update_secondary_display(f"{self.current_input} = {formatted_result}")
                    self.current_input = formatted_result
                    self.result_displayed = True
                    return
            
            # Format real numbers
            if isinstance(result, (int, float)):
                if result == int(result) and abs(result) < 1e15:
                    formatted_result = str(int(result))
                else:
                    formatted_result = f"{result:.10g}"
            else:
                formatted_result = str(result)
            
            self.display_var.set(formatted_result)
            self.add_to_history(self.current_input, formatted_result)
            self.update_secondary_display(f"{self.current_input} = {formatted_result}")
            self.current_input = formatted_result
            self.result_displayed = True
            
        except Exception as e:
            self.update_secondary_display("Error")
            messagebox.showerror("Calculation Error", f"Invalid expression: {str(e)}")
    
    def preprocess_expression(self, expression):
        """Preprocess expression for evaluation"""
        import re
        
        # Replace special symbols
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
        
        # Handle implicit multiplication
        expression = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', expression)
        expression = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', expression)
        expression = re.sub(r'\)(\d)', r')*\1', expression)
        expression = re.sub(r'(\d)\(', r'\1*(', expression)
        
        return expression
    
    def create_safe_namespace(self):
        """Create safe namespace for eval"""
        return {
            # Math functions mapped to calculator methods
            'sin': self.calc.sin, 'cos': self.calc.cos, 'tan': self.calc.tan,
            'asin': self.calc.asin, 'acos': self.calc.acos, 'atan': self.calc.atan,
            'sinh': self.calc.sinh, 'cosh': self.calc.cosh, 'tanh': self.calc.tanh,
            'asinh': self.calc.asinh, 'acosh': self.calc.acosh, 'atanh': self.calc.atanh,
            'sqrt': self.calc.sqrt, 'exp': self.calc.exp, 'ln': self.calc.ln,
            'log10': self.calc.log10, 'log2': self.calc.log2, 'log': self.calc.log,
            'abs': self.calc.absolute, 'ceil': self.calc.ceiling, 'floor': self.calc.floor,
            'round': self.calc.round_number, 'gcd': self.calc.gcd, 'lcm': self.calc.lcm,
            'factorial': self.calc.factorial,
            
            # Constants
            'pi': math.pi, 'e': math.e,
            
            '__builtins__': {},
        }
    
    def clear_entry(self):
        """Clear current input"""
        self.current_input = ""
        self.display_var.set("0")
        self.result_displayed = False
    
    def all_clear(self):
        """Clear everything including memory"""
        self.clear_entry()
        self.calc.memory_clear()
        self.update_memory_display()
    
    def backspace(self):
        """Remove last character"""
        if self.current_input:
            self.current_input = self.current_input[:-1]
            self.display_var.set(self.current_input if self.current_input else "0")
            self.result_displayed = False
    
    def toggle_sign(self):
        """Toggle sign of current number"""
        if self.current_input:
            if self.current_input.startswith('-'):
                self.current_input = self.current_input[1:]
            else:
                self.current_input = '-' + self.current_input
            self.display_var.set(self.current_input)
    
    def reciprocal(self):
        """Calculate reciprocal"""
        if self.current_input:
            try:
                value = float(self.current_input)
                if value == 0:
                    messagebox.showerror("Error", "Cannot divide by zero")
                    return
                result = 1 / value
                self.display_var.set(str(result))
                self.add_to_history(f"1/{self.current_input}", str(result))
                self.current_input = str(result)
                self.result_displayed = True
            except:
                messagebox.showerror("Error", "Invalid input for reciprocal")
    
    def factorial(self):
        """Calculate factorial"""
        if self.current_input:
            try:
                value = float(self.current_input)
                if value < 0 or value != int(value):
                    messagebox.showerror("Error", "Factorial only defined for non-negative integers")
                    return
                result = self.calc.factorial(int(value))
                self.display_var.set(str(result))
                self.add_to_history(f"{int(value)}!", str(result))
                self.current_input = str(result)
                self.result_displayed = True
            except Exception as e:
                messagebox.showerror("Error", str(e))
    
    def memory_store(self):
        """Store current value in memory"""
        if self.current_input:
            try:
                value = float(self.current_input)
                self.calc.memory_store(value)
                self.update_memory_display()
                self.add_to_history(f"MS {value}", "stored")
            except:
                messagebox.showerror("Error", "Invalid value for memory")
    
    def memory_recall(self):
        """Recall value from memory"""
        value = self.calc.memory_recall()
        self.current_input = str(value)
        self.display_var.set(self.current_input)
        self.result_displayed = True
    
    def memory_clear(self):
        """Clear memory"""
        self.calc.memory_clear()
        self.update_memory_display()
        self.add_to_history("MC", "cleared")
    
    def memory_add(self):
        """Add current value to memory"""
        if self.current_input:
            try:
                value = float(self.current_input)
                self.calc.memory_add(value)
                self.update_memory_display()
                self.add_to_history(f"M+ {value}", f"M={self.calc.memory}")
            except:
                messagebox.showerror("Error", "Invalid value for memory")
    
    def memory_subtract(self):
        """Subtract current value from memory"""
        if self.current_input:
            try:
                value = float(self.current_input)
                self.calc.memory_subtract(value)
                self.update_memory_display()
                self.add_to_history(f"M- {value}", f"M={self.calc.memory}")
            except:
                messagebox.showerror("Error", "Invalid value for memory")
    
    def update_memory_display(self):
        """Update memory display"""
        self.memory_var.set(f"M: {self.calc.memory}")
    
    def change_angle_mode(self, event=None):
        """Change angle mode and update display"""
        mode = self.angle_mode_var.get().lower()
        self.calc.set_angle_mode(mode)
        
        # Update mode indicator
        if mode == 'radians':
            self.mode_label.configure(text="RAD", fg='#ff6b6b')
        else:
            self.mode_label.configure(text="DEG", fg='#4ecdc4')
        
        self.add_to_history(f"Mode: {mode}", "changed")
    
    def update_secondary_display(self, text=""):
        """Update secondary display with expression or result"""
        self.secondary_display.configure(text=text)
    
    def add_to_history(self, expression, result):
        """Add calculation to history display"""
        self.history_text.config(state=tk.NORMAL)
        self.history_text.insert(tk.END, f"{expression} = {result}\n")
        self.history_text.see(tk.END)
        self.history_text.config(state=tk.DISABLED)
    
    def clear_history(self):
        """Clear history display"""
        self.history_text.config(state=tk.NORMAL)
        self.history_text.delete(1.0, tk.END)
        self.history_text.config(state=tk.DISABLED)
        self.calc.clear_history()
    
    def launch_ip_calculator(self):
        """Launch the IP Calculator in a new window"""
        try:
            # Create and run IP calculator in a separate window
            ip_calculator = IPCalculatorGUI()
            ip_calculator.run()
        except Exception as e:
            messagebox.showerror("IP Calculator Error", 
                               f"Failed to launch IP Calculator: {str(e)}")
    
    def run(self):
        """Start the GUI"""
        self.root.mainloop()

def main():
    """Main function to start the GUI calculator"""
    try:
        calculator = ScientificCalculatorGUI()
        calculator.run()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
