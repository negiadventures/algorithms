def calc_edit_distance(input, output):
    matrix = list()
    for r in range(0, len(input)):
        matrix.append([0 for c in range(0, len(output))])
    for i in range(len(input)):
        matrix[i][0] = i
    for j in range(len(output)):
        matrix[0][j] = j
    for i in range(len(input)):
        for j in range(len(output)):
            matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + abs(i - j))
    return matrix[len(input) - 1][len(output) - 1]


if __name__ == '__main__':
    word_list = ['select', 'from', 'join', 'inner join', 'left join', 'right join', 'where', 'male', 'mail', 'malt']
    retry = True
    while (retry):
        print('Enter a word...')
        word = str(input())
        print('Enter fuzziness..')
        fuzziness = int(input())
        suggestions = []
        if word.lower() not in word_list:
            for w in word_list:
                if abs(len(word) - len(w)) <= fuzziness:
                    word_split = list(word)
                    w_split = list(w)
                    for x in w_split:
                        if x in word_split:
                            word_split.remove(x)
                    if len(word_split) < fuzziness:
                        if calc_edit_distance(word, w) <= fuzziness:
                            suggestions.append(w)
            if len(suggestions) == 0:
                print(word, 'doesn''t exists in the word list. Try increasing the fuzziness to see similar results.')
            else:
                print('Did you mean any of these?', suggestions)
        else:
            print(word, 'exists in the word list.')
        print('Do you want to continue? Press ''n'' for No, ''y'' for Yes.')
        retry = True if str(input()) == 'y' else False

        
        
#### EXAMPLE #####
# Enter a word...
# mald
# Enter fuzziness..
# 1
# mald doesnt exists in the word list. Try increasing the fuzziness to see similar results.
# Do you want to continue? Press n for No, y for Yes.
# y
# Enter a word...
# mald
# Enter fuzziness..
# 2
# Did you mean any of these? ['male', 'mail', 'malt']
# Do you want to continue? Press n for No, y for Yes.
# n
# Process finished with exit code 0
