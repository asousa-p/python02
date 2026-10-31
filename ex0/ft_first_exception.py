def input_temperature(temp_str: str) -> int:
    temp_int: int = int(temp_str)
    return temp_int


def test_temperature(temp_test: str) -> None:
    print(f"Input data is '{temp_test}'")
    try:
        input_temperature(temp_test)
        print(f"Temperature is now {temp_test}°C")
    except ValueError as e:
        print(f"Caught input_temperature error: {e}")


if __name__ == "__main__":
    print("=== Garden Temperature ===")
    print("")
    test_temperature("25")
    print("")
    test_temperature("abc")
    print("")
    print("All test completed - program didn't crash!")
