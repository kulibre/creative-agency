import os
import re

target_file = r"c:\Users\Dell\Downloads\appreciated_branding_685113.framer.app\appreciated-branding-685113.framer.app\index.html"

try:
    with open(target_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix Nullish Coalescing Operator: "? ?" -> "??"
    # Be careful not to replace valid text, but in likely minified JS, this pattern is almost certainly an error.
    # We will use regex to textually replace it.
    
    # We'll replace "? ?" with "??"
    original_len = len(content)
    new_content = content.replace("? ?", "??")
    
    # Fix Optional Chaining: "? ." -> "?."
    new_content = new_content.replace("? .", "?.")

    if len(new_content) != original_len:
        print(f"Modified content length: {len(new_content)} (orig: {original_len})")
        with open(target_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Syntax fixes applied.")
    else:
        print("No patterns found to fix.")

except Exception as e:
    print(f"Error: {e}")
