import sys
import re

def scan_binary(file_path):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        
        print(f"[*] Scanning {file_path} ({len(data)} bytes)...")
        print("-" * 50)
        
        # 1. Look for ASCII strings (minimum 4 printable characters)
        # This acts like the Linux 'strings' command
        ascii_strings = re.findall(b'[ -~]{4,}', data)
        
        # 2. Check for your specific Engineering Signature
        engineer_signature = None
        for s in ascii_strings:
            decoded = s.decode('ascii', errors='ignore')
            if "FLAG" in decoded or "ENG_" in decoded: 
                engineer_signature = decoded
                print(f"[+] Found Signature: {decoded}")
                
        if not engineer_signature:
            print("[-] No recognized engineer signature found.")
            
        print("-" * 50)
        
    except FileNotFoundError:
        print(f"[-] Error: File '{file_path}' not found.")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "mystery.bin"
    scan_binary(target)
