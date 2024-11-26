## Dataset
[[Test Dataset]](https://ihtc2024.github.io/assets/files/ihtc2024_test_dataset.zip)

[[Solution Dataset]](https://ihtc2024.github.io/assets/files/ihtc2024_test_solutions.zip)


## Validator
The validator that certifies the quality of a given solution is provided as [a C++ source code](https://github.com/ihtc2024/ihtc2024.github.io/blob/main/assets/files/IHTP_Validator.cc)  and should be compiled using, for example, the GNU compiler g++. The compilation requires that file [`json.hpp`](https://github.com/nlohmann/json/blob/develop/single_include/nlohmann/json.hpp) is in the path. The validator receives as command line parameters the instance and the solution files, as shown in the following example:

`./IHTP_Validator.exe test01.json sol_test01.json`

To get additional details on constraint violations and individual objectives, the keyword `verbose` can be added as a third parameter

### Compile IHTP_Validator
Sadly for Windows users, I use ubuntu for compile `IHTP_Validator.cc`. To compile a `.cc` file in Ubuntu, you can use the `g++` compiler, which is part of the GNU Compiler Collection (GCC) and specifically handles C++ files. Here are the steps to compile your `IHTP_Validator.cc` file:

1. Install g++:
```
sudo apt update
sudo apt install g++
```
2. Navigate to the File's Directory:
```
cd /path/to/your/file

```
3. Compile the file:
```
g++ -o IHTP_Validator.exe IHTP_Validator.cc

```
4. Run the compile:
```
./IHTP_Validator.exe
```
