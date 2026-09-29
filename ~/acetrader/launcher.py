#!/usr/bin/env python3
"""
AceTrader launcher — pick real or demo mode, then run.
"""

import os
import sys
import subprocess

CONFIG = "config.py"


def clear():
    os.system("clear" if os.name != "nt" else "cls")


def banner():
    print(r"""
    ___                 _____              _
   / _ \               |_   _| _ __ _  __| | ___ _ __
  / /_\ \  ___ ___ ___   | || '__/ _` |/ _` |/ _ \ '__|
 / /   \ \|___|___|___|  | || | | (_| | (_| |  __/ |
 \/     \/               |_||_|  \__,_|\__,_|\___|_|
""")
    print("  AceTrader\n")


def read_config():
    """Parse config.py as text — keep only the flag lines we care about."""
    with open(CONFIG) as f:
        return f.read()


def write_mode(real: bool):
    """Toggle PAPER_MODE in config.py."""
    lines = read_config().splitlines()
    out = []
    for ln in lines:
        if ln.strip().startswith("PAPER_MODE"):
            # preserve indentation, replace value
            out.append("PAPER_MODE = " + ("False" if real else "True"))
        else:
            out.append(ln)
    with open(CONFIG, "w") as f:
        f.write("\n".join(out) + "\n")


def current_mode():
    txt = read_config()
    for ln in txt.splitlines():
        s = ln.strip()
        if s.startswith("PAPER_MODE"):
            val = s.split("=", 1)[1].strip()
            return "REAL" if val == "False" else "DEMO"
    return "DEMO"


def menu():
    clear()
    banner()
    print("  What would you like to play?\n")
    print("  [1]  Real money 💰")
    print("  [2]  Demo / practice money 💰")
    print("  [0]  Exit\n")
    print(f"  Current mode: {current_mode()}\n")
    try:
        return input("  Your choice >> ").strip()
    except (EOFError, KeyboardInterrupt):
        return "0"


def confirm_real():
    clear()
    banner()
    print("  ⚠  REAL MONEY MODE\n")
    print("  Every trade places a real order. Losses are permanent.")
    print("  Pocket Broker is flagged as a high-risk platform.\n")
    print("  Current risk caps in config.py:")
    txt = read_config()
    for ln in txt.splitlines():
        s = ln.strip()
        if s.startswith(("TRADE_AMOUNT", "MAX_DAILY_LOSS", "MAX_DRAWDOWN")):
            print("    " + s)
    print()
    ans = input("  Type YES to continue with real money >> ").strip()
    return ans == "YES"


def launch():
    print(f"\n  [*] Starting AceTrader ({current_mode()} mode)...\n")
    try:
        subprocess.run(
            [sys.executable, "main.py"],
            check=False,
        )
    except KeyboardInterrupt:
        print("\n  [*] Stopped.")


def ensure_config_exists():
    if not os.path.exists(CONFIG):
        print(f"[!] {CONFIG} not found. Run this from ~/acetrader.")
        sys.exit(1)


def main():
    ensure_config_exists()

    while True:
        choice = menu()

        if choice == "0":
            print("  Bye.")
            break

        if choice == "1":
            if confirm_real():
                write_mode(real=True)
                print("  [✓] Mode set to REAL.")
                launch()
                input("\n  Press Enter to return to menu...")
            else:
                print("  Cancelled.")

        elif choice == "2":
            write_mode(real=False)
            print("  [✓] Mode set to DEMO.")
            launch()
            input("\n  Press Enter to return to menu...")

        else:
            print("  [!] Pick 1, 2, or 0.")
            input("  Enter to continue...")


if __name__ == "__main__":
    main()
