"""
IP Calculator Demo - Showcasing Network Calculation Features
"""

from ip_calculator import IPCalculator

def demo_basic_operations():
    """Demo basic IP operations"""
    print("🌐 BASIC IP OPERATIONS")
    print("=" * 50)
    
    calc = IPCalculator()
    
    # IP Validation
    test_ips = ["192.168.1.1", "10.0.0.1", "256.256.256.256", "2001:db8::1"]
    print("📝 IP Validation:")
    for ip in test_ips:
        valid = calc.validate_ip(ip)
        status = "✅ Valid" if valid else "❌ Invalid"
        print(f"   {ip:<20} - {status}")
    
    print("\n🔢 IP Conversions:")
    
    # IP to Binary
    test_ip = "192.168.1.100"
    binary = calc.ip_to_binary(test_ip)
    print(f"   {test_ip} → Binary: {binary}")
    
    # IP to Decimal
    decimal = calc.ip_to_decimal(test_ip)
    print(f"   {test_ip} → Decimal: {decimal:,}")
    
    # Decimal to IP
    back_to_ip = calc.decimal_to_ip(decimal)
    print(f"   {decimal:,} → IP: {back_to_ip}")
    
    print()

def demo_subnet_operations():
    """Demo subnet calculations"""
    print("🔗 SUBNET OPERATIONS")
    print("=" * 50)
    
    calc = IPCalculator()
    
    # Subnet Information
    network = "192.168.1.0/24"
    print(f"📊 Network Information for {network}:")
    
    info = calc.subnet_info(network)
    print(f"   Network Address:    {info['network_address']}")
    print(f"   Broadcast Address:  {info['broadcast_address']}")
    print(f"   Subnet Mask:        {info['netmask']}")
    print(f"   Total Addresses:    {info['total_addresses']:,}")
    print(f"   Usable Hosts:       {info['usable_addresses']:,}")
    print(f"   First Usable:       {info['first_usable']}")
    print(f"   Last Usable:        {info['last_usable']}")
    print(f"   Network Class:      {info['network_class']}")
    print(f"   Private Network:    {info['is_private']}")
    
    # Subnet Splitting
    print(f"\n🔪 Splitting {network} into /26 subnets:")
    subnets = calc.subnet_split(network, 26)
    for i, subnet in enumerate(subnets[:6], 1):  # Show first 6
        print(f"   {i}. {subnet}")
    if len(subnets) > 6:
        print(f"   ... and {len(subnets) - 6} more subnets")
    
    # Host Calculations
    print(f"\n👥 Host Calculations:")
    prefixes = [24, 25, 26, 27, 28, 30]
    for prefix in prefixes:
        hosts = calc.calculate_hosts(prefix)
        print(f"   /{prefix} → {hosts['usable_hosts']:,} usable hosts")
    
    print()

def demo_advanced_features():
    """Demo advanced IP features"""
    print("🚀 ADVANCED FEATURES")
    print("=" * 50)
    
    calc = IPCalculator()
    
    # IP Range Analysis
    print("📈 IP Range Analysis:")
    start_ip = "192.168.1.10"
    end_ip = "192.168.1.50"
    
    range_info = calc.analyze_ip_range(start_ip, end_ip)
    print(f"   Range: {start_ip} - {end_ip}")
    print(f"   Total Addresses: {range_info['total_addresses']:,}")
    print(f"   Suggested Network: {range_info['suggested_network']}")
    print(f"   Required Host Bits: {range_info['required_host_bits']}")
    
    # Wildcard Mask
    print(f"\n🎯 Wildcard Mask Calculation:")
    subnet_mask = "255.255.255.192"
    wildcard = calc.wildcard_mask(subnet_mask)
    print(f"   Subnet Mask: {subnet_mask}")
    print(f"   Wildcard:    {wildcard}")
    
    # IP in Subnet Check
    print(f"\n🔍 IP in Subnet Check:")
    test_cases = [
        ("192.168.1.100", "192.168.1.0/24"),
        ("10.0.0.50", "192.168.1.0/24"),
        ("192.168.1.255", "192.168.1.0/24")
    ]
    
    for ip, network in test_cases:
        is_in = calc.ip_in_subnet(ip, network)
        status = "✅ Yes" if is_in else "❌ No"
        print(f"   Is {ip} in {network}? {status}")
    
    print()

