from github import Github

g = Github("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")

repo = g.get_repo("rahul-nakum14/test")

def get_dirname():
    file = repo.get_contents("")
    for i in file:
        if i.type == "dir":
            print(i.name)

def list_all_file(): #except dir
    file = repo.get_contents("")
    for i in file:
        if i.type == "dir":
            continue
        print(i.name)

def list_all_file1(): #include dir
    file = repo.get_contents("")
    for i in file:
        print(i.name)

def get_file_by_name():
    file = repo.get_contents("test1.txt")
    content = file.decoded_content.decode('utf-8')
    print(content)

def printing_file_data_dir():
    file = repo.get_contents("insidedir/dir_data.txt")
    content = file.decoded_content.decode('utf-8')
    print(content)

def create_file():
    repo.create_file("created.txt","this is message created","It is content of remote cretded file")

def update_file():
    contents = repo.get_contents("created.txt")
    repo.update_file(contents.path,"updated","Now it is updated",contents.sha)

def create_file():
    repo.create_file("created.txt","this is message created","It is content of remote cretded file")

def create_file_dir():
    repo.create_file("insidedir/createdirfile.txt","File inside dir","This is content of file inside Directory of newly creted file")

def update_file_dir():
    contents = repo.get_contents("insidedir/createdirfile.txt")
    repo.update_file(contents.path,"updated","Now it is updated",contents.sha)

def delete_file():
    contents = repo.get_contents("test2.txt")
    repo.delete_file(contents.path,"Deleted",contents.sha)

def delete_file_dir():
    contents = repo.get_contents("insidedir/createdirfile.txt")
    repo.delete_file(contents.path,"Deleted",contents.sha)

if __name__ == "__main__":
    # get_dirname()
    # list_all_file()
    # get_file_by_name()
    # list_all_file1()
    # printing_file_data_dir()
    # create_file()
    # update_file()
    # create_file_dir()
    # update_file_dir()
    # delete_file()
    delete_file_dir()


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



#create inside directory file
'''
from github import Github

# Authenticate with your GitHub username and password
g = Github("username", "password")

# Get the repository
repo = g.get_repo("user/repo")

# Create the directory if it doesn't exist
path = "/insidedir/createdirfile.txt"
if not repo.get_contents(path):
    repo.create_file(path, "File inside dir", "This is content of file inside Directory of newly created file")
'''
