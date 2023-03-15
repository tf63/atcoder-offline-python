# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "atcoder_offline"
copyright = "2023, fuku63"
author = "fuku63"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.autodoc", "sphinx.ext.napoleon", "sphinx_rtd_theme"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "ja"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = [".rst", ".md"]
# source_suffix = '.rst'

from recommonmark.parser import CommonMarkParser

source_parsers = {
    ".md": CommonMarkParser,
}

source_suffix = [".rst", ".md"]

# TODO:2020-08-15 この部分はsphinx-quickstartで生成されたコードから変更しています。
# チュートリアル全体でpathlibを扱っているのでpathlibでパスを生成しています。
from pathlib import Path
import sys

sys.path.insert(0, str(Path("../tests/")))
