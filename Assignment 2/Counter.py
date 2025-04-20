# Vowel and Consonant Counter
def Count(text):
    stripped_text = ''.join(text.split())
    final_text = stripped_text.lower()
    vowel_counter = 0
    cons_counter = 0
    for ch in final_text:
        if ch in 'aeiou':
            vowel_counter += 1
        elif ch.isalpha():
            cons_counter += 1
    print("Vowels:", vowel_counter)
    print("Consonont: ",cons_counter)

Count("Hello, World!")