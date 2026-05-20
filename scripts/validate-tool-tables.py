#!/usr/bin/env python3
"""
Tool Table Schema Validator
Enforces TOOL-TABLE-SCHEMA.md rules.
"""
import re
import sys
from pathlib import Path

def main():
    errors = []
    for md_file in Path('.').rglob('tools/**/*.md'):
        content = md_file.read_text(encoding='utf-8', errors='ignore')
        # Simple header check
        if '| Name | Vendor/Webpage | GitHub Repo | Brief Description | Tags | Latest Commit | Creation Date | Stars |' in content:
            # Count columns in rows
            rows = re.findall(r'\|\s*[^|]+\s*\|', content)
            for row in rows:
                if row.count('|') != 9:  # 8 columns + separators
                    errors.append(f"Invalid row in {md_file}")
    if errors:
        print('\n'.join(errors))
        sys.exit(1)
    print('✅ Tool tables validated.')
    sys.exit(0)

if __name__ == "__main__":
    main()