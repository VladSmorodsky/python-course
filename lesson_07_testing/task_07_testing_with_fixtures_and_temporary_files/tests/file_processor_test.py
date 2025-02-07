import pytest

from lesson_07_testing.task_07_testing_with_fixtures_and_temporary_files.src.file_processor import FileProcessor


@pytest.fixture
def temporary_file_path(tmpdir):
    """
    Fixture for temporary file
    :return:
    """
    return tmpdir / 'test.txt'


class TestFileProcessor:

    @pytest.mark.parametrize("data, expectedData", [
        ("Hello World!", "Hello World!\n"),
        ("  ", "\n")
    ])
    def test_write_file(self, data, expectedData, temporary_file_path):
        """
        Test write file
        :param temporary_file_path:
        :return:
        """
        FileProcessor.write_to_file(temporary_file_path, data)
        with open(temporary_file_path, 'r') as file:
            result = file.read()
        assert expectedData == result

    @pytest.mark.parametrize("data, expectedData", [
        (["Hello World!", "Test"], "Hello World!\nTest\n"),
        (["Hello World!", "Test", "  "], "Hello World!\nTest\n\n"),
    ])
    def test_write_file_with_several_lines(self, data, expectedData, temporary_file_path):
        """
        Test writing a lot of lines (With text and empty strings)
        :param data:
        :param expectedData:
        :param temporary_file_path:
        :return:
        """
        for row in data:
            FileProcessor.write_to_file(temporary_file_path, row)
        with open(temporary_file_path, 'r') as file:
            result = file.read()
        assert expectedData == result

    def test_write_file_raises_file_not_found_error(self):
        """
        Test if FileNotFoundError raised
        :return:
        """
        with pytest.raises(FileNotFoundError):
            FileProcessor.read_from_file('error_file.txt')

    @pytest.mark.parametrize("data, expectedData", [
        (["Hello World!", "Test"], "Hello World!\nTest\n"),
        (["Hello World!", "Test", "  "], "Hello World!\nTest\n\n"),
    ])
    def test_read_file(self, temporary_file_path, data, expectedData):
        """
        Test reading data
        :param temporary_file_path:
        :param data:
        :param expectedData:
        :return:
        """
        for row in data:
            FileProcessor.write_to_file(temporary_file_path, row)
        result = FileProcessor.read_from_file(temporary_file_path)
        assert expectedData == result

    def test_read_file_raises_file_not_found_error(self):
        """
        Test FileNotFoundError raised
        :return:
        """
        with pytest.raises(FileNotFoundError):
            FileProcessor.read_from_file('not_found_file.txt')