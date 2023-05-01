import os
import os.path


def import_folder(path):
    dirs = os.listdir(path)
    data = {}
    if len(dirs) > 0:
        for d in dirs:
            data[d] = []
            for _, _, files in os.walk(os.path.join(path, d)):
                if len(files) > 0:
                    for f in files:
                        data[d].append(f)
    return data
