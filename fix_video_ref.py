import os

file_path = r"c:\Users\Dell\Downloads\appreciated_branding_685113.framer.app\framerusercontent.com\sites\48MCOqhODfyVzOdG9mV1qX\NcH5029BgX79nKIytcGse2DRphtQ5TjdrRsFljuy3ts.DT5eIYEg.mjs"
target_string = "framerusercontent.com/assets/oPHhAHkpf9UuzwlxgfTNSVFIn8.mp4"
replacement_string = "/shape-video.mp4"

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if target_string in content:
        new_content = content.replace(target_string, replacement_string)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully replaced '{target_string}' with '{replacement_string}'")
    else:
        print(f"Target string '{target_string}' not found in file.")
        # Try finding partial
        partial = "oPHhAHkpf9UuzwlxgfTNSVFIn8.mp4"
        if partial in content:
            print("Found partial match, attempting context print:")
            idx = content.find(partial)
            print(content[max(0, idx-100):min(len(content), idx+100)])

except Exception as e:
    print(f"Error: {e}")
