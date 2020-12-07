# Standard library imports
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

GITHUB_PROFILE = ""
GITHUB_PROJECT = ""
PROJECT_NAME = "Project"
PROJECT_AUTHOR = ""

project = PROJECT_NAME
copyright = f"20120, {PROJECT_AUTHOR}"
author = PROJECT_AUTHOR


extensions = ["sphinx.ext.autodoc", "sphinx.ext.viewcode", "sphinx_issues"]
issues_github_path = f"{GITHUB_PROFILE}/{GITHUB_PROJECT}"
templates_path = ["_templates"]

language = "pt_BR"
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
html_theme = "alabaster"

html_static_path = ["_static"]

locale_dirs = ["locale/"]
gettext_compact = False
