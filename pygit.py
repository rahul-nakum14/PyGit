from github import Github

class github_test:
    def __init__(self) :
        self.token = Github("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")
        self.repo = self.token.get_repo("rahul-nakum14/test")
        self.file = self.repo.get_contents("")
    
    
    def get_dirname(self):
        for i in self.file:
            if i.type == "dir":
                print(i.name)
        

    def list_all_file(self): #except dir
        for i in self.file:
            if i.type == "dir":
                continue
            print(i.name)

    def list_all_file1(self): #include dir
        for i in self.file:
            if i.type == "dir":
                print(i.name+"/")
                continue
            print(i.name)

    def get_file_by_name(self, file_name, dir_name=None):
        if dir_name:
            file = self.repo.get_contents(dir_name + "/" + file_name)
            content = file.decoded_content.decode('utf-8')
            print(content)
        else:
            file = self.repo.get_contents(file_name)
            content = file.decoded_content.decode('utf-8')
            print(content)

    def create_file(self, file_name, commit_message, data, dir_name=None):
        if dir_name:
            self.repo.create_file(f"{dir_name}/{file_name}", commit_message, data)
        else:
            self.repo.create_file(file_name, commit_message, data)

    def update_file(self, file_name, commit_message, data, dir_name=None):
       
        if dir_name:
            contents = self.repo.get_contents(f"{dir_name}/{file_name}")
            self.repo.update_file(contents.path,commit_message,data,contents.sha)
        else:
            contents = self.repo.get_contents(file_name)
            self.repo.update_file(contents.path,"updated","Now it is updated",contents.sha)

    def delete_file(self, file_name, dir_name=None):
        if dir_name:
            contents = self.repo.get_contents(f"{dir_name}/{file_name}")
            self.repo.delete_file(contents.path,"Deleted",contents.sha)
        else:
            contents = self.repo.get_contents(file_name)
            self.repo.delete_file(contents.path,"Deleted",contents.sha)


if __name__ == "__main__":
    obj = github_test()
    # obj.list_all_file()
    # obj.get_dirname()
    # obj.get_file_by_name('test1.txt')
    # obj.list_all_file1()
    # obj.printing_file_data_dir("insidedir","dir_data.txt")
    # obj.create_file('eeeeeee.txt','commmmit message','eeeeeeeeeeeeee itsdata','insidedir')
    # obj.update_file('eeeeeeeeeeee4444.txt','message commit','updatedd',)
    # obj.delete_file('eeeeeee.txt','insidedir')
    # obj.get_file_by_name('dir_data.txt','insidedir')

    print('Enter which Op. you want to perform \n')
    print("[1] Get directory Name ")
    print("[2] Get list of all file (Not include directory)")
    print("[3] Get list of all file ( include directory)")
    print("[4] Read the content of file by name")
    print("[5] Create file")
    print("[6] Update file")
    print("[7] Delete file")

    choice = int(input("Enter Choice  "))

    try:
        match choice:
            case 1:
                obj.get_dirname()

            case 2:
                obj.list_all_file()

            case 3:
                obj.list_all_file1()
            
            case 4:
                file_name = input("Enter File Name ")
                dir_name = input("Enter Directory Name (Press Enter If Not) ")
                obj.get_file_by_name(file_name,dir_name)

            case 5:
                file_name = input("Enter File Name ")
                dir_name = input("Enter Directory Name (Press Enter If Not) ")
                commit_message = input("Enter Commit Message ")
                File_content = input("Enter File Content ")
                obj.create_file(file_name,commit_message,File_content,dir_name)

            case 6:
                file_name = input("Enter File Name ")
                dir_name = input("Enter Directory Name (Press Enter If Not) ")
                commit_message = input("Enter Commit Message ")
                File_content = input("Enter File Content ")
                obj.update_file(file_name,commit_message,File_content,dir_name)

            
            case 7:
                file_name = input("Enter File Name ")
                dir_name = input("Enter Directory Name (Press Enter If Not) ")
                obj.delete_file(file_name,dir_name)
            
    except Exception as e:
        print(str(e))
        
            

































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
    # list_all_file1()
























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
