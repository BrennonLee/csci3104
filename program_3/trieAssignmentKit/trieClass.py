# Name: Brennon Lee
# Email: Brle1617@colorado.edu
# Student ID:	103419905
# On my honor as a University of Colorado student, I acknowledge that
# I did not receive any unauthorized help for this assignment.
# I understand that systems like MOSS can easily detect code plagiarism.



from __future__ import print_function
import sys

# We will use a class called my trie node
class MyTrieNode:
    # Initialize some fields

    def __init__(self, isRootNode):
        #The initialization below is just a suggestion.
        #Change it as you will.
        # But do not change the signature of the constructor.
        self.isRoot = isRootNode
        self.isWordEnd = False # is this node a word ending node
        self.isRoot = False # is this a root node
        self.count = 0 # frequency count
        self.next = {} # Dictionary mappng each character from a-z to the child node


    def addWord(self,w):
        assert(len(w) > 0)
        for char in w:        #for each letter in the word
            if char not in self.next:   #if this letter is not a child of the current letter, ADD IT!
                self.next[char] = MyTrieNode(False)
            self = self.next[char]    #move self to the next character in the word.
        self.isWordEnd = True   #once out of loop, you are at the end of the word.
        self.count = self.count + 1 #increase frequency of how many times w is added
        return

    def lookupWord(self,w):
        for char in w:
            if char in self.next.keys():
                self= self.next[char]
            else:
                return 0;
        if (self.isWordEnd == True):
            return self.count

        return 0


    def dfs(self, word, x):
        for char in self.next.keys():
            if (self.next[char].isWordEnd == True):
                tup = (word+char, self.next[char].count)
                x.append(tup)
            self.next[char].dfs(word+char,x)
        return x




    def autoComplete(self,w):
        List = []
        x = []

        if (self.lookupWord(w)):        #check to find if w passed in is already a completed word
            tup = (w, self.lookupWord(w))
            List.append(tup)


        word_count = 0
        word_length = len(w)
        for char in w:                  #Loop through as far as we can with given word
            if char in self.next:
                word_count += 1
                self = self.next[char]

        if (word_count != word_length): #if how far we loop doesnt match the word, then return []
            return []
        dfs_array = self.dfs(w,x)        #Else go into dfs to return all possible words

        List += (dfs_array)             #Add dfs_array to our list


        return List




if (__name__ == '__main__'):
    t= MyTrieNode(True)
    lst1=['test','testament','testing','ping','pin','pink','pine','pint','testing','pinetree']

    for w in lst1:
        t.addWord(w)

    j = t.lookupWord('testy') # should return 0
    j2 = t.lookupWord('telltale') # should return 0
    j3 = t.lookupWord ('testing') # should return 2
    lst3 = t.autoComplete('pi')
    print('Completions for \"pi\" are : ')
    print(lst3)

    lst4 = t.autoComplete('tes')
    print('Completions for \"tes\" are : ')
    print(lst4)
