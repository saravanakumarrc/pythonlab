
def reverse(input):
    output = [0] * len(input)
    i = len(input) - 1;
    for x in range(0,len(input)):
        output[i] = input[x]
        i = i - 1
    return output

def reverse2(input):
    output = []
    for i in range(1,len(input)+1):
        output.append(input[i * -1])
    return output

print(reverse2([1,2,3,4,5]))




