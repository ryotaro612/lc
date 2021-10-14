#include "google/others/guess_the_word.cc"
#include <gtest/gtest.h>

TEST(guess_the_word, 1) {

    Solution s;
    vector<string> wordlist = {
        "wichbx", "oahwep", "tpulot", "eqznzs", "vvmplb", "eywinm", "dqefpt",
        "kmjmxr", "ihkovg", "trbzyb", "xqulhc", "bcsbfw", "rwzslk", "abpjhw",
        "mpubps", "viyzbc", "kodlta", "ckfzjh", "phuepp", "rokoro", "nxcwmo",
        "awvqlr", "uooeon", "hhfuzz", "sajxgr", "oxgaix", "fnugyu", "lkxwru",
        "mhtrvb", "xxonmg", "tqxlbr", "euxtzg", "tjwvad", "uslult", "rtjosi",
        "hsygda", "vyuica", "mbnagm", "uinqur", "pikenp", "szgupv", "qpxmsw",
        "vunxdn", "jahhfn", "kmbeok", "biywow", "yvgwho", "hwzodo", "loffxk",
        "xavzqd", "vwzpfe", "uairjw", "itufkt", "kaklud", "jjinfa", "kqbttl",
        "zocgux", "ucwjig", "meesxb", "uysfyc", "kdfvtw", "vizxrv", "rpbdjh",
        "wynohw", "lhqxvx", "kaadty", "dxxwut", "vjtskm", "yrdswc", "byzjxm",
        "jeomdc", "saevda", "himevi", "ydltnu", "wrrpoc", "khuopg", "ooxarg",
        "vcvfry", "thaawc", "bssybb", "ccoyyo", "ajcwbj", "arwfnl", "nafmtm",
        "xoaumd", "vbejda", "kaefne", "swcrkh", "reeyhj", "vmcwaf", "chxitv",
        "qkwjna", "vklpkp", "xfnayl", "ktgmfn", "xrmzzm", "fgtuki", "zcffuv",
        "srxuus", "pydgmq"};
    Master m("ccoyyo", wordlist);
    s.findSecretWord(wordlist, m);
    EXPECT_TRUE(m.is_ok());
}