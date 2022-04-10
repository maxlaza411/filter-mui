# filter-mui

This program converts MUI DataGrid filters into Django queries. 

# How to Use

Submit your MUI filters to your Django backend via a JSON String. Create a query set and then run the function add_mui_filters(query_set, json_string_filters, column_field_mappings). This will apply all of the MUI filters to the QuerySet and then return it. By default all of the columnFields are convert from camelCase to snake_case. For example the column medicalRecordNumber will be converted to medical_record_number. Say for the field is called MRN on the frontend then it would convert to M_R_N, but this is not consistent with the database so you need to pass in {"MRN": "medical_record_number"} to the column_field_mappings. 

# Example

from filtermui import add_mui_filters


def patient_table_query(filter)
    patients = patient.objects.all()


# Things still being worked on

- I have not finished the integration or unit tests yet.
- Program needs performance update. There was a lot of slowdown on my last addition.
