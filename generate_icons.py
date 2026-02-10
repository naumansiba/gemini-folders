import base64

# Simple 1x1 transparent PNG or similar base64. 
# Actually let's use a 16x16 blue square
APP_ICON_B64 = "iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAA6SURBVDhPY/wPBAwUACMjI/8JAG5hYWAE04wMIDAwMDIyMhKjF6sLmJGR/wQ1gH6gH0B+oB8YqB8AAQYAMzMvwd/vmk4AAAAASUVORK5CYII="

def create_icon(filename):
    with open(filename, "wb") as f:
        f.write(base64.b64decode(APP_ICON_B64))
    print(f"Created {filename}")

if __name__ == "__main__":
    create_icon("icon16.png")
    create_icon("icon48.png")
    create_icon("icon128.png")
