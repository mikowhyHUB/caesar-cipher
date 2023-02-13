from src.buffer import Text, Buffer
import pytest
import datetime


@pytest.fixture
def text_object():
    return Text("Test", "encrypted", 13)


def test_text_object(text_object):
    assert text_object.name == "Test"
    assert text_object.status == "encrypted"
    assert text_object.rot == 13


def test_buffer_object():
    buffer = Buffer()
    assert buffer.text.rot == None
    assert buffer.text.status == None
    assert buffer.text.name == None


def test_to_dct(text_object):
    result = text_object.to_dct(name="test", memory="text", status="encrypted", rot=47)
    expected_result = {
        "test": "text",
        "created": str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")),
        "status": "encrypted",
        "rot": 47,
    }
    assert result == expected_result
