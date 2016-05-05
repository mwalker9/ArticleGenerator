import possibleWords
import numpy as np
def getWord(document, title=False):
	model = "body"
	phrase = document
	if len(phrase.split()) > 10:
		phrase = document.split()[-10:]
		phrase = " ".join(phrase)
		phrase = phrase.strip()
	if title:
		model = "title"	
	#print(phrase)
	arr = possibleWords.getProbabilities(phrase, order=5, model=model)
	words = []
	probabilities = []
	for m in arr:
		words.append(m["word"])
		probabilities.append(np.exp(m["probability"]))
	probabilities = np.asarray(probabilities) / sum(probabilities)
	if len(words) == 0:
		return getWord(phrase.split()[-1])
	index = np.argmax(np.random.multinomial(1, probabilities))
	return words[index]