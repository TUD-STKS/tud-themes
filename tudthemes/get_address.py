import os
from pathlib import Path

current_themes = ["default", "bright", "dark"]

def get_address(theme=None):
    pkg_root = Path(os.path.dirname(__file__))
    theme_folder = Path("themes")
    # Prüfe, ob choose_theme korrekten Wert hat
    if theme is not None:
        assert (theme in current_themes), "the theme does not exist"
    else:
        theme = "default"
    return str(pkg_root / theme_folder / Path(theme))
    