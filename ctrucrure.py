import os

dirs = [
    "app",
    "core",
    "tests",
    "data"
]
files = {
    "app": ["main.py"],
    "core": [
        "domain.py","transforms.py","recursion.py","memo.py",
        "ftypes.py","lazy.py","frp.py","compose.py","service.py","report.py"
    ],
    "tests": ["test_lab1.py"],
    "data": ["seed.json"],
    "": ["requirements.txt","README.md","pyproject.toml","ruff.toml"]
}

for d in dirs:
    os.makedirs(d, exist_ok=True)
for folder, flist in files.items():
    for f in flist:
        open(os.path.join(folder, f) if folder else f, "w").close()
