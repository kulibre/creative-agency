
import os

file_path = r"c:\Users\Dell\Downloads\appreciated_branding_685113.framer.app\appreciated-branding-685113.framer.app\index.html"

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
in_handover = False
handover_buffer = []

for line in lines:
    if 'id="__framer__handoverData">' in line:
        in_handover = True
        # Keep the start tag, but maybe strip the newline after it if the content starts immediately?
        # The file content viewed showed: ...handoverData">[{"0":1... ending with proper content.
        # But subsequent lines were split.
        handover_buffer.append(line.rstrip('\n\r'))
    elif in_handover:
        if '</script>' in line:
            in_handover = False
            # Append the accumulated buffer as one line
            # Check if current line has content before </script>
            parts = line.split('</script>')
            handover_buffer.append(parts[0].strip()) # Add content before script end
             # Join all buffer parts. We add spaces? No, JSON strings split by downloader usually have extra whitespace added.
            # But if a string was "foo\nbar", joining with space "foo bar" is usually safer than "foobar" for attributes like `srcset`.
            # Wait, `srcset` in HTML uses spaces. `... 512w, ...`
            # The split was `...1766\n        512w...`
            # If I join with space: `...1766         512w...`.
            # If I join with empty string: `...1766        512w...` (spaces were in next line indentation).
            # I should strip leading spaces from the next line?
            # Ideally I just join them.
            
            # Let's simple join with nothing, but assuming I strip the indentation of the continuation lines.
            full_line = "".join(handover_buffer) 
            # But wait, `line.rstrip` kept the previous line content.
            # The next line has indentation `        512w`.
            # If I just join, I keep 8 spaces. `...1766        512w`. This is valid in a string?
            # Yes, spaces in a string are valid. Newlines are NOT (unless escaped).
            # So simply joining them (removing the actual \n character) makes it a valid string with spaces.
            
            new_lines.append(full_line + '</script>' + parts[1] if len(parts)>1 else full_line + '</script>\n')
            handover_buffer = []
        else:
            # Middle line. Strip newline.
            handover_buffer.append(line.rstrip('\n\r'))
    else:
        new_lines.append(line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Fixed handover JSON.")
