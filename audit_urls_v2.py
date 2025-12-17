
import re

file_path = r"c:\Users\Dell\Downloads\appreciated_branding_685113.framer.app\framerusercontent.com\sites\48MCOqhODfyVzOdG9mV1qX\shared-lib.CA4b826s.mjs"

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Check for new URL(..., ".") or new URL(..., "..")
# Regex: new URL <any chars> , <quote> . <any chars>
broken_pattern = re.compile(r'new URL\([^,]+,\s*[\'"]\.')

matches = broken_pattern.finditer(content)
count = 0
for m in matches:
    # Check if this match is wrapped in "new URL(..., import.meta.url)"
    # We can peek ahead to see if "import.meta.url" follows immediately?
    # No, we want to find cases where the second arg IS THE STRING starting with .
    
    # We found `new URL(A, ".`
    # If the text immediately following `.` is NOT wrapped, it's a bug.
    # But wait, my fix wrapped the *entire* string.
    # So `new URL(A, new URL(".", import.meta.url))`
    # The regex `new URL\([^,]+,\s*[\'"]\.` will match `new URL(".", import.meta.url)` ?
    # No, `new URL(".", ...` matches `new URL(A, B)` where A is `.`.
    # My regex searches for `new URL(A, B)` where B follows comma.
    
    # The previous fix produced: `new URL(first_arg, new URL("rel_path", import.meta.url))`
    # Here the second inner URL has `rel_path` as first arg.
    # The OUTER URL has `new URL(...)` as second arg.
    
    # So valid: `new URL('foo', new URL('bar', base))`
    # Invalid: `new URL('foo', 'bar')` where bar starts with .
    
    # Let's find invalid ones.
    start = m.start()
    chunk = content[start:start+200]
    
    # If the match is `new URL('foo', new URL` -> The second arg starts with `n`, not `.`.
    # So `new URL\([^,]+,\s*[\'"]\.` WONT match the outer valid call.
    
    # Will it match the INNER valid call? `new URL('bar', import.meta.url)`?
    # Yes, `new URL('bar',` matches.
    # But wait, the second arg is `import.meta.url`. It does NOT start with `.`.
    
    # So valid inner: `new URL('./path', import.meta.url)`
    # Arg1 = `./path`. Arg2 = `import.meta.url`.
    # My regex is checking `new URL` followed by Arg1??
    # `new URL\([^,]+,\s*[\'"]\.)`
    # `[^,]+` matches `( './path'`... wait.
    # `new URL` then `(` then `[^,]+` (e.g. `'./path'`) then `,` then `space` then `'` then `.`.
    
    # This regex matches `new URL(A, './B')`.
    # It does NOT match `new URL('./A', B)`.
    
    # So if I find a match, it means `new URL(..., './...')`.
    # This is EXACTLY the bug (relative base).
    
    # Exception: `new URL(..., './...', base)` - 3 args? new URL only takes 2.
    
    # So any match is a bug?
    # Unless `new URL` is used differently? No.
    
    count += 1
    print(f"Potential BROKEN URL at {start}: {chunk[:80]}")

if count == 0:
    print("No broken URL calls found (checked for single dot too).")
else:
    print(f"Found {count} broken calls.")
