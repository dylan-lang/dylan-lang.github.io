# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'dylan-lang.github.io'
copyright = '2024, Dylan Hackers'
author = 'Dylan Hackers'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'

html_static_path = ['_static']

# Configure logo
html_theme_options = {
    "sidebar_hide_name": True,
    "light-logo": "images/opendylan-light.png",
    "dark-logo": "images/opendylan-dark.png",
}

# Ignore certification verification
tls_verify = False
