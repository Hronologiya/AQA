from app.db import init_db, insert_data, get_data, update_data, delete_data

def test_database_operations():
    init_db()
    insert_data("test_name", "test_value")
    data = get_data()
    assert len(data) > 0, "No data fetched from the database."

    update_data(data[0][0], "updated_name", "updated_value")
    updated_data = get_data()
    assert updated_data[0][1] == "updated_name", "Data not updated."

    delete_data(updated_data[0][0])
    final_data = get_data()
    assert len(final_data) == 0, "Data not deleted."

if __name__ == "__main__":
    test_database_operations()
    print("All tests passed.")