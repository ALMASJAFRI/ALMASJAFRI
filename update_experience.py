"""Updates the internship duration in README.md (start: April 2026)."""
import re
from datetime import date

START_YEAR, START_MONTH = 2026, 4  # Apr 2026
README = "README.md"

today = date.today()
months = max(1, (today.year - START_YEAR) * 12 + (today.month - START_MONTH))

# (pattern, replacement) - each targets one of the 4 places the duration appears
rules = [
    # Typing SVG line
    (r"\d+\+Months\+of\+Internship\+Experience",
     f"{months}+Months+of+Internship+Experience"),
    # Professional Summary
    (r"\*\*\d+ months of internship experience\*\*",
     f"**{months} months of internship experience**"),
    # Quick Facts table
    (r"\d+ months \(Apr 2026",
     f"{months} months (Apr 2026"),
    # Work Experience badge
    (r"\d+%20Months-22c55e",
     f"{months}%20Months-22c55e"),
]

with open(README, "r", encoding="utf-8") as f:
    text = f.read()

for pattern, repl in rules:
    text = re.sub(pattern, repl, text)

with open(README, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Experience set to {months} months")
