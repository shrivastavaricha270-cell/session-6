def normalize(text):
    return " ".join(text.lower().split())

def count_words(text):
    return len(normalize(text).split())

sample = input("Enter text: ")
print("Normalized:", normalize(sample))
print("Word count:", count_words(sample))
