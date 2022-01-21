ab = open("all possible pass words with 8 nums.gen" , 'w')
out = ""
for a in range(0,10):
	for b in range(0,10):
		for c in range(0,10):
			for d in range(0,10):
				for e in range(0,10):
					for f in range(0,10):
						for g in range(0,10):
							for h in range(0,10):
								out += str(a) + str(b) + str(c) + str(d) + str(e) + str(f) + str(g) + str(h) + '\n'
								#a.write(out)
ab.write(out)


