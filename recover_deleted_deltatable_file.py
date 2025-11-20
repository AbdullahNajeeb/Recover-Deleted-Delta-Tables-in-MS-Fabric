import sempy_labs.lakehouse as lake

# table_name: Insert deleted table name

lake.recover_lakehouse_object(
    file_path="Tables/table_name",
    lakehouse="lakehouse_name")

# file_name: Insert deleted parquet file_name
lake.recover_lakehouse_object(
    file_path="Files/Folder/file_name",
    lakehouse="lakehouse_name")



# Altering Retention Period to Avoid Removal of Deleted Tables/Files before Recovery.
%%sql
ALTER TABLE table_name SET TBLPROPERTIES (
  'delta.logRetentionDuration' = '45 days',
  'delta.deletedFileRetentionDuration' = '45 days');
