import wordGenerator
def getTitle():
	title = "The"
	for i in range(3):
		title = title + " " + wordGenerator.getWord(title, True)
	return title

def getDocument():
	document = "In"
	for i in range(500):
		document = document + " " + wordGenerator.getWord(document)
	return document
	

print(getTitle())
print("")
print(getDocument())