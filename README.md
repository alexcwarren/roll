# roll

A tiny Python command-line utility for simulating dice rolls.

Supports d4, d6, d8, d10, and d20 dice, and lets you roll multiple dice expressions in a single command.

## Install

Make sure [Python 3](https://www.python.org/downloads/) is installed, then download `roll.py`.

No additional runtime dependencies are required.

## Usage

Run the script from a terminal:

```shell
python roll.py <number of dice>d<die type>
```

For example:

```shell
python roll.py 2d20
```

Possible output:

```text
2d20:
9 16 = 25
```

This represents two d20 rolls: `9` and `16`, for a total of `25`.

You can pass multiple dice expressions at once:

```shell
python roll.py 1d20 3d6
```

Possible output:

```text
1d20:
14 = 14
3d6:
5 2 3 = 10
```

Supported die types:

- d4
- d6
- d8
- d10
- d20

Invalid or unsupported dice expressions display the command help instead of rolling.

## Development

Install the development dependency:

```shell
pip install -r requirements-dev.txt
```

Run the test suite:

```shell
pytest
```

## License

Licensed under the MIT License. See [`LICENSE`](LICENSE).
