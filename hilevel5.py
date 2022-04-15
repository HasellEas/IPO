from ast import literal_eval

kortej = literal_eval(input())

maximal = max(kortej)
minimal = min(kortej)

output = '('

for num in kortej:
    if num == maximal:
        output+=str(minimal)
    elif num == minimal:
        output+=str(maximal)
    else:
        output+=str(num)
    output+=','

output = output[0:-1] + ')'

print(output)