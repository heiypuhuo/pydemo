def f():
	print("sdfa")


def chengfa():
	tem = range(1,10)
	for x in tem :
		for y in range(1,x+1):
			print("%s * %s = %s" %(x,y,y*x),end="    ")
		print(end=("\n"))


def while1():
	a = 30
	while(a > 0):

		a -= 1
		if (a == 10):
			break
		elif(a == 16):
			continue
		print("woshi",a,end="  ")



if __name__ == "__main__":
	f()
	chengfa()
	while1()

