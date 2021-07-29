# File integrity checker

This script will help you to check integrity of your files.<br>
**Only `MD5` and `SHA1` encryption algorithms are supported.**<br>

The program will indicate the checking status with each filename. There are the following states:<br>
- `OK` - hash amounts match
- `FAIL` - hash amounts are different
- `NOT FOUND` - the file could not be found
- `ERROR` - an error occurred

## Run via console

To launch the script specify *file with hashes* and *folder with files to check*.<br>

### Hashes file structure
`<filename> <algorythm> <hash>`<br>

Example:
```
file_01.bin md5 d41d8cd98f00b204e9800998ecf8427e
file_02.bin md5 e4942b384074c211c1e097e3090834f1
file_06.txt sha1 e4942b384074c211c1e097e3090834f1
```

### Program launch structure:

`python <path to the program file> <path to the input file> <path to the directory containing the files to check>`<br>

Example:
```sh
$ python nurse.py hashes.txt files
```

Result:
```sh
>>> file_01.bin OK
>>> file_02.bin FAIL
>>> file_03.bin ERROR
>>> file_04.txt OK
>>> Unknown algorithm for file "files\file_05.txt" sha256, allowed types: md5, sha1
>>> file_05.txt ERROR
>>> file_06.txt NOT FOUND
```
