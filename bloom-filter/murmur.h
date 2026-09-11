#ifndef MURMUR_H
#define MURMUR_H

#include <cstdint>
#include <cstddef>

uint32_t murmur3_32(const uint8_t *key, size_t len, uint32_t seed);
uint32_t hash_string(const std::string& s, uint32_t seed);

#endif // MURMUR_H