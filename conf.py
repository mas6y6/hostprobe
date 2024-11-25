# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
from hostprobe._version import __version__ as _v

project = 'hostprobe'
copyright = '2024, malachi196'
author = 'malachi196'
version = _v

# -- General configuration ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    'README.rst'
]
extensions = []
language = 'en'
master_doc = 'index'
pygments_style = 'sphinx'
source_suffix = '.rst'
templates_path = ['docs/_templates']

# -- Options for HTML output ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['docs/_static']