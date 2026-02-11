import os
from pathlib import Path
from typing import Literal


BrowserType = Literal['chrome', 'firefox']

BROWSER: BrowserType = os.getenv('BROWSER', 'chrome').lower()
HEADLESS: bool = os.getenv('HEADLESS', 'false').lower() == 'true'
SELENIUM_MODE: Literal['local', 'remote'] = os.getenv('SELENIUM_MODE', 'local').lower()

if BROWSER not in ('chrome', 'firefox'):
    raise ValueError(f'{BROWSER} браузер не поддерживается. Используйте chrome или firefox')

if SELENIUM_MODE not in ('local', 'remote'):
    raise ValueError(f'{SELENIUM_MODE} не поддерживается. Используйте local или remote')

PROJECT_ROOT = Path(__file__).parent
ASSETS_DIR = Path(os.getenv('ASSETS_DIR', PROJECT_ROOT/'assets'))
