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


def distances():
    f = open(dists, "w")
    for folder in os.listdir(di_raw):
        for image in os.listdir(di_raw + '/' + folder):
            t1 = di_raw + '/' + folder +'/'+ image
            t2 = di_clean + '/' + folder +'/'+ image
            print(t1)
            print(t2)
            if os.path.exists(t2):
                jacc_vocab, jacc_vocab_pos = td.vocab_distance(t1, t2)
                f.write(folder + '/' + image + ' ')
                f.write(str(jacc_vocab) + ' ' + str(jacc_vocab_pos))
                f.write("\n")
    f.close()
