# Bloom Filter

A basic implementation of a Bloom Filter, a probabilistic data structure used for efficient membership testing.

A Bloom Filter consists of a bit array of size m and uses k hash functions to map each inserted element to multiple positions in the array.

## Operations
- insert(x) — hashes an element and sets the corresponding bits.
- lookup(x) — checks the corresponding bits to determine whether an element is possibly present.

A Bloom Filter has an important property:

If lookup(x) returns false, the element is definitely not present.
If lookup(x) returns true, the element is possibly present.

This means Bloom Filters can have false positives, but they do not have false negatives (assuming elements are only inserted and not deleted).

## Parameters
m — size of the bit array
k — number of hash functions
n — expected number of elements to be inserted
P — desired false-positive probability

The approximate false-positive probability is:

$$
P = \left(1-\left(1-\frac{1}{m}\right)^{kn}\right)^k
$$

Here, 1/m is the probability of selecting a particular bit when hashing an element. Therefore,

$$
\left(1-\frac{1}{m}\right)^{kn}
$$

represents the probability that a particular bit remains unset after all n insertions using k hash functions.

For a desired false-positive probability P, the required bit-array size can be approximated by:

$$
m = \frac{-n\ln(P)}{(\ln 2)^2}
$$

The optimal number of hash functions is:

$$
k = \frac{m}{n}\ln 2
$$

## Hashing

The implementation uses MurmurHash3 as the underlying hash function.

Instead of maintaining k completely independent hash functions, double hashing is used to generate the k positions:

$$
h_i(x) = h_1(x) + i \cdot h_2(x)
$$

The resulting hash values are mapped to positions in the bit array using modulo m.

## Implementation

Current Bloom Filter implementation uses:

- std::bitset as the bit array
- MurmurHash3 for hashing
- Double hashing for generating multiple hash positions
- Configurable m and k
- insert() and lookup() operations