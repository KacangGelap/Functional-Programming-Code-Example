def is_prime(number):
    if number < 2:
        return False
    return all(number % i != 0 for i in range(2, number))
def find_primes(numbers):
    return [is_prime(num) for num in numbers]


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    primes = find_primes(numbers)
    print(primes)
