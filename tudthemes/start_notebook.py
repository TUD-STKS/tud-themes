import os
import base64
from pathlib import Path

from .get_address import get_address


def create_common_stylesheet(common_path, output_path):
    '''
    The TU Dresden Logo gets converted into a css string 
    and saved in the respective custom folder
    '''
    with open(common_path / 'Logo_TU_Dresden.svg', 'rb') as svg:
        encoded_string = base64.b64encode(svg.read())
    stylesheet = '#ipython_notebook img{ display:block; background: url("data:image/svg+xml;base64,' \
                 f'{encoded_string.decode("utf-8")}");' '}'
    with open(output_path / 'common.css', 'w') as f:
        print(stylesheet, file=f)


def start_notebook(theme_select='bright',notebook_dir=None):
    '''
    Use this function to start jupyter notebook with one of the embedded themes
    '''
    pkg_root = Path(os.path.dirname(__file__))
    if not notebook_dir:
        notebook_dir = os.path.expanduser('~')

    custom_style_dir = get_address(theme_select)
    common_dir = pkg_root / 'themes' / 'common'
    create_common_stylesheet(common_dir,
                             custom_style_dir / 'custom')

    os.environ["JUPYTER_CONFIG_DIR"] = str(custom_style_dir)
    os.system('jupyter notebook --notebook-dir="' + notebook_dir + '"')
