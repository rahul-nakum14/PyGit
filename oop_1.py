from github import Github
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--createfile",help="Input domain file")
parser.add_argument("--uploadfile",help="Write output to file")
args = parser.parse_args()

class test:
    g = Github("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")
    repo = g.get_repo("rahul-nakum14/test")

    def create_file(self,filename):
            self.repo.create_file(filename,"this is message created"," ")

    def upload_file(self, filename):
        try:
            with open(filename, 'r') as f:
                content = f.readlines()
                self.repo.create_file(filename, "".join(content), "")
        except GithubException:
            print("A GithubException occurred:")



    # def delete_file(self):
    #     contents = self.repo.get_contents("test2.txt")
    #     self.repo.delete_file(contents.path,"Deleted",contents.sha)

if __name__ == "__main__":
    obj = test()
    if args.createfile:
        obj.create_file(sys.argv[2])

    if args.uploadfile:
        obj.create_file(sys.argv[2])
    # obj.upload_file()
  
