def two_fer(name="you"):
	if name != "you":
		return "One for {}, one for me.".format(name)
	else:
		return "One for you, one for me."