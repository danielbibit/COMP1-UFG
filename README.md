# COMP1-UFG
Compiler for the MGol language, produced in the compilers 1 class

## How this project is organized
```
compiler/
├─ lexical/
├─ semantic/
├─ syntax/
docs/
├─ requirements/
│  ├─ T1/
│  ├─ T2/
│  ├─ T3/
tests/
├─ resources/
│  ├─ valid_source.mgol
│  ├─ invalid_source.mgol
├─ T1_run.py
├─ T2_run.py
├─ test_lexical.py
├─ test_semantic.py
├─ test_syntax.py
```
### compiler
main package, contains sub-packages dividing the compiler into 'lexical', 'semantic' and 'syntax'
packages. All the source code is located here.

### docs
Contains the project requirements and documentation/study material for parts of the code, like the
automaton used in the lexical analyser.

### tests
This directory contains the unit tests and the derivables to T1 and T2 parts of the project.

The directory resources contains the files that are used in the unit tests and T1 and T2.

Files that begin with 'test' are unit test files. See the end of this file to see how to run them.

## How to run T1, T2 and T3
This class is separeted in three small projects, the totality is the final compiler
for the mgol language, to run parts of the compiler, use these files, they contain only what was
requested on the requirement document:

### T1
From the project root, run on a terminal:
```bash
python3 tests/T1_run.py
```
### T2
*TBD*
### T3
*TBD*

## How to run unit tests
From the project root, run:
```bash
python3 -m unittest -v tests/test_name.py
```
