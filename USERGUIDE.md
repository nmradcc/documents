# Developer's Guide
This guide serves to provide step-by-step training and procedures for the development of NMRA DCC Standards, Recommended Practices, Technical Notes, and other documents using this GitHub NMRA Documents repository.

# Purpose of using Git and GitHub
1. Maintain a fully attributed, fully commented history of development
2. Defect (issue) tracking
3. Ensure public oversite

# Repository Structure
Fundamentally, there are two top level directories: [drafts](drafts) and [standards](standards). Documents that are undergoing revision are created in or copied to the [drafts](drafts) directory. Once a document has been peer reviewed and approved, it is copied to the [standards](standards) directory and removed from the [drafts](drafts) directory.

There is a third top level directory: [templates](templates). This is where document templates which can be used as starting points for new documents can be found. (TBD, this doesn't exist yet, work in progress).

# Github Desktop Workflow
[GitHub Desktop](https://desktop.github.com/) is a GUI based interface for interacting with GitHub. While it is not as feature rich as other Git clients, it is easier for novice users to get started with. [GitHub Desktop](https://desktop.github.com/) os available as a free download for Linux, Mac OS X, and Windows.

## GitHub Desktop Setup
When opening GitHub Desktop for the first time, you will be asked for your GitHub login credentials. These are the same credentials (username and email) that you used when granted access to the NMRA Documents repository.

The first thing you will want to do is "clone" the nmradcc/documents repository. "Cloning" is the act of downloading a copy of the repository to your local computer. If you are tracking a large number of GitHub projects, then typing "nmradcc" into the search bar will narrow down the list of repositories.
1. type nmradcc into the search bar
2. select nmradcc/documents
3. select "clone nmradcc/documents" button.
<img src="https://user-images.githubusercontent.com/2278798/90160917-0214ce80-dd58-11ea-9424-db82a4565dd2.png" width="800" />

4. Choose a location on your computer at which the repository will be cloned. This can be anywhere, but the location should be rememberd, as this is the location from which the documents will be edited.
<img src="https://user-images.githubusercontent.com/2278798/90161602-ff66a900-dd58-11ea-9d8a-1aa97df4820f.png" width="400" />

As you can see, there is now a complete copy of the respository on the local computer.
<img src="https://user-images.githubusercontent.com/2278798/90166313-a51d1680-dd5f-11ea-8c48-9152c575502b.png" width="800"/>

## Creating a New Document
### Branching
New documents should be created in the drafts folder on a new branch. A branch is a unique view of the repository and its contents. Changes made on one branch are not visable on another branch, which is a useful feature for when a document is still in development. A Git repository always has a special branch called "master". The "master" branch is the primary view that most people will see by default, and is typically the staring point for all other branches. A branch can have any name as long as it is unique. The branch name should generally descibe the work to be done on that branch.

<img src="https://user-images.githubusercontent.com/2278798/90162661-9d0ea800-dd5a-11ea-9a57-93ca61a84450.png" width="800"/>
<img src="https://user-images.githubusercontent.com/2278798/90163013-232aee80-dd5b-11ea-9f74-012f084d071b.png" width="400"/>
<img src="https://user-images.githubusercontent.com/2278798/90164052-88331400-dd5c-11ea-97c4-c691ec7ef974.png" width="800"/>

### Saving New Document
The new document can simply be saved in the local file system in the location where the repository was previously cloned.
