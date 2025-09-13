def greater_digit_sum(a:int,b:int)->int:
    def digit_sum(n:int)->int:
        return sum(int(d) for d in str(abs(n)))
    sum_a=digit_sum(a)
    sum_b=digit_sum(b)

    if sum_a>sum_b:
        return sum_a
    elif sum_b>sum_a:
        return sum_b
    else:
        return max(a,b)
    

print(greater_digit_sum(58,90))
