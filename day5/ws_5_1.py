# 아래 함수를 수정하시오.
def reverse_string(input_str):
    rev = ''.join(reversed(input_str))
    return rev

result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
