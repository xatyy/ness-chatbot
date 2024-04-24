"""test_main.py"""
from streamlit.testing.v1 import AppTest
from read_file import read_file_to_string # Decided to move the file read function to a separate file because I had issues with importing the main into the test unit.


def test_read_file_to_string():
    result = read_file_to_string('test_file.txt')
    assert result == "File content"

def test_not_found_read_file_to_string():
    file_path = 'non_existent.txt'
    result = read_file_to_string(file_path)
    assert result == f"File '{file_path}' not found."

def test_chatting(): # Used an example from streamlit docs to test the chatting function,
    at = AppTest.from_file("main.py").run()
    at.chat_input[0].set_value("Tell me something about the scenario").run()
    assert at.chat_message[0].markdown[0].value == "Tell me something about the scenario"
    assert at.chat_message[0].avatar == "user"
