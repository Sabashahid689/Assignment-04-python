def main():
  fruits ={'apple': 1.5, 'durian': 50, 'jackfruit': 80, 'kiwi': 1, 'rambutan': 1.5, 'mango': 5}

  total_const = 0
  for fruits_name in fruits:
    price = fruits[fruits_name]
    amount_bought = int(input(f"How many {fruits_name} do you want to buy? "))
    total_const += (price * amount_bought)

  print("Your total is $: " + str(total_const))

if __name__ == '__main__':
  main()