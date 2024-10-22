# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath('../dcnodatg/'))
sys.path.insert(0, os.path.realpath(os.path.dirname(__file__)))
sys.path.insert(0, os.path.abspath('../external_sources/netbox/'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Netbox PtoV Plugin'
copyright = '2024, Mencken Davidson'
author = 'Mencken Davidson'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.napoleon',
    'myst_parser',
    'sphinx.ext.intersphinx',  # Link to other project's documentation (see mapping below)
    'sphinx.ext.viewcode',  # Add a link to the Python source code for classes, functions etc.
    'sphinx.ext.autodoc',
    'autoapi.extension',
    ]

source_suffix = [".rst",  ".md"]
templates_path = ['_templates']
exclude_patterns = ['_build', '_templates', 'Thumbs.db', '.DS_Store']
html_show_sourcelink = False  # Remove 'view source code' from top of page (for html, not python)
html_theme = 'sphinx_rtd_theme'
autoapi_template_dir = "_templates/autoapi"
autodoc_typehints = "description"
autoapi_own_page_level = "module"
autapi_ignore = []
autoapi_dirs = ['../netbox_ptov/', '../external_sources/netbox/']
autoapi_type = "python"
autoapi_options = [
    "members",
    "undoc-members",
    "show-inheritance",
    "show-module-summary",
    "imported-members",
]

html_css_files = [
    "css/custom.css",
]

on_rtd = os.environ.get("READTHEDOCS", None) == "True"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_static_path = ['_static']

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = True
napoleon_use_admonition_for_examples = True
napoleon_use_admonition_for_notes = True
napoleon_use_admonition_for_references = True
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True
napoleon_preprocess_types = False
napoleon_type_aliases = None
napoleon_attr_annotations = True

def contains(seq, item):
    return item in seq

def prepare_jinja_env(jinja_env) -> None:
    jinja_env.tests["contains"] = contains

autoapi_prepare_jinja_env = prepare_jinja_env


html_theme_options = {
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': -1,
    'includehidden': True,
    'titles_only': False
}