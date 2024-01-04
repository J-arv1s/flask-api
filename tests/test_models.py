from application.characters.models import Character

def test_create():
    character = Character("good", "a", "a", "f", 12, "d", 19)

    assert character.alignment == "good"
    assert character.height == 12
    assert character.weight == 19
