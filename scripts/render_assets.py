#!/usr/bin/env python3
"""Generate active static SVGs. Copy, evidence and links live in README.md."""
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STYLE = '''
    .panel { fill: #141d25; stroke: #3b4b58; }
    .rule { stroke: #3b4b58; }
    .text { fill: #edf3f4; }
    .muted { fill: #b2c0ca; }
    .accent { fill: #8dceae; }
    text { font-family: Arial, Helvetica, sans-serif; }
    .mono { font-family: Menlo, Consolas, monospace; }
    @media (prefers-color-scheme: light) {
      .panel { fill: #f6f8fa; stroke: #c5cdd5; }
      .rule { stroke: #c5cdd5; }
      .text { fill: #1f2933; }
      .muted { fill: #4b5c69; }
      .accent { fill: #286448; }
    }
'''


def text(x, y, value, size, css='text', weight=400):
    return f'<text x="{x}" y="{y}" class="{css}" font-size="{size}" font-weight="{weight}">{escape(value)}</text>'


def svg(width, height, title, description, body):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">{escape(title)}</title>
  <desc id="desc">{escape(description)}</desc>
  <style>{STYLE}  </style>
  <rect x="1" y="1" width="{width-2}" height="{height-2}" rx="16" class="panel"/>
  {body}
</svg>
'''


def hero(mobile=False):
    w, h = (420, 280) if mobile else (840, 286)
    x = 24 if mobile else 36
    body = text(x, 34, '~/prijesh · zsh', 15, 'muted mono')
    body += f'<path d="M{x} 52 H{w-x}" class="rule"/>'
    body += text(x, 88, '$ whoami', 16, 'accent mono')
    body += text(x-2, 156, 'prijesh', 66, weight=700)
    body += text(x+218, 156, '.', 66, 'accent', 700)
    body += text(x, 193, 'INDEPENDENT SOFTWARE DEVELOPER', 15 if mobile else 20, 'muted', 600)
    if mobile:
        body += text(x, 230, 'Building products across', 21)
        body += text(x, 258, 'mobile, web, and desktop.', 21)
    else:
        body += text(x, 239, 'Building products across mobile, web, and desktop.', 25)
    return svg(w, h, 'prijesh. Independent software developer',
               'Building products across mobile, web, and desktop.', body)


def main():
    assets = ROOT / 'assets'
    (assets / '01-hero.svg').write_text(hero())
    (assets / '01-hero-mobile.svg').write_text(hero(True))
    for name, category in [
        ('stow', 'DESKTOP / GIT WORKFLOWS'),
        ('topside', 'NATIVE macOS / SYSTEM INTEGRATION'),
        ('khoj', 'MOBILE / MAPS AND ROUTING'),
        ('loomrail', 'WEB / AGENT WORKFLOWS'),
    ]:
        body = text(25, 49, name + '.', 35, weight=700)
        body += text(26, 81, category, 13, 'accent mono')
        (assets / f'featured-{name}.svg').write_text(
            svg(420, 106, name.title(), category, body))


if __name__ == '__main__':
    main()
