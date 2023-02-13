from src.buffer import Text
import pytest


@pytest.fixture
def text_object():
    return Text("Test", "encrypted", 13)


def test_text_object(text_object):
    assert text_object.name == "Test"
    assert text_object.status == "encrypted"
    assert text_object.rot == 13


#
#
# def test_adding_text_object_to_dict(text_object):
#     assert text_object.to_dct('test', 'list', 'encrypted', 13) == {'test': 'list', 'created': 'test',
#                                                                    'status': 'encrypted', 'rot': 13}
