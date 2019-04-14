# Sequences

Positionally ordered collection of other objects. Left to right order.

# Strings

Strings are one sequences of one-character strings.

## Sequence operations

* indexing expression: `s[0]` (zero-based)
* index backwards: `s[-1]` (last item)
* slicing
  * `s[1:3]`: chars 1 to 2
print("Copy is not the original" + str(message is message[:]))

  * `s[1:]`: char 1 to the end
  * `s[:-1]`: everything but the last character
  * `s[:]`: full string
* concatenation: using `+`
* repetition: using `*`

## String-specific operations

* find: `s.find('foo')`
* replace: `s.replace('foo', 'bar')`
* upper: `s.upper()`
* lower: `s.lower()`
* split: `s.split(',')`
* digits only?: `s.isdigit()`
* alphanum?: `s.isalpha()`
* strip right: `s.rstrip()`
* capitalize: `s.capitalize()`
