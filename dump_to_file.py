
file_path = r"c:\Users\Dell\Downloads\appreciated_branding_685113.framer.app\framerusercontent.com\sites\48MCOqhODfyVzOdG9mV1qX\shared-lib.CA4b826s.mjs"
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    if len(lines) >= 7:
        line7 = lines[6]
        chunk = line7[19000:20000]
        with open("dump.txt", "w", encoding="utf-8") as out:
            out.write(chunk)
