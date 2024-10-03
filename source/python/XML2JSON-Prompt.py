# Crete a python function which converts an XML file to a JSON file
# parameter should be input file and output file.
# make sure that the input file has a valid XML format
# provide a proper error message if the input file is not a valid XML
# the file should be writen to local disk
# the function should be able to handle large files 

import xml.etree.ElementTree as ET
import json
from collections import defaultdict
def xml_to_json(input_file, output_file):
    try:
        tree = ET.parse(input_file)
    except ET.ParseError:
        print(f"Error: {input_file} is not a well-formed XML document.")
        return
    root = tree.getroot()
    result_dict = etree_to_dict(root)
    try:
        with open(output_file, 'w') as f:
            json.dump(result_dict, f, indent=4)
    except IOError:
        print(f"Error: Unable to write to {output_file}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    
def etree_to_dict(t: ET.Element) -> dict:
    d = {t.tag: {"@" + k: v for k, v in t.attrib.items()}}
    children = list(t)
    if children:
        dd = defaultdict(list)
        for dc in map(etree_to_dict, children):
            for k, v in dc.items():
                dd[k].append(v)
        for k, v in dd.items():
            if len(v) == 1:
                d[t.tag][k] = v[0]
            else:
                d[t.tag][k] = v
    if t.text:
        text = t.text.strip()
        if children or t.attrib:
            if text:
                d[t.tag]['#text'] = text
        else:
            d[t.tag] = text
    return d

if __name__ == "__main__":
    # Create a sample XML document
    xml_data = """<?xml version="1.0"?>
<feedback xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <version>1.0</version>
  <report_metadata>
    <org_name>Enterprise Copilot</org_name>
    <email>copilot@openai.com</email>
    <report_id>e0381c24b5234bed3hdl0hk2b5c944d0b6</report_id>
    <date_range>
      <begin>1711238400</begin>
      <end>1711324800</end>
    </date_range>
  </report_metadata>
  <policy_published>
    <domain>openai.com</domain>
    <adkim>s</adkim>
    <aspf>r</aspf>
    <p>none</p>
    <sp>none</sp>
    <pct>100</pct>
    <fo>0</fo>
  </policy_published>
</feedback>"""

    # Write the XML data to a file
    with open('.\\source\\python\\input.xml', 'w') as f:
        f.write(xml_data)

    # Call the function to convert the XML to JSON
    xml_to_json('.\\source\\python\\input.xml', '.\\source\\python\\output.json')