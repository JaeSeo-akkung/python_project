#print("Hello, World!")

def add(a, b):
  
    result = a * b

    if result >= 9:
        #9보다 크거나 같으면 결과에서 9를 뺀다
        result = result - 9
    else:
        #9보다 작으면 결과를 그대로 반환
        pass

    return result
