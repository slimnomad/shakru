"""Vendor the upstream fonts and UI icons used by the approved design."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from subprocess import run

ROOT = Path(__file__).resolve().parents[1]
assets = {
    'assets/fonts/anton.ttf': 'https://raw.githubusercontent.com/google/fonts/main/ofl/anton/Anton-Regular.ttf',
    'assets/fonts/anton-OFL.txt': 'https://raw.githubusercontent.com/google/fonts/main/ofl/anton/OFL.txt',
    'assets/fonts/roboto.ttf': 'https://raw.githubusercontent.com/google/fonts/main/ofl/roboto/Roboto%5Bwdth,wght%5D.ttf',
    'assets/fonts/roboto-OFL.txt': 'https://raw.githubusercontent.com/google/fonts/main/ofl/roboto/OFL.txt',
    'assets/google.png': 'https://www.gstatic.com/images/branding/googleg/1x/googleg_standard_color_128dp.png',
    'assets/icons/LICENSE.txt': 'https://raw.githubusercontent.com/tabler/tabler-icons/main/LICENSE',
}
for name in ['moped', 'map-pin', 'arrow-right', 'x', 'search', 'minus', 'plus']:
    assets[f'assets/icons/{name}.svg'] = f'https://raw.githubusercontent.com/tabler/tabler-icons/main/icons/outline/{name}.svg'

def download(item):
    target, url = item
    path = ROOT / target
    path.parent.mkdir(parents=True, exist_ok=True)
    run(['curl', '-fsSL', '--max-time', '30', url, '-o', str(path)], check=True)
    return f'{target}: {path.stat().st_size} bytes'

with ThreadPoolExecutor(max_workers=5) as pool:
    for result in pool.map(download, assets.items()):
        print(result)
