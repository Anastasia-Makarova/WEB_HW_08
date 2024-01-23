from models import Subscriber
from faker import Faker


fake = Faker()


if __name__ == '__main__':

    for i in range(100):
        subscriber=Subscriber(
            fullname = fake.name(),
            email = fake.email(),
            phone = fake.phone_number())
            
        subscriber.save()
        

    

