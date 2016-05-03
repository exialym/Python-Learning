# -*- coding: utf-8 -*-
#!/usr/bin/env python
# ----------------------------------------------------------------------------
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
# ----------------------------------------------------------------------------
# Author: Matteo Bertozzi <theo.bertozzi@gmail.com>
# Site: http://th30z.blogspot.com
# ----------------------------------------------------------------------------

import unicodedata

# List Of English Stop Words
# http://armandbrahaj.blog.al/2009/04/14/list-of-english-stop-words/
_WORD_MIN_LENGTH = 3
_STOP_WORDS = frozenset([
'a', 'about', 'above', 'above', 'across', 'after', 'afterwards', 'again', 
'against', 'all', 'almost', 'alone', 'along', 'already', 'also','although',
'always','am','among', 'amongst', 'amoungst', 'amount',  'an', 'and', 'another',
'any','anyhow','anyone','anything','anyway', 'anywhere', 'are', 'around', 'as',
'at', 'back','be','became', 'because','become','becomes', 'becoming', 'been', 
'before', 'beforehand', 'behind', 'being', 'below', 'beside', 'besides', 
'between', 'beyond', 'bill', 'both', 'bottom','but', 'by', 'call', 'can', 
'cannot', 'cant', 'co', 'con', 'could', 'couldnt', 'cry', 'de', 'describe', 
'detail', 'do', 'done', 'down', 'due', 'during', 'each', 'eg', 'eight', 
'either', 'eleven','else', 'elsewhere', 'empty', 'enough', 'etc', 'even', 
'ever', 'every', 'everyone', 'everything', 'everywhere', 'except', 'few', 
'fifteen', 'fify', 'fill', 'find', 'fire', 'first', 'five', 'for', 'former', 
'formerly', 'forty', 'found', 'four', 'from', 'front', 'full', 'further', 'get',
'give', 'go', 'had', 'has', 'hasnt', 'have', 'he', 'hence', 'her', 'here', 
'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself', 'him', 
'himself', 'his', 'how', 'however', 'hundred', 'ie', 'if', 'in', 'inc', 
'indeed', 'interest', 'into', 'is', 'it', 'its', 'itself', 'keep', 'last', 
'latter', 'latterly', 'least', 'less', 'ltd', 'made', 'many', 'may', 'me', 
'meanwhile', 'might', 'mill', 'mine', 'more', 'moreover', 'most', 'mostly', 
'move', 'much', 'must', 'my', 'myself', 'name', 'namely', 'neither', 'never', 
'nevertheless', 'next', 'nine', 'no', 'nobody', 'none', 'noone', 'nor', 'not', 
'nothing', 'now', 'nowhere', 'of', 'off', 'often', 'on', 'once', 'one', 'only',
'onto', 'or', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out',
'over', 'own','part', 'per', 'perhaps', 'please', 'put', 'rather', 're', 'same',
'see', 'seem', 'seemed', 'seeming', 'seems', 'serious', 'several', 'she', 
'should', 'show', 'side', 'since', 'sincere', 'six', 'sixty', 'so', 'some', 
'somehow', 'someone', 'something', 'sometime', 'sometimes', 'somewhere', 
'still', 'such', 'system', 'take', 'ten', 'than', 'that', 'the', 'their', 
'them', 'themselves', 'then', 'thence', 'there', 'thereafter', 'thereby', 
'therefore', 'therein', 'thereupon', 'these', 'they', 'thickv', 'thin', 'third',
'this', 'those', 'though', 'three', 'through', 'throughout', 'thru', 'thus', 
'to', 'together', 'too', 'top', 'toward', 'towards', 'twelve', 'twenty', 'two', 
'un', 'under', 'until', 'up', 'upon', 'us', 'very', 'via', 'was', 'we', 'well', 
'were', 'what', 'whatever', 'when', 'whence', 'whenever', 'where', 'whereafter',
'whereas', 'whereby', 'wherein', 'whereupon', 'wherever', 'whether', 'which', 
'while', 'whither', 'who', 'whoever', 'whole', 'whom', 'whose', 'why', 'will', 
'with', 'within', 'without', 'would', 'yet', 'you', 'your', 'yours', 'yourself',
'yourselves', 'the'])

