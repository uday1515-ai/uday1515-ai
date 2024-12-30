class Assignment:
    def find_maximum(self, a, b, c):
        return max(a, b, c)
    def find_largest(self, numbers):
        if not numbers:  
            return None
        largest = numbers[0]
        for number in numbers:
            if number > largest:
                largest = number
        return largest
    def linear_search(self, arr, target):
        for index, value in enumerate(arr):
            if value == target:
                return index 
        return -1 
    def factorial(self, n):
        if n < 0:
            return None  
        if n == 0 or n == 1:
            return 1
        return n * self.factorial(n - 1)
    def is_prime(self, number):
        if number <= 1:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True
assignment = Assignment()
print("Maximum:", assignment.find_maximum(10, 20, 30))
print("Largest:", assignment.find_largest([10, 100, 30, 40, 50]))
print("Linear Search (Index):", assignment.linear_search([10, 100, 30, 40, 50], 30))
print("Factorial:", assignment.factorial(5))
print("Is Prime:", assignment.is_prime(5))