import os
import time

NODE_ID = "12007250"

while True:
    print(f"\n🌀 [AUTO-RESTART] Starting Nexus Node ID: {NODE_ID}")
    os.system(f"~/.nexus/bin/nexus-cli start --node-id {NODE_ID}")
    print("⚠️  Node process ended. Auto-restarting in 10 seconds...\n")
    time.sleep(10)
