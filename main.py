from faker import Faker

fake = Faker('tr_TR')

for _ in range(10):
    print(f'İsim: {fake.name()}')
    print(f'Meslek: {fake.job()}')
    print(f'Adres: {fake.address()}')
    print(f'IP adresi: {fake.ipv4_private()}')
    print('*******')

