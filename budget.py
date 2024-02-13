class Category:

  def __init__(self, category) -> None:
    self.category = category
    self.ledger = []
    self.balance = 0

  def deposit(self, amount: float, description: str = ""):

    self.ledger.append({'amount': amount, 'description': description})
    self.balance += amount
    return True

  def withdraw(self, amount: float, description: str = ""):
    if (self.check_funds(amount)):
      withdraw = {'amount': -amount, 'description': description}

      self.ledger.append(withdraw)
      self.balance -= amount
      return True
    return False

  def get_balance(self):
    return self.balance

  def check_funds(self, amount: float):
    if (amount > self.balance):
      return False
    return True

  def transfer(self, amount: float, TargetCategory: "Category"):
    if (self.check_funds(amount)):
      self.withdraw(amount, "Transfer to {}".format(TargetCategory.category))
      TargetCategory.deposit(amount, "Transfer from {}".format(self.category))
      return True
    return False

  def __str__(self) -> str:
    padding = int((30 - len(self.category)) / 2)
    header = "".rjust(padding, "*") + self.category + "".ljust(padding, "*")

    if (len(header) < 30):
      header = header.rjust(30, "*")

    row = ""
    for element in range(len(self.ledger)):

      description = str(self.ledger[element]["description"])[:23].ljust(
        23, " ")
      amount = ("%.2f" % float(self.ledger[element]["amount"])).rjust(7, " ")
      row += (description + amount + "\n")
    row += "Total: {}".format(self.balance)
    return header + "\n" + row


def create_spend_chart(categories: list[Category]):
  categoryName = []
  percentage = []
  spentByCategory = []
  total = 0
  returnString = "Percentage spent by category"
  padding = len(categories) * 3 + 1

  for cat in categories:
    #Get array of category names
    categoryName.append(cat.category)
    spent = 0
    for i in cat.ledger:

      if (i["amount"] < 0):
        spent += i["amount"]
    #Get spent amount by category
    spentByCategory.append(spent)
    total += spent
  for i in spentByCategory:
    #Get %
    percent = (int((i / total) * 100) * .1) * 10

    percentage.append(percent)

  for i in range(0, 110, 10):
    currentLine = ""

    for n in range(len(percentage)):

      if (percentage[n] >= 100 - i):

        currentLine += " {} ".format("o")
      else:
        currentLine += " {} ".format(" ")

    returnString += "\n" + (str(100 - i).rjust(3, " ") +
                            "|") + currentLine + " "

  bottomLine = ""
  testline = ""
  longestCategory = len(max(categoryName, key=len))
  for i in range(longestCategory):
    for j in range(len(categoryName)):
      bottomLine += " {} ".format(categoryName[j].ljust(longestCategory,
                                                        " ")[i])
    testline += "\n" + "    " + bottomLine + " "
    bottomLine = ""

  returnString += "\n" + "    " + "".rjust(padding, "-")
  returnString += testline
  return returnString
