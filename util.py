def isTextHasAllThingsInlist(text, needworklist):
	result = True
	for everyContent in needworklist:
		result = everyContent in text  and result
	return  result

def isTextHasOneThingsInlist(text, needworklist):
	result = True
	for everyContent in needworklist:
		result = str(everyContent) in text  or result
	return  result