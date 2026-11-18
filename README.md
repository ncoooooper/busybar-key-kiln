# Key Kiln

Separate daily physical key presses from characters entered in an opt-in writing pad.

Run swift companion/keys.swift ~/key-counts.json for system-wide aggregate key-down counts. It reads the WindowServer event counter only. For characters, run python3 companion/writer.py ~/character-counts.json using a Python installation with Tk. Only text inserted in that visible writer counts, including paste. Deletion leaves the cumulative typed count intact. The writer stores counts and minute numbers only. Set key_file and character_file to the same paths.

## Connect the bar

Copy companion/example.json to a private config.json and adjust it for your source. From the project folder run `python3 companion/serve.py --config config.json`. Use Python 3.10+. Set Local companion URL to `http://127.0.0.1:8770/reading` on the emulator and allow local port 8770. On hardware, bind the companion to a trusted LAN interface and set its reachable address. The wheel browses pages. Click refreshes. Start pins or unpins the current page. The last good reading is labeled offline after a source error.

## Run locally

From this folder, run `~/.busy-emulator/bin/busy-emulator dev --once` with BUSY Bar Emulator open. Back exits.

![BUSY Bar front display](screenshots/front-1.png)
