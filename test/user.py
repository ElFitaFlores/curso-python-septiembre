import re

user_dict = None

def register_user(
    first_name,
    last_name,
    birthdate,
    gender,
    email
):
    global user_dict
    GENDER_MALE = 'male'
    GENDER_FEMALE = 'female'
    GENDER_OTHERS = 'others'

    if gender not in [GENDER_FEMALE, GENDER_MALE, GENDER_OTHERS]:
        raise Exception(f'Genders can be {GENDER_MALE}, {GENDER_FEMALE} or {GENDER_OTHERS}')

    if not validate_email(email):
        raise Exception('Incorrect email format.')

    user_dict = {
        'first_name': first_name,
        'last_name': last_name,
        'birthdate': birthdate,
        'gender': gender,
        'email': email,
    }

    return 'User succesfully regitered.'



def validate_email(email):
   pat = r"^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   return re.match(pat, email)