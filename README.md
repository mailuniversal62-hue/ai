
# AceTrader

Auto-trader for Pocket Broker. Runs as a service on Kali. Dashboard on phone.

**Paper mode by default** — no real money until you flip `PAPER_MODE = False` in `config.py`.

## Install

```bash
git clone https://github.com/YOU/acetrader.git
cd acetrader
chmod +x setup.sh
./setup.sh


Run manually
source venv/bin/activate
python3 main.py           # the bot
python3 dashboard.py      # the dashboard (separate terminal)

Install as services
sudo cp acetrader.service dashboard.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable acetrader dashboard
sudo systemctl start acetrader dashboard



---

## SETUP ON KALI

```bash
mkdir -p ~/acetrader/logs
cd ~/acetrader
# paste all the files above
chmod +x setup.sh
./setup.sh
nano config.py   # paste SSID



Test manually first:
source venv/bin/activate
python3 main.py          # in terminal 1
python3 dashboard.py     # in terminal 2



THEN INSTALL AS SERVICES
# passwordless sudo for start/stop
sudo visudo -f /etc/sudoers.d/acetrader


Paste:
ace ALL=(ALL) NOPASSWD: /bin/systemctl start acetrader
ace ALL=(ALL) NOPASSWD: /bin/systemctl stop acetrader
ace ALL=(ALL) NOPASSWD: /bin/systemctl restart acetrader



bash
sudo cp ~/acetrader/acetrader.service /etc/systemd/system/
sudo cp ~/acetrader/dashboard.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable acetrader dashboard
sudo systemctl start acetrader dashboard


Check
sudo systemctl status acetrader
sudo systemctl status dashboard


WHAT TO DO NOW
Build the folder, paste the files

./setup.sh

Paste your SSID in config.py

Run python3 main.py — should connect and start logging signals

Run python3 dashboard.py — open on your phone

Test start/stop buttons (they'll only work after services are installed with sudoers set up)
