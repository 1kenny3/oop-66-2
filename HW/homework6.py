from faker import Faker  #Эта библиотека нужна для генерации ложных данных 
from colorama import Fore, Back, Style #Эта библиотека нужна для покраски текста в терминале  

fake = Faker(['it_IT', 'en_US', 'ja_JP', 'ru_RU'])


for _ in range(10):
  print(fake.name())

print('-' * 30)


for _ in range(10):
    print(fake.country())

print('-' * 30)

for _ in range(10):
    print(fake.company())

print('-' * 30)


for _ in range(10):
    print(fake.email())

print('-' * 30)


for i in range(5):
    name = fake.name()
    email = fake.email()
    ip = fake.ipv4()
    
    # Скрещиваем: цвета из colorama прямо в f-строки перед данными от faker
    print(f"  {Fore.YELLOW}Имя: {Style.BRIGHT}{name}")
    print(f"  {Fore.BLUE}Email: {email}")
    print(f"  {Fore.MAGENTA}IP-адрес: {Back.BLACK}{ip}")
    print(Fore.GREEN + "-" * 40)




def two_sum(nums, target):
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    
            

nums = [2, 7, 11, 15, 26, 17, 33]
target = 9

result = two_sum(nums, target)
print(result)