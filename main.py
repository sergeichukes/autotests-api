import xml.etree.ElementTree as ET
from pathlib import Path
import json

p = Path(r'C:\Users\serge\Documents\projects\autotests-api\new_json.json').resolve()
print(p)
data = json.loads(Path('new_json.json').read_text())

print(data)
