# Merges two directories.
# If dest does not contain source file, just moves it over.
# If dest does contain source file, then renames dest file to .old[n] extension and then moves file over
# If two files are identical, then just moves file over, overwriting the dest file

import sys, os, filecmp, pathlib

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 mergedir.py src_dir dst_dir")
        sys.exit()

    src_dir = sys.argv[1]
    dst_dir = sys.argv[2]

    # very important to normalize the paths
    src_dir = os.path.normpath(src_dir) + "/"
    dst_dir = os.path.normpath(dst_dir) + "/"
    print("src:", src_dir)
    print("dst:", dst_dir)

    # try to move over every file in src_dir
    for path, dirnames, filenames in os.walk(src_dir):
        for filename in filenames:
            path_equiv_at_dst = dst_dir + path[len(src_dir):]
            full_src_filepath = os.path.join(path, filename)
            full_dst_filepath = os.path.join(path_equiv_at_dst, filename)
            # if destination path doesn't exist, move over the file
            # check if it exists (yes, there is a race here, so only use this if you're sure no other program is accessing the directory)
            if not os.path.exists(full_dst_filepath):
                dirpart = os.path.dirname(full_dst_filepath)
                os.makedirs(dirpart, exist_ok=True)
                os.rename(full_src_filepath, full_dst_filepath)
            else: # It exists, so we may have to rename it.
                # Check if two files are identical
                if filecmp.cmp(full_src_filepath, full_dst_filepath):
                    # they are identical, so just overwrite
                    os.rename(full_src_filepath, full_dst_filepath)
                else:
                    # not identical, so rename old file to something different
                    i = 0
                    while True:
                        i += 1
                        new_name= full_dst_filepath+".old"+str(i)
                        # check if filename exists
                        if not os.path.exists(new_name):
                            os.rename(full_dst_filepath, new_name)
                            os.rename(full_src_filepath, full_dst_filepath)
                            break



