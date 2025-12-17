import os
import re

root_dir = r"c:\Users\Dell\Downloads\appreciated_branding_685113.framer.app"
extensions = ['.js', '.mjs']

# Updated regex to include backticks
# looking for: new URL(..., `...`) or "..." or '...'
# Quote group now includes `
pattern = re.compile(r'new URL\(([^,]+),\s*([\'"`])((\.\./|[a-zA-Z0-9_.-]+/)[^"`\']+)\2\)')

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Function to replace the match
        def replacer(match):
            first_arg = match.group(1)
            quote = match.group(2)
            rel_path = match.group(3)
            
            # Check if it's already wrapped (prevent double wrapping if run multiple times)
            # The regex ensures it ends with the closing quote \2 matching \2.
            # If we replaced it, it would look like new URL(..., new URL(..., ...))
            # The regex expects a string literal as the second arg.
            # So `new URL(..., new URL(...))` naturally won't match the regex (arg2 is not a string literal).
            
            return f"new URL({first_arg}, new URL({quote}{rel_path}{quote}, import.meta.url))"

        new_content, count = pattern.subn(replacer, content)

        if count > 0:
            print(f"Fixed {count} new URL() calls in {file_path}")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
        else:
            print(f"No matches in {file_path}")

    except Exception as e:
        print(f"Failed to process {file_path}: {e}")

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if any(file.lower().endswith(ext) for ext in extensions):
            process_file(os.path.join(root, file))

print("JS URL fix (v2 with backticks) completed.")
