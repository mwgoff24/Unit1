'''
Lab 1.02 - Using the Interpreter
Part 1
Using the interpreter, type in the expressions below. Copy and paste the output into the output column. If the
result is unexpected, note that in the third column.
Section 1
    Input                   Output                          Did it do something unexpected?
a   5 + 2 * 2               9                               No
b   2/3                     0.6666...   
c   2.0 * 1.5               3.0
d   (2 + 3) * 10            50
e   5.0 // 2                2.0                             Thought would be error
f   5.0 % 2                 1.0                             Wasn't expecting this result
Section 2
    Input                   Output                          Did it do something unexpected?
a   a
b   'a'

Section 3
    Input                   Output                          Did it do something unexpected?
a   'a + b'
b   'a' + 'b'

Section 4
    Input                   Output                          Did it do something unexpected?
a   'a' * 'b'
b   'a' * 2

Part 2
Before going to the IDE
1. For each item, predict the data type of the result and enter into the "String/Integer/Float" column.
2. Next, predict the value of the result for each item and enter into it into the "Prediction of Result"
column.

###################################################################################
#integers are whole numbers, floats are decimals, strings are surrounded by quotes#
###################################################################################

    Expression                  String/Integer/Float        Prediction of Result                Interpreter Result
a   10 * 2                      integer                     20                                  20
b   .5 * 2                      integer                     1
c   10/2                        integer
d   10%2                        float
e   2 ** 3                      float
f   (2+5)*3                     integer
g   2 + 5 * 3                   integer
h   'ab' + '12' + '3'           string
i   x                           float
j   "ab" + "cd"
k   'abc' * 2
l   '1'*2 + '2' * 3
m   1 * 2 + '3' * 2
n   'A' ** 2
o   'bc' % 2
p   'bc' / 2

Now go to the IDE
Use the interpreter to evaluate the expressions, write down results in the "Interpreter Result" column.
'''