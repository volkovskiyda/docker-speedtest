import subprocess
import json

SPEEDTEST_OUTPUT=subprocess.getoutput("speedtest --json")
JSON = json.loads(SPEEDTEST_OUTPUT)
SERVER=JSON["server"]
SERVER_SPONSOR=SERVER["sponsor"]
SERVER_NAME=SERVER["name"]
SERVER_COUNTRY=SERVER["country"]
SERVER_DISTANCE=SERVER["d"]
CLIENT=JSON["client"]
CLIENT_IP=CLIENT["ip"]
CLIENT_ISP=CLIENT["isp"]
CLIENT_COUNTRY=CLIENT["country"]
DOWNLOAD=JSON["download"]
UPLOAD=JSON["upload"]
SENT=JSON["bytes_sent"]
RECEIVED=JSON["bytes_received"]
PING=JSON["ping"]
print()
print(SPEEDTEST_OUTPUT)
print()
print(f"Server: {SERVER_SPONSOR} - {SERVER_NAME} [{SERVER_COUNTRY} - {round(SERVER_DISTANCE, 3)} km]")
print(f"Client: {CLIENT_ISP} [{CLIENT_COUNTRY} - {CLIENT_IP}]")
print()
print(f"Download: {round(DOWNLOAD / 1000000, 1)} Mbit/s [{round(RECEIVED / 1048576, 3)} MB]")
print(f"Upload: {round(UPLOAD  / 1000000, 1)} Mbit/s [{round(SENT / 1048576, 3)} MB]")
print()
print(f"Ping: {PING} ms")
