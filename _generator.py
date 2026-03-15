#!/usr/bin/env python3
"""
Auto-generate addons.xml dan addons.xml.md5 untuk Kodi repository
"""

import os
import hashlib
import xml.etree.ElementTree as ET
from pathlib import Path

def generate_addons_xml():
    """Generate addons.xml dan addons.xml.md5"""
    
    print("=" * 60)
    print("  Kodi Repository - Addons.xml Generator")
    print("=" * 60)
    print("\n🚀 Starting addons.xml generation...\n")
    
    # Root element
    addons_xml = ET.Element('addons')
    addons_found = 0
    
    # Scan folder zips
    zips_path = Path('zips')
    
    if not zips_path.exists():
        print("❌ Error: Folder 'zips' tidak ditemukan!")
        print("   Pastikan menjalankan script dari root folder repository")
        return False
    
    # Scan setiap subfolder di zips
    for addon_folder in sorted(zips_path.iterdir()):
        if not addon_folder.is_dir():
            continue
        
        # Skip hidden folders
        if addon_folder.name.startswith('.'):
            continue
        
        # Skip files yang bukan folder
        addon_xml_path = addon_folder / 'addon.xml'
        
        if addon_xml_path.exists():
            try:
                print(f"📦 Found addon: {addon_folder.name}")
                tree = ET.parse(addon_xml_path)
                addon = tree.getroot()
                
                # Dapatkan info addon
                addon_id = addon.get('id')
                addon_version = addon.get('version')
                addon_name = addon.get('name')
                
                print(f"   ID: {addon_id}")
                print(f"   Name: {addon_name}")
                print(f"   Version: {addon_version}")
                
                addons_xml.append(addon)
                addons_found += 1
                
            except ET.ParseError as e:
                print(f"⚠️  Warning: Error parsing {addon_xml_path}")
                print(f"   Error: {e}")
                continue
            except Exception as e:
                print(f"⚠️  Warning: Unexpected error with {addon_xml_path}")
                print(f"   Error: {e}")
                continue
    
    if addons_found == 0:
        print("\n❌ Error: Tidak ada addon ditemukan di folder zips/")
        print("   Pastikan struktur folder benar:")
        print("   zips/")
        print("   ├── repository.dns.kodi/")
        print("   │   └── addon.xml")
        print("   └── script.dns.google.auto/")
        print("       └── addon.xml")
        return False
    
    # Save addons.xml dengan formatting
    tree = ET.ElementTree(addons_xml)
    ET.indent(tree, space="    ")
    
    addons_xml_path = zips_path / 'addons.xml'
    tree.write(addons_xml_path, encoding='UTF-8', xml_declaration=True)
    
    print(f"\n✅ addons.xml generated successfully!")
    print(f"   Location: {addons_xml_path}")
    print(f"   Total addons: {addons_found}")
    
    # Generate MD5 checksum
    with open(addons_xml_path, 'rb') as f:
        content = f.read()
        md5 = hashlib.md5(content).hexdigest()
    
    md5_path = zips_path / 'addons.xml.md5'
    with open(md5_path, 'w') as f:
        f.write(md5)
    
    print(f"\n✅ MD5 checksum generated!")
    print(f"   Checksum: {md5}")
    print(f"   Location: {md5_path}")
    
    return True

def main():
    """Main function"""
    success = generate_addons_xml()
    
    print("\n" + "=" * 60)
    if success:
        print("✅ Generation completed successfully!")
        print("\nFiles generated:")
        print("  - zips/addons.xml")
        print("  - zips/addons.xml.md5")
    else:
        print("❌ Generation failed!")
        print("\nPlease check errors above and try again.")
        exit(1)
    print("=" * 60 + "\n")

if __name__ == "__main__":
    main()
