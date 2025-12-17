import os

file_path = r"c:\Users\Dell\Downloads\appreciated_branding_685113.framer.app\appreciated-branding-685113.framer.app\index.html"

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    i = 0
    fixed = False
    while i < len(lines):
        line = lines[i]
        # Check for the specific broken line identified
        # Line 21407 ends with: "matchMedia":"(min-width:
        # Actually it was mediaQuery
        # Content: ... {"hash":"1nmzu2p","mediaQuery":"(min-width:
        # Next line:         810px) and (max-width: 1439.98px)"} ...
        
        if 'mediaQuery":"(min-width:' in line and line.strip().endswith(':'):
            # Found the split line.
            # We assume the next line completes it.
            next_line = lines[i+1]
            combined = line.rstrip('\n\r') + " " + next_line.lstrip()
            new_lines.append(combined)
            i += 2
            fixed = True
            print("Fixed broken JSON line.")
        else:
            new_lines.append(line)
            i += 1

    if fixed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
    else:
        print("Pattern not found, scanning content manually to see if it's already fixed or different.")
        # Fallback: Read whole content and regex replace
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            import re
            # Regex to find newline inside the specific mediaQuery string
            pattern = re.compile(r'("mediaQuery":"\(min-width:)\s*\n\s*(\d+px\))')
            if pattern.search(content):
                print("Found pattern via regex, replacing...")
                new_content = pattern.sub(r'\1 \2', content)
                with open(file_path, 'w', encoding='utf-8') as f_out:
                    f_out.write(new_content)
                print("Fixed via regex.")

except Exception as e:
    print(f"Error: {e}")
