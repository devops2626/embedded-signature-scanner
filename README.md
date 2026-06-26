# Embedded Systems Signature Scanner

## Engineer Identity
**Barki Mustapha**
- Engineering Automation & Embedded Systems Specialist
- GitHub: [@devops2626](https://github.com/devops2626)
- Email: devops26@icloud.com

## Project Purpose
This repository demonstrates embedding and scanning for cryptographic/identifying signatures in firmware binaries. Standard practice for provenance and integrity in embedded systems engineering.

## Files
- `stream_scanner.py`: Scans binaries for ASCII strings and engineer signatures (ENG_ prefix).
- `mystery.bin`: Test binary with embedded signature.

## Usage
```bash
python3 stream_scanner.py mystery.bin
```

## Embedding Signature
```bash
echo "ENG_BARKI_MUSTAPHA_EMBEDDED_2026" | dd of=your_binary bs=1 seek=512 conv=notrunc
```

Proudly maintained by Barki Mustapha for scaling embedded automation solutions.
