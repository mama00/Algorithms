def calculate(a,b,c):
    if a==b:
        return
    if a<b:
        if a*c<=b:
            return calculate(a*c,b,c) + 1
        else:
            n_if_mul=int((a*c-b)/2) +(a*c-b) % 2 + 1
            closest_to_b=int(b/c) if int(b/c)==b/c else int(b/c)+1
            number_retract=int((a-closest_to_b)/2) + (a-closest_to_b) % 2
            number_retract_after=int((closest_to_b*c-b)/2) + (closest_to_b*c-b) % 2
            return number_retract+number_retract_after+1

            


    else:
        return int((a-b)/2) + (a-b) % 2

number_test=int(input())
n=[0]
for i in range(number_test):
    a,b,c=map(int,input().split())
    print(calculate(a,b,c))
