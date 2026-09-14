# Helpful Terminal Commands

## Updating "dependencies.txt"

```
python write_dependencies.txt > dependencies.txt
```

# Removing Flow Enforcement

```
sed -i '' -E 's/^# (@login_required|@flow\.step)/\1/' snake_plus_plus/website/views.py
```

## Using djLint

```
# What is it?
# Auto-formatter for jinja html

# Install it
pip install djlint

# Preview auto-formatting changes
djlint snake_plus_plus/website/templates --check --profile=jinja

# Apply auto-formatting changes
djlint snake_plus_plus/website/templates/ --reformat --profile=jinja
```


