MOV @m, R0
MOV 10, R3
system 5
MOVB (R0), R1
A:
XOR  BCA7, R1
MOVB R1,(R0)
ADD 1, R0
MOVB (R0), R1
SUB 1, R3
JNZ A
MOV @M, R0
SYSTEM 5
MOV 10, R3
system 5
MOVB (R0), R1
B:
XOR  BCA7, R1
MOVB R1,(R0)
ADD 1, R0
MOVB (R0), R1
SUB 1, R3
JNZ B
MOV @M, R0
SYSTEM 5
STOP
M:
 DATA 10
 DATA 28
 DATA 44
 DATA 82
 DATA 1FF
 DATA 82
 DATA 82
 DATA FE