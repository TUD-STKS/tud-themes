import os
from pathlib import Path
from .get_address import get_address


def start_notebook(theme_select='bright',browser_en=True):
    pkg_root = Path(os.path.dirname(__file__))
    home_dir = os.path.expanduser('~')
    custom_style_dir = get_address(theme_select)
    os.environ["JUPYTER_CONFIG_DIR"] = custom_style_dir
    if browser_en:
        os.system('jupyter notebook --notebook-dir=' + home_dir)
    else:
        os.system('jupyter notebook --no-browser --notebook-dir=' + home_dir)