def word_split(text):
	"""
	Split a text in words. Returns a list of tuple that contains
	(word, location) location is the starting byte position of the word.
	"""
	word_list = []
	wcurrent = []
	windex = None
	wordIndex = 0

	for i, c in enumerate(text):
		if c.isalnum():
			wcurrent.append(c)
			windex = i
		elif wcurrent:
			word = u''.join(wcurrent)
			wordIndex += 1
			word_list.append((wordIndex, word, windex - len(word) + 1))
			wcurrent = []

	if wcurrent:
		word = u''.join(wcurrent)
		wordIndex += 1
		word_list.append((wordIndex, word, windex - len(word) + 1))

	return word_list

def words_cleanup(words):
	"""
	Remove words with length less then a minimum and stopwords.
	"""
	cleaned_words = []
	for index, word, wordindex in words:
		if len(word) < _WORD_MIN_LENGTH or word in _STOP_WORDS:
			continue
		cleaned_words.append((index, word, wordindex))
	return cleaned_words

def words_normalize(words):
	"""
	Do a normalization precess on words. In this case is just a tolower(),
	but you can add accents stripping, convert to singular and so on...
	"""
	normalized_words = []
	for index, word, wordindex in words:
		wnormalized = word.lower()
		normalized_words.append((index, wnormalized, wordindex))
	return normalized_words

def word_index(text):
	"""
	Just a helper method to process a text.
	It calls word split, normalize and cleanup.
	"""
	words = word_split(text)
	words = words_normalize(words)
	words = words_cleanup(words)
	return words

def inverted_index(text):
	"""
	Create an Inverted-Index of the specified text document.
		{word:[locations]}
	"""
	inverted = {}

	for index, word, wordindex in word_index(text):
		locations = inverted.setdefault(word, [])
		locations.append((index,wordindex))

	return inverted

def inverted_index_add(inverted, doc_id, doc_index):
	"""
	Add Invertd-Index doc_index of the document doc_id to the 
	Multi-Document Inverted-Index (inverted), 
	using doc_id as document identifier.
		{word:{doc_id:[locations]}}
	"""
	for word, locations in doc_index.iteritems():
		indices = inverted.setdefault(word, {})
		indices[doc_id] = locations
	return inverted
def extract_text(doc, index): 
	return documents[doc][index-20:index+20].replace('\n', ' ')
def searchType(query):
	searchType = 0
	for i, c in enumerate(query):
		if c == "-":
			searchType = 1
		if c == "~":
			searchType = 2
	return searchType

