import json

def read_json(file_name):
    with open(f'test_data/{file_name}') as f:
        return json.load(f)

#yaha only function bana hai actual read nahi ho raha hai, read test file m hoga