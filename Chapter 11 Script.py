fname=input("Enter file name:")
if len(fname)<1:fname="regex_sum_1901185.txt"
hd=open(fname)
import re
count = 0
for line in hd:
    numbers = re.findall('[0-9]+', line)
    for number in numbers:
        count = count + int(number)
print(count)