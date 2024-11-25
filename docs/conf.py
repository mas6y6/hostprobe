# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import importlib.util
from pathlib import Path

version_path = Path(__file__).resolve().parent.parent / "hostprobe/_version.py"
spec = importlib.util.spec_from_file_location("versionfile", str(version_path))
versionfile = importlib.util.module_from_spec(spec)
spec.loader.exec_module(versionfile)


project = 'hostprobe'
copyright = '2024, malachi196'
author = 'malachi196'

version = versionfile.__version__

# -- General configuration ------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

exclude_patterns = [
    '_build',
    'Thumbs.db',
    '.DS_Store',
    'README.rst',
]
extensions = []
language = 'en'
master_doc = 'index'
pygments_style = 'sphinx'
source_suffix = '.rst'
templates_path = ['_templates']

# -- Options for HTML output ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']