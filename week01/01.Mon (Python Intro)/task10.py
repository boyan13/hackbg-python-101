#NaN Expand
def nan_expand(times):
	result = "NaN"

	for i in range(times):
		result = "Not a " + result

	return result

print( nan_expand(0) )
print( nan_expand(1) )
print( nan_expand(2) )
print( nan_expand(50) )