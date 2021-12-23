import os
import subprocess
from multiprocessing import Pool
import text_distances as td
import blob_detection as bd

data = "./data"

sample = data + "/sample_1850_to_1859"
clean = data +"/sample_clean"

di_raw = data +"/digitized_raw"
di_clean = data +"/digitized_clean"

dists = data + "distances.txt"


def split():
    """
    Split cleaned samples in order to compute on Google Colab as well as in
    remote
    """
    size = len(os.listdir(clean))
    for f in os.listdir(clean)[:int(size/3)]:
        c = "mv " + clean + '/' + f + " " + data + \
                '/' + "split" + '/' + f
        print(c)
        os.system(c)


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




### digitize sample
print("Digitizing sample...")
# digitize(sample, di_raw)

### clean data
print("Cleaning digitized sample...")
#bd.clean_data()

### digitize cleaned data
print("Digitizing cleaned sample...")
#digitize(clean, di_clean)

### compute distances
#td.distances()

### split data
#split()


print("Done !")
