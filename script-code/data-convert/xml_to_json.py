import json
import xmltodict
import xml.etree.ElementTree as ET


with open("annotations.xml") as xml_file:
    data_dict = xmltodict.parse(xml_file.read())
    # xml_file.close()

json_data = json.dumps(data_dict)

with open("data.json", "w") as json_file:
    json_file.write(json_data)
    # json_file.close()


tree = ET.parse('annotations.xml')
root = tree.getroot()
d = {}
for child in root:
    if child.tag not in d:
        d[child.tag] = []
    dic = {}
    for child2 in child:
        if child2.tag not in dic:
            dic[child2.tag] = child2.text
    d[child.tag].append(dic)
print(d)
