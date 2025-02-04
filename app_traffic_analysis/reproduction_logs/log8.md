## Issue: 1st in hard ones: JSON parsing issue


**Fix**: Try to modify JSON string parsing code. Nest another `try...excpt` blcok in `test_with_golden.py`:
    
```python
try:
    json_obj = json.loads(json_string)
except Exception as e:
    try:
        str1 = json_string.split("'''")[0] + "}"
        str2 = json_string.split("'''")[1][:-1]
        json_obj = json.loads(str1)
        json_obj["text"] = str2
    except Exception as e2:
        import re

        pattern = r"// .*?\""
        cleaned_text = re.sub(pattern, '"', json_string)
        json_obj = json.loads(cleaned_text)
```

**Faulty JSON string**:

```JSON
{"type": "graph","data": {  "directed": false,  "multigraph": false,  "graph": {},  "nodes": [    {      "ip_address": "10.55.223.209",      "color": "steelblue",      "size": 4,      "labels": ["type=VM"],      "id": "10.55.223.209"    },    {      "ip_address": "149.196.199.81",      "color": "#ff0000", // Assuming highest byte weight      "size": 4,      "labels": ["type=VM"],      "id": "149.196.199.81"    },    {      "ip_address": "10.55.136.2",      "color": "steelblue",      "size": 4,      "labels": ["type=VM"],      "id": "10.55.136.2"    },    {      "ip_address": "10.55.204.47",      "color": "steelblue",      "size": 4,      "labels": ["type=VM"],      "id": "10.55.204.47"    },    {      "ip_address": "10.55.11.110",      "color": "steelblue",      "size": 4,      "labels": ["type=VM"],      "id": "10.55.11.110"    },    {      "ip_address": "10.55.111.179",      "color": "#ff4500", // Second highest byte weight      "size": 4,      "labels": ["type=VM"],      "id": "10.55.111.179"    },    {      "ip_address": "10.55.192.247",      "color": "steelblue",      "size": 4,      "labels": ["type=VM"],      "id": "10.55.192.247"    },    {      "ip_address": "10.55.25.2",      "color": "#ff6347", // Third highest byte weight      "size": 4,      "labels": ["type=VM"],      "id": "10.55.25.2"    },    {      "ip_address": "10.55.218.175",      "color": "steelblue",      "size": 4,      "labels": ["type=VM"],      "id": "10.55.218.175"    },    {      "ip_address": "10.55.227.88",      "color": "#ff4500", // Second highest byte weight      "size": 4,      "labels": ["type=VM"],      "id": "10.55.227.88"    }  ],  "links": [    {      "source_ip_address": "149.196.199.81",      "target_ip_address": "10.55.227.88",      "byte_weight": 1.0824926674973954,      "connection_weight": 0.5751799817272489,      "packet_weight": 0.8967376844051819,      "source": "149.196.199.81",      "target": "10.55.227.88"    },    {      "source_ip_address": "10.55.111.179",      "target_ip_address": "10.55.25.2",      "byte_weight": 1.6856020671703364,      "connection_weight": 0.13089314460287413,      "packet_weight": 0.6299688175490727,      "source": "10.55.111.179",      "target": "10.55.25.2"    },    {      "source_ip_address": "10.55.227.88",      "target_ip_address": "10.55.25.2",      "byte_weight": 0.46166850774476115,      "connection_weight": 0.21475819782321132,      "packet_weight": 1.0206248780754055,      "source": "10.55.25.2",      "target": "10.55.227.88"    }  ]}}
```