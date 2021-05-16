import re
y = "aa bb cc bb ff bb ee"
x = "aa bb cc dd ff gg ee"
if re.match(".*[dz]", y):
    print("y zawiera d lub z")
if re.match(".*[dz]", x):
    print("x zawiera d lub z")
if re.match(".* ([a-z]{2}) .* \\1", y):
    print("y zawiera dwa razy to samo")
if re.match(".* ([a-z]{2}) .* \\1", x):
    print("x zawiera dwa razy to samo")
# zastępowanie
print (re.sub('[bc]+', "XX", y, 2))
print (re.sub('[bc]+', "XX", y))
# zachłanność
print (re.sub('bb (.*) bb', "X \\1 X", y))
print (re.sub('.*bb (.*) bb.*', "\\1", y))
print (re.sub('.*?bb (.*) bb.*', "\\1", y))