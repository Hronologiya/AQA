from app.db import init_db, insert_data, get_data, update_data, delete_data


def main():
    init_db()
    print("Database initialized.")

    insert_data("test_name", "test_value")
    print("Data inserted.")

    data = get_data()
    print(f"Data fetched: {data}")

    update_data(1, "updated_name", "updated_value")
    print("Data updated.")

    delete_data(1)
    print("Data deleted.")


if __name__ == "__main__":
    main()