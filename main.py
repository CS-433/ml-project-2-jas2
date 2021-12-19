import blob_detection as bd
import os
import subprocess

data = "./data"

sample = "/sample_1850_to_1859"
clean = "/sample_clean"

di_raw = "/digitized_raw"
di_clean = "/digitized_clean"

def clean_data():

    # go through all folders that were digitized RAW
    for raw_folder in os.listdir(data + di_raw):
        # go through all images inside these folders
        src = data + sample + '/' + raw_folder
        dst = data + clean + '/' + raw_folder
        print(src, dst)
        if not os.path.exists(dst):
            os.mkdir(dst)

        for image in os.listdir(src):
            if "xml" not in image: # sample contains xml files
                bd.clear_image(image, src, dst)

def digitize(src, dst):
    for folder in os.listdir(src):
        if not os.path.exists(src + '/' + folder.name):
            os.mkdir(src + folder.name)

        # for each file
        for image in os.scandir(src + folder.name):

            if "xml" not in entry2.name: # sample contains xml files
                source = src + '/' + folder.name + '/' + image.name
                target = dst + '/' + folder.name + '/' + image.name[:-4]

                command = "tesseract " + source + ' ' + \
                     target + " --dpi 150 --psm 1"

                print("\n" + command)
                result = subprocess.run(command, stderr=subprocess.PIPE,\
                         stdout=subprocess.PIPE, shell=True)


### digitize sample
print("Digitizing sample...")
# digitize(data + sample, data + di_raw)

### clean data
print("Cleaning sample...")
clean_data()

### digitize cleaned data
print("Digitizing cleaned sample...")
# digitize(data + clean, data + di_clean)


print("Done !")
