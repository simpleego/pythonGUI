def analyze_string(text):
    length = len(text)
    words = len(text.split())
    return length, words

input_text = input("문자열을 입력하시오: ")

result_length, result_words = analyze_string(input_text)

print(f"문자열 길이: {result_length}")
print(f"단어 개수: {result_words}")
