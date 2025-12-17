
import re

file_path = r"c:\Users\Dell\Downloads\appreciated_branding_685113.framer.app\framerusercontent.com\sites\48MCOqhODfyVzOdG9mV1qX\shared-lib.CA4b826s.mjs"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# We look for new URL(..., "...") where the second arg starts with . and is NOT wrapped in new URL(..., import.meta.url)
# This is hard to regex perfectly, but we can look for specific patterns.
# The previous fix produced: new URL(..., new URL("...", import.meta.url))
# The BROKEN pattern looks like: new URL("...", "../../../...")

# Let's find matches of: new URL( [^,]+ , ["'] \.\.
# i.e. new URL, then arg1, then comma, then quote, then ..
broken_pattern = re.compile(r'new URL\([^,]+,\s*[\'"]\.\.')

matches = broken_pattern.finditer(content)
count = 0
for m in matches:
    count += 1
    start = m.start()
    end = min(start + 100, len(content))
    print(f"Broken URL call found at {start}: {content[start:end]}")

if count == 0:
    print("No obvious broken URL calls found.")
else:
    print(f"Found {count} broken calls.")
