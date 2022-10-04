# filter-mui

This program converts MUI DataGrid filters into Django queries. It is integrated with Django Channels.

# How to Use

Submit your MUI filters to your Django backend via a JSON String. Create a query set and then run the function add_mui_filters(query_set, json_string_filters, column_field_mappings). This will apply all of the MUI filters to the QuerySet and then return that updated QuerySet. By default all of the columnFields are convertdc from camelCase to snake_case. For example, the column medicalRecordNumber will be converted to medical_record_number. Say the field is called MRN on the frontend then it would convert to M_R_N, but this is not consistent with the database so you need to pass in {"MRN": "medical_record_number"} to the column_field_mappings. The column_field_mappings is also needed for traversing tables as seen below.

# Installation

Run the following:
Please note that the PIP installation does not currently work. I'm working on correcting this error. Please install the source code.

```python
pip install filtermui
```

# Example

The following example allows the user to filter a MUI DataGrid displaying the following data of a patient model with the attributes medical_record_number (stored as "MRN" on front-end), first_name, last_name, date_of_birth, and place_of_birth (ForeignKey):

```python
from filtermui import add_mui_filters

# Made up function called when user submits new query.
def patient_table_query(filter):
  patients = patient.objects.all()
  
  patients = add_mui_filters(
    patients,
    filter,
    {"MRN": "medical_record_number", "placeOfBirth": "__place_of_birth__name"},
  ) 
  
  return patients # This returns a QuerySet - you will often encode this into JSON. 
  
```

Note how in the mappings placeOfBirth is in camelCase. This is becuase it's submitted in cammel case and it is more efficent not to convert it if you are providing a mapping. It uses __ in place of birth becuase it is a diffrent table - we must specify when we traverse tables.


Here is some of my production code:

```python
 def resolve_all_timeouts(root, info, page_size, page_number, mui_filter_model):
        # Error w/ string reading
        prefiltered_timeouts = abx_timeout.objects.filter(
            prescription__drug__ignore=False, active=True
        )

        filtered_timeouts = add_mui_filters(
            prefiltered_timeouts,
            mui_filter_model,
            {
                "timeoutId": lambda *_: "pk",
                "status": status_filter_interpreter,
                "firstName": "prescription__visit__patient__first_name",
                "lastName": "prescription__visit__patient__last_name",
                "patientName": "prescription__visit__patient__full_name",
                "MRN": "prescription__visit__patient__pk",
                "antibioticName": "prescription__drug__name",
                "dose": "prescription__dose",
                "route": "prescription__route",
                "room": "prescription__visit__room",
                "frequency": "prescription__frequency",
                "doseRouteFrequency": "prescription__frequency__dose_route_frequency",
                "startDate": "prescription__start_date",
                "indicationForDrug": "prescription__indication",
                # Next is one to many. Won't work?
                "cultureAndSensitivity": "prescription__visit__culture__text",
                "imaging": "prescription__visit__imaging__text",
                "labs": "prescription__visit__lab_trio__text",
                "stopDate": "prescription__end_date",
                "timeoutCompleted": timeout_completed_interpreter,
            }
        )
```

# Active Areas of Improvment

- Documentation
- PIP Installation
