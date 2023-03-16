from src.example import example_view


# Just a example test
# Feel free to delete this file
def test_example_view():
    response = example_view()
    assert response == {"example": "example"}
