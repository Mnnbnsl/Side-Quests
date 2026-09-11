#include<bits/stdc++.h>
using namespace std; 
#include"murmur.h"

static inline uint32_t murmur_32_scramble(uint32_t k) {
    k *= 0xcc9e2d51;
    k = (k << 15) | (k >> 17); // circular left shift by n = (x << n) | (x >> (32 - n)) 
    // k = rotl(k, 15) alternately
    k *= 0x1b873593;
    return k;
}

uint32_t murmur3_32(const uint8_t *key, size_t len, uint32_t seed) {
    // initializing h with seed
    uint32_t h = seed;
    uint32_t k;

    for (size_t i = len >> 2; i; i--) {
        // copying 4 bytes into k
        memcpy(&k, key, sizeof(uint32_t));
        key += sizeof(uint32_t);
        h ^= murmur_32_scramble(k);
        h = (h << 13) | (h >> 19);
        h = (h * 5) + 0xe6546b64;
    }

    // read the tail
    k = 0;
    for (size_t i = len & 3; i; i--) {
        k <<= 8;
        k |= key[i - 1];
    }

    h ^= murmur_32_scramble(k);

    // Avalanche effect
    h ^= len;
    h ^= h >> 16;
    h *= 0x85ebca6b;
    h ^= h >> 13;
    h *= 0xc2b2ae35;
    h ^= h >> 16;
    return h;
}

uint32_t hash_string(const string& s, uint32_t seed) {
    return murmur3_32(
        reinterpret_cast<const uint8_t*>(s.data()),
        s.size(),
        seed
    );
}
