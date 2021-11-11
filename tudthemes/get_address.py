import os
from pathlib import Path


def get_address(theme=None):
    pkg_root = Path(os.path.dirname(__file__))
    theme_folder = Path("themes")
    current_themes = [filename for filename in os.listdir(pkg_root / theme_folder) 
                    if os.path.isdir(os.path.join(pkg_root / theme_folder,filename))] 
    if "common" in current_themes:
        current_themes.remove("common")

    # Prüfe, ob choose_theme korrekten Wert hat
    if theme is not None:
        assert (theme in current_themes), "the theme does not exist"
    else:
        theme = "default"
    return str(pkg_root / theme_folder / Path(theme))
    