def demo_common_networks():
    """Demo common network information"""
    print("📚 COMMON NETWORKS & PORTS")
    print("=" * 50)
    
    calc = IPCalculator()
    
    # Common Networks
    print("🏠 Common Network Addresses:")
    networks = calc.get_common_networks()
    for network, description in networks.items():
        print(f"   {network:<18} - {description}")
    
    # Port Information
    print(f"\n🔌 Port Information:")
    ports = calc.port_operations()
    print(f"   Well-Known Ports: {ports['well_known_range']}")
    print(f"   Registered Ports: {ports['registered_range']}")
    print(f"   Dynamic Ports:    {ports['dynamic_private_range']}")
    print(f"   Total Ports:      {ports['total_ports']:,}")
    
    print(f"\n   Sample Well-Known Ports:")
    sample_ports = list(ports['well_known_ports'].items())[:8]
    for port, service in sample_ports:
        print(f"   Port {port:<4} - {service}")
    
    print()

def demo_ipv6_operations():
    """Demo IPv6 operations"""
    print("🌍 IPv6 OPERATIONS")
    print("=" * 50)
    
    calc = IPCalculator()
    
    # IPv6 Validation and Conversion
    ipv6_addresses = [
        "2001:db8::1",
        "fe80::1",
        "::1",
        "2001:0db8:85a3::8a2e:0370:7334"
    ]
    
    print("📝 IPv6 Address Validation:")
    for ipv6 in ipv6_addresses:
        valid = calc.validate_ip(ipv6)
        status = "✅ Valid" if valid else "❌ Invalid"
        print(f"   {ipv6:<30} - {status}")
    
    # IPv6 Subnet Information
    print(f"\n📊 IPv6 Subnet Information:")
    ipv6_network = "2001:db8::/32"
    
    try:
        info = calc.subnet_info(ipv6_network)
        print(f"   Network: {info['network_address']}")
        print(f"   Prefix:  /{info['prefix_length']}")
        print(f"   Version: IPv{info['version']}")
        print(f"   Private: {info['is_private']}")
        
        # IPv6 doesn't have usable host limitation like IPv4
        if info['total_addresses'] > 10**15:
            print(f"   Addresses: >10^15 (practically unlimited)")
        else:
            print(f"   Addresses: {info['total_addresses']:,}")
            
    except Exception as e:
        print(f"   Error: {e}")
    
    print()

def main():
    """Run all IP calculator demos"""
    print("🔥 IP CALCULATOR DEMONSTRATION")
    print("=" * 60)
    print("Welcome to the IP Calculator feature showcase!")
    print("This demo shows the comprehensive network calculation capabilities.")
    print("=" * 60)
    print()
    
    try:
        demo_basic_operations()
        demo_subnet_operations() 
        demo_advanced_features()
        demo_common_networks()
        demo_ipv6_operations()
        
        print("🎉 DEMONSTRATION COMPLETE")
        print("=" * 50)
        print("The IP Calculator is now integrated into your scientific calculator!")
        print("Access it from:")
        print("• Main menu → Option 3 (IP Calculator)")
        print("• Scientific Calculator GUI → 📡 IP Calculator button")
        print()
        print("Features include:")
        print("✅ IP address validation and conversion")
        print("✅ Subnet calculations and splitting")
        print("✅ Host calculations and range analysis")
        print("✅ IPv4 and IPv6 support")
        print("✅ Common network references")
        print("✅ Binary, decimal, and dotted-decimal conversions")
        print("✅ Wildcard mask calculations")
        print("✅ Network summarization")
        print("=" * 50)
        
    except Exception as e:
        print(f"❌ Demo error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
