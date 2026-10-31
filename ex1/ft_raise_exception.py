def input_temperature(temp_str: str) -> int:
    temp_int: int = int(temp_str)
    if temp_int > 40:
        raise ValueError(f"{temp_int}°C is too hot for plans (max 40°C)")
    if temp_int < 0:
        raise ValueError(f"{temp_int}°C is too cold for plans (min 0°C)")
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
    test_temperature("100")
    print("")
    test_temperature("-50")
    print("")
    print("All test completed - program didn't crash!")
