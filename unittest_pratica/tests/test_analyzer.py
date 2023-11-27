from analyzer import analyze_json_file


def test_analyze_json_file():
    result = analyze_json_file("person_data.json")
    assert result == "A pessoa de nome João tem 30 anos de idade."
