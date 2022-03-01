""" This test script starts a notebook server using the selected theme """
import tudthemes

if __name__ == '__main__':
    theme = 'dark'
    working_dir = None
    tudthemes.start_notebook(theme_select=theme, notebook_dir=working_dir)
