def read_root():
    return {
        "message": "Hello world"
    }

def test_read_root():
    assert read_root() == {"message": "Hello world"}