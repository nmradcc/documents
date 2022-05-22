# Developer Guide
This guide serves to provide step-by-step training and procedures for the development of NMRA DCC Standards, Recommended Practices, Technical Notes, and other documents using this GitHub NMRA Documents repository.

- [Purpose of using Git and GitHub](#purpose-of-using-git-and-github)
- [Repository Structure](#repository-structure)
- [Github Desktop Workflow](#github-desktop-workflow)
  * [GitHub Desktop Setup](#github-desktop-setup)
  * [Creating a New Document](#creating-a-new-document)
    + [Branching](#branching)
    + [Saving New Document](#saving-new-document)
  * [Committing Changes](#committing-changes)
  * [Publishing a Document](#publishing-a-document)
  * [Fetching Changes From GitHub](#fetching-changes-from-github)
- [Releasing a Document from drafts to standards](#releasing-a-document-from-drafts-to-standards)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>

# Purpose of using Git and GitHub
1. Maintain a fully attributed, fully commented history of development
2. Defect (issue) tracking
3. Ensure public oversite

# Repository Structure
Fundamentally, there are two top level directories: [drafts](drafts) and [standards](standards). Documents that are undergoing revision are created in or copied to the [drafts](drafts) directory. Once a document has been peer reviewed and approved, it is copied to the [standards](standards) directory and removed from the [drafts](drafts) directory.

There is a third top level directory: [templates](templates). This is where document templates which can be used as starting points for new documents can be found. (TBD, this doesn't exist yet, work in progress).

# Github Desktop Workflow
[GitHub Desktop](https://desktop.github.com/) is a GUI based interface for interacting with GitHub. While it is not as flexible as other Git clients, it is easier for novice users to get started with and contains the necessary features. [GitHub Desktop](https://desktop.github.com/) os available as a free download for Linux, Mac OS X, and Windows. Advanced Git users may choose to use other Git clients at their own discression.

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
New documents should be created in the [drafts](drafts) folder on a new branch. A branch is a unique view of the repository and its contents. Changes made on one branch are not visable on another branch, which is a useful feature for when a document is still in development. A Git repository always has a special branch called "master". The "master" branch is the primary view that most people will see by default, and is typically the staring point for all other branches. A branch can have any name as long as it is unique. The branch name should generally descibe the work to be done on that branch.

<img src="https://user-images.githubusercontent.com/2278798/90162661-9d0ea800-dd5a-11ea-9a57-93ca61a84450.png" width="800"/>
<img src="https://user-images.githubusercontent.com/2278798/90163013-232aee80-dd5b-11ea-9f74-012f084d071b.png" width="400"/>
<img src="https://user-images.githubusercontent.com/2278798/90164052-88331400-dd5c-11ea-97c4-c691ec7ef974.png" width="800"/>

### Saving New Document
The new document can simply be saved in the computer's local file system in the location where the repository was previously cloned.

<img src="https://user-images.githubusercontent.com/2278798/90174804-28dd0000-dd6c-11ea-9d08-f1e3fd60eb43.png" width="800"/>

Moving back over to the GitHub Desktop application, The new file should be present present and listed as "changed". At this point, the Git Repository knows nothing about the new document. In order for it to become part of the git repository, we need to commit it.

<img src="https://user-images.githubusercontent.com/2278798/90179450-17e3bd00-dd73-11ea-99af-d3a844964657.png" width="800"/>

## Committing Changes
Anytime that a document is updated, the resulting work should be "committed" to the repository in order to save the changes.
<img src="https://user-images.githubusercontent.com/2278798/90180207-41511880-dd74-11ea-82f5-02399ee5cf73.png" width="800"/>

After committing changes, they still only reside on the local computer, it is important to publish those changes to GitHub so that others can see them. Publishing insures that a copy resides on the GitHub server, and that the committed changes are recoverable even if the local computer were to crash and loose its local copy.
<img src="https://user-images.githubusercontent.com/2278798/90180711-ff74a200-dd74-11ea-87fb-c6f96fc1ca0f.png" width="800"/>

## Publishing a Document
Once a document is ready to be published, the development branch can be merged into the "master" branch. This is accomplished by using a [Pull Rquest](https://github.com/nmradcc/documents/pulls). Choose the option "New pull request".
<img src="https://user-images.githubusercontent.com/2278798/90181271-cb4db100-dd75-11ea-87be-dc36fa9f86ce.png" width="800"/>

Choose the branch that you are merging to on the left, typically "master". Choose the branch you are merging from on the right, in this example "new-document-example". Choose "Create pull Request".
<img src="https://user-images.githubusercontent.com/2278798/90181568-4adb8000-dd76-11ea-8d5a-423fd5948465.png" width="800"/>

At this point, you may optionally modify the name, leave comments, add reviewers, add assignees, and/or add labels. These can also be added later. Once satisfied, choose "Create pull request".
<img src="https://user-images.githubusercontent.com/2278798/90182412-8a569c00-dd77-11ea-9616-664689893668.png" width="800"/>

Once having addressed any applicable review comments the branch may be merged. Note that a reviewer is not necessarily required to complete the merge. Select the option "Squash and merge". If this is your first time merging, you may need to click the down arrow in the green box to select the "Squash and merge" option. Once the operation is complete, you will be given an option to delete the branch. You may continue to add changes to the branch, however, if you are finished with using the branch, it is a good idea to delete it in order to remove clutter.

<img src="https://user-images.githubusercontent.com/2278798/90182848-313b3800-dd78-11ea-83c9-a29a0b186691.png" width="800"/>

## Fetching Changes From GitHub
Often times it is necessary to update the local copy of the repository on your computer. This can be done with a fetch operation. in this example, we move to the master branch and fetch the latest changes, which include the previously merged of the "new document example".
1. Make sure that the current branch is "master".
2. Click on "Fetch origin".
<img src="https://user-images.githubusercontent.com/2278798/90183883-defb1680-dd79-11ea-8228-37a2de5385af.png" width="800"/>

# Releasing a Document from drafts to standards
1. Finalize document.
   * Open document
   * Accept all changes and stop tracking
   * Remove "Draft" suffix from the Quick Parts Title field
   * Review and cleanup as needed whitespace
   * Add an entry to the Document History table with the published data and description
   * Update the Table of Contents (if applicable), "update all fields"
   * Save and close document
   * Commit or upload document to Git (document is still in drafts folder at this point)
2. Merge working branch back to master (document is still in drafts folder at this point).
   * A pull request should be used for this purpose
3. Create a new branch for the adoption process.
   * git checkout master
   * git pull
   * git checkout -b \<username\>-adopt-\<document identifier\>
     - text inside of \<\> should be replaced
4. Delete the files from the standars director. This step should be skipped if adopting a standard into the repository for the first time, and there are no previously adopted files.
   * git rm standards/S-9.x.x.x.docx
   * git rm standards/S-9.x.x.x.pdf
5. Commit the document removal to the branch.
6. Move the files from draft to standards.
   * git mv {drafts,standards}/S-9.x.x.x.docx
   * git mv {drafts,standards}/S-9.x.x.x.pdf
7. Commit the document move to the branch.
8. Create a pull request with these changes on GitHub. Ask a maintainer to review the pull request.
9. IMPORTANT: The PR must be merged with a "Create a merge commit" option.
10. Delete branch.
