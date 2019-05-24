class FizzBuzz():
    """ Fizzbuzz class to encapsulate all the functions to solve the problem

        The objects must have a fizznumber and a buzznumber
    """

    def __init__(self,fizznumber, buzznumber):
        
        self.fizznumber = fizznumber
        self.buzznumber = buzznumber

    def solve(self, start, end):
        """ Returns a list of fizzbuzz solutions. 
            The list is bounded with start and end values
            
            :param start: int
            :param end: int
            :return: list
        """

        def int_to_fizzbuzz(i):
            """ Returns the fizzbuzz solution for an int

                :param i: int
                :return: int
            """ 
            entry = ''
            if i%self.fizznumber == 0:
                entry += "Fizz"
            if i%self.buzznumber == 0:
                entry += "Buzz"
            if i%self.fizznumber != 0 and i%self.buzznumber != 0:
                entry = i
            return entry

        return [int_to_fizzbuzz(i) for i in range(start, end+1)]

if __name__ == "__main__":

    # Initialize constants and fb object
    start = 1
    end = 100
    fb = FizzBuzz(3,5)
    
    # Solve fb problem
    for i in fb.solve(start, end):
        print(i)