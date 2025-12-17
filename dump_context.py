
file_path = r"c:\Users\Dell\Downloads\appreciated_branding_685113.framer.app\framerusercontent.com\sites\48MCOqhODfyVzOdG9mV1qX\shared-lib.CA4b826s.mjs"
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    if len(lines) >= 7:
        line7 = lines[6]
        start = max(0, 19154 - 1000)
        end = min(len(line7), 19154 + 1000)
        print(f"--- START ---\n{line7[start:end]}\n--- END ---")
