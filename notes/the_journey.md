# The Journey

## Weeks 1-3

* Draft feasible timeline for project:
    * Make basic Snake work and make it platform agnostic.
    * Make Snake++.
    * Design experiment.
    * Evaluate both Snake apps (heuristic or student beta testers).
* Make and share repo with faculty mentor.
* Fixes to basic Snake (`hinojosa_snake`):
    * Commented out function in `game.py` to make Snake platform agnostic (runs on Windows, Linux,
    and now macOS too).
    * Set port for Snake from default 5000 to 5001 since the default port is sometimes busy on macOS.
* Explore basic Snake.
* Begin making Snake++...
    * Created skeleton of main pages.
    * Cleaned up CSS.
    * Cleaned up HTML indentation.
    * Fixed CSS/HTML bugs that came with those changes.
    * Added more error messages and fixed close button.
    * Added flow enforcement (currently commented out).
* Create `write_dependencies.py` script to generate `dependencies.txt`
* Rewrote git history to remove `model` that was accidentally cached.

## Weeks 4-6

* Continue making Snake++.
    * Misc HTML/CSS (spacing, alignment, font type, font size, etc.), bug fixes,
    and variable name consistency updates.
    * Made train button work by commenting out "@authenticated_only" in `events.py`
    (works with "@login_required" in `views.py`).
    * Replaced dropdowns with sliders.
    * Added `params.py` to store training input values as single source of truth.
    * Connected `alpha`, `gamma`, and `epsilon` to training process.
    * Fixed `write_dependencies.py` to include simple-websocket (missed b/c that is from runtime,
    not env).

* Submit registration to conferences.
