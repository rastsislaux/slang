import os
from slang_stdlib import *

# Code from module method.slang
def slang_method() -> None:
	print(str("Hello") + str(_SPC) + str("world!"), end = '')
	

def write_and_return(a : int) -> int:
	print(str(a), end = '')
	return a
	
def return2() -> int:
	return 2
	
def main() -> None:
	strn = ''
	dbl = 0.0
	intg = 0
	bln = False
	vect = []
	print(str("Hello,") + str(_SPC) + str("world!") + str(_NWL), end = '')
	vect.append(123)
	vect.append("TESTING")
	print(str(vect) + str(_NWL), end = '')
	strn = "hello!"
	dbl = 12.5
	intg = 13
	bln = True
	return2()
	intg = return2()
	print("Hello!")
	strn = print("Hello!")
	while intg<26:
		print(str(intg) + str(_SPC), end = '')
		intg = inc(intg, 2)
		
	while True:
		print(str(intg) + str(_SPC), end = '')
		intg = inc(intg)
		if intg==51:
			break
			
		
	print(str(_NWL), end = '')
	numbers = []
	numbers = [1,2,3,4,5,6,7,8,9,10]
	rng = range(0, 10, 2)
	for i in rng:
		print(str(numbers[i]) + str(_SPC), end = '')
		
	print(str(_NWL), end = '')
	dictionary = {}
	dictionary.update({"key":"value","key2":"value2"})
	print(str(dictionary["key"]) + str(_NWL), end = '')
	

if __name__ == "__main__":
	main()
