from faker import Faker

faker = Faker(locale="pt_BR")

print(faker.name())
print(faker.phone_number())
print(faker.cpf())


def create_user(name, email):

    return {
        "first_name": name.split()[0],
        "last_name": name.split()[-1],
        "email": email,
        "email_domain": email.split("@")[-1],
    }
