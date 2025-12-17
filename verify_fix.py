
file_path = r"c:\Users\Dell\Downloads\appreciated_branding_685113.framer.app\framerusercontent.com\sites\48MCOqhODfyVzOdG9mV1qX\shared-lib.CA4b826s.mjs"
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

if "import.meta.url" in content and "new URL(" in content:
    # Check for the specific nested pattern
    # new URL(..., new URL(
    count = content.count("new URL(")
    nested = content.count("new URL(`, import.meta.url)") + content.count("new URL(', import.meta.url)") + content.count('new URL(", import.meta.url)')
    # Also backticks might have content: new URL(`...`, import.meta.url)
    
    # Let's just print a snippet where we expect the fix
    idx = content.find("import.meta.url")
    if idx != -1:
        print(f"Found fix context: ...{content[idx-50:idx+20]}...")
    else:
        print("Fix NOT found (import.meta.url missing)")
else:
    print("File content missing expected keywords")
