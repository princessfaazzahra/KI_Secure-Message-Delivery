import sys
import os
from Crypto.PublicKey import RSA

def generate_keys(name):
    # Buat folder keys/ kalau belum ada
    os.makedirs("keys", exist_ok=True)

    # Generate RSA 2048-bit key pair
    key = RSA.generate(2048)

    # Simpan private key
    private_key_path = f"keys/{name}_private.pem"
    with open(private_key_path, "wb") as f:
        f.write(key.export_key())
    print(f"[+] Private key saved: {private_key_path}")

    # Simpan public key
    public_key_path = f"keys/{name}_public.pem"
    with open(public_key_path, "wb") as f:
        f.write(key.publickey().export_key())
    print(f"[+] Public key saved:  {public_key_path}")

    print(f"\n[!] PENTING:")
    print(f"    - Kirim file '{public_key_path}' ke partner kamu.")
    print(f"    - JANGAN pernah kirim file '{private_key_path}' ke siapapun!")

if __name__ == "__main__":
    # Allow any safe name (letters, digits, underscore, dash) so you can use custom names
    import re

    if len(sys.argv) != 2:
        print("Usage: python generate_keys.py <name>")
        print("Example: python generate_keys.py sender")
        print("         python generate_keys.py receiver")
        print("You can also use any short identifier (letters, digits, underscore, dash).")
        sys.exit(1)

    name = sys.argv[1]
    if not re.fullmatch(r"[A-Za-z0-9_-]+", name):
        print("Invalid name. Use letters, digits, underscore or dash only (no spaces).")
        sys.exit(1)

    generate_keys(name)
