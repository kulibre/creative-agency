
import re

file_path = r"c:\Users\Dell\Downloads\appreciated_branding_685113.framer.app\framerusercontent.com\sites\48MCOqhODfyVzOdG9mV1qX\shared-lib.CA4b826s.mjs"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all occurrences of new URL(...)
# matches = re.finditer(r'new URL\(([^)]+)\)', content)
# Simple scan to avoid complicated nested parenthesis regex issues
start = 0
while True:
    idx = content.find('new URL(', start)
    if idx == -1:
        break
    
    # Grab a chunk around it
    chunk = content[idx:idx+300]
    print(f"Match at {idx}: {chunk}")
    start = idx + 1
