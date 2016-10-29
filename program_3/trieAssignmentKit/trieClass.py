#LastName:
#FirstName:
#Email:
#Comments:

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
                     #make child part of the trie
                print("current char is: ", char, "and self.isEndWord is: ", self.isWordEnd)
            self = self.next[char]    #move self to the next character in the word.
        self.isWordEnd = True   #once out of loop, you are at the end of the word.
        print("character at end of word is: ", char, "and value if endword is: ", self.isWordEnd)
        self.count = self.count + 1 #increase frequency of how many times w is added
        print("word added was: ",w, "and self.count is: " , self.count)
        print('\n')
        return

    def lookupWord(self,w):
        print("word is: ", w)
        for char in w:
            # print ("Looking for char: ", char)
            # print ("chars in w are: ",self.next)
            # print ("count is: ", count)
            if char in self.next:
                print("current char in word is: ", char)
                self= self.next[char]
                print ("value of endword is: ", self.isWordEnd)
        print("\n")
        if (self.isWordEnd == True):
            return self.count
        # Return frequency of occurrence of the word w in the trie
        # returns a number for the frequency and 0 if the word w does not occur.

        # YOUR CODE HERE
        return 0


    def autoComplete(self,w):
        #Returns possible list of autocompletions of the word w
        #Returns a list of pairs (s,j) denoting that
        #         word s occurs with frequency j
        #YOUR CODE HERE
        print("Word to complete: ", w)
        print ('\n')
        for char in w:
            # print ("char is: ",char)
            # array = array.join(char)
            if (char in self.next):
                self = self.next[char]
                # print("self.isWordEnd is: ", self.isWordEnd)

                 #loop through all the characters as far as we can
                # print ("combined array is: ", array)
        # cursor = MyTrieNode(False)
        # cursor = self
        self = self.next
        print("entering child loop")
        word = [w]
        for each in self.next:
            # print ("self.next value is", self.next)
            print ("each value is: ",each)
            # print("self.isWordEnd is: ", self.isWordEnd)
            while (self.isWordEnd != True):
                # print("self value is: ", self.next)
                word.append( self.next )
                self = self.next[char]
            whole_word = ''.join(word)
        print ("whole word is: ", whole_word)
        return (whole_word)
        return [('Walter',1),('Mitty',2),('Went',3),('To',4),('Greenland',2)] #TODO: change this line, please




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
