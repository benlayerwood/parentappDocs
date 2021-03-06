# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'ElternApp'
copyright = '2022, Benjamin Schichtholz'
author = 'Benjamin Schichtholz'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'alabaster'
#
html_logo = 'images/elternapp_logo_200.png'

html_theme_options = {
    'font_family': 'sans-serif',
    'body_text': '#292929',
    'head_font_family': 'helvetica',
    'relbar_border': '#292929',
    'footnote_border': '#292929',
}

# -- Options for EPUB output
epub_show_urls = 'footnote'
