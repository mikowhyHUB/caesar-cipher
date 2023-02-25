from src.buffer import Text, Buffer
import pytest
import datetime


@pytest.fixture
def buffer():
    return Buffer()


class TestBuffer:
    def setup_method(self):
        self.buffer = Buffer()

    def test_buffer_init(self):
        assert self.buffer.memory == []

    @pytest.mark.parametrize('word', ['hello', 'xyz xyz', '123'])
    def test_buffer_add_text(self, buffer, word):
        buffer.memory.append(word)
        assert buffer.memory == [word]

    def test_buffer_add_multiple_texts(self, buffer):
        buffer.memory.append("hello")
        buffer.memory.append("world")
        assert buffer.memory == ["hello", "world"]

    def test_buffer_clear(self, buffer):
        buffer.memory.append("hello")
        buffer.memory.clear()
        assert buffer.memory == []


@pytest.fixture
def text_object():
    return Text("encrypted", 13)


def test_text_object(text_object):
    assert text_object.status == "encrypted"
    assert text_object.rot == 13


def test_to_dct(text_object):
    result = text_object.to_dct(status="encrypted", rot=47)
    expected_result = {
        "text": [],
        "created": str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")),
        "status": "encrypted",
        "rot": 47,
    }
    assert result == expected_result
