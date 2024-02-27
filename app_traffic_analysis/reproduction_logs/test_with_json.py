import json


json_string = '{"type": "graph",\n"data": {\n  "directed": false,\n  "multigraph": false,\n  "graph": {},\n  "nodes": [\n    {\n      "ip_address": "10.55.223.209",\n      "color": "steelblue",\n      "size": 4,\n      "labels": ["type=VM"],\n      "id": "10.55.223.209"\n    },\n    {\n      "ip_address": "149.196.199.81",\n      "color": "#ff0000",  // Assuming highest byte weight\n      "size": 4,\n      "labels": ["type=VM"],\n      "id": "149.196.199.81"\n    },\n    {\n      "ip_address": "10.55.136.2",\n      "color": "steelblue",\n      "size": 4,\n      "labels": ["type=VM"],\n      "id": "10.55.136.2"\n    },\n    {\n      "ip_address": "10.55.204.47",\n      "color": "steelblue",\n      "size": 4,\n      "labels": ["type=VM"],\n      "id": "10.55.204.47"\n    },\n    {\n      "ip_address": "10.55.11.110",\n      "color": "steelblue",\n      "size": 4,\n      "labels": ["type=VM"],\n      "id": "10.55.11.110"\n    },\n    {\n      "ip_address": "10.55.111.179",\n      "color": "#ff4500",  // Assuming second highest byte weight\n      "size": 4,\n      "labels": ["type=VM"],\n      "id": "10.55.111.179"\n    },\n    {\n      "ip_address": "10.55.192.247",\n      "color": "steelblue",\n      "size": 4,\n      "labels": ["type=VM"],\n      "id": "10.55.192.247"\n    },\n    {\n      "ip_address": "10.55.25.2",\n      "color": "#ff6347",  // Assuming third highest byte weight\n      "size": 4,\n      "labels": ["type=VM"],\n      "id": "10.55.25.2"\n    },\n    {\n      "ip_address": "10.55.218.175",\n      "color": "steelblue",\n      "size": 4,\n      "labels": ["type=VM"],\n      "id": "10.55.218.175"\n    },\n    {\n      "ip_address": "10.55.227.88",\n      "color": "#ff4500",  // Assuming second highest byte weight\n      "size": 4,\n      "labels": ["type=VM"],\n      "id": "10.55.227.88"\n    }\n  ],\n  "links": [\n    {\n      "source_ip_address": "149.196.199.81",\n      "target_ip_address": "10.55.227.88",\n      "byte_weight": 1.0824926674973954,\n      "connection_weight": 0.5751799817272489,\n      "packet_weight": 0.8967376844051819,\n      "source": "149.196.199.81",\n      "target": "10.55.227.88"\n    },\n    {\n      "source_ip_address": "10.55.111.179",\n      "target_ip_address": "10.55.25.2",\n      "byte_weight": 1.6856020671703364,\n      "connection_weight": 0.13089314460287413,\n      "packet_weight": 0.6299688175490727,\n      "source": "10.55.111.179",\n      "target": "10.55.25.2"\n    },\n    {\n      "source_ip_address": "10.55.227.88",\n      "target_ip_address": "10.55.25.2",\n      "byte_weight": 0.46166850774476115,\n      "connection_weight": 0.21475819782321132,\n      "packet_weight": 1.0206248780754055,\n      "source": "10.55.25.2",\n      "target": "10.55.227.88"\n    }\n  ]\n}\n\'\'\'\nNote: The colors assigned to the nodes are hypothetical and represent a gradient from red (highest byte weight) to lighter shades (lower byte weights). The actual calculation of byte weights and corresponding colors would require processing the total byte weight for each node based on the edges connected to it and then mapping these weights to a color sc}'

# print(json_string)
if "//" in json_string:
    import re

    pattern = r"// .*?\n"
    json_string2 = re.sub(pattern, "\n", json_string)
    json_string = json_string2
    # print(json_string2)

try:
    ret = json.loads(json_string)
except Exception as e:
    str1 = json_string.split("'''")[0] + "}"
    str2 = json_string.split("'''")[1][:-1]
    # print(str1)
    ret = json.loads(str1)
    ret["text"] = str2


print(json.dumps(ret, indent=4))
print("Done!")
