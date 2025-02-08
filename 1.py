# #1
# def g_to_o(grams):
#     print(28.3495231 * grams, "ounces")

# x = int(input())
# g_to_o(x)

# #2
# def F_to_C(temperature):
#     print("C = ", (5 / 9) * (temperature - 32))

# x = int(input())
# F_to_C(x)

# #3
# print(10 // 2)
# print(10 % 3)

#Ex 4
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(list):
    result = []
    for num in list:
        if is_prime(num):
            result.append(num)
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_prime(numbers)

print(result)


fsdkjfhlweuhfiu
dofhsijdhfouihdf
sdofhjsiudhfiusdhf
sdhfuishdfyg

def imdb_more_than_5_2(movie):
    return movie.get("imdb", 0) > 5.5

list = [movie for movie in movies if imdb_more_than_5_2(movie)]

for movie in list:
    print(f"{movie['name']} {movie['imdb'] } {movie['category']}")
