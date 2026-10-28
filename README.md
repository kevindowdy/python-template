# python-template
Template repository for Python applications.

## Getting started on Windows

1. Create a virtual env
```
python -m venv .venv
```
2. Activate virtual env
```
.venv\Scripts\Activate.ps1
```
3. Install dependencies (--user=false to prevent errors in a managed environment)
```
$env:PIP_USER="false"
pip install -r .\requirements.txt
```
