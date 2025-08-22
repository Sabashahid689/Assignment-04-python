import random

def random_number():
  for i in range(10):
    num:list[int] = random.randint(1, 100)
    print(num)

if __name__ == '__main__':
  random_number()