from string import punctuation, whitespace
def add_prefix_un(word):
  
    return "un" + word
def make_word_groups(vocab_words):
   
    prefix = vocab_words[0]
    return prefix + " :: " + " :: ".join([prefix + w for w in vocab_words[1:]])
def remove_suffix_ness(word):
   
    base = word[:-4]
    if base[-1] == 'i':
        return base[:-1] + 'y'
    return base
def noun_to_verb(sentence, index):
  
    return sentence.split()[index].rstrip(punctuation+whitespace) + "en"