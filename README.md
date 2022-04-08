# filter-mui
NOTE: THIS IS STILL A WORK IN PROGRESS I HAVE NOT FINISHED A WORKING VERSION

This program converts MUI DataGrid filters into Django queries. 

# How to Use

Submit the MUI filter model over the API via a JSON string. Input a query and that JSON into the add_mui_filters() function to return a new QuerySet with the MUI filters applied to the orignal QuerySet. Often times columnFields do not convert directly to a a valid QuerySet.filter() argument which may happen when you traverse models in the MUI DataGrid or use a diffrent naming convention on the frontend. You may provide add_mui_filters() function with the column_field_mappings arguemnt which allows you to create a dict mapping MUI columnFields to filter inputs. 

If you are querying for timeouts (ex. orginal QS is timeout.objects.all() or similar) and you have the columnField timeoutId you need to provide the mapping {"timeoutId": "pk"}. If no mapping is provided for a columnField then the string will be converted from camelCase to snake_case. Please note if you are not using camelCase in the frontend or snake_case in the backend you will have to specify a mapping unless they maigcally lign up.

# Things still being worked on

- I have not finished the integration or unit tests yet.
- The program "and chains" all filters. I'm working on reading the linkOperator. 
