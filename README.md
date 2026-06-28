# Epicidiom

A small Python starter project with one place for app code and one place for tests.

## Start Coding

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
python -m epicidiom
python -m unittest discover -s tests
```

## Project Layout

```text
src/epicidiom/    App code
tests/            Tests
```

Edit `src/epicidiom/__main__.py` to change what runs from the command line.
