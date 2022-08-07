# my posts on instagram

IG : clovis.lfbv

All of those repositories are the codes of my posts on instagram.

I advise you to use the blender software if you want to run the code of my 
second post, my third post or my fourth post.

Please don't forget to follow instagram account @clovis.lfbv to be notified 
when I publish a new post and leave a like to support me.

## Working on the files

### Cloning the repo

```sh
git clone git@github.com:clovislfbv/instagram_posts.git
```

Now, you're good to go!

### Workflow with branches

DON'T COMMIT OR PUSH TO MASTER

Create a new branch for each "feature".

It is recommended to create your new branch from master.
Little tutorial:
- Go on the command line and use `cd` to go to the main folder of the game (the one with the file `README.md` in it)
- Ask git to go on the `master` branch: `git checkout master` (note: if there is an error, STOP THERE and fix it, usually you need to commit some work, THINK TWICE BEFORE RUNNING `git stash`, it will more or less forget what you did
- Get the latest stuff from the `master` branch: `git pull`
- Actually create your new branch: `git switch -c my-super-cool-branch` (secret tip: replace `my-super-cool-branch` with the name of your new branch following this format: `[username]/[feature name]`)
- push for the first time, to create your new branch on GitHub: `git push --set-upstream origin my-super-cool-branch`
- Work
- add, commit, and so on
- push
- Create a Pull Request: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request
