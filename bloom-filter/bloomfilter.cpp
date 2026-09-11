/*
    operations in a bloom filter : 
        insert(x)
        lookup(x)
    
        m - size of bit array
    k - number of hash functions 
    n - number of expected elements to be inserted

    prob_fp (P) = (1 - (1 - 1/m)^(kn))^k
        where 1/m is the prob of the particular bit being chosen to set,
        so (1 - 1/m) is the prob of bit not being chosen
        (1 - 1/m)^(kn) is prob of bit being unset after all insertions

    size of bit array (m) = -n * ln(P) / (ln(2))^2 , if we want a particular P only

    optimal number of hashes (k) = m/n * ln(2)

    we will use double hashing do generate k positions to map to.
    hash function used - Murmur hash 
*/

#include<bits/stdc++.h>
#include"murmur.h"
using namespace std; 
using ll = long long;

template<size_t M>
bool lookup(const bitset<M> &bitarray, const string &s, int k, int m) {
    uint32_t h1 = hash_string(s, 17);
    uint32_t h2 = hash_string(s, 37);

    for (int i = 1; i <= k; i++) {
        uint32_t hash = h1 + i * h2;
        hash = hash % m;

        if (bitarray.test(hash) == false) return false;
    }
    return true;
}

template<size_t M>
void insert(bitset<M> &bitarray, const string &s, int k, int m) {
    uint32_t h1 = hash_string(s, 17);
    uint32_t h2 = hash_string(s, 37);
    
    for (int i = 1; i <= k; i++) {
        uint32_t hash = h1 + i * h2;
        hash = hash % m;
        bitarray.set(hash);
    }

    cout << s << " added.\n";
}

