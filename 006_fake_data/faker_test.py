# coding: utf8

from faker import Faker

## 实例化
fake = Faker(locale='zh_CN')

name = fake.name()
address = fake.address()

print(name, address)

print(dir(fake))
print('-' * 60)
print(
    fake.random_digit(),
    fake.random_int(),
)
print('-' * 60)
for name in range(4):
    print(fake.user_agent())

# print('-' * 60)
# print(fake.word())
# print('-' * 60)
# print(fake.sentence())
# print('-' * 60)
# print(fake.paragraph())
# print('-' * 60)
# print(fake.text())
# print('-' * 60)
# print(fake.simple_profile())
# print('-' * 60)
# print(fake.profile())
# print('-' * 60)
# print(fake.linux_platform_token())

# print("salary xxx")
# print(dir(fake))