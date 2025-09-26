from faker import Faker


class Fake:
    def __init__(self, faker: Faker):
        self.faker = faker

    def text(self) -> str:
        return self.faker.word()

    def integer(self, start: int = 1, end: int = 100) -> int:
        return self.faker.random_int(start, end)

    def email(self, domain: str | None = None) -> str:
        return self.faker.email(domain=domain)


faker = Fake(faker=Faker())
