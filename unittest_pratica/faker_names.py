from faker import Faker

faker = Faker(locale="pt_BR")

print(faker.name())
print(faker.phone_number())
print(faker.cpf())
