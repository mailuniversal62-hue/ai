#!/bin/bash
set -e

echo "[*] Creating venv..."
python3 -m venv venv
source venv/bin/activate

echo "[*] Installing deps..."
pip install --upgrade pip
pip install -r requirements.txt

echo "[*] Creating directories..."
mkdir -p logs

echo "[+] Done."
echo "[+] Run: source venv/bin/activate && python3 main.py"
