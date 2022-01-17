import os
from pathlib import Path


def get_address(theme=None):
    '''
    List all integrated themes and check if requested theme exists.
    If True or None the path to the custom folder is returned.
    '''
    pkg_root = Path(os.path.dirname(__file__))
    theme_folder = Path("themes")
    current_themes = [filename for filename in os.listdir(pkg_root / theme_folder) 
                    if os.path.isdir(os.path.join(pkg_root / theme_folder,filename))] 
    if "common" in current_themes:
        current_themes.remove("common")

    # check if choose_theme exists
    if theme is not None:
        assert (theme in current_themes), "The theme does not exist."
    else:
        theme = "default"
    return pkg_root / theme_folder / Path(theme)
