def solution(numbers):
    new_numbers=list(map(str, numbers))
    new_keys= []
    def x4nums(x):
        h= x*4
        return h[:4]
        
    
    new_numbers.sort(key= x4nums, reverse= True)
    return str(int(''.join(new_numbers)))