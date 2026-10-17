from pydantic import BaseModel
class User(BaseModel):
    email: str | None = None

# 1. Basic function hints
def full_name(first: str, last: str) -> str:
    return f"{first} {last}"


print(full_name("Venkatesh", "anandhan"))


# 2. Dict lookup that may find nothing
def get_user_age(users: dict[str, int], name: str) -> int | None:
    return users.get(name)


users = {"asha": 90, "ravi": 75}
print(get_user_age(users, "asha"))
print(get_user_age(users, "kumar"))


# 3. List of numbers
def average(numbers: list[float]) -> float:
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


print(average([80, 90, 100]))
print(average([]))



def create_user(email: str | None = None)-> str:
    user = User(email=email)
    return str(user)


print(create_user("venkatesh@example.com"))
print(create_user())


