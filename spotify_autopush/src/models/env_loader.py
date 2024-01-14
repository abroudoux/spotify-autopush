import os
from dotenv import load_dotenv
from rich import print


class EnvLoader:
    """
    A class dedicated to loading and validating environment variables from a .env file.

    This class is respoTIFY_nsible for ensuring that all necessary environment variables are correctly loaded into the application's environment. It provides functionality to load variables from a .env file and validate their presence.

    Methods:
    --------
    load_env():
        Loads environment variables from a .env file and validates them.

    validate(env):
        Validates the necessary environment variables to ensure they are present.
    """

    def load_env(self) -> None:
        """
        Loads environment variables from a .env file and validates their presence.

        This method uses the 'dotenv' library to load environment variables from a .env file located in the application's root directory. After loading the variables, it calls the 'validate' method to ensure all required variables are present.

        If a required environment variable is missing, it prints an error message using the 'rich' library for better formatting.

        Raises:
        -------
        ValueError: If any required environment variables are missing.
        """
        load_dotenv()
        try:
            self.validate(os.environ)
        except ValueError as e:
            print(f"[bold red]Error: {e}[/bold red]")

    def validate(self, env: os._Environ[str]) -> None:
        """
        Validates the presence of necessary environment variables.

        This method checks for the existence of all required environment variables. The list of required variables is defined within the method. If any of these variables are missing, a ValueError is raised with a descriptive message.

        Parameters:
        -----------
        env (os._Environ[str]): The environment variables dictionary to validate.

        Raises:
        -------
        ValueError: If any required environment variables are not found in 'env'.
        """
        required_keys = ["GITHUB_PERSONAL_ACCESS", "SPOTIFY_CLIENT_ID", "SPOTIFY_CLIENT_SECRET", "SPOTIFY_REDIRECT_URI"]
        for key in required_keys:
            if not env.get(key):
                raise ValueError(
                    f"Required environment variable '{key}' is missing. Please set it in your .env file.")
