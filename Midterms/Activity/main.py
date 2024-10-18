from Stack import Stack, Arithmetic, Reverse

matcher = Arithmetic()

check1 = '(z + x) * y (a + b)'
check2 = '((({{}}]]a+b)]ad{'

if matcher.is_matched(check1):
    print("Look if its Correct at the file")
else:
    print("Look if its Wrong at them file")

if matcher.is_matched(check2):
    print("Look if its Correct at the file")
else:
    print("Look if its Wrong at the file")


Reverse.reverse_file('file.txt')
