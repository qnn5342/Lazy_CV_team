import mlab
from Module.service import Service
from faker import Faker
from random import randint, choice


mlab.connect()

fake = Faker()
for i in range (50):
    print("Saving service", i +1, '.....')
    service = Service(name=fake.name(),
                        yob= randint(1990,2000),
                        gender= randint(0,1),
                        height= randint(150,180),
                        phone = fake.phone_number(),
                        address= fake.address(),
                        status=choice([True, False]))
    service.save()
