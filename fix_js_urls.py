import os
import re

root_dir = r"c:\Users\Dell\Downloads\appreciated_branding_685113.framer.app"
extensions = ['.js', '.mjs']

# Regex to find new URL(first_arg, "relative_path")
# We look for: new URL( <anything reasonable>, <quote>../<anything><quote> )
# We need to capture the quote style to match ending quote.
pattern = re.compile(r'new URL\(([^,]+),\s*([\'"])((\.\./|[a-zA-Z0-9_.-]+/)[^"\']+)\2\)')

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Function to replace the match
        def replacer(match):
            first_arg = match.group(1)
            quote = match.group(2)
            rel_path = match.group(3)
            
            # If the path looks like one we replaced (starts with ../ or is relative), wrap it.
            # We specifically look for our replacements which look like ../framer...
            # But the regex constraints (starts with ../ or folder/) are broad.
            # Let's check if it points to one of our known domains to be safe, or just looks like a file path.
            
            # Result: new URL(first_arg, new URL("rel_path", import.meta.url))
            return f"new URL({first_arg}, new URL({quote}{rel_path}{quote}, import.meta.url))"

        new_content, count = pattern.subn(replacer, content)

        if count > 0:
            print(f"Fixed {count} new URL() calls in {file_path}")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

    except Exception as e:
        print(f"Failed to process {file_path}: {e}")

for root, dirs, files in os.walk(root_dir):
    for file in files:
        if any(file.lower().endswith(ext) for ext in extensions):
            process_file(os.path.join(root, file))

print("JS URL fix completed.")
