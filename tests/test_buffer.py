from src.buffer import Text, Buffer
import pytest
import datetime


class TestBuffer:
    def setup_method(self):
        self.buffer = Buffer()

    def test_buffer_init(self):
        assert self.buffer.memory == []

    @pytest.mark.parametrize('word', ['hello', 'xyz xyz', '123'])
    def test_buffer_add_text(self, word):
        self.buffer.memory.append(word)
        assert self.buffer.memory == [word]

    def test_buffer_add_multiple_texts(self):
        self.buffer.memory.append("hello")
        self.buffer.memory.append("world")
        assert self.buffer.memory == ["hello", "world"]

    def test_buffer_clear(self):
        self.buffer.memory.append("hello")
        self.buffer.memory.clear()
        assert self.buffer.memory == []


@pytest.fixture()
def text():
    return Text()


def test_text_object():
    text = Text("encrypted", 13)
    assert text.status == "encrypted"
    assert text.rot == 13


def test_to_dct(text):
    result = text.to_dct(status="encrypted", rot=47)
    expected_result = {
        "text": [],
        "created": str(datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")),
        "status": "encrypted",
        "rot": 47,
    }
    assert result == expected_result
