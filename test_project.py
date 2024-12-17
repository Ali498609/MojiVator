from unittest.mock import mock_open, patch
from project import get_quote,store_data,track_emotions

def test_get_quote():
    assert get_quote("✨") == "Sorry, There is no quote for the given emoji"
    assert get_quote("😆") == ("😆", "Laughter is the best medicine; keep laughing out loud!")
    assert get_quote("😇") == ("😇", "Goodness in your heart reflects in your actions—stay amazing!")
    assert get_quote("❤️") == "Sorry, There is no quote for the given emoji"

def test_store_data():
    assert store_data("😆") == "😆 is Stored!"
    assert store_data("😊") == "😊 is Stored!"

def test_track_emotions():
    # Mock content of userdata.csv
    userdata_mock = (
        "2024-12-14 11:21:08,😫\n"
        "2024-12-14 11:24:54,😭\n"
        "2024-12-14 11:35:57,😤\n"
    )

    # Expected output based on mocked file
    expected_output = (
        "At this time: 2024-12-14 11:21:08, your emotion is this: 😫\n"
        "At this time: 2024-12-14 11:24:54, your emotion is this: 😭\n"
        "At this time: 2024-12-14 11:35:57, your emotion is this: 😤"
    )

    with patch("builtins.open", mock_open(read_data=userdata_mock)):
        result = track_emotions("yes")
        assert result == expected_output
