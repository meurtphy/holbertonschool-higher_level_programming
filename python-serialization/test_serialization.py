from task_00_basic_serialization import serialize_and_save_to_file

#
data_to_serialize = {
    "name": "Jonh Doe",
    "age": 30,
    "city": "New York"
}


serialize_and_save_to_file(data_to_serialize, "data.json")