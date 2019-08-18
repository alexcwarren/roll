# roll
Simulate rolling one or more different types of dice (e.g. d4's, d6's, d8's, d10's, and d20's).

## Install
Assuming you have Python 3 already installed, download `roll.py`.

## Usage
From the directory you downloaded `roll.py`, execute the script:
```
python roll.py <number of dice>d<die type>
```
e.g.
```
python roll.py 2d20
```
The output could look something like this:
```
2d20:
9 16 = 25
```
What the above output implies is that you rolled two d20 dice: a 9 for the first d20 and a 16 for the second d20 where their sum is 25.

You can pass as many dice arguments as you like.
For example:
```
python roll.py 1d20 3d6
```
Possible output:
```
1d20:
14 = 14
3d6:
5 2 3 = 10
```
