from collections import Counter
import os

def file_name_to_voc(file_name):
    f = open(file_name, 'r')
    txt = f.read()
    f.close()
    return txt.split()

def jaccard(l1, l2):
    s1 = Counter(l1)
    s2 = Counter(l2)
    intersection = list((s1 & s2).elements())
    union = list((s1 | s2).elements())
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

    s = Counter(voc)
    s_truth = Counter(voc_truth)

    errors = s - s_truth
    true_vals = s_truth - s

    return list(errors.elements()), list(true_vals.elements())

def computeAllErrors(GT="ground_truth", di_clean="di_clean", di_raw="di_raw"):
    """
    Get values to compare distances to a ground truth between raw and cleaned
    data
    """

    def errorsAndWrite(path, GT):
        return errors(path, GT)


    f = open("results.txt", "w")

    ce = []
    ct = []
    re = []
    rt = []
    for folder in os.listdir(GT):
        for txt in os.listdir(GT + '/' + folder):

            path = GT + '/' + folder + '/' + txt
            clean_path = di_clean + '/' + folder + '/' + txt
            raw_path = di_raw + '/' + folder + '/' + txt

            tce, tct = errorsAndWrite(clean_path, path)
            tre, trt = errorsAndWrite(raw_path, path)

            ce += tce
            ct += tct
            re += tre
            rt += trt

    for x in ce:
        f.write(x + ' ')
    f.write('\n')
    for x in ct:
        f.write(x + ' ')
    f.write('\n')
    for x in re:
        f.write(x + ' ')
    f.write('\n')
    for x in rt:
        f.write(x + ' ')
    f.write('\n')

    f.close()

def distances():
    f = open("dists.txt", "w")
    di_raw = "di_raw"
    di_clean = "di_clean"
    for folder in os.listdir(di_raw):
        for image in os.listdir(di_raw + '/' + folder):
            t1 = di_raw + '/' + folder +'/'+ image
            t2 = di_clean + '/' + folder +'/'+ image
            print(t1)
            print(t2)
            if os.path.exists(t2):
                jacc_vocab, jacc_vocab_pos = vocab_distance(t1, t2)
                f.write(folder + '/' + image + ' ')
                f.write(str(jacc_vocab) + ' ' + str(jacc_vocab_pos))
                f.write("\n")
    f.close()
