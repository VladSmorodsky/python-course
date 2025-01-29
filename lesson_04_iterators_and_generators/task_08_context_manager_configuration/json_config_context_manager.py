import json


class JsonConfigContextmanager:
    """
    Read configuration on start context and save it into file after exit form context.
    """

    def __init__(self, config_file_path: str) -> None:
        self._config_file_path = config_file_path
        self._config = {}

    def __enter__(self) -> dict:
        """
        Open file, load config from it and return content
        :return:
        """
        try:
            with open(self._config_file_path, 'r') as file:
                self._config = json.load(file)
        except FileNotFoundError:
            self._config = {}
        return self._config

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Write _config object into json file
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
        with open(self._config_file_path, 'w') as file:
            print(self._config)
            json.dump(self._config, file, indent=4)
