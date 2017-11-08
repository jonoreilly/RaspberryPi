@ add 2 variables

	.data
	.balign 4

string:	.asciz "\na + b = %d\n"
a:	.word	33
b:	.word	44
c:	.word	0		@ will contain a+b

	.text
	.global main
	.extern printf

main:
	push	{ip, lr}	// push return address + dummy register

	ldr	r1, =a		// point r1 to a
	ldr	r1, [r1]	// store in r1 the value pointed by r1 (a)

	ldr	r2, =b
	ldr	r2, [r2]

	add	r1, r1, r2	// store in r1 the sum of r1 and r2

	ldr	r2, =c
	str	r1, [r2]	// dump r1 into the register pointed by r2 (c) as a string

	ldr	r0, =string	// point r0 to the string "\na + b = %d\n"
	ldr	r1, [r2]	// store in r1 the value pointed by r2 (c)
	bl	printf		// print r0 (string) and r1(a+b) as param

	pop	{ip, pc}	// pop returns address into pc
