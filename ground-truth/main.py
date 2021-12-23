import os
import subprocess
from multiprocessing import Pool
import text_distances as td
import blob_detection as bd

def split():
    size = len(os.listdir(clean))
    for f in os.listdir(clean)[:int(size/3)]:
        c = "mv " + clean + '/' + f + " " + data + \
                '/' + "toGoogle" + '/' + f
        print(c)
        os.system(c)


def loop(raw_folder):
    # go through all images inside these folders
    src = "../"+ sample + '/' + raw_folder
    dst = "di_clean" + '/' + raw_folder
    print(src, dst)
    if not os.path.exists(dst):
        os.mkdir(dst)

    for image in os.listdir(src):
        if "xml" not in image: # sample contains xml files
            # in case of unexpected interruption
            if not os.path.exists(dst + '/' + image):
                bd.clear_image(image, src, dst)

def clean_data():

    pool = Pool(3)
    results = pool.map(loop, os.listdir("di_raw"))

def digitize(src, dst):
    for folder in os.listdir(src):
        src_path = src + '/' + folder
        dst_path = dst + '/' + folder
        if not os.path.exists(dst_path):
            print("creating folder")
            os.mkdir(dst_path)

        # for each file
        for image in os.listdir(src + '/' + folder):

            if "xml" not in image: # sample contains xml files
                source = src_path + '/' + image
                target = dst_path + '/' + image[:-4]

                if not os.path.exists(target + ".txt"):

                    command = "tesseract " + source + ' ' + \
                            target + " --dpi 150 --psm 1"
                    print("\n" + command)
                    os.system(command)

def distances():
    dists = data + "distances.txt"
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



### digitize sample
print("Digitizing sample...")
# digitize(sample, di_raw)

### clean data
print("Cleaning digitized sample...")
#clean_data()

### digitize cleaned data
print("Digitizing cleaned sample...")
#digitize("clean", "di_clean")

### compute distances
#distances()

### compute errors
td.computeAllErrors()

print("Done !")
