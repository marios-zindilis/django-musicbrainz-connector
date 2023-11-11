project = 'Django MusicBrainz Connector'
copyright = '2023, Marios Zindilis'
author = 'Marios Zindilis'

extensions = [
    "sphinx.ext.autodoc",  # https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html
    "sphinx.ext.viewcode",  # https://www.sphinx-doc.org/en/master/usage/extensions/viewcode.html
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'alabaster'  # or maybe "classic"?
html_static_path = ['_static']

root_doc = "docs/index"
pygments_style = "sphinx"
