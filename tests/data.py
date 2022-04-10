# Three and w/ mapping.
json_string_one = '{ "items": [ { "id": 1, "columnField": "timeoutCompleted", "operatorValue": "is", "value": true }, { "columnField": "MRN", "id": 28384, "operatorValue": "contains", "value": "ffre" }, { "columnField": "patientName", "operatorValue": "endsWith", "id": 41157, "value": "Bob" } ], "linkOperator": "and" }'

# Two filters with special operators. Or linker. No mapping.
json_string_two = '{ "items": [ { "columnField": "firstName", "operatorValue": "endsWith", "id": 79947, "value": "d" }, { "columnField": "indicationForDrug", "operatorValue": "isEmpty", "id": 44682 } ], "linkOperator": "or" }'

# Two filters. No linker.
json_string_three = '{ "items": [ { "id": 1, "columnField": "timeoutCompleted", "operatorValue": "is", "value": true }, { "columnField": "status", "id": 25556, "operatorValue": "contains", "value": "xds" } ] }'

# One filer w/ link.
json_string_four = '{ "items": [ { "id": 1, "columnField": "timeoutCompleted", "operatorValue": "is", "value": true } ], "linkOperator": "or" }'

# Two filters. No Link. One incomplete.
json_string_five = '{ "items": [ { "id": 1, "columnField": "timeoutCompleted", "operatorValue": "is", "value": true }, { "columnField": "status", "id": 3467, "operatorValue": "contains" } ] }'
