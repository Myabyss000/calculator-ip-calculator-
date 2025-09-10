"""
Visual GUI Demo - Showcasing the Refined Calculator Interface
Demonstrates the improved visual design and modern styling
"""

import tkinter as tk
from calculator_gui import ScientificCalculatorGUI
import time

class GUIDemoShowcase:
    def __init__(self):
        self.demo_window = tk.Tk()
        self.demo_window.title("🎨 GUI Refinement Showcase")
        self.demo_window.geometry("600x400")
        self.demo_window.configure(bg='#1a1a1a')
        self.calculator_instance = None
        
        self.create_demo_interface()
    
    def create_demo_interface(self):
        """Create the demo interface"""
        # Title
        title_label = tk.Label(
            self.demo_window,
            text="🧮 Scientific Calculator GUI Refinements",
            font=('Segoe UI', 18, 'bold'),
            bg='#1a1a1a',
            fg='#ffffff',
            pady=20
        )
        title_label.pack()
        
        # Improvements list
        improvements_frame = tk.Frame(self.demo_window, bg='#2d2d2d', padx=20, pady=20)
        improvements_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)
        
        improvements_title = tk.Label(
            improvements_frame,
            text="✨ Visual Improvements Made:",
            font=('Segoe UI', 14, 'bold'),
            bg='#2d2d2d',
            fg='#00d4aa',
            anchor='w'
        )
        improvements_title.pack(fill=tk.X, pady=(0, 15))
        
        improvements = [
            "🎨 Modern dark theme with professional color scheme",
            "📱 Enhanced display with secondary expression preview",
            "🎯 Color-coded buttons by function type with hover effects",
            "💫 Improved typography using Segoe UI font",
            "📊 Redesigned history panel with icons and better styling",
            "🎛️ Mode selector with visual indicators (RAD/DEG)",
            "✨ Subtle borders and visual depth effects",
            "🖱️ Interactive hover animations on buttons",
            "📏 Better spacing and responsive grid layout",
            "🔤 Enhanced mathematical symbols and Unicode characters"
        ]
        
        for improvement in improvements:
            improvement_label = tk.Label(
                improvements_frame,
                text=improvement,
                font=('Segoe UI', 11),
                bg='#2d2d2d',
                fg='#ffffff',
                anchor='w',
                wraplength=500
            )
            improvement_label.pack(fill=tk.X, pady=2)
        
        # Buttons
        button_frame = tk.Frame(self.demo_window, bg='#1a1a1a', pady=20)
        button_frame.pack()
        
        launch_btn = tk.Button(
            button_frame,
            text="🚀 Launch Refined Calculator",
            command=self.launch_calculator,
            font=('Segoe UI', 12, 'bold'),
            bg='#00d4aa',
            fg='#ffffff',
            bd=0,
            relief=tk.FLAT,
            padx=30,
            pady=10,
            cursor='hand2'
        )
        launch_btn.pack(side=tk.LEFT, padx=10)
        
        close_btn = tk.Button(
            button_frame,
            text="❌ Close Demo",
            command=self.demo_window.destroy,
            font=('Segoe UI', 12, 'bold'),
            bg='#ff6b6b',
            fg='#ffffff',
            bd=0,
            relief=tk.FLAT,
            padx=30,
            pady=10,
            cursor='hand2'
        )
        close_btn.pack(side=tk.LEFT, padx=10)
    
    def launch_calculator(self):
        """Launch the refined calculator"""
        if self.calculator_instance is None:
            self.calculator_instance = ScientificCalculatorGUI()
        
        # Minimize the demo window
        self.demo_window.iconify()
        
        # Show the calculator
        self.calculator_instance.root.deiconify()
        self.calculator_instance.root.lift()
        
        # Set up a callback to show the demo again when calculator closes
        self.calculator_instance.root.protocol("WM_DELETE_WINDOW", self.on_calculator_close)
    
    def on_calculator_close(self):
        """Handle calculator window closing"""
        if self.calculator_instance:
            self.calculator_instance.root.destroy()
            self.calculator_instance = None
        
        # Restore the demo window
        self.demo_window.deiconify()
        self.demo_window.lift()
    
    def run(self):
        """Run the demo"""
        self.demo_window.mainloop()

def main():
    """Main function to run the GUI showcase"""
    print("🎨 Starting GUI Refinement Showcase...")
    
    try:
        demo = GUIDemoShowcase()
        demo.run()
    except Exception as e:
        print(f"❌ Error in demo: {e}")
        # Fallback: Launch calculator directly
        print("🔄 Launching calculator directly...")
        calculator = ScientificCalculatorGUI()
        calculator.run()

if __name__ == "__main__":
    main()
