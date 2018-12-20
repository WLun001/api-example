import json
import xmltodict
from flask import Flask, request

app = Flask(__name__)

# with open("sample.xml", 'r') as f:
#     xmlString = f.read()

# print("XML input (sample.xml):")
# print(xmlString)

# jsonString = json.dumps(xmltodict.parse(xmlString), indent=4)

# print("\nJSON output(output.json):")
# print(jsonString)

# with open("output.json", 'w') as f:
#     f.write(jsonString)


@app.route('/json-to-xml', methods=['POST'])
def xml_converter():
    data = request.data
    print(data)
    return json.dumps(xmltodict.parse(data), indent=4)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
