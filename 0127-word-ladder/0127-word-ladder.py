class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        word_set = set()
        q = deque()
        for w in wordList:
            word_set.add(w)
        if beginWord in word_set:
            word_set.remove(beginWord)
        ch = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        q.append([beginWord, 1])

        while(len(q) > 0):
            [word, steps] = q.popleft()

            if word == endWord:
                return steps
            for i in range(len(word)):
                original = word[i]
                for j in range(26):
                    temp = list(word)

                    temp[i] = ch[j]
                    word = "".join(temp)
                    if word in word_set:
                        word_set.remove(word)
                        q.append([word, steps+1])

                temp = list(word)
                temp[i] = original
                word = "".join(temp)
        
        return 0