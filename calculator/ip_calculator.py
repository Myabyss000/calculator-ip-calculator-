"""
IP Calculator Module
Comprehensive IP address calculations and subnet operations
"""

import ipaddress
import socket
import struct
from typing import List, Dict, Tuple, Union

class IPCalculator:
    """Comprehensive IP address calculator with subnet operations"""
    
    def __init__(self):
        self.history = []
    
    def add_to_history(self, operation: str, result: str):
        """Add calculation to history"""
        self.history.append(f"{operation} = {result}")
        if len(self.history) > 50:  # Keep last 50 calculations
            self.history.pop(0)
    
    def get_history(self) -> List[str]:
        """Get calculation history"""
        return self.history.copy()
    
    def clear_history(self):
        """Clear calculation history"""
        self.history = []
    
    # Basic IP Operations
    def validate_ip(self, ip_str: str) -> bool:
        """Validate if string is a valid IP address"""
        try:
            ipaddress.ip_address(ip_str)
            return True
        except ValueError:
            return False
    
    def ip_to_binary(self, ip_str: str) -> str:
        """Convert IP address to binary representation"""
        try:
            ip = ipaddress.ip_address(ip_str)
            if isinstance(ip, ipaddress.IPv4Address):
                # Convert to 32-bit binary
                binary = format(int(ip), '032b')
                # Format as dotted binary (8.8.8.8 format)
                formatted = '.'.join([binary[i:i+8] for i in range(0, 32, 8)])
                self.add_to_history(f"IP {ip_str} to binary", formatted)
                return formatted
            else:  # IPv6
                binary = format(int(ip), '0128b')
                # Format as colon-separated 16-bit groups
                formatted = ':'.join([binary[i:i+16] for i in range(0, 128, 16)])
                self.add_to_history(f"IPv6 {ip_str} to binary", formatted)
                return formatted
        except ValueError as e:
            raise ValueError(f"Invalid IP address: {e}")
    
    def ip_to_decimal(self, ip_str: str) -> int:
        """Convert IP address to decimal representation"""
        try:
            ip = ipaddress.ip_address(ip_str)
            decimal = int(ip)
            self.add_to_history(f"IP {ip_str} to decimal", str(decimal))
            return decimal
        except ValueError as e:
            raise ValueError(f"Invalid IP address: {e}")
    
    def decimal_to_ip(self, decimal: int, version: int = 4) -> str:
        """Convert decimal to IP address"""
        try:
            if version == 4:
                if not (0 <= decimal <= 4294967295):  # 2^32 - 1
                    raise ValueError("Decimal value out of range for IPv4")
                ip = ipaddress.IPv4Address(decimal)
            else:  # IPv6
                if not (0 <= decimal <= 340282366920938463463374607431768211455):  # 2^128 - 1
                    raise ValueError("Decimal value out of range for IPv6")
                ip = ipaddress.IPv6Address(decimal)
            
            result = str(ip)
            self.add_to_history(f"Decimal {decimal} to IPv{version}", result)
            return result
        except (ValueError, ipaddress.AddressValueError) as e:
            raise ValueError(f"Invalid decimal value: {e}")
    
    def binary_to_ip(self, binary_str: str, version: int = 4) -> str:
        """Convert binary string to IP address"""
        try:
            # Remove dots or colons if present
            clean_binary = binary_str.replace('.', '').replace(':', '')
            
            if version == 4:
                if len(clean_binary) != 32:
                    raise ValueError("Binary string must be 32 bits for IPv4")
                decimal = int(clean_binary, 2)
                ip = ipaddress.IPv4Address(decimal)
            else:  # IPv6
                if len(clean_binary) != 128:
                    raise ValueError("Binary string must be 128 bits for IPv6")
                decimal = int(clean_binary, 2)
                ip = ipaddress.IPv6Address(decimal)
            
            result = str(ip)
            self.add_to_history(f"Binary {binary_str} to IPv{version}", result)
            return result
        except ValueError as e:
            raise ValueError(f"Invalid binary string: {e}")
    
    # Subnet Calculations
    def subnet_info(self, network_str: str) -> Dict[str, Union[str, int]]:
        """Get comprehensive subnet information"""
        try:
            network = ipaddress.ip_network(network_str, strict=False)
            
            # Calculate first and last usable addresses efficiently
            if isinstance(network, ipaddress.IPv4Network):
                if network.num_addresses > 2:
                    first_usable = str(network.network_address + 1)
                    last_usable = str(network.broadcast_address - 1)
                else:
                    first_usable = 'N/A'
                    last_usable = 'N/A'
            else:  # IPv6Network
                if network.prefixlen >= 120:  # Small enough to enumerate safely
                    try:
                        hosts_list = list(network.hosts())
                        first_usable = str(hosts_list[0]) if hosts_list else 'N/A'
                        last_usable = str(hosts_list[-1]) if hosts_list else 'N/A'
                    except:
                        first_usable = 'N/A (too large)'
                        last_usable = 'N/A (too large)'
                else:
                    first_usable = 'N/A (too large)'
                    last_usable = 'N/A (too large)'
            
            info = {
                'network_address': str(network.network_address),
                'broadcast_address': str(network.broadcast_address) if isinstance(network, ipaddress.IPv4Network) else 'N/A (IPv6)',
                'netmask': str(network.netmask),
                'prefix_length': network.prefixlen,
                'total_addresses': network.num_addresses,
                'usable_addresses': max(0, network.num_addresses - 2) if isinstance(network, ipaddress.IPv4Network) else network.num_addresses,
                'first_usable': first_usable,
                'last_usable': last_usable,
                'network_class': self._get_network_class(network.network_address) if isinstance(network, ipaddress.IPv4Network) else 'N/A',
                'is_private': network.is_private,
                'is_multicast': network.is_multicast,
                'is_reserved': network.is_reserved,
                'version': network.version
            }
            
            self.add_to_history(f"Subnet info for {network_str}", f"Network: {info['network_address']}/{info['prefix_length']}")
            return info
        except ValueError as e:
            raise ValueError(f"Invalid network: {e}")
    
    def subnet_split(self, network_str: str, new_prefix: int) -> List[str]:
        """Split a subnet into smaller subnets"""
        try:
            network = ipaddress.ip_network(network_str, strict=False)
            
            if new_prefix <= network.prefixlen:
                raise ValueError("New prefix must be larger than current prefix")
            
            subnets = list(network.subnets(new_prefix=new_prefix))
            subnet_list = [str(subnet) for subnet in subnets]
            
            self.add_to_history(f"Split {network_str} into /{new_prefix}", f"{len(subnet_list)} subnets")
            return subnet_list
        except ValueError as e:
            raise ValueError(f"Error splitting subnet: {e}")
    
    def subnet_summary(self, networks: List[str]) -> str:
        """Summarize multiple networks into a supernet"""
        try:
            network_objects = [ipaddress.ip_network(net, strict=False) for net in networks]
            
            # Find the common supernet
            summary = list(ipaddress.collapse_addresses(network_objects))
            summary_list = [str(net) for net in summary]
            
            result = ', '.join(summary_list)
            self.add_to_history(f"Summarize {len(networks)} networks", result)
            return result
        except ValueError as e:
            raise ValueError(f"Error summarizing networks: {e}")
    
    def ip_in_subnet(self, ip_str: str, network_str: str) -> bool:
        """Check if IP address is in given subnet"""
        try:
            ip = ipaddress.ip_address(ip_str)
            network = ipaddress.ip_network(network_str, strict=False)
            
            result = ip in network
            self.add_to_history(f"Is {ip_str} in {network_str}?", str(result))
            return result
        except ValueError as e:
            raise ValueError(f"Invalid IP or network: {e}")
    
    def calculate_hosts(self, prefix_length: int, version: int = 4) -> Dict[str, int]:
        """Calculate number of hosts for given prefix length"""
        try:
            if version == 4:
                if not (0 <= prefix_length <= 32):
                    raise ValueError("IPv4 prefix length must be 0-32")
                host_bits = 32 - prefix_length
                total_addresses = 2 ** host_bits
                usable_hosts = max(0, total_addresses - 2)  # Subtract network and broadcast
            else:  # IPv6
                if not (0 <= prefix_length <= 128):
                    raise ValueError("IPv6 prefix length must be 0-128")
                host_bits = 128 - prefix_length
                total_addresses = 2 ** host_bits
                usable_hosts = total_addresses  # No network/broadcast concept in IPv6
            
            result = {
                'prefix_length': prefix_length,
                'host_bits': host_bits,
                'total_addresses': total_addresses,
                'usable_hosts': usable_hosts,
                'subnets_in_parent': 2 ** (prefix_length - (prefix_length - 1)) if prefix_length > 0 else 1
            }
            
            self.add_to_history(f"Hosts for /{prefix_length}", f"{usable_hosts} usable hosts")
            return result
        except ValueError as e:
            raise ValueError(f"Invalid prefix length: {e}")
    
    # Advanced IP Operations
    def wildcard_mask(self, netmask_str: str) -> str:
        """Calculate wildcard mask from subnet mask"""
        try:
            netmask = ipaddress.IPv4Address(netmask_str)
            wildcard_int = (~int(netmask)) & 0xFFFFFFFF
            wildcard = ipaddress.IPv4Address(wildcard_int)
            
            result = str(wildcard)
            self.add_to_history(f"Wildcard mask for {netmask_str}", result)
            return result
        except ValueError as e:
            raise ValueError(f"Invalid subnet mask: {e}")
    
    def next_network(self, network_str: str) -> str:
        """Get the next network of the same size"""
        try:
            network = ipaddress.ip_network(network_str, strict=False)
            next_net = network.supernet().subnets(new_prefix=network.prefixlen)
            
            # Find current network and get the next one
            networks = list(next_net)
            current_index = networks.index(network)
            
            if current_index + 1 < len(networks):
                result = str(networks[current_index + 1])
            else:
                raise ValueError("No next network available")
            
            self.add_to_history(f"Next network after {network_str}", result)
            return result
        except (ValueError, IndexError) as e:
            raise ValueError(f"Cannot find next network: {e}")
    
    def previous_network(self, network_str: str) -> str:
        """Get the previous network of the same size"""
        try:
            network = ipaddress.ip_network(network_str, strict=False)
            prev_net = network.supernet().subnets(new_prefix=network.prefixlen)
            
            # Find current network and get the previous one
            networks = list(prev_net)
            current_index = networks.index(network)
            
            if current_index > 0:
                result = str(networks[current_index - 1])
            else:
                raise ValueError("No previous network available")
            
            self.add_to_history(f"Previous network before {network_str}", result)
            return result
        except (ValueError, IndexError) as e:
            raise ValueError(f"Cannot find previous network: {e}")
    
    # Network Analysis
    def analyze_ip_range(self, start_ip: str, end_ip: str) -> Dict[str, Union[str, int, List[str]]]:
        """Analyze an IP range and suggest optimal subnets"""
        try:
            start = ipaddress.ip_address(start_ip)
            end = ipaddress.ip_address(end_ip)
            
            if start.version != end.version:
                raise ValueError("Start and end IP must be same version")
                
            if int(start) >= int(end):
                raise ValueError("Start IP must be less than end IP")
            
            # Calculate the range
            total_ips = int(end) - int(start) + 1
            
            # Find the smallest subnet that can contain this range
            import math
            required_bits = math.ceil(math.log2(total_ips))
            max_bits = 32 if isinstance(start, ipaddress.IPv4Address) else 128
            prefix_length = max_bits - required_bits
            
            # Try to create a network that encompasses the range
            try:
                # Start with the start IP and try different prefix lengths
                for prefix in range(prefix_length, max_bits + 1):
                    try:
                        network = ipaddress.ip_network(f"{start}/{prefix}", strict=False)
                        if end in network:
                            suggested_network = str(network)
                            break
                    except ValueError:
                        continue
                else:
                    suggested_network = "Multiple subnets required"
            except:
                suggested_network = "Complex range - manual subnetting required"
            
            result = {
                'start_ip': start_ip,
                'end_ip': end_ip,
                'total_addresses': total_ips,
                'suggested_network': suggested_network,
                'required_host_bits': required_bits,
                'minimum_prefix': max(0, max_bits - required_bits)
            }
            
            self.add_to_history(f"Analyze range {start_ip}-{end_ip}", f"{total_ips} addresses")
            return result
        except ValueError as e:
            raise ValueError(f"Invalid IP range: {e}")
    
    # Utility Methods
    def _get_network_class(self, ip: ipaddress.IPv4Address) -> str:
        """Determine network class for IPv4 address"""
        first_octet = int(str(ip).split('.')[0])
        
        if 1 <= first_octet <= 126:
            return "A"
        elif 128 <= first_octet <= 191:
            return "B"
        elif 192 <= first_octet <= 223:
            return "C"
        elif 224 <= first_octet <= 239:
            return "D (Multicast)"
        elif 240 <= first_octet <= 255:
            return "E (Experimental)"
        else:
            return "Invalid"
    
    def get_common_networks(self) -> Dict[str, str]:
        """Get common network addresses and their descriptions"""
        return {
            '10.0.0.0/8': 'Private Class A (RFC 1918)',
            '172.16.0.0/12': 'Private Class B (RFC 1918)',
            '192.168.0.0/16': 'Private Class C (RFC 1918)',
            '127.0.0.0/8': 'Loopback (RFC 3330)',
            '169.254.0.0/16': 'Link-Local (RFC 3927)',
            '224.0.0.0/4': 'Multicast Class D',
            '240.0.0.0/4': 'Reserved Class E',
            '0.0.0.0/8': 'This Network (RFC 1122)',
            '255.255.255.255/32': 'Broadcast Address'
        }
    
    def port_operations(self) -> Dict[str, Union[str, int, Dict[int, str]]]:
        """Common port number operations and well-known ports"""
        well_known_ports = {
            20: 'FTP Data',
            21: 'FTP Control',
            22: 'SSH',
            23: 'Telnet',
            25: 'SMTP',
            53: 'DNS',
            67: 'DHCP Server',
            68: 'DHCP Client',
            80: 'HTTP',
            110: 'POP3',
            143: 'IMAP',
            443: 'HTTPS',
            993: 'IMAPS',
            995: 'POP3S'
        }
        
        return {
            'well_known_ports': well_known_ports,
            'well_known_range': '0-1023',
            'registered_range': '1024-49151',
            'dynamic_private_range': '49152-65535',
            'total_ports': 65536
        }
