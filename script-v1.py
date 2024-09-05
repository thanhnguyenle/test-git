import git
import os

class GitRepoManager:
    def __init__(self, repo_url, clone_dir):
        """
        Initialize the GitRepoManager with repository URL and clone directory.
        """
        self.repo_url = repo_url
        self.clone_dir = clone_dir
        self.repo = None

    def clone_repo(self, branch=None):
        """
        Clone the repository into the specified directory. Optionally, clone a specific branch.
        """
        if os.path.exists(self.clone_dir):
            print(f"Repository already exists at {self.clone_dir}")
            self.repo = git.Repo(self.clone_dir)
        else:
            if branch:
                print(f"Cloning branch {branch} from {self.repo_url} to {self.clone_dir}")
                self.repo = git.Repo.clone_from(self.repo_url, self.clone_dir, branch=branch)
            else:
                print(f"Cloning default branch from {self.repo_url} to {self.clone_dir}")
                self.repo = git.Repo.clone_from(self.repo_url, self.clone_dir)
        
        return self.repo

    def checkout(self, ref):
        """
        Checkout to a specific branch, tag, or commit hash.
        """
        if self.repo is None:
            raise ValueError("Repository not cloned yet. Use clone_repo() first.")

        print(f"Checking out to {ref}")
        self.repo.git.checkout(ref)

    def fetch_all_tags(self):
        """
        Fetch all tags in the repository.
        """
        if self.repo is None:
            raise ValueError("Repository not cloned yet. Use clone_repo() first.")
        
        print("Fetching all tags...")
        self.repo.git.fetch('--tags')

    def get_current_commit_hash(self):
        """
        Get the current commit hash.
        """
        if self.repo is None:
            raise ValueError("Repository not cloned yet. Use clone_repo() first.")
        
        return self.repo.head.commit.hexsha

    def pull_latest(self):
        """
        Pull the latest changes from the remote repository for the current branch.
        """
        if self.repo is None:
            raise ValueError("Repository not cloned yet. Use clone_repo() first.")
        
        print("Pulling latest changes...")
        self.repo.remotes.origin.pull()

# Example usage
if __name__ == "__main__":
    repo_url = "https://github.com/your-repo.git"
    clone_dir = "/path/to/your/clone"
    
    git_manager = GitRepoManager(repo_url, clone_dir)
    
    # Clone the repository (default branch or a specific branch)
    git_manager.clone_repo(branch="main")  # Replace with your branch if needed

    # Checkout a specific branch, commit, or tag
    git_manager.checkout("a_commit_hash_or_tag")  # Use actual ref

    # Optionally fetch all tags if needed
    git_manager.fetch_all_tags()

    # Pull the latest changes from the current branch
    git_manager.pull_latest()

    # Get the current commit hash
    current_commit = git_manager.get_current_commit_hash()
    print(f"Current commit hash: {current_commit}")
