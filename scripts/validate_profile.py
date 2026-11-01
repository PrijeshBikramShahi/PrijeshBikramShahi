#!/usr/bin/env python3
"""Dependency-free local checks for the profile's links and active SVG assets."""
from html.parser import HTMLParser
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
readme = (ROOT / 'README.md').read_text()
errors = []
references = re.findall(r'\]\(([^\s)]+)\)', readme)


class Images(HTMLParser):
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ('src', 'srcset', 'href'):
            if key in attrs:
                references.append(attrs[key])
        if tag == 'img' and not attrs.get('alt', '').strip():
            errors.append('HTML image needs meaningful alt text')


Images().feed(readme)
if re.search(r'!\[\s*\]', readme):
    errors.append('Markdown image needs meaningful alt text')
if re.search(r'<table\b', readme, re.I):
    errors.append('Avoid fixed table layouts for the profile')

active = set()
for reference in references:
    if reference.startswith(('https://', 'mailto:', '#')):
        continue
    path = (ROOT / reference.split('#')[0]).resolve()
    if not path.is_relative_to(ROOT) or not path.is_file():
        errors.append(f'Missing or out-of-repository asset: {reference}')
    elif path.suffix == '.svg':
        active.add(path)

ns = {'svg': 'http://www.w3.org/2000/svg'}
for path in sorted(active):
    try:
        root = ET.parse(path).getroot()
        if not root.get('viewBox'):
            errors.append(f'{path.name}: missing viewBox')
        for tag in ('title', 'desc'):
            if root.find(f'svg:{tag}', ns) is None:
                errors.append(f'{path.name}: missing {tag}')
        for element in root.iter():
            if element.tag.rsplit('}', 1)[-1] in ('script', 'foreignObject', 'animate'):
                errors.append(f'{path.name}: active or unsupported SVG content')
            for key, value in element.attrib.items():
                if key.startswith('on') or ('href' in key and not value.startswith('#')):
                    errors.append(f'{path.name}: external or executable SVG attribute')
    except ET.ParseError as exc:
        errors.append(f'{path.name}: {exc}')

if errors:
    print('\n'.join(errors), file=sys.stderr)
    sys.exit(1)
print(f'Validated README references and {len(active)} active SVGs. External links require a separate online review.')
