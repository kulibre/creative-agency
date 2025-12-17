
import os

# Define the file to process
file_path = "index.html"

# Domains/Folders that were previously referenced with ../
domains = [
    "framer.com",
    "framerusercontent.com",
    "fonts.gstatic.com",
    "fonts.googleapis.com",
    "app.framerstatic.com",
    "events.framer.com"
]

def fix_links(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        changes = 0
        original_content = content
        
        for domain in domains:
            # Replace "../domain" with "domain"
            target = f"../{domain}"
            replacement = domain # Since index.html is now in root, and so are these folders
            
            if target in content:
                count = content.count(target)
                content = content.replace(target, replacement)
                changes += count
                print(f"Replaced {count} occurrences of '{target}' with '{replacement}'")

        if changes > 0:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Successfully fixed {changes} links in {file_path}")
        else:
            print(f"No changes needed for {file_path}")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    if os.path.exists(file_path):
        fix_links(file_path)
    else:
        print(f"File {file_path} not found.")
