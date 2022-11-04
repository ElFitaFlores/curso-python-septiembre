from user import register_user
import pytest

class TestRegisterUser:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.user_data = {
            'first_name': 'Rafael',
            'last_name': 'Flores',
            'birthdate': '1992-11-27',
            'gender': 'male',
            'email': 'rflores@levelup.gt'
        }

    def test_user_is_registered(self):
        #Act
        message = register_user(**self.user_data)

        #Assert
        assert message == 'User succesfully regitered.'
        from user import user_dict
        assert user_dict == self.user_data

    def test_should_raise_an_error_if_gender_is_incorrect(self):
        with pytest.raises(Exception) as error:
            self.user_data['gender'] = 'incorrect'

            message = register_user(**self.user_data)

        assert str(error.value) == 'Genders can be male, female or others'

    def test_should_raise_an_error_if_email_is_incorrect(self):
        with pytest.raises(Exception) as error:
            self.user_data.update({'email': 'formato-incorrecto-de-email'})

            register_user(**self.user_data)

        assert str(error.value) == 'Incorrect email format.'