def search(inverted, query):
	"""
	Returns a set of documents id that contains all the words in your query.
	"""
	myQuery = query.split(" ")
	finalResult = {}
	for queryItem in myQuery:
		searchtype = searchType(queryItem)
		if searchtype == 0:
			words = [word for _, word, _ in word_index(queryItem) if word in inverted]
			results = [set(inverted[word].keys()) for word in words]
			results = reduce(lambda x, y: x & y, results) if results else []
			for _, word, _ in word_index(queryItem):
				for doc in results:
					indexs=[]
					for wordIndex,index in inverted[word][doc]:
						indexs.append(index)
					if len(indexs) != 0:
						indices = finalResult.setdefault(word, {})
						indices[doc] = indexs
			# for _, word, _ in word_index(queryItem):
			# 	if len(finalResult) == 0:
			# 		for doc in results:
			# 			for wordIndex,index in inverted[word][doc]:
			# 				finalResult.append((doc,index))
			# 	else:
			# 		for doc in results:
			# 			for wordIndex,index in inverted[word][doc]:
			# 				for result in finalResult:
			# 					if doc == result[0]:
			# 						finalResult.append((doc,index))
			# 						break

		elif searchtype == 1:
			words = [word for _, word, _ in word_index(queryItem) if word in inverted]
			results = [set(inverted[word].keys()) for word in words]
			results = reduce(lambda x, y: x & y, results) if results else []
			for doc in results:
				indexs=[]
				for i in range(1,len(words)):
					for j in range(0,len(inverted[words[i]][doc])):
						for k in range(0,len(inverted[words[0]][doc])):
							if (inverted[words[i]][doc][j][0]-inverted[words[0]][doc][k][0])==(i):
								indexs.append(inverted[words[0]][doc][k][1])
				if len(indexs) != 0:
					indices = finalResult.setdefault(queryItem, {})
					indices[doc] = indexs
			# if len(finalResult) == 0:
			# 	for doc in results:
			# 		for i in range(1,len(words)):
			# 			for j in range(0,len(inverted[words[i]][doc])):
			# 				for k in range(0,len(inverted[words[0]][doc])):
			# 					if (inverted[words[i]][doc][j][0]-inverted[words[0]][doc][k][0])==(i):
			# 						finalResult.append((doc,inverted[words[0]][doc][k][1]))
			# else:
			# 	for doc in results:
			# 		for i in range(1,len(words)):
			# 			for j in range(0,len(inverted[words[i]][doc])):
			# 				for k in range(0,len(inverted[words[0]][doc])):
			# 					if (inverted[words[i]][doc][j][0]-inverted[words[0]][doc][k][0])==(i):
			# 						for result in finalResult:
			# 							if doc == result[0]:
			# 								finalResult.append((doc,inverted[words[0]][doc][k][1]))
			# 								break
		elif searchtype == 2:
			words = [word for _, word, _ in word_index(queryItem) if word in inverted]
			results = [set(inverted[word].keys()) for word in words]
			results = reduce(lambda x, y: x & y, results) if results else []
			words = queryItem.split("~")
			word1 = words[0]
			word2 = words[2]
			k = int(words[1])
			for doc in results:
				indexs=[]
				goal = set()
				find = set()
				for index in inverted[word1][doc]:
					goal=goal|set(range(index[0]-k,index[0]+k+1))
				for index in inverted[word2][doc]:
					find=find|set(range(index[0],index[0]+1))
				goal = find & goal
				for wordIndex in goal:
					for index in inverted[word2][doc]:
						if index[0]== wordIndex:
							indexs.append(index[1])
				if len(indexs) != 0:
					indices = finalResult.setdefault(word2, {})
					indices[doc] = indexs


			
			

	
	finalFileAll = set()
	finalFileHas = set()
	finalFileDelete = set()
	for word, indexs in finalResult.iteritems():
		finalFileAll=finalFileAll|set(indexs.keys())
		if len(finalFileHas)==0:
			finalFileHas=finalFileHas|set(indexs.keys())
		else:
			finalFileHas=finalFileHas&set(indexs.keys())
	finalFileDelete = finalFileAll - finalFileHas
	for word,indexs in finalResult.iteritems():
		for fileNo in finalFileDelete:
			if indexs.has_key(fileNo):
				indexs.pop(fileNo)
	print "Search for '%s': %r" % (query, finalFileHas)
	for word,indexs in finalResult.iteritems():
		for fileNo, index in indexs.iteritems():
		 	for ind in index:
		 		print '    - %s in %s : %s ...' % (word, fileNo, extract_text(fileNo, ind))




		    	 			
	    	 	
	    

if __name__ == '__main__':
	doc1 = """
Niners head coach Mike Singletary will let Alex Smith remain his starting 
quarterback, but his vote of confidence is anything but a long-term mandate.
Smith now will work on a week-to-week basis, because Singletary has voided 
his year-long lease on the job.
"I think from this point on, you have to do what's best for the football team,"
Singletary said Monday, one day after threatening to bench Smith during a 
27-24 loss to the visiting Eagles.
"""

	doc2 = """
The fifth edition of West Coast Green, a conference focusing on "green" home 
innovations and products, rolled into San Francisco's Fort Mason last week 
intent, per usual, on making our living spaces more environmentally friendly 
- one used-tire house at a time.
To that end, there were presentations on topics such as water efficiency and 
the burgeoning future of Net Zero-rated buildings that consume no energy and 
produce no carbon emissions.
"""
	doc3 = """
The fifth edition of West Coast week basis
"""

    # Build Inverted-Index for documents
	inverted = {}
	documents = {'doc1':doc1, 'doc2':doc2, 'doc3':doc3}
	for doc_id, text in documents.iteritems():
		doc_index = inverted_index(text)
		inverted_index_add(inverted, doc_id, doc_index)

    # Print Inverted-Index
	for word, doc_locations in inverted.iteritems():
		print word, doc_locations

    # Search something and print results
	queries = ['week', 'coast','West coast', 'West-coast-green','West-coast week','week~2~basis','week~2~basis bench']
	for query in queries:
		search(inverted, query)
        

