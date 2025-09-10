"""
IP Calculator GUI - Advanced network calculator interface
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
from ip_calculator import IPCalculator
import threading
import ipaddress

class IPCalculatorGUI:
    """GUI interface for IP Calculator"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.ip_calc = IPCalculator()
        self.setup_gui()
        
    def setup_gui(self):
        """Setup the GUI interface"""
        self.root.title("Advanced IP Calculator")
        self.root.geometry("900x700")
        self.root.configure(bg="#1a1a1a")
        
        # Configure style
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TNotebook', background='#1a1a1a')
        style.configure('TNotebook.Tab', background='#2d2d2d', foreground='white', 
                       padding=[12, 8])
        style.map('TNotebook.Tab', background=[('selected', '#404040')])
        
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create tabs
        self.create_basic_tab()
        self.create_subnet_tab()
        self.create_conversion_tab()
        self.create_analysis_tab()
        self.create_history_tab()
        
    def create_basic_tab(self):
        """Create basic IP operations tab"""
        frame = tk.Frame(self.notebook, bg="#1a1a1a")
        self.notebook.add(frame, text="Basic Operations")
        
        # Title
        title = tk.Label(frame, text="Basic IP Operations", font=("Segoe UI", 16, "bold"), 
                        fg="white", bg="#1a1a1a")
        title.pack(pady=10)
        
        # IP Validation section
        validation_frame = tk.Frame(frame, bg="#2d2d2d", relief="raised", bd=1)
        validation_frame.pack(fill='x', padx=20, pady=5)
        
        tk.Label(validation_frame, text="IP Validation", font=("Segoe UI", 12, "bold"), 
                fg="#4CAF50", bg="#2d2d2d").pack(pady=5)
        
        input_frame = tk.Frame(validation_frame, bg="#2d2d2d")
        input_frame.pack(pady=5)
        
        tk.Label(input_frame, text="IP Address:", fg="white", bg="#2d2d2d").pack(side='left', padx=5)
        self.validate_entry = tk.Entry(input_frame, bg="#404040", fg="white", insertbackground="white")
        self.validate_entry.pack(side='left', padx=5)
        
        validate_btn = tk.Button(input_frame, text="Validate", bg="#4CAF50", fg="white",
                               command=self.validate_ip)
        validate_btn.pack(side='left', padx=5)
        
        self.validate_result = tk.Label(validation_frame, text="", fg="white", bg="#2d2d2d")
        self.validate_result.pack(pady=5)
        
        # IP Information section
        info_frame = tk.Frame(frame, bg="#2d2d2d", relief="raised", bd=1)
        info_frame.pack(fill='x', padx=20, pady=5)
        
        tk.Label(info_frame, text="IP Information", font=("Segoe UI", 12, "bold"), 
                fg="#2196F3", bg="#2d2d2d").pack(pady=5)
        
        info_input_frame = tk.Frame(info_frame, bg="#2d2d2d")
        info_input_frame.pack(pady=5)
        
        tk.Label(info_input_frame, text="Network (e.g., 192.168.1.0/24):", fg="white", bg="#2d2d2d").pack(side='left', padx=5)
        self.info_entry = tk.Entry(info_input_frame, bg="#404040", fg="white", insertbackground="white", width=20)
        self.info_entry.pack(side='left', padx=5)
        
        info_btn = tk.Button(info_input_frame, text="Get Info", bg="#2196F3", fg="white",
                           command=self.get_network_info)
        info_btn.pack(side='left', padx=5)
        
        # Results display
        self.info_display = scrolledtext.ScrolledText(info_frame, height=8, bg="#404040", fg="white",
                                                     insertbackground="white", wrap='word')
        self.info_display.pack(fill='both', expand=True, padx=10, pady=5)
        
    def create_subnet_tab(self):
        """Create subnet operations tab"""
        frame = tk.Frame(self.notebook, bg="#1a1a1a")
        self.notebook.add(frame, text="Subnet Operations")
        
        # Title
        title = tk.Label(frame, text="Subnet Calculator", font=("Segoe UI", 16, "bold"), 
                        fg="white", bg="#1a1a1a")
        title.pack(pady=10)
        
        # Subnet splitting section
        split_frame = tk.Frame(frame, bg="#2d2d2d", relief="raised", bd=1)
        split_frame.pack(fill='x', padx=20, pady=5)
        
        tk.Label(split_frame, text="Subnet Splitting", font=("Segoe UI", 12, "bold"), 
                fg="#FF9800", bg="#2d2d2d").pack(pady=5)
        
        split_input_frame = tk.Frame(split_frame, bg="#2d2d2d")
        split_input_frame.pack(pady=5)
        
        tk.Label(split_input_frame, text="Network:", fg="white", bg="#2d2d2d").pack(side='left', padx=5)
        self.split_network_entry = tk.Entry(split_input_frame, bg="#404040", fg="white", 
                                          insertbackground="white", width=15)
        self.split_network_entry.pack(side='left', padx=5)
        
        tk.Label(split_input_frame, text="New Prefix:", fg="white", bg="#2d2d2d").pack(side='left', padx=5)
        self.split_prefix_entry = tk.Entry(split_input_frame, bg="#404040", fg="white", 
                                         insertbackground="white", width=5)
        self.split_prefix_entry.pack(side='left', padx=5)
        
        split_btn = tk.Button(split_input_frame, text="Split", bg="#FF9800", fg="white",
                            command=self.split_subnet)
        split_btn.pack(side='left', padx=5)
        
        self.split_result = scrolledtext.ScrolledText(split_frame, height=6, bg="#404040", fg="white",
                                                    insertbackground="white", wrap='word')
        self.split_result.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Host calculation section
        host_frame = tk.Frame(frame, bg="#2d2d2d", relief="raised", bd=1)
        host_frame.pack(fill='x', padx=20, pady=5)
        
        tk.Label(host_frame, text="Host Calculation", font=("Segoe UI", 12, "bold"), 
                fg="#9C27B0", bg="#2d2d2d").pack(pady=5)
        
        host_input_frame = tk.Frame(host_frame, bg="#2d2d2d")
        host_input_frame.pack(pady=5)
        
        tk.Label(host_input_frame, text="Prefix Length:", fg="white", bg="#2d2d2d").pack(side='left', padx=5)
        self.host_prefix_entry = tk.Entry(host_input_frame, bg="#404040", fg="white", 
                                        insertbackground="white", width=5)
        self.host_prefix_entry.pack(side='left', padx=5)
        
        tk.Label(host_input_frame, text="IP Version:", fg="white", bg="#2d2d2d").pack(side='left', padx=5)
        self.ip_version = tk.StringVar(value="4")
        version_combo = ttk.Combobox(host_input_frame, textvariable=self.ip_version, 
                                   values=["4", "6"], width=3, state="readonly")
        version_combo.pack(side='left', padx=5)
        
        host_btn = tk.Button(host_input_frame, text="Calculate", bg="#9C27B0", fg="white",
                           command=self.calculate_hosts)
        host_btn.pack(side='left', padx=5)
        
        self.host_result = tk.Label(host_frame, text="", fg="white", bg="#2d2d2d", justify='left')
        self.host_result.pack(pady=5)
        
    def create_conversion_tab(self):
        """Create IP conversion tab"""
        frame = tk.Frame(self.notebook, bg="#1a1a1a")
        self.notebook.add(frame, text="Conversions")
        
        # Title
        title = tk.Label(frame, text="IP Address Conversions", font=("Segoe UI", 16, "bold"), 
                        fg="white", bg="#1a1a1a")
        title.pack(pady=10)
        
        # IP to Binary
        binary_frame = tk.Frame(frame, bg="#2d2d2d", relief="raised", bd=1)
        binary_frame.pack(fill='x', padx=20, pady=5)
        
        tk.Label(binary_frame, text="IP ↔ Binary Conversion", font=("Segoe UI", 12, "bold"), 
                fg="#00BCD4", bg="#2d2d2d").pack(pady=5)
        
        binary_input_frame = tk.Frame(binary_frame, bg="#2d2d2d")
        binary_input_frame.pack(pady=5)
        
        tk.Label(binary_input_frame, text="Input:", fg="white", bg="#2d2d2d").pack(side='left', padx=5)
        self.conversion_entry = tk.Entry(binary_input_frame, bg="#404040", fg="white", 
                                       insertbackground="white", width=40)
        self.conversion_entry.pack(side='left', padx=5)
        
        convert_frame = tk.Frame(binary_frame, bg="#2d2d2d")
        convert_frame.pack(pady=5)
        
        ip_to_bin_btn = tk.Button(convert_frame, text="IP → Binary", bg="#00BCD4", fg="white",
                                command=self.ip_to_binary)
        ip_to_bin_btn.pack(side='left', padx=5)
        
        bin_to_ip_btn = tk.Button(convert_frame, text="Binary → IP", bg="#00BCD4", fg="white",
                                command=self.binary_to_ip)
        bin_to_ip_btn.pack(side='left', padx=5)
        
        ip_to_dec_btn = tk.Button(convert_frame, text="IP → Decimal", bg="#00BCD4", fg="white",
                                command=self.ip_to_decimal)
        ip_to_dec_btn.pack(side='left', padx=5)
        
        dec_to_ip_btn = tk.Button(convert_frame, text="Decimal → IP", bg="#00BCD4", fg="white",
                                command=self.decimal_to_ip)
        dec_to_ip_btn.pack(side='left', padx=5)
        
        self.conversion_result = scrolledtext.ScrolledText(binary_frame, height=4, bg="#404040", fg="white",
                                                         insertbackground="white", wrap='word')
        self.conversion_result.pack(fill='both', expand=True, padx=10, pady=5)
        
    def create_analysis_tab(self):
        """Create network analysis tab"""
        frame = tk.Frame(self.notebook, bg="#1a1a1a")
        self.notebook.add(frame, text="Analysis")
        
        # Title
        title = tk.Label(frame, text="Network Analysis Tools", font=("Segoe UI", 16, "bold"), 
                        fg="white", bg="#1a1a1a")
        title.pack(pady=10)
        
        # IP Range Analysis
        range_frame = tk.Frame(frame, bg="#2d2d2d", relief="raised", bd=1)
        range_frame.pack(fill='x', padx=20, pady=5)
        
        tk.Label(range_frame, text="IP Range Analysis", font=("Segoe UI", 12, "bold"), 
                fg="#E91E63", bg="#2d2d2d").pack(pady=5)
        
        range_input_frame = tk.Frame(range_frame, bg="#2d2d2d")
        range_input_frame.pack(pady=5)
        
        tk.Label(range_input_frame, text="Start IP:", fg="white", bg="#2d2d2d").pack(side='left', padx=5)
        self.start_ip_entry = tk.Entry(range_input_frame, bg="#404040", fg="white", 
                                     insertbackground="white", width=15)
        self.start_ip_entry.pack(side='left', padx=5)
        
        tk.Label(range_input_frame, text="End IP:", fg="white", bg="#2d2d2d").pack(side='left', padx=5)
        self.end_ip_entry = tk.Entry(range_input_frame, bg="#404040", fg="white", 
                                   insertbackground="white", width=15)
        self.end_ip_entry.pack(side='left', padx=5)
        
        analyze_btn = tk.Button(range_input_frame, text="Analyze Range", bg="#E91E63", fg="white",
                              command=self.analyze_range)
        analyze_btn.pack(side='left', padx=5)
        
        self.range_result = scrolledtext.ScrolledText(range_frame, height=6, bg="#404040", fg="white",
                                                    insertbackground="white", wrap='word')
        self.range_result.pack(fill='both', expand=True, padx=10, pady=5)
        
        # Common Networks
        common_frame = tk.Frame(frame, bg="#2d2d2d", relief="raised", bd=1)
        common_frame.pack(fill='x', padx=20, pady=5)
        
        tk.Label(common_frame, text="Common Network Addresses", font=("Segoe UI", 12, "bold"), 
                fg="#607D8B", bg="#2d2d2d").pack(pady=5)
        
        common_btn = tk.Button(common_frame, text="Show Common Networks", bg="#607D8B", fg="white",
                             command=self.show_common_networks)
        common_btn.pack(pady=5)
        
        self.common_result = scrolledtext.ScrolledText(common_frame, height=6, bg="#404040", fg="white",
                                                     insertbackground="white", wrap='word')
        self.common_result.pack(fill='both', expand=True, padx=10, pady=5)
        
    def create_history_tab(self):
        """Create history tab"""
        frame = tk.Frame(self.notebook, bg="#1a1a1a")
        self.notebook.add(frame, text="History")
        
        # Title
        title = tk.Label(frame, text="Calculation History", font=("Segoe UI", 16, "bold"), 
                        fg="white", bg="#1a1a1a")
        title.pack(pady=10)
        
        # History controls
        control_frame = tk.Frame(frame, bg="#1a1a1a")
        control_frame.pack(fill='x', padx=20, pady=5)
        
        refresh_btn = tk.Button(control_frame, text="Refresh History", bg="#4CAF50", fg="white",
                              command=self.refresh_history)
        refresh_btn.pack(side='left', padx=5)
        
        clear_btn = tk.Button(control_frame, text="Clear History", bg="#f44336", fg="white",
                            command=self.clear_history)
        clear_btn.pack(side='left', padx=5)
        
        # History display
        self.history_display = scrolledtext.ScrolledText(frame, bg="#404040", fg="white",
                                                       insertbackground="white", wrap='word')
        self.history_display.pack(fill='both', expand=True, padx=20, pady=10)
        
    # Event handlers
    def validate_ip(self):
        """Validate IP address"""
        try:
            ip = self.validate_entry.get().strip()
            if not ip:
                self.validate_result.config(text="Please enter an IP address", fg="#f44336")
                return
            
            is_valid = self.ip_calc.validate_ip(ip)
            if is_valid:
                # Get additional info
                try:
                    ip_obj = ipaddress.ip_address(ip)
                    version = ip_obj.version
                    is_private = ip_obj.is_private
                    is_multicast = ip_obj.is_multicast
                    is_loopback = ip_obj.is_loopback
                    
                    info = f"✓ Valid IPv{version} address"
                    if is_private:
                        info += " (Private)"
                    if is_multicast:
                        info += " (Multicast)"
                    if is_loopback:
                        info += " (Loopback)"
                    
                    self.validate_result.config(text=info, fg="#4CAF50")
                except:
                    self.validate_result.config(text="✓ Valid IP address", fg="#4CAF50")
            else:
                self.validate_result.config(text="✗ Invalid IP address", fg="#f44336")
        except Exception as e:
            self.validate_result.config(text=f"Error: {str(e)}", fg="#f44336")
    
    def get_network_info(self):
        """Get comprehensive network information"""
        try:
            network = self.info_entry.get().strip()
            if not network:
                messagebox.showerror("Error", "Please enter a network address")
                return
            
            info = self.ip_calc.subnet_info(network)
            
            # Format the information
            display_text = f"Network Information for {network}\n"
            display_text += "=" * 50 + "\n\n"
            
            display_text += f"Network Address:     {info['network_address']}\n"
            display_text += f"Broadcast Address:   {info['broadcast_address']}\n"
            display_text += f"Subnet Mask:         {info['netmask']}\n"
            display_text += f"Prefix Length:       /{info['prefix_length']}\n"
            display_text += f"Network Class:       {info['network_class']}\n\n"
            
            display_text += f"Total Addresses:     {info['total_addresses']:,}\n"
            display_text += f"Usable Addresses:    {info['usable_addresses']:,}\n"
            display_text += f"First Usable:        {info['first_usable']}\n"
            display_text += f"Last Usable:         {info['last_usable']}\n\n"
            
            display_text += f"IP Version:          IPv{info['version']}\n"
            display_text += f"Private Network:     {info['is_private']}\n"
            display_text += f"Multicast:           {info['is_multicast']}\n"
            display_text += f"Reserved:            {info['is_reserved']}\n"
            
            self.info_display.delete(1.0, tk.END)
            self.info_display.insert(1.0, display_text)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to get network info: {str(e)}")
    
    def split_subnet(self):
        """Split subnet into smaller subnets"""
        try:
            network = self.split_network_entry.get().strip()
            prefix = self.split_prefix_entry.get().strip()
            
            if not network or not prefix:
                messagebox.showerror("Error", "Please enter both network and new prefix")
                return
            
            subnets = self.ip_calc.subnet_split(network, int(prefix))
            
            display_text = f"Splitting {network} into /{prefix} subnets:\n"
            display_text += "=" * 50 + "\n\n"
            
            for i, subnet in enumerate(subnets, 1):
                display_text += f"{i:3d}. {subnet}\n"
            
            display_text += f"\nTotal subnets: {len(subnets)}"
            
            self.split_result.delete(1.0, tk.END)
            self.split_result.insert(1.0, display_text)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to split subnet: {str(e)}")
    
    def calculate_hosts(self):
        """Calculate number of hosts for prefix length"""
        try:
            prefix = self.host_prefix_entry.get().strip()
            version = int(self.ip_version.get())
            
            if not prefix:
                messagebox.showerror("Error", "Please enter a prefix length")
                return
            
            result = self.ip_calc.calculate_hosts(int(prefix), version)
            
            display_text = f"Prefix Length: /{result['prefix_length']} (IPv{version})\n"
            display_text += f"Host Bits: {result['host_bits']}\n"
            display_text += f"Total Addresses: {result['total_addresses']:,}\n"
            display_text += f"Usable Hosts: {result['usable_hosts']:,}"
            
            self.host_result.config(text=display_text)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to calculate hosts: {str(e)}")
    
    def ip_to_binary(self):
        """Convert IP to binary"""
        try:
            ip = self.conversion_entry.get().strip()
            if not ip:
                messagebox.showerror("Error", "Please enter an IP address")
                return
            
            result = self.ip_calc.ip_to_binary(ip)
            self.conversion_result.delete(1.0, tk.END)
            self.conversion_result.insert(1.0, f"IP: {ip}\nBinary: {result}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed: {str(e)}")
    
    def binary_to_ip(self):
        """Convert binary to IP"""
        try:
            binary = self.conversion_entry.get().strip()
            if not binary:
                messagebox.showerror("Error", "Please enter a binary string")
                return
            
            # Determine IP version based on binary length
            clean_binary = binary.replace('.', '').replace(':', '')
            version = 6 if len(clean_binary) == 128 else 4
            
            result = self.ip_calc.binary_to_ip(binary, version)
            self.conversion_result.delete(1.0, tk.END)
            self.conversion_result.insert(1.0, f"Binary: {binary}\nIP: {result}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed: {str(e)}")
    
    def ip_to_decimal(self):
        """Convert IP to decimal"""
        try:
            ip = self.conversion_entry.get().strip()
            if not ip:
                messagebox.showerror("Error", "Please enter an IP address")
                return
            
            result = self.ip_calc.ip_to_decimal(ip)
            self.conversion_result.delete(1.0, tk.END)
            self.conversion_result.insert(1.0, f"IP: {ip}\nDecimal: {result:,}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed: {str(e)}")
    
    def decimal_to_ip(self):
        """Convert decimal to IP"""
        try:
            decimal_str = self.conversion_entry.get().strip()
            if not decimal_str:
                messagebox.showerror("Error", "Please enter a decimal number")
                return
            
            decimal = int(decimal_str)
            # Determine version based on size
            version = 6 if decimal > 4294967295 else 4
            
            result = self.ip_calc.decimal_to_ip(decimal, version)
            self.conversion_result.delete(1.0, tk.END)
            self.conversion_result.insert(1.0, f"Decimal: {decimal:,}\nIP: {result}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Conversion failed: {str(e)}")
    
    def analyze_range(self):
        """Analyze IP range"""
        try:
            start_ip = self.start_ip_entry.get().strip()
            end_ip = self.end_ip_entry.get().strip()
            
            if not start_ip or not end_ip:
                messagebox.showerror("Error", "Please enter both start and end IP addresses")
                return
            
            result = self.ip_calc.analyze_ip_range(start_ip, end_ip)
            
            display_text = f"IP Range Analysis\n"
            display_text += "=" * 30 + "\n\n"
            display_text += f"Start IP: {result['start_ip']}\n"
            display_text += f"End IP: {result['end_ip']}\n"
            display_text += f"Total Addresses: {result['total_addresses']:,}\n"
            display_text += f"Required Host Bits: {result['required_host_bits']}\n"
            display_text += f"Minimum Prefix: /{result['minimum_prefix']}\n"
            display_text += f"Suggested Network: {result['suggested_network']}\n"
            
            self.range_result.delete(1.0, tk.END)
            self.range_result.insert(1.0, display_text)
            
        except Exception as e:
            messagebox.showerror("Error", f"Range analysis failed: {str(e)}")
    
    def show_common_networks(self):
        """Show common network addresses"""
        try:
            networks = self.ip_calc.get_common_networks()
            ports = self.ip_calc.port_operations()
            
            display_text = "Common Network Addresses (RFC Standards)\n"
            display_text += "=" * 50 + "\n\n"
            
            for network, description in networks.items():
                display_text += f"{network:<18} - {description}\n"
            
            display_text += f"\n\nWell-Known Ports ({ports['well_known_range']})\n"
            display_text += "-" * 30 + "\n"
            
            for port, service in list(ports['well_known_ports'].items())[:10]:
                display_text += f"Port {port:<5} - {service}\n"
            
            display_text += f"\nPort Ranges:\n"
            display_text += f"• Well-Known: {ports['well_known_range']}\n"
            display_text += f"• Registered: {ports['registered_range']}\n"
            display_text += f"• Dynamic: {ports['dynamic_private_range']}\n"
            display_text += f"• Total Ports: {ports['total_ports']:,}\n"
            
            self.common_result.delete(1.0, tk.END)
            self.common_result.insert(1.0, display_text)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load common networks: {str(e)}")
    
    def refresh_history(self):
        """Refresh calculation history"""
        try:
            history = self.ip_calc.get_history()
            
            if not history:
                display_text = "No calculations in history yet.\n\nUse the other tabs to perform IP calculations."
            else:
                display_text = f"Calculation History ({len(history)} entries)\n"
                display_text += "=" * 50 + "\n\n"
                
                for i, entry in enumerate(reversed(history[-20:]), 1):  # Show last 20 entries
                    display_text += f"{i:2d}. {entry}\n"
            
            self.history_display.delete(1.0, tk.END)
            self.history_display.insert(1.0, display_text)
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to refresh history: {str(e)}")
    
    def clear_history(self):
        """Clear calculation history"""
        try:
            if messagebox.askyesno("Confirm", "Are you sure you want to clear the calculation history?"):
                self.ip_calc.clear_history()
                self.history_display.delete(1.0, tk.END)
                self.history_display.insert(1.0, "History cleared.")
                messagebox.showinfo("Success", "Calculation history has been cleared.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to clear history: {str(e)}")
    
    def run(self):
        """Start the GUI"""
        # Initial history refresh
        self.refresh_history()
        self.root.mainloop()

def main():
    """Main function to run IP Calculator GUI"""
    app = IPCalculatorGUI()
    app.run()

if __name__ == "__main__":
    main()
