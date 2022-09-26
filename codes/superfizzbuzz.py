class ReadNum:
    def __init__(self,num: int):
        self.num = num
    def check(self):
        pass

class Fizz(ReadNum):
    def check(self):
        if(self.num%3==0):
            return 'Fizz'
        else:
            return None

class Buzz(ReadNum):
    def check(self):
        if(self.num%5==0):
            return 'Buzz'
        else:
            return None

class FizzBuzz(ReadNum):
    def check(self):
        if(self.num%3==0 and self.num%5==0):
            return 'FizzBuzz'
        else:
            return None

class FizzFizz(ReadNum):
    def check(self):
        if(self.num%9==0):
            return 'FizzFizz'
        else:
            return None

class BuzzBuzz(ReadNum):
    def check(self):
        if(self.num%25==0):
            return 'BuzzBuzz'
        else:
            return None

class FizzFizzBuzzBuzz(ReadNum):
    def check(self):
        if(self.num%9==0 and self.num%25==0):
            return 'FizzFizzBuzzBuzz'
        else:
            return None

def superfizzbuzz(num: int):
        ReadNum(num).check()
        result = None
        if Fizz(num).check() != None:
            result = Fizz(num).check()
        if Buzz(num).check() != None:
            result = Buzz(num).check()
        if FizzBuzz(num).check() != None:
            result = FizzBuzz(num).check()
        if FizzFizz(num).check() != None:
            result = FizzFizz(num).check()
        if BuzzBuzz(num).check() != None:
            result = BuzzBuzz(num).check()
        if FizzFizzBuzzBuzz(num).check() != None:
            result = FizzFizzBuzzBuzz(num).check()        
        return result

