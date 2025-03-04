import re
from pathlib import Path

file_path = Path("c:/Study/pp2/lab_5/raw.txt")
with file_path.open("r", encoding="utf-8") as f:
    text = f.read()

def to_snake(s):
    return '_'.join(s.split()).lower()

pattern = r'\b(?:[A-Z][a-z]+|[A-Z]{2,})(?:\s+(?:[A-Z][a-z]+|[A-Z]{2,}))*\b'

matches = re.findall(pattern, text)

snake_names = [to_snake(match) for match in matches]

filtered = [name for name in snake_names]

unique_filtered = []
seen = set()
for name in filtered:
    if name not in seen:
        unique_filtered.append(name)
        seen.add(name)

print(unique_filtered)