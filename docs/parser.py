import xmlschema
import json
import sys

# Replace 'your_schema.xsd' with your actual XSD file path
xsd_file = 'schemas/KodyKrajow_v13-0E.xsd'

with open("schemas/kraje_schema.json", 'w') as fh:
    json.dump(xmlschema.to_dict(xsd_file), fh, indent=4, ensure_ascii=False)
