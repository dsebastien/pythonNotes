# Virtual environments

## Virtual what?

Virtual environments isolate a full python installation along with all the dependencies etc.
A virtual environment also includes the python binaries and core libraries!

## Why?

Avoid global installations and side-effects of dependencies and transitive dependencies. Increase build stability/reproductibility.


## Example

`python3 -m venv foo`

This will create a virtual environment called `foo` in a sub-folder.

To enable a virtual environment