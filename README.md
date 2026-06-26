# Embedded Systems Signature Scanner

## Professional Identity
**Barki Mustapha**  
**Engineering Automation & Embedded Systems Specialist**  

- **GitHub**: [devops2626](https://github.com/devops2626)  
- **Email**: devops26@icloud.com  
- **Focus**: Firmware integrity, binary signature embedding, embedded systems automation, and DevOps practices.

## Project Description
This repository contains a Python-based binary stream scanner designed to extract printable strings and identify custom engineering signatures (e.g., `ENG_` prefixed markers) from firmware images and binaries. It supports provenance verification and integrity checks for embedded systems development.

The tool was created to demonstrate secure signature embedding practices in binaries.

## Key Features
- Scans for ASCII strings (like Linux `strings` command)
- Detects custom engineering signatures (`ENG_`, `FLAG{}`)
- Lightweight and reusable for CI/CD pipelines
- Includes sample `mystery.bin` with embedded signature

## Usage
```bash
# Clone the repo
git clone https://github.com/devops2626/embedded-signature-scanner.git
cd embedded-signature-scanner

# Run the scanner
python3 stream_scanner.py mystery.bin
```

Expected output will detect:
```
[+] Found Signature: ENG_BARKI_MUSTAPHA_EMBEDDED_2026_ENGINEERING_AUTOMATION
```

## Embedding Your Signature
To embed your own signature in a binary:
```bash
echo "ENG_BARKI_MUSTAPHA_EMBEDDED_2026_ENGINEERING_AUTOMATION" | dd of=your_binary.bin bs=1 seek=1024 conv=notrunc
```

## Future Enhancements
- Cryptographic signature verification (SHA-256, CRC32)
- Support for more file formats
- Integration with build pipelines

---

*Maintained by Barki Mustapha — Engineering Automation & Embedded Systems*  
*All rights reserved. Contributions welcome via Pull Requests.*