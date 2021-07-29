import sys
import traceback
import os.path
import hashlib

def main(hashes):
    for h in hashes:
        try:
            wet_row = h.strip().split(' ')
            file_info = struct(*wet_row)
            result =  compare_hashes(file_info)

            print(f"{wet_row[0]} {result}")

        except Exception:
            print(f"{wet_row[0]} ERROR")

def compare_hashes(struct):

    BUF_SIZE = 65536 # 64Kb block size

    filename = struct['filename']
    alg = struct['algorythm'].lower()
    old_hash = struct['hash']
    
    if not os.path.exists(filename):
        return "NOT FOUND"

    if alg == 'md5':
        cypher = hashlib.md5()
    elif alg == 'sha1':
        cypher = hashlib.sha1()
    else:
        print(f"Unknown algorithm for file \"{filename}\" {alg}, allowed types: md5, sha1")
        return "ERROR"

    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            cypher.update(data)

    new_hash = cypher.hexdigest()
    if old_hash == new_hash:
        return "OK"
    else:
        return "FAIL"

def struct(filename, algorythm, hash):
    return {
        "filename": os.path.join(folder_path, filename),
        "algorythm": algorythm,
        "hash": hash,
    }

def read_hashes(filepath):
    with open(filepath, 'r') as file:
        return file.readlines()

def file_exist(filepath):
    if not os.path.exists(filepath):
        raise FileExistsError(f"File \"{filepath}\" not found")
    else:
        return True

def check_args(args: list):
    try:
        args_count_got = len(args)
        args_count_expect = 3

        assert args_count_got == args_count_expect

    except AssertionError:
        traceback.print_exc()
        print(f"Wrong args count, got {args_count_got}, expected {args_count_expect}, {args}")

        exit()

if __name__ == "__main__":
    program_args = sys.argv
    check_args(program_args)

    hases_path = program_args[1]
    folder_path = program_args[2]

    file_exist(hases_path)
    file_exist(folder_path)

    hashes = read_hashes(hases_path)

    main(hashes)
