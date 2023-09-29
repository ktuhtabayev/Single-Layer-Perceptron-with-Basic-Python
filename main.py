

print("Implementing Single Layer Perceptron Using Basic Python")

n = int(input("Set a number of inputs value: "))

threshold = float(input(f"Set a threshold value between range of {0} and {n}: "))
while threshold < 0 or threshold > n:
    threshold = float(input(f"Incorrect window of threshold value, enter again: "))

print("Enter binary inputs(0 or 1) and weights(between 0 and 1) values:")
inputs_list, weights_list = [], []
i = 0
while i < n:
    inputs = float(input(f'input[{i+1}] = '))
    while inputs != 0 and inputs != 1:
        inputs = float(input(f'input[{i+1}] = '))

    weights = float(input(f'weight[{i+1}] = '))
    while weights < 0 or weights > 1:
        weights = float(input(f'weight[{i+1}] = '))

    i += 1
    inputs_list.append(inputs)
    weights_list.append(weights)

print("Value of inputs:\t", inputs_list)
print("Value of weights:\t", weights_list)

sum = 0
for i in range(n):
    sum += inputs_list[i] * weights_list[i]

print("Sum =", sum)
print("\nWill I go to the concert?")

if sum > threshold:
    print("Yes")
else:
    print("No")
