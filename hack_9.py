"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    final_result = []

    i = 0
    while i < len(result):
        final_result.append(result[i])
        final_result.append('@')
        i += 1
    return final_result  
