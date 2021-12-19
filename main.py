import os
import subprocess
import text_distances as td
import blob_detection as bd

data = "./data"

sample = data + "/sample_1850_to_1859"
clean = data +"/sample_clean"

di_raw = data +"/digitized_raw"
di_clean = data +"/digitized_clean"

distances = data + "distances.txt"

def clean_data():

    # go through all folders that were digitized RAW
    for raw_folder in os.listdir(di_raw):
        # go through all images inside these folders
        src = sample + '/' + raw_folder
        dst = clean + '/' + raw_folder
        print(src, dst)
        if not os.path.exists(dst):
            os.mkdir(dst)

        for image in os.listdir(src):
            if "xml" not in image: # sample contains xml files
                # in case of unexpected interruption
                if not os.path.exists(dst + '/' + image):
                    bd.clear_image(image, src, dst)

def digitize(src, dst):
    for folder in os.listdir(src):
        if not os.path.exists(src + '/' + folder):
            os.mkdir(src + folder)

        # for each file
        for image in os.scandir(src + folder):

            if "xml" not in entry2.name: # sample contains xml files
                source = src + '/' + folder + '/' + image
                target = dst + '/' + folder + '/' + image[:-4]

                command = "tesseract " + source + ' ' + \
                     target + " --dpi 150 --psm 1"

                print("\n" + command)
                result = subprocess.run(command, stderr=subprocess.PIPE,\
                         stdout=subprocess.PIPE, shell=True)

def distances():
    f = open(distances, "w")
    for folder in os.listdir(di_raw):
        for image in os.listdir(di_raw + '/' + folder):
            t1 = di_raw + '/' + folder + image
            t1 = di_clean + '/' + folder + image
            f.write(folder + ' ')
            f.write(vocab_distance(t1, t2))
            f.write("\n")
    f.close()


### digitize sample
print("Digitizing sample...")
# digitize(sample, di_raw)

### clean data
print("Cleaning digitized sample...")
clean_data()

### digitize cleaned data
print("Digitizing cleaned sample...")
# digitize(clean, di_clean)

### compute distances
# distances()


print("Done !")
