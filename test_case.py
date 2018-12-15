import pytest
from main import construct

def test_simple_json():
    simple_json = {"name": "Boris"}
    
    node = construct(simple_json)
    assert node.__str__() == "NAME(Boris)"
