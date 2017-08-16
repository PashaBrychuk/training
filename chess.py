def safe_pawns(pawns):
    pawns_indexes = set()
    res = 0
    for p in pawns:
        row = int(p[1])-1
        col = ord(p[0])-97
        pawns_indexes.add((row, col))
        for row, col in pawns_indexes:
            res = res + is_safe(row, col, pawns_indexes)
    return res
def is_safe(row,col,pawns_indexes):
	
		s = ((row - 1, col - 1) in pawns_indexes) or ((row - 1, col + 1) in pawns_indexes)
		if s==True:
            print "!"
			return 1
		return 0
print  safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"})

"""def safe_pawns(pawns):
    pawns_indexes = set()
    for p in pawns:
        row = int(p[1])-1
        col = ord(p[0])-97
        pawns_indexes.add((row, col))
        count = 0
    
        for row, col in pawns_indexes:
            if ((row - 1, col - 1) in pawns_indexes) or ((row - 1, col + 1) in pawns_indexes):
                
                    count=count+1
    return count
    """