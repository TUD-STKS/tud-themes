""" This test script starts a notebook server using the selected theme """
import tudthemes


if __name__ == '__main__':
    theme = 'dark'
    tudthemes.start_notebook(theme_select=theme, browser_en=True)
