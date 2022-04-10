# filter-mui

This program converts MUI DataGrid filters into Django queries. 

# How to Use

Submit your MUI filters to your Django backend via a JSON String. Create a query set and then run the function add_mui_filters(query_set, json_string_filters, column_field_mappings). This will apply all of the MUI filters to the QuerySet and then return that updated QuerySet. By default all of the columnFields are convertdc from camelCase to snake_case. For example, the column medicalRecordNumber will be converted to medical_record_number. Say the field is called MRN on the frontend then it would convert to M_R_N, but this is not consistent with the database so you need to pass in {"MRN": "medical_record_number"} to the column_field_mappings. The column_field_mappings is also needed for traversing tables as seen below.

# Example

The following example allows the user to filter a MUI DataGrid displaying the following data of a patient model with the attributes medical_record_number (stored as MRN on front-end), first_name, last_name, date_of_birth, and place_of_birth (ForeignKey):

```python
from filtermui import add_mui_filters

# Made up function called when user submits new query.
def patient_table_query(filter)
  patients = patient.objects.all()
  
  patients = add_mui_filters(patients, filter, {"MRN": "medical_record_number", "placeOfBirth": "__place_of_birth__name"})
  
  return patients # This returns a QuerySet - you will often encode this into JSON. 
  
```

Note how in the mappings placeOfBirth is in camelCase. This is becuase it's submitted in cammel case and it is more efficent not to convert it if you are providing a mapping. It uses __ in place of birth becuase it is a diffrent table - we must specify when we traverse tables.

# Things still being worked on

- Performance updates
