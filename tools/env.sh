#!/bin/bash
python3 -m venv redteam_env
source redteam_env/bin/activate
pip install langchain ollama jinja2 pdfkit requests matplotlib
