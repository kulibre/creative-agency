
import os
import re

file_path = "index.html"
video_filename = "hero-bg.mp4"

# The HTML for the video tag
# We style it to be absolute, covering the hero section, behind content.
video_html = f'''
<div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 0; overflow: hidden; pointer-events: none;">
    <video autoplay loop muted playsinline style="width: 100%; height: 100%; object-fit: cover;">
        <source src="{video_filename}" type="video/mp4">
    </video>
    <div style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.4);"></div>
</div>
'''

def inject_video():
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        return

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Target hierarchy:
        # <section class="framer-1drbok6" data-framer-name="Hero section" id="home">
        #   <div class="framer-ilm3pm" data-framer-name="Hero"> -> Inject here, before content or as background
        
        # Finding the Hero section div by its class and data attribute. 
        # The class 'framer-ilm3pm' seems unique enough from previous cat, but regex is safer with data-framer-name="Hero"
        
        # We want to inject it RIGHT AFTER the opening tag of the Hero container so it sits at the bottom of the stack (if z-index logic applies normally) 
        # OR we use z-index.
        
        # The Hero section has children with z-index: 2 (from CSS view earlier).
        # So our video wrapper needs z-index: 0 or 1.
        
        # Let's look for: <div class="framer-ilm3pm" data-framer-name="Hero">
        target_str = '<div class="framer-ilm3pm" data-framer-name="Hero">'
        
        if target_str in content:
            # Inject immediately after
            new_content = content.replace(target_str, target_str + video_html)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print("Successfully injected video background.")
        else:
            print("Could not find target Hero section string.")
            # Fallback search if classes changed?
            # Regex search for data-framer-name="Hero"
            match = re.search(r'<div [^>]*data-framer-name="Hero"[^>]*>', content)
            if match:
                print("Found via regex, replacing...")
                span = match.span()
                new_content = content[:span[1]] + video_html + content[span[1]:]
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print("Successfully injected video background via regex.")
            else:
                print("Failed to find Hero section.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    inject_video()
