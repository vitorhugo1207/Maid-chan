from random import randrange
from datetime import datetime
from time import sleep

class diceMain():
    def __init__(self, dice):
        self.dice = dice
        self.diceT = None
        self.diceA = None
        self.diceMin = 1 # The minimum for start scroll dice
        self.rollList = []
        self.rollBonus = None
        self.rollTotal = None

    def getScrollTimes(self):
        '''Dice scroll times'''
        
        diceFindD = self.dice.find('d')
        self.diceA = self.dice[:diceFindD].replace('d', '') # Extraction time of dice roll and remove "d"
        if self.diceA == '':
            self.diceA = 1
        self.diceT = self.dice[diceFindD:].replace('d', '') # Extraction interval of draw

    def bonus(self):
        '''Bonus extraction'''

        if '+' in self.dice:
            diceFindBonus = self.dice.find('+')
            self.rollBonus = self.dice[diceFindBonus:].replace('+', '')
            self.diceT = self.diceT[:diceFindBonus - 1].replace('+', '')
            try:
                self.rollBonus = int(self.rollBonus)
            except ValueError:
                dice = self.dice[:diceFindBonus]

        elif '-' in self.dice:
            diceFindBonus = self.dice.find('-')
            self.rollBonus = self.dice[diceFindBonus:].replace('-', '')
            self.diceT = self.diceT[:diceFindBonus - 1].replace('-', '')
            try:
                self.rollBonus = int(self.rollBonus)
            except ValueError:
                dice = self.dice[:diceFindBonus]

        elif '*' in self.dice:
            diceFindBonus = self.dice.find('*')
            self.rollBonus = self.dice[diceFindBonus:].replace('*', '')
            self.diceT = self.diceT[:diceFindBonus - 1].replace('*', '')
            try:
                self.rollBonus = int(self.rollBonus)
            except ValueError:
                dice = self.dice[:diceFindBonus]

        elif '/' in self.dice:
            diceFindBonus = self.dice.find('/')
            self.rollBonus = self.dice[diceFindBonus:].replace('/', '')
            self.diceT = self.diceT[:diceFindBonus - 1].replace('/', '')
            try:
                self.rollBonus = int(self.rollBonus)
            except ValueError:
                dice = self.dice[:diceFindBonus]
        
        if self.diceT == '0': # If not have 'd' in dice
            self.diceA = 1
            self.diceT = dice

    def sumDice(self):
        '''Sum List of dice roll and roll bonus'''

        if '+' in self.dice:
            self.rollTotal = sum(self.rollList) + self.rollBonus
            self.rollList.append(f'+{self.rollBonus}')
            self.rollBonus = ''

        elif '-' in self.dice:
            self.rollTotal = sum(self.rollList) - self.rollBonus
            self.rollList.append(f'-{self.rollBonus}')
            self.rollBonus = ''

        elif '*' in self.dice:
            self.rollTotal = sum(self.rollList) * self.rollBonus
            self.rollList.append(f'*{self.rollBonus}')
            self.rollBonus = ''

        elif '/' in self.dice:
            self.rollTotal = sum(self.rollList) / self.rollBonus
            self.rollList.append(f'/{self.rollBonus}')
            self.rollBonus = ''

        else:
            self.rollTotal = sum(self.rollList)

    def dataShow(self):
        '''Data show'''
        pass

    def diceRoll(self):
        self.getScrollTimes()
        self.bonus()

        try:
            # __Str for Int__
            self.diceT = int(self.diceT) + 1 # Counting with the 0
            self.diceA = int(self.diceA)
        except:
            print('I am sorry, did not understood. Type "help" for instructions.')
            sleep(5)
            dice = ''
            return

        # __Loop of scroll dice time__
        try:
            for x in range(self.diceA):
                self.rollList.append(randrange(self.diceMin, self.diceT))  # self.diceMin (Minimum) between self.diceT (Total)
        except:
            print('I am sorry, did not understood. Type "help" for instructions.')
            sleep(5)
            dice = ''
            return

        self.sumDice()
        self.dataShow()
