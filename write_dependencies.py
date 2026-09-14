"""
Print pinned requirements for every third-party package this
repo imports.

Usage (from the repo root, with the project environment active):
    python write_deps.py > dependencies.txt

By Claude Code (Opus 5) on 9/13/2026
"""
import ast
import pathlib
from importlib.metadata import packages_distributions, version

# import name -> installed distribution(s), e.g. "flask_login"
# -> ["Flask-Login"]
dists = packages_distributions()

modules = set()
for path in pathlib.Path(".").rglob("*.py"):
    if any(part.startswith(".") for part in path.parts):
        continue
    for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
        if isinstance(node, ast.Import):
            modules |= {alias.name.split(".")[0] for alias in
node.names}
        elif isinstance(node, ast.ImportFrom) and node.level == 0 and node.module:
            modules.add(node.module.split(".")[0])

# Standard-library and local modules have no distribution, so
# they drop out here.
packages = {dist for module in modules for dist in
dists.get(module, [])}
for dist in sorted(packages, key=str.lower):
    print(f"{dist}=={version(dist)}")