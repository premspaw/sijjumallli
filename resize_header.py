import os

files = [
    "index.html",
    "criminal-law.html",
    "civil-law.html",
    "constitutional-law.html",
    "family-law.html",
    "ndps-matters.html",
    "money-laundering.html",
    "dispute-resolution.html",
    "non-litigation.html",
    "service-matters.html"
]

base_dir = r"c:\Users\TEJAL CHAVAN\Desktop\sijjumallli\sijjumallli"

replacements = {
    # 1. Navbar default height
    "  height: 70px;": "  height: 90px;",
    
    # 2. Navbar stuck state height insertion
    """#nav.stuck {
  padding: 1.1rem 5vw;
  background: #000000;
  border-bottom: 1px solid rgba(255,255,255,0.15);
  backdrop-filter: blur(12px);
}""": """#nav.stuck {
  height: 76px;
  padding: 1.1rem 5vw;
  background: #000000;
  border-bottom: 1px solid rgba(255,255,255,0.15);
  backdrop-filter: blur(12px);
}""",

    # 3. Logo text size (SMA)
    "  font-size: 1.55rem; font-weight: 500;": "  font-size: 1.8rem; font-weight: 500;",
    
    # 4. Logo vertical line height
    "  .nav-vline { width: 1px; height: 26px; background: rgba(255, 255, 255, 0.2); }": "  .nav-vline { width: 1px; height: 34px; background: rgba(255, 255, 255, 0.2); }",
    ".nav-vline { width: 1px; height: 26px; background: rgba(255, 255, 255, 0.2); }": ".nav-vline { width: 1px; height: 34px; background: rgba(255, 255, 255, 0.2); }",

    # 5. Firm name text size
    "  font-size: 0.9rem; font-weight: 400; color: #ffffff; letter-spacing: 0.06em; line-height: 1.3;": "  font-size: 1.05rem; font-weight: 400; color: #ffffff; letter-spacing: 0.06em; line-height: 1.3;",
    "font-size: 0.9rem; font-weight: 400; color: #ffffff; letter-spacing: 0.06em; line-height: 1.3;": "font-size: 1.05rem; font-weight: 400; color: #ffffff; letter-spacing: 0.06em; line-height: 1.3;",
    
    # 6. Tagline span text size
    "  display: block; font-size: 0.6rem;\n  font-family: 'Poppins', sans-serif; font-weight: 300;\n  letter-spacing: 0.18em; text-transform: uppercase; color: #a0a0a0;": "  display: block; font-size: 0.72rem;\n  font-family: 'Poppins', sans-serif; font-weight: 300;\n  letter-spacing: 0.18em; text-transform: uppercase; color: #a0a0a0;",
    "display: block; font-size: 0.6rem;\n  font-family: 'Poppins', sans-serif; font-weight: 300;\n  letter-spacing: 0.18em; text-transform: uppercase; color: #a0a0a0;": "display: block; font-size: 0.72rem;\n  font-family: 'Poppins', sans-serif; font-weight: 300;\n  letter-spacing: 0.18em; text-transform: uppercase; color: #a0a0a0;",

    # 7. Navigation links text size and spacing
    "  font-size: 0.62rem; font-weight: 500; letter-spacing: 0.22em; text-transform: uppercase;": "  font-size: 0.8rem; font-weight: 500; letter-spacing: 0.18em; text-transform: uppercase;",
    "font-size: 0.62rem; font-weight: 500; letter-spacing: 0.22em; text-transform: uppercase;": "font-size: 0.8rem; font-weight: 500; letter-spacing: 0.18em; text-transform: uppercase;",
    
    # 8. Dropdown items text size
    "  font-size: 0.7rem !important;": "  font-size: 0.82rem !important;",
    
    # 9. Subpage content margin-top
    "  margin-top: 70px;": "  margin-top: 90px;"
}

for filename in files:
    file_path = os.path.join(base_dir, filename)
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
        
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    original = content
    for target, replacement in replacements.items():
        content = content.replace(target, replacement)
        
    if content != original:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Successfully resized and updated header elements in {filename}!")
    else:
        print(f"No changes needed or matching targets not found in {filename}.")
