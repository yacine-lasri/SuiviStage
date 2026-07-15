from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def ready(self):
        # Import the module that contains the @receiver decorators.
        # This connects the post_save signal to create_profile_on_signup.
        import users.models  # noqa: F401
