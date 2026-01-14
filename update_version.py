import re
import datetime

def update_version():
    filepath = 'index.html'
    with open(filepath, 'r') as f:
        content = f.read()

    # Regex to find the version span
    # <span id="version-number">v1.0.0</span>
    pattern = r'(<span id="version-number">v)(\d+)\.(\d+)\.(\d+)(</span>)'

    match = re.search(pattern, content)
    if match:
        prefix = match.group(1)
        major = int(match.group(2))
        minor = int(match.group(3))
        patch = int(match.group(4))
        suffix = match.group(5)

        old_version = f"{major}.{minor}.{patch}"

        # Increment patch version
        new_patch = patch + 1
        new_version = f"{major}.{minor}.{new_patch}"

        new_content = re.sub(pattern, f"{prefix}{new_version}{suffix}", content)

        with open(filepath, 'w') as f:
            f.write(new_content)

        print(f"Updated version from v{old_version} to v{new_version}")
    else:
        print("Version pattern not found in index.html")

if __name__ == "__main__":
    update_version()
