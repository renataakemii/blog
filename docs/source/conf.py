# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = "Chega pra conversar"
copyright = "2024, Renata Imai"
author = "Renata Imai"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.githubpages",
    "sphinx.ext.intersphinx",
    "sphinxemoji.sphinxemoji",
    "ablog",
    "sphinx_gallery.gen_gallery",
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

source_suffix = [".rst"]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "pydata_sphinx_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = ["custom.css"]

html_theme_options = {
    "navbar_center": ["navbar-nav"],
    "show_nav_level": 0,
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "navbar_start": ["navbar-logo"],
    "navbar_align": "left",
    # "announcement": "Confira nossa <a href='https://renataakemii.github.io/posts/2024-03-12-um-breve-desabafo.html'>última publicação!</a>",
    "secondary_sidebar_items": ["page-toc"],
    "pygment_dark_style": "monokai",
    "pygment_light_style": "default",
}

# html_sidebars = {
#     "build/html/": [
#         "posts/postcard.html",
#         "posts/recentposts.html",
#         "posts/tagcloud.html",
#         "posts/archives.html",
#     ],
# }

# The name for this set of Sphinx documents.
html_title = "Chega pra conversar"

# -- Ablog options -----------------------------------------------------------

# blog_title = "Chega pra conversar"
# blog_path = "posts"
# blog_baseurl = "https://renataakemii.github.io"
# blog_feed_fulltext = True
# blog_feed_archives = True
# fontawesome_included = True
# post_redirect_refresh = 1

# -- sphinx-gallery options --------------------------------------------------

sphinx_gallery_conf = {
     'examples_dirs': 'developing',   # path to your example scripts
     'gallery_dirs': 'auto_examples',  # path to where to save gallery generated output
}
