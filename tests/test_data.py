# Three and w/ mapping.
JSON_STRING_ONE = '{ "items": [ { "id": 1, "columnField": "timeoutCompleted", "operatorValue": "is", "value": true }, { "columnField": "MRN", "id": 28384, "operatorValue": "contains", "value": "ffre" }, { "columnField": "patientName", "operatorValue": "endsWith", "id": 41157, "value": "Bob" } ], "linkOperator": "and" }'

# Two filters with special operators. Or linker. No mapping.
JSON_STRING_TWO = '{ "items": [ { "columnField": "firstName", "operatorValue": "endsWith", "id": 79947, "value": "d" }, { "columnField": "indicationForDrug", "operatorValue": "isEmpty", "id": 44682 } ], "linkOperator": "or" }'

# Two filters. No linker.
JSON_STRING_THREE = '{ "items": [ { "id": 1, "columnField": "timeoutCompleted", "operatorValue": "is", "value": true }, { "columnField": "status", "id": 25556, "operatorValue": "contains", "value": "xds" } ] }'

# One filer w/ link.
JSON_STRING_FOUR = '{ "items": [ { "id": 1, "columnField": "timeoutCompleted", "operatorValue": "is", "value": true } ], "linkOperator": "or" }'

# Two filters. No Link. One incomplete.
JSON_STRING_FIVE = '{ "items": [ { "id": 1, "columnField": "timeoutCompleted", "operatorValue": "is", "value": true }, { "columnField": "status", "id": 3467, "operatorValue": "contains" } ] }'
