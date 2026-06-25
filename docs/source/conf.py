# Configuration file for the Sphinx documentation builder.

try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:
    import tomli as tomllib

from pathlib import Path

_pyproject = Path(__file__).resolve().parents[2] / 'pyproject.toml'
_version = tomllib.loads(_pyproject.read_text())['project']['version']

# -- Project information

project = 'DSUPDT Guide'
copyright = '2026, GDEX@NCAR, https://gdex.ucar.edu/'
author = 'Zaihua Ji'

release = _version
version = '.'.join(_version.split('.')[:2])

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'
