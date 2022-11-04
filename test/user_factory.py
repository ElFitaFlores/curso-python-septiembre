from user import register_user
from faker import Faker

fake = Faker()

class UserFactory:
    def create():
        user_data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'birthdate': fake.date(),
            'gender': 'male',
            'email': fake.email(),
        }
        register_user(**user_data)

        return user_data