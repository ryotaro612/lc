#include "google/design/lru_cache.cc"
#include <gtest/gtest.h>
TEST(lru_cache, 1) {
    LRUCache s(2);
    s.put(1, 1);
    s.put(2, 2);
    EXPECT_EQ(1, s.get(1));
    s.put(3, 3);
    EXPECT_EQ(-1, s.get(2));
    s.put(4, 4);
    EXPECT_EQ(-1, s.get(1));
    EXPECT_EQ(3, s.get(3));
    EXPECT_EQ(4, s.get(4));
}
TEST(lru_cache, 2) {
    LRUCache s(3);
    s.put(1, 1);
    s.put(2, 2);
    s.put(3, 3);
    s.put(4, 4);
    EXPECT_EQ(4, s.get(4));
    EXPECT_EQ(3, s.get(3));
    EXPECT_EQ(2, s.get(2));
    EXPECT_EQ(-1, s.get(1));
    s.put(5, 5);
    EXPECT_EQ(-1, s.get(1));
    EXPECT_EQ(2, s.get(2));
    EXPECT_EQ(3, s.get(3));
    EXPECT_EQ(-1, s.get(4));
    EXPECT_EQ(5, s.get(5));
}