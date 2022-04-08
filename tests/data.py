# One filter. timeoutId needs to map to id. 
json_string_one = '{ "items": [ { "id": 1, "columnField": "timeoutId", "operatorValue": "contains", "value": "de" } ] }'

# Two filters with special operators. Or linker.
json_string_two = '{ "items": [ { "columnField": "firstName", "operatorValue": "endsWith", "id": 79947, "value": "d" }, { "columnField": "indicationForDrug", "operatorValue": "isEmpty", "id": 44682 } ], "linkOperator": "or" }'

# Two filters. No linker. 
json_string_three = '{ "items": [ { "id": 1, "columnField": "timeoutCompleted", "operatorValue": "is", "value": true }, { "columnField": "room", "id": 72321, "operatorValue": "contains" } ] }'

# One filer w/ link.
