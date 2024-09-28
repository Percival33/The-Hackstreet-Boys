import xmlschema
import json
import sys

# Replace 'your_schema.xsd' with your actual XSD file path
xsd_file = 'schema.xsd'

with open("schema.json", 'w') as fh:
    json.dump(xmlschema.to_dict(xsd_file), fh, indent=4, ensure_ascii=False)
