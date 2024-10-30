def test_user_registration(registration_page):
    message = registration_page.register_and_get_message(
        first_name="John",
        last_name="Doe",
        email="jxohn.doe@example.com",
        password="Password1234"
    )

    assert message in ["Registration complete", "User already exists"], f"Неочікуване повідомлення: {message}"