# Lu Xun corpus (DHG508 Assignment 2, Part 1)

Digitised plain-text corpus of **Lu Xun (周树人, 1881-1936)**, prepared for a RAG
(retrieval-augmented generation) chat application: 54 books, about 4.33 million
characters (3.53 million Chinese characters), one .txt file per book.

## Structure

    LuXun_works/            32 books written by Lu Xun himself
    Writings_about_LuXun/   22 books about him by other authors

**LuXun_works** - fiction (Na Han, Pang Huang, Gu Shi Xin Bian), prose poetry and essays
(Ye Cao, Zhao Hua Xi Shi), the sixteen zawen collections (Fen, Re Feng, Hua Gai Ji, Er Yi Ji,
San Xian Ji, Er Xin Ji, Wei Zi You Shu, Nan Qiang Bei Diao Ji, Zhun Feng Yue Tan, Hua Bian Wen Xue,
Qie Jie Ting Za Wen I-III, Ji Wai Ji I-II), the letters Liang Di Shu, and the scholarly and
editorial works (Zhongguo Xiao Shuo Shi Lue, Han Wen Xue Shi Gang Yao, Gu Xiao Shuo Gou Chen,
Tang Song Chuan Qi Ji, Xiao Shuo Jiu Wen Chao, Ji Kang Ji, Hui Ji Jun Gu Shu Za Ji,
Gu Ji Xu Ba Ji, Yi Wen Xu Ba Ji).

**Writings_about_LuXun** - memoirs and biographies by Xu Shoushang, Xu Guangping, Zhou Zuoren,
Wang Yeqiu, Sun Fuyuan, Jing Youlin, Xiao Hong, Lin Chen, Ping Xin, Xue Wei and Zhou Guanwu,
plus the biographies by Komada Takeo (trans. Fan Quan) and Zheng Xuejia.

## Format

Plain text, UTF-8 without BOM, LF line endings, one book per file. Each file opens with a header
giving the book title, author, first edition, source URL and character count; chapters inside a
file are separated by a rule line, so any chunk can be cited back to a specific book and chapter.

## Source and processing

