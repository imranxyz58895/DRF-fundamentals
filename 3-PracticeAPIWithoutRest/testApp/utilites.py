import json 

def validate_json(data):
    try:
        if json.loads(data):
            return True
    except json.JSONDecodeError as error: 
        return False