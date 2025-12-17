
file_path = r"c:\Users\Dell\Downloads\appreciated_branding_685113.framer.app\framerusercontent.com\sites\48MCOqhODfyVzOdG9mV1qX\shared-lib.CA4b826s.mjs"
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    if len(lines) >= 7:
        line7 = lines[6]
        # target is 19154. Let's look widely.
        start = 19100
        end = 19300
        print(f"LEN: {len(line7)}")
        print(f"CHUNK: {line7[start:end]}")
        
    else:
        print("File too short")
