# Helpful Terminal Commands

## Updating "dependencies.txt"

```
python write_dependencies.txt > dependencies.txt
```

# Removing Temporary DEV Comments

Remove the DEV comments, flow enforcement, and authentication enforcement
to fully launch the project.

```
sed -i '' -E \
    -e 's/^# (@login_required|@flow\.step|@authenticated_only)/\1/' \
    -e '/^# DEV:/,/^$/d' \
    snake-plus-plus/website/views.py snake-plus-plus/website/events.py
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


