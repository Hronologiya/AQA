import pytest
import allure
from app.db import init_db, insert_data, get_data, update_data, delete_data

@allure.feature('Database Operations')
def test_connect_db():
    with allure.step("Initialize the database"):
        init_db()
        assert True, "Connected to the database successfully."

@allure.feature('Database Operations')
def test_insert_data():
    with allure.step("Insert data into the database"):
        insert_data("test_name", "test_value")
    with allure.step("Fetch data from the database"):
        data = get_data()
        assert len(data) > 0, "No data fetched from the database."
        assert data[0][1] == "test_name", "Data not inserted correctly."

@allure.feature('Database Operations')
def test_update_data():
    with allure.step("Fetch data from the database"):
        data = get_data()
        record_id = data[0][0]
    with allure.step("Update data in the database"):
        update_data(record_id, "updated_name", "updated_value")
    with allure.step("Fetch updated data from the database"):
        updated_data = get_data()
        assert updated_data[0][1] == "updated_name", "Data not updated correctly."

@allure.feature('Database Operations')
def test_delete_data():
    with allure.step("Fetch data from the database"):
        data = get_data()
        record_id = data[0][0]
    with allure.step("Delete data from the database"):
        delete_data(record_id)
    with allure.step("Fetch final data from the database"):
        final_data = get_data()
        assert len(final_data) == 0, "Data not deleted."

if __name__ == "__main__":
    test_connect_db()
    test_insert_data()
    test_update_data()
    test_delete_data()
    print("All tests passed.")
