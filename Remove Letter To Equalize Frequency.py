

def equalFrequency(word: str) -> bool:


    letter_list = list(set([letter for letter in word]))

    counted_letter = []
    for unique_letter in letter_list:
        counted_letter.append(word.count(unique_letter))


    res = False
    for i in range(len(counted_letter)):
        minus_counted_letter = counted_letter.copy()
        minus_counted_letter[i] = minus_counted_letter[i] - 1

        if 0 in minus_counted_letter:
            minus_counted_letter.remove(0)

        if min(minus_counted_letter) == max(minus_counted_letter):
            res = True


    return res


word = "aaaa"
print(equalFrequency(word))