All texts were taken from the public full-text collection of the Lu Xun Library
(https://luxunlib.com), which reproduces proofread printed editions; the first-edition details in
each header come from that catalogue. Processing was limited to HTML-to-text conversion and removal
of site navigation - no wording was altered.

Lu Xun died in 1936, so his works are in the public domain (life + 50 years in mainland China and
Taiwan); the memoirs by Xu Shoushang, Xu Guangping and the other authors are likewise out of
copyright.

## Contents

### LuXun_works (32 books, 2,629,782 characters)

| File | Title | Author | First edition | Characters |
|---|---|---|---|---|
| 01_呐喊.txt | 呐喊 | 鲁迅 | 1923年8月 | 72,081 |
| 02_彷徨.txt | 彷徨 | 鲁迅 | 1926年8月 | 74,009 |
| 03_故事新编.txt | 故事新编 | 鲁迅 | 1936年1月 | 57,431 |
| 04_野草.txt | 野草 | 鲁迅 | 1927年7月 | 21,086 |
| 05_朝花夕拾.txt | 朝花夕拾 | 鲁迅 | 1928年9月 | 41,843 |
| 06_坟.txt | 坟 | 鲁迅 | 1927年3月 | 114,726 |
| 07_热风.txt | 热风 | 鲁迅 | 1925年11月 | 36,274 |
| 08_华盖集.txt | 华盖集 | 鲁迅 | 1926年6月 | 60,332 |
| 09_华盖集续编.txt | 华盖集续编 | 鲁迅 | 1927年5月 | 77,364 |
| 10_而已集.txt | 而已集 | 鲁迅 | 1928年10月 | 62,517 |
| 11_三闲集.txt | 三闲集 | 鲁迅 | 1932年9月 | 63,806 |
| 12_二心集.txt | 二心集 | 鲁迅 | 1932年10月 | 87,829 |
| 13_伪自由书.txt | 伪自由书 | 鲁迅 | 1933年10月 | 61,966 |
| 14_南腔北调集.txt | 南腔北调集 | 鲁迅 | 1934年3月 | 78,280 |
| 15_准风月谈.txt | 准风月谈 | 鲁迅 | 1934年12月 | 76,537 |
| 16_花边文学.txt | 花边文学 | 鲁迅 | 1936年6月 | 51,465 |
| 17_且介亭杂文.txt | 且介亭杂文 | 鲁迅 | 1937年7月 | 75,498 |
| 18_且介亭杂文二集.txt | 且介亭杂文二集 | 鲁迅 | 1937年7月 | 93,111 |
| 19_且介亭杂文末编.txt | 且介亭杂文末编 | 鲁迅 | 1937年7月 | 63,414 |
| 20_集外集.txt | 集外集 | 鲁迅 | 1935年5月 | 69,718 |
| 21_集外集拾遗.txt | 集外集拾遗 | 鲁迅 | 1938年（收入《鲁迅全集》） | 80,207 |
| 22_集外集拾遗补编.txt | 集外集拾遗补编 | 鲁迅 | 1952年 | 238,546 |
| 23_中国小说史略.txt | 中国小说史略 | 鲁迅 | 1923年12月（上册）；1924年6月（下册） | 151,562 |
| 24_汉文学史纲要.txt | 汉文学史纲要 | 鲁迅 | 1938年（正式出版） | 27,411 |
| 25_古籍序跋集.txt | 古籍序跋集 | 鲁迅 | 待补 | 40,834 |
| 26_译文序跋集.txt | 译文序跋集 | 鲁迅 | 待补 | 103,517 |
| 27_古小说钩沉.txt | 古小说钩沉 | 鲁迅（辑录） | 待补 | 197,086 |
| 28_唐宋传奇集.txt | 唐宋传奇集 | 鲁迅（编） | 1927年12月（上册）；1928年2月（下册） | 141,408 |
| 29_小说旧闻钞.txt | 小说旧闻钞 | 鲁迅（辑录） | 1926 年 | 65,651 |
| 30_嵇康集.txt | 嵇康集 | 嵇康著，鲁迅校勘 | 1947 年 10 月 | 63,074 |
| 31_会稽郡故书杂集.txt | 会稽郡故书杂集 | 鲁迅（辑录） | 1915年（木刻本） | 33,624 |
| 32_两地书.txt | 两地书 | 鲁迅、许广平 | 1933年4月 | 140,779 |

### Writings_about_LuXun (22 books, 1,697,251 characters)

| File | Title | Author | First edition | Characters |
|---|---|---|---|---|
| 01_亡友鲁迅印象记.txt | 亡友鲁迅印象记 | 许寿裳 | 1947年10月 | 51,343 |
| 02_我所认识的鲁迅.txt | 我所认识的鲁迅 | 许寿裳 | 1952年 | 62,619 |
| 03_鲁迅的思想与生活.txt | 鲁迅的思想与生活 | 许寿裳 | 1947年6月 | 37,814 |
| 04_欣慰的纪念.txt | 欣慰的纪念 | 许广平 | 1951年7月 | 79,114 |
| 05_鲁迅回忆录.txt | 鲁迅回忆录 | 许广平 | 1961年5月（单行本） | 94,079 |
| 06_关于鲁迅的生活.txt | 关于鲁迅的生活 | 许广平 | 1954年6月 | 26,460 |
| 07_鲁迅的故家.txt | 鲁迅的故家 | 周作人 | 1953年3月，上海出版公司初版 | 122,064 |
| 08_鲁迅小说里的人物.txt | 鲁迅小说里的人物 | 周作人 | 1954年，上海出版公司 | 118,030 |
| 09_鲁迅的青年时代.txt | 鲁迅的青年时代 | 周作人 | 1957年，中国青年出版社 | 74,287 |
| 10_民元前的鲁迅先生.txt | 民元前的鲁迅先生 | 王冶秋 | 1943年4月 | 69,704 |
| 11_鲁迅传.txt | 鲁迅传 | 小田岳夫 | 1946年9月初版 | 69,779 |
| 12_鲁迅正传.txt | 鲁迅正传 | 郑学稼 | 1941年 | 63,024 |
| 13_鲁迅的书.txt | 鲁迅的书 | 欧阳凡海 | 1942年5月 | 287,238 |
| 14_鲁迅先生二三事.txt | 鲁迅先生二三事 | 孙伏园 | 1942年4月 | 26,885 |
| 15_鲁迅回忆断片.txt | 鲁迅回忆断片 | 荆有麟 | 1943年11月 | 50,067 |
| 16_回忆鲁迅先生.txt | 回忆鲁迅先生 | 萧红 | 1940年7月初版，生活书店发行 | 43,620 |
| 17_鲁迅事迹考.txt | 鲁迅事迹考 | 林辰 | 1948年7月初版 | 65,358 |
| 18_鲁迅散论.txt | 鲁迅散论 | 雪苇 | 1948年4月大连初版 | 31,508 |
| 19_关于鲁迅.txt | 关于鲁迅 | 梅子编 | 1942年10月 | 35,573 |
| 20_论鲁迅的思想.txt | 论鲁迅的思想 | 平心 | 1941年3月初版 | 113,436 |
| 21_民族魂鲁迅.txt | 民族魂鲁迅 | 萧红 | 1940年10月，发表于《大公报》 | 9,954 |
| 22_回忆鲁迅房族和社会环境35年间（1902-1936）的演变.txt | 回忆鲁迅房族和社会环境35年间（1902-1936）的演变 | 周冠五（观鱼）著 | 人民文学出版社 1959年 | 160,518 |
