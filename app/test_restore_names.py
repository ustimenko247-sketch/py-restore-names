import pytest


def restore_names(users: list[dict]) -> None:
    for user in users:
        if "first_name" not in user or user["first_name"] is None:
            if "full_name" in user:
                user["first_name"] = user["full_name"].split()[0]


def test_restore_none_or_missing() -> None:
    users = [
        {"first_name": None,
         "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"last_name": "Adams",
         "full_name": "Mike Adams"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Jack",
         "last_name": "Holy",
         "full_name": "Jack Holy"},
        {"first_name": "Mike",
         "last_name": "Adams",
         "full_name": "Mike Adams"},
    ]


def test_restore_existing() -> None:
    users = [
        {"first_name": "Anna",
         "last_name": "Smith",
         "full_name": "Anna Smith"},
        {"first_name": "John",
         "last_name": "Doe",
         "full_name": "John Doe"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Anna",
         "last_name": "Smith",
         "full_name": "Anna Smith"},
        {"first_name": "John",
         "last_name": "Doe",
         "full_name": "John Doe"},
    ]


def test_restore_mixed() -> None:
    users = [
        {"first_name": None,
         "last_name": "Brown",
         "full_name": "Chris Brown"},
        {"first_name": "Emily",
         "last_name": "Clark",
         "full_name": "Emily Clark"},
        {"last_name": "Taylor",
         "full_name": "Robert Taylor"},
    ]
    restore_names(users)
    assert users == [
        {"first_name": "Chris",
         "last_name": "Brown",
         "full_name": "Chris Brown"},
        {"first_name": "Emily",
         "last_name": "Clark",
         "full_name": "Emily Clark"},
        {"first_name": "Robert",
         "last_name": "Taylor",
         "full_name": "Robert Taylor"},
    ]
