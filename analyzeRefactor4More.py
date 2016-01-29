import sys
import re
import os
import psutil # if this makes an error, you need to install the psutil package on your system
import time

maxmem = 0
def showMemTime(when='Resources'):
  global maxmem
  # memory and time measurement
  process = psutil.Process(os.getpid())
  mem = process.memory_info().rss / float(2 ** 20)
  maxmem = max(maxmem, mem)
  ts = process.cpu_times()
  sys.stderr.write("{when:<20}: {mb:4.0f} MB (max {maxmb:4.0f} MB), {user:4.1f} s user, {system:4.1f} s system\n".format(
    when=when, mb=mem, maxmb=maxmem, user=ts.user, system=ts.system))
#initialize ngramcounter class which that compute ngram and display
class NGramCounter:
  def __init__(self,k,n,m):
    self.ngrams = {} # initialize storage dictionary (datatype of {} is 'dict')
    self.number=n #initialize storage number grams
    self.leng=m		#Length of word
    self.kmost=k	#Most frequence variable

  def count(self,*word):			#Word tuples
    # make bigram (datatype of (,) is 'tuple')
    gramtimes=len(word) #finding length of list
    a=0
    liste=[]	
    while a<gramtimes:
      liste.append(word[a][-self.leng:])		#adding element into list
      a = a+1
    ngram=tuple(liste)	#converting list to tuple
    # increase count for this bigram by one
    if ngram not in self.ngrams:
      # if it was not yet in the dictionary
      self.ngrams[ngram] = 1
    else:
      # if it was already in the dictionary
      self.ngrams[ngram] += 1

    del gramtimes # deleting trivial variable
    del a # deleting trivial variable
    del liste # deleting trivial variable
    del ngram # deleting trivial variable

  def display(self):
    showMemTime('begin display')

    # build list of all frequencies and trigrams
    ngram_freq = self.ngrams.items()
    showMemTime('after items')

    # sort that list by frequencies (i.e., second field), descending
    print "sorting ..."
    ngram_freq.sort(key = lambda x:x[1], reverse = True)
    showMemTime('after sorting')

    # iterate over the first five (or less) elements
    print "creating output ..."
    for ngram, occurred in ngram_freq[0:self.kmost]:
      print "%d-ending %dgram '%s' occured %d times" % \
        (self.leng, self.number, ngram, occurred)
    
    del ngram_freq # deleting trivial variable
    del ngram # deleting trivial variable
	
#def displayKMostfrequentNGramsInfile
def displayKMostFrequentNGramsInFile(k,n,m,filename):
  showMemTime('begin') # let's observe where we use our memory and time
  #-------------------------------------------
  # initialize NGgrams counter
  nesne = NGramCounter(k,n,m)

  del n # deleting trivial variable
  del m # deleting trivial variable
  #--------------------------------------------
  # read input file
  print "reading from file "+filename
  inputdata = open(filename,'r')
  del filename # deleting trivial variable
  q=0
  
  for line in inputdata:
    showMemTime('after reading')
    # split on all newlines and spaces
    print "splitting"
    inputwords = re.split(r' |\n',line)
    showMemTime('after splitting')

    del line # deleting trivial variable

    # remove empty strings
    inputwords = filter(lambda x: x != '', inputwords)
    showMemTime('after filtering')

    # go through all words
    print "going over words"
    for idx in range(0,len(inputwords)):
      # let's show resources after all 50 K words
      if q == 250:		# There are average 200 words in every line.
        showMemTime('while counting')
        q=0
		
      #count NGram if we can look back n-1 chracters
      if idx >= nesne.number-1:
        nesne.count (*inputwords[idx-nesne.number:idx])
    q = q+1
  
  del idx # deleting trivial variable
  del inputwords # deleting trivial variable
  del q				# deleting trivial variable
  del inputdata			# deleting trivial variable
  
  showMemTime('after counting')
  print "NGrams:"
  nesne.display()
  del nesne				#deleting nesne object
  

# this is our main function
def main():

  #displayKMostFrequentNGramsInFile(30,2,2,'english.txt')
  #displayKMostFrequentNGramsInFile(30,2,3,'english.txt')
  #displayKMostFrequentNGramsInFile(30,2,4,'english.txt')
    
  #displayKMostFrequentNGramsInFile(20,3,2,'english.txt')			# ENGLISH TEXT
  #displayKMostFrequentNGramsInFile(20,3,3,'english.txt')
    
  #displayKMostFrequentNGramsInFile(15,4,2,'english.txt')
  #displayKMostFrequentNGramsInFile(15,4,3,'english.txt')

  #--------------------------------------------------------
    
  #displayKMostFrequentNGramsInFile(30,2,2,'german.txt')
  #displayKMostFrequentNGramsInFile(30,2,3,'german.txt')
  #displayKMostFrequentNGramsInFile(30,2,4,'german.txt')

  #displayKMostFrequentNGramsInFile(20,3,2,'german.txt')			# GERMAN TEXT
  #displayKMostFrequentNGramsInFile(20,3,3,'german.txt')

  #displayKMostFrequentNGramsInFile(15,4,2,'german.txt')
  #displayKMostFrequentNGramsInFile(15,4,3,'german.txt')

  #--------------------------------------------------------

  #displayKMostFrequentNGramsInFile(30,2,2,'turkish.txt')
  #displayKMostFrequentNGramsInFile(30,2,3,'turkish.txt')
  #displayKMostFrequentNGramsInFile(30,2,4,'turkish.txt')

  #displayKMostFrequentNGramsInFile(20,3,2,'turkish.txt')			# TURKISH TEXT
  #displayKMostFrequentNGramsInFile(20,3,3,'turkish.txt')

  #displayKMostFrequentNGramsInFile(15,4,2,'turkish.txt')
  displayKMostFrequentNGramsInFile(15,4,3,'turkish.txt') 

main()
showMemTime('at the end')
