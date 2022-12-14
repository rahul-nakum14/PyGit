from github import Github
import json

g = Github("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")

repo = g.get_repo('rahul-nakum14/Competitive-Programming')



'''list code with specidfied file name'''

file = repo.get_contents("hascycle.py")
content = file.decoded_content.decode('utf-8')
print(content)


''' to get alll file nd match given file name'''
# for x in file:
#         if x.name == "hascycle.py":
#         # Use the decoded_content attribute to get the source code
#         # of the file as a string
#             content = x.decoded_content.decode('utf-8')
#             print(content)

    # content = x.decoded_content.decode('utf-8')
    # # Print the content of the file
    # print(content)


'''Get all of the contents of the repository recursively'''
# while file:
#      file_content = file.pop(0)
#      if file_content.type == "dir":
#          file.extend(repo.get_contents(file_content.path))
#      else:
#          print(file_content)


