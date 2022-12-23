import random

class Dice:
  def __init__(self, dice_string: str):
    self.dice_string = dice_string
    self.rolls = []
    self.bonus = None
    self.total = None
    self.parse_dice_string()

  def parse_dice_string(self):
    # Split dice string into rolls and bonus
    if '+' in self.dice_string or '-' in self.dice_string or '*' in self.dice_string or '/' in self.dice_string:
      self.bonus = int(self.dice_string.split('d')[1])
      self.dice_string = self.dice_string.split('d')[0]
     self.rolls = [int(x) for x in self.dice_string.split('d')]
     if len(self.rolls) == 1:
       self.rolls.append(self.rolls[0])
       self.rolls[0] = 1

  def roll(self):
    # Roll the dice and apply bonus
    rolls = [random.randint(1, self.rolls[1]) for _ in range(self.rolls[0])]
    self.total = sum(rolls)
    if self.bonus:
      bonus_op = self.dice_string.split('d')[1][0]
      self.total = {'+': self.total + self.bonus, '-': self.total - self.bonus, 
                    '*': self.total * self.bonus, '/': self.total / self.bonus}[bonus_op]
    return self.total

dice = Dice('2d20+5')
print(dice.roll())
