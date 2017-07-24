
clear_text = raw_input("text you want to encrypt: ")
key = raw_input("please set a key: ")
encrypt_strings = "abcdefghiklmnopqrstuvwxyz"

# Remove duplicate letters in key. (i and j are also 'the same')

# Add 'z' when letters in pair are the same letter.

crypt_list = key
for e in encrypt_strings:
    if e not in crypt_list:
        crypt_list += e

print "\ncrypt_list is: {0}".format(crypt_list)
crypt_matrix = [crypt_list[i*5:i*5+5] for i in range(5)]
print "\ncrypt_matrix is: {0}".format(crypt_matrix)

clear_text_words = clear_text.split(" ")
clear_text_letter_pairs = [[word[i:i+2] for i in range(0, len(word), 2)] for word in clear_text_words]
print "\nclear_text_words is: {0}".format(clear_text_words)
print "\nclear_text_letter_pairs is: {0}".format(clear_text_letter_pairs)

crypt_text_letter_pairs = clear_text_letter_pairs
for word in crypt_text_letter_pairs:
    for i in range(len(word)):
        letter_pair = word[i]
        la, lb = letter_pair[0], letter_pair[1]
        la_index, lb_index = crypt_list.find(la), crypt_list.find(lb)
        la_i, la_j = la_index / 5, la_index % 5
        lb_i, lb_j = lb_index / 5, lb_index % 5

        print "{0}'s index is ({1}, {2})".format(la, la_i, la_j)
        print "{0}'s index is ({1}, {2})".format(lb, lb_i, lb_j)

        if la_i == lb_i:
            word[i] = crypt_matrix[la_i][(la_j+1) % 5] + crypt_matrix[lb_i][(lb_j+1) % 5]
        elif la_j == lb_j:
            word[i] = crypt_matrix[(la_i+1) % 5][la_j] + crypt_matrix[(lb_i+1) % 5][lb_j]
        else:
            word[i] = crypt_matrix[la_i][lb_j] + crypt_matrix[lb_i][la_j]

print "\ncrypt_text_letter_pairs is:{0}".format(crypt_text_letter_pairs)
crypt_text_words = clear_text_words
for i in range(len(crypt_text_words)):
    letter_pairs = crypt_text_letter_pairs[i]
    crypt_text_words[i] = "".join(letter_pairs)

crypt_text = " ".join(crypt_text_words)
print "crypt_text is: {0}".format(crypt_text)