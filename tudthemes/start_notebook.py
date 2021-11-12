import os
from pathlib import Path
from .get_address import get_address

import base64


def create_common_stylesheet(common_path, output_path):
    with open(common_path / 'Logo_TU_Dresden.svg', 'rb') as svg:
        encoded_string = base64.b64encode(svg.read())
    stylesheet = '#ipython_notebook img{ display:block; background: url("data:image/svg+xml;base64,' \
                 f'{encoded_string.decode("utf-8")}");' '}'
    with open(output_path / 'common.css', 'w') as f:
        print(stylesheet, file=f)


def start_notebook(theme_select='bright',browser_en=True):
    pkg_root = Path(os.path.dirname(__file__))
    home_dir = os.path.expanduser('~')
    custom_style_dir = get_address(theme_select)
    create_common_stylesheet(pkg_root / 'themes' / 'common',
                             Path(custom_style_dir) / 'custom')
    os.environ["JUPYTER_CONFIG_DIR"] = custom_style_dir
    if browser_en:
        os.system('jupyter notebook --notebook-dir="' + home_dir + '"')
    else:
        os.system('jupyter notebook --no-browser --notebook-dir=' + home_dir)
