import os
import sys
import sphinx_rtd_theme
sys.path.insert(0, os.path.abspath('./typing_app'))
sys.path.insert(0, os.path.abspath('./typing_app/util'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.githubpages',
]

autodoc_mock_imports = [
    'pygame',
]

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

autodoc_modules = [
    'typing_app.main',
    'typing_app.main_menu',
    'typing_app.ranking',
    'typing_app.ranking_list',
    'typing_app.ranking_menu',
    'typing_app.game_mode,'
    'typing_app.util.standard_input_reader',
    'typing_app.util.standard_csv_operator',
]
