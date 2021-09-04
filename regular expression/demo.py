#Pattern matching
#re -- package for pattern matching

# import re
# count=0
# matcher=re.finditer('ab','ababbab')
# for match in matcher:
#     count+=1
# print("count=",count)

# import re
# count=0
# matcher=re.finditer('ab','abaabbab')
# for match in matcher:
#     print("match available at",match.start()) #return position
#     print("group=",match.group())  #which object find match
#     count+=1
# print("count=",count)


# import re
# x="[abc]"
# matcher=re.finditer(x,'abt c@c b df a')
# for match in matcher:
#     print("match available at",match.start())
#     print("group=",match.group())

# import re
# x="[^abc]"
# matcher=re.finditer(x,'abt c@c b df a')
# for match in matcher:
#     print("match available at",match.start())
#     print("group=",match.group())

# import re
# x="[a-z]"
# matcher=re.finditer(x,'abt c@c Ab df a')
# for match in matcher:
#     print("match available at",match.start())
#     print("group=",match.group())
#
# import re
# x="[A-Z]"
# matcher=re.finditer(x,'abt Vc@c Ab df a')
# for match in matcher:
#     print("match available at",match.start())
#     print("group=",match.group())

# import re
# x="[a-zA-Z]"
# matcher=re.finditer(x,'ab5t Vc@c A68b df a7')
# for match in matcher:
#     print("match available at",match.start())
#     print("group=",match.group())

# import re
# x="[0-9]"
# matcher=re.finditer(x,'ab5t Vc@c A68b df a7')
# for match in matcher:
#     print("match available at",match.start())
#     print("group=",match.group())

# import re
# x="[^0-9a-zA-Z]"
# matcher=re.finditer(x,'ab5t Vc@c A68b df a7')
# for match in matcher:
#     print("match available at",match.start())
#     print("group=",match.group())

# import re
# x="\w" #words without symbols
# matcher=re.finditer(x,'ab5t Vc@c A68b df a7')
# for match in matcher:
#     print("match available at",match.start())
#     print("group=",match.group())

# import re
# x="\W" #not words
# matcher=re.finditer(x,'ab5t Vc@c A68b df a7')
# for match in matcher:
#     print("match available at",match.start())
#     print("group=",match.group())

# import re
# x="\d" #digits
# matcher=re.finditer(x,'ab5t Vc@c A68b df a7')
# for match in matcher:
#     print("match available at",match.start())
#     print("group=",match.group())

# import re
# x="\D" #except digits
# matcher=re.finditer(x,'ab5t Vc@c A68b df a7')
# for match in matcher:
#     print("match available at",match.start())
#     print("group=",match.group())

# import re
# x="\s" #space
# matcher=re.finditer(x,'ab5t Vc@c A68b df a7')
# for match in matcher:
#     print("match available at",match.start())
#     print("group=",match.group())