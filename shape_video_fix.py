
import os
import re

file_path = "index.html"
video_filename = "shape-video.mp4"

# The HTML for the video tag
# We style it to be absolute, covering the container.
# z-index: 0 to ensure it's at the back, but the container has `overflow: hidden` so it should clip.
# We'll use object-fit: cover to fill the shape.
video_html = f'''
<div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; overflow: hidden; pointer-events: none;">
    <video autoplay loop muted playsinline style="width: 100%; height: 100%; object-fit: cover;">
        <source src="{video_filename}" type="video/mp4">
    </video>
</div>
'''

def inject_video():
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Target string
        # <div class="framer-joxslq" data-framer-appear-id="joxslq" data-framer-name="Container" style="opacity:0.001;transform:none">
        
        # We need to be careful about the exact attributes and order.
        # regex is safer for attributes order differences, though in this file it seems generated and consistent.
        
        # We will look for data-framer-name="Right" then find the nested data-framer-name="Container"
        # Actually, standard regex for the specific Container line should be fine.
        
        target_regex = r'(<div [^>]*data-framer-name="Right"[^>]*>\s*<div [^>]*data-framer-appear-id="joxslq"[^>]*>)'
        
        # The above regex might be tricky across lines.
        # Let's try to match the Container tag directly.
        # The class `framer-joxslq` and `data-framer-name="Container"` are key.
        
        # Let's just search for the specific unique line content we saw:
        # <div class="framer-joxslq" data-framer-appear-id="joxslq" data-framer-name="Container" style="opacity:0.001;transform:none">
        # BUT, to be safe, I'll use a regex that is flexible with spaces and attributes.
        
        pattern = r'(<div\s+class="framer-joxslq"\s+data-framer-appear-id="joxslq"\s+data-framer-name="Container"\s+style="opacity:0\.001;transform:none">)'
        
        match = re.search(pattern, content)
        
        if match:
            print("Found target container.")
            span = match.span()
            # Inject AFTER the opening tag
            new_content = content[:span[1]] + video_html + content[span[1]:]
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("Successfully injected shape video.")
        else:
            print("Could not find target shape container. Trying looser regex...")
            # Fallback
            fallback_pattern = r'(<div [^>]*data-framer-name="Container"[^>]*data-framer-appear-id="joxslq"[^>]*>)'
            match = re.search(fallback_pattern, content)
            if match:
                print("Found target container with looser regex.")
                span = match.span()
                new_content = content[:span[1]] + video_html + content[span[1]:]
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print("Successfully injected shape video.")
            else:
                print("Failed to find target container.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    inject_video()
