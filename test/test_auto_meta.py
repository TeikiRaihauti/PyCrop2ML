import json
import xml.etree.ElementTree as ET

from pycropml.modelunit import ModelUnit
from pycropml.inout import Input, Output


def test1():
    with open('test\data\SQ.json', 'r') as f:
        sc = json.load(f)

    component = sc
    return json_to_xml(component)


def json2cml(unit):
    """
    Convert a JSON object to a ModelUnit instance.
    """
    # TODO : Look at the constructor of a Model
    model_unit = ModelUnit(unit)

    metadata = unit.get('metadata', {})
    model_unit.name = metadata.get('Title', '')
    model_unit.authors = metadata.get('Authors', '')
    model_unit.institution = metadata.get('Institution', '')
    model_unit.uri = metadata.get('URI', '')
    model_unit.doi = metadata.get('DOI', '')
    model_unit.extended_description = metadata.get('Extended description', '')
    model_unit.short_description = metadata.get('Short description', '')
     
    description=unit.get('description', '')
    model_unit.add_description(description)

    process = unit.get('process', None)


    inputs=[Input(input) for input in process.get('inputs', [])]
    model_unit.inputs = inputs
    outputs=[Output(output) for output in process.get('outputs', [])]
    model_unit.outputs = outputs
    functions = [function for function in process.get('functions', [])]
    model_unit.function = functions
    initialization = process.get('init', "")
    model_unit.initialization = initialization

    return model_unit


def dict_to_xml(element, data):
    if isinstance(data, dict):
        for k, v in data.items():
            sub_elem = ET.SubElement(element, k)
            dict_to_xml(sub_elem, v)
    elif isinstance(data, list):
        # Use singular tag name for each element in a list
        parent_tag = element.tag
        element.clear()  # Remove the parent placeholder element
        for item in data:
            sub_elem = ET.SubElement(element, parent_tag[:-1] if parent_tag.endswith('s') else 'item')
            dict_to_xml(sub_elem, item)
    else:
        element.text = str(data)

def json_to_xml(json_obj):
    root = ET.Element("")
    dict_to_xml(root, json_obj)
    return ET.tostring(root, encoding="unicode")


test1_result = test1()
with open("test\data\SQ.xml", "w", encoding="utf-8") as f:
    f.write(test1_result)