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
    if(len(union) > 0):
        return (len(intersection) / len(union))
    else:
        return 1


def vocab_distance(file_name1, file_name2):
    voc1 = file_name_to_voc(file_name1)
    voc2 = file_name_to_voc(file_name2)

    jacc_vocab = jaccard(voc1, voc2)

    old_voc1 = voc1.copy()
    voc1.insert(0, "0")
    voc1_pos = list(zip(voc1, old_voc1))

    old_voc2 = voc2.copy()
    voc2.insert(0, "0")
    voc2_pos = list(zip(voc2, old_voc2))

    jacc_vocab_pos = jaccard(voc1_pos, voc2_pos)

    return jacc_vocab, jacc_vocab_pos

def errors(file_name, truth_file):
    voc = file_name_to_voc(file_name)
    voc_truth = file_name_to_voc(truth_file)

    s = set(voc)
    s_truth = set(voc_truth)

    errors = s - s_truth
    true_vals = s_truth - s

    return errors, true_vals
