
file_path = r"c:\Users\Dell\Downloads\appreciated_branding_685113.framer.app\framerusercontent.com\sites\48MCOqhODfyVzOdG9mV1qX\shared-lib.CA4b826s.mjs"
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    # Line 7 (index 6)
    if len(lines) >= 7:
        line7 = lines[6] # 0-indexed
        # We want around char 19154
        start = max(0, 19154 - 200)
        end = min(len(line7), 19154 + 200)
        print(f"Context at 19154: ...{line7[start:end]}...")
    else:
        print("File has fewer than 7 lines.")
