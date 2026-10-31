def garden_operations(operation_number: int) -> None:
    abc: str = "abc"
    num: int = 1
    if operation_number == 0:
        abc = int(abc)
    if operation_number == 1:
        num /= 0
    if operation_number == 2:
        open("/non/existent/file")
    if operation_number == 3:
        abc += num


def test_error_types() -> None:
    for i in range(0, 5):
        print(f"Testing operation {i}...")
        try:
            garden_operations(i)
            print("Operation completed successfully")
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("")
    print("All error types tested successfully!")
