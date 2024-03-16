def words_comparer(w1, w2):
    # if len(w1) != len(w2):
    #     return False
    for i in range(len(w1)):
        if len(w2) <= i:
            return 1
        if ord(w1[i]) > ord(w2[i]):
            return 1
        if ord(w1[i]) < ord(w2[i]):
            return -1
    if len(w1) < len(w2):
        return -1
    return 0


def bin_founder(a_list, word):
    beg = 0
    fin = len(a_list) - 1
    while beg <= fin:
        mid = (fin + beg) // 2
        if words_comparer(a_list[mid], word) == 0:
            print("We found it!!!")
            return
        if words_comparer(a_list[mid], word) == -1:
            beg = mid + 1
        else:
            fin = mid - 1
    print("We didn't find it((9")


word_list = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx']
bin_founder(word_list, 'abc')
bin_founder(word_list, 'def')
bin_founder(word_list, 'ghi')
bin_founder(word_list, 'jkl')
bin_founder(word_list, 'mno')
bin_founder(word_list, 'pqr')
bin_founder(word_list, 'stu')
bin_founder(word_list, 'vwx')
bin_founder(word_list, 'abd')
bin_founder(word_list, 'abcd')
bin_founder(word_list, 'ab')
