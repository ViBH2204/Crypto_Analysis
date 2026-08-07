import subprocess
import sys

scripts = [
    "scripts/fetch_historical.py",
    "scripts/fetch_live.py"
]

for script in scripts:
    print(f"\nRunning {script}...\n")

    result = subprocess.run([sys.executable, script])

    if result.returncode != 0:
        raise Exception(f"{script} failed")

print("\nDatabase updated successfully!")