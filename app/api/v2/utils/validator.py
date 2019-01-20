from flask import abort
from werkzeug.security import generate_password_hash, check_password_hash
errors = []
def validate(inputdata, required_fields=[]):
    ''' This function validates all required input fields '''
    errors = []
    keys = list(inputdata.keys())

    for field in required_fields:
        if field not in keys:
            errors.append('{} required'.format(field))
        else:
            if len(str(inputdata[field]).strip(' ')) <= 0:
                errors.append('{} cannot be empty'.format(field))

    if len(errors) > 0:
        return errors
    return inputdata
    