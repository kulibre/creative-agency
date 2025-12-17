import os

# Root directory of the downloaded site
root_dir = r"c:\Users\Dell\Downloads\appreciated_branding_685113.framer.app"

# Domains that map to folders in the root directory
# Key: Domain string found in files
# Value: Folder name in root_dir (usually the same)
domains = [
    "framer.com",
    "framerusercontent.com",
    "fonts.gstatic.com",
    "fonts.googleapis.com",
    "app.framerstatic.com",
    "events.framer.com"
]

extensions = ['.html', '.js', '.mjs', '.css']

def get_rel_path_to_root(file_path, root):
    # Directory of the current file
    file_dir = os.path.dirname(file_path)
    # Relative path from file_dir to root
    return os.path.relpath(root, file_dir)

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        rel_to_root = get_rel_path_to_root(file_path, root_dir)
        
        # Determine prefix for relative path (e.g., "../" or "./")
        # os.path.relpath returns "." if same dir
        prefix = rel_to_root
        if prefix != "." and not prefix.endswith(os.path.sep):
            prefix += "/"
        if prefix == ".":
            prefix = "./" # Explicit relative path for same dir usually safer in some contexts, or just "" but "framer.com" might be confused with root relative?
            # Actually, if file is in root, and we want to access "framer.com" folder => "./framer.com" or "framer.com".
            # Safest is probably just use the name if in root?
            # But let's stick to standard path joining.
            prefix = ""
        
        # Fix: Windows relpath uses backslashes, web uses forward slashes.
        prefix = prefix.replace("\\", "/")

        changes = 0
        for domain in domains:
            # We look for https://domain and http://domain
            # Also potentially //domain ?
            
            # Target replacement: prefix + domain
            replacement = prefix + domain
            
            # 1. https://domain
            target = f"https://{domain}"
            if target in content:
                content = content.replace(target, replacement)
                changes += 1
            
            # 2. http://domain (unlikely but possible)
            target = f"http://{domain}"
            if target in content:
                content = content.replace(target, replacement)
                changes += 1

        if changes > 0:
            print(f"Fixed {changes} links in {file_path}")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
                
    except Exception as e:
        print(f"Failed to process {file_path}: {e}")

# Walk
for root, dirs, files in os.walk(root_dir):
    for file in files:
        if any(file.lower().endswith(ext) for ext in extensions):
            process_file(os.path.join(root, file))

print("Recursive link fix completed.")
