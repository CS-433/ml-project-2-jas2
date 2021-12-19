import os
import subprocess
from multiprocessing import Pool

def digitize_folder(entry):
    sub_dst = dst + '/' + entry
    if not os.path.exists(sub_dst):
        os.mkdir(sub_dst)

        # for each file
        with os.scandir(src + '/' + entry) as ti:
            for entry2 in ti:

                if "xml" not in entry2.name:
                    source = src + '/' + entry + '/' + entry2.name
                    target = dst + '/' + entry + '/' + entry2.name[:-4]

                    command = "tesseract " + source + ' ' + \
                              target + " --dpi 150 --psm 1"

                    print("\n" + command)
                    result = subprocess.run(command, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
                    log.writelines(result.stderr.decode('utf-8'))
                    log.write('\n')



src = "sample_1850_to_1859"
dst = "dst"
dir_entry = os.listdir(src)

log = open('log.txt', 'w')
for entry in dir_entry:
    digitize_folder(entry)
log.close()

print("Done !")
