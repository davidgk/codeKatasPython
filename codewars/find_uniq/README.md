# definition of FIND_UNIQ


## description
There is an array with some numbers. All numbers are equal except for one. Try to find it!

## Codewars link

This is the [link](https://www.codewars.com/kata/585d7d5adb20cf33cb000235/train/python)


## Examples

```text
    find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
    find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
    test.assert_equals(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
    test.assert_equals(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
    test.assert_equals(find_uniq([ 3, 10, 3, 3, 3 ]), 10)
```

It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
