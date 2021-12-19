
def file_name_to_voc(file_name):
    f = open(file_name, 'r')
    txt = f.read()
    f.close()
    return txt.split()

def jaccard(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    intersection = s1 & s2
    union = s1 | s2
    return len(intersection) / len(union)


# main function
def vocab_distance(file_name1, file_name2):
    voc1 = file_name_to_voc(file_name1)
    voc2 = file_name_to_voc(file_name2)

    jacc_vocab = jaccard(voc1, voc2)

    voc1_pos = [(w, i) for i, w in enumerate(voc1)]
    voc2_pos = [(w, i) for i, w in enumerate(voc2)]

    jacc_vocab_pos = jaccard(voc1_pos, voc2_pos)

    return jacc_vocab, jacc_vocab_pos
