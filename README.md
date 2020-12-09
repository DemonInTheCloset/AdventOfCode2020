# AdventOfCode2020
My solutions to AdventOfCode 2020 (https://adventofcode.com)

# Prepare Environment Script
## How to Use
1. Download `template.py` and `prepare_environment.py` (You can modify template.py however you like, but remember to keep `FILE_NAME = None`)
2. Create a file called session.txt
3. Get your session cookies from adventofcode.com (search google on how to do that)
4. Save them to session.txt (You only need "session: yoursecretkey")
5. DON'T SHARE THEM
6. Install the requests library (`pip install requests`)
7. Run the script (`python prepare_environment.py DAY`)

The script will download the input from Advent of Code and write it to `inputDAY.txt`, it will also copy the `template.py` file to `dayDAY.py` and fill the variable FILE_NAME.

Replace DAY with the day number.
