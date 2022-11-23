

def words_sorting(*args):
    word_dict = {}
    total_sum = 0

    for word in args:
        current_sum = 0
        for ch in word:
            current_sum += ord(ch)

        word_dict[word] = current_sum
        total_sum += current_sum

    final_dict = {}

    if total_sum % 2 == 0:
        for key, value in sorted(word_dict.items(), key=lambda kvpt:kvpt[0]):
            final_dict[key] = value
    else:
        for key, value in sorted(word_dict.items(), key=lambda kvpt: -kvpt[1]):
            final_dict[key] = value

    result = ""

    for ky, vl in final_dict.items():
        result += f"{ky} - {vl}\n"

    return result

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))

