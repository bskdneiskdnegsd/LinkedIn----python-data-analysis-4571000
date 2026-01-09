'''
Find palindromes
Palindromes are pairs of words that become each other when we reverse the order of their letters. That means that all palindromes are anagrams!

Your task: Write a function that returns all palindromes of seven letters or more. You will work with the dictionary of anagram sets indexed by signature that we created in video 02_03.

Parameters
anagrams_by_signature: A dictionary containing sets of anagrams, indexed by their signature

Result
A list of set objects containing all palindromic pairs of seven letters or more
'''

# Python code​​​​​​‌‌‌​‌‌‌​​​​‌‌​‌​​‌‌​​‌​‌‌ below
# Use print("messages...") to debug your solution.


'''
Note: I think the below should work for what the exercise intended, but it is inefficient and the challenge would not run fully (message was 'Process has timed out. This may mean that your solution is not optimized enoughs to handle some cases.'). I initially implemented it by looking for true palindromes, but the challenge wanted pairs of words that are reverses of each other (based on the expected result). My initial cose worked and found the 2 actual palindromes. Here is what GenAI has to say about my code:

--

You're very close! Your approach works conceptually, but there are a few issues that will bite you:

What could be improved

Quadratic time:
The double loop over seven_plus_words is O(n2)O(n^2)O(n2). You can do it in O(n)O(n)O(n) by checking whether each word’s reverse exists in the same set.

Duplicate pairs:
With the nested loop, you’ll add {i, j} and {j, i} as separate entries (because you append sets to a list). Using a pair canonicalization (e.g., frozenset) prevents duplicates.

Function naming:
The function is named palindromes, but the expected output is reverse pairs (e.g., 'rewarder' and 'redrawer'), not palindromic words ('level' etc.). Consider renaming to reduce confusion.

Self-palindromes:
If you do want true palindromes (word equals its reverse), your current code would add {word} as a 1-element set. Your expected output suggests you don’t want those—only reverse pairs—so we should explicitly exclude them.
'''

show_expected_result = True
show_hints = True

def get_all_words(anagrams_by_signature):
    all_words = set()
    for key, value in anagrams_by_signature.items():
        all_words.update(value)
    return all_words

def palindromes(anagrams_by_signature):
    seven_plus_words = {i for i in get_all_words(anagrams_by_signature) if len(i) > 6}
    palindromes = []
    for i in seven_plus_words:
        for j in seven_plus_words:
            if i == j[::-1]:
                palindromes.append(set([i, j]))
    return palindromes
