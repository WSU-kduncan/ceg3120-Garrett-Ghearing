<h1> Command line git </h1>
<ul>
<li>clone</li>
<ol>
    <li>Clones a repistory into a new direcotry</li>
    <li>creates remote tracking for all the branches inside of it</li>
    <li>git clone "URL" or you can do git clone -l "file path"</li>
</ol>
<li>add</li>
<ol>
    <li>add files to be tracked</li>
    <li>prepares the tracked files to be ready for a commit</li>
    <li>holds a snapshot of the content within the working tree it is this snapshot that is pushed with a commit </li>
    <li>  git add "filepath" or git commit -a -m " message here "
</ol>
<li>rm</li>
<ol>
    <li>removes file from the working tree and the index</li>
    <li>in order for git rm the files must be identical to each other or else it will fail</li>
    <li>git rm "filename"</li>
</ol>
<li>commit</li>
<ol>
    <li>creates a new commit containning the current snapshots of the index from git add</li>
    <li>prompts a request for a message log</li>
    <li>git commit -a -m "testing markdown formatting"</li>
</ol>
<li>push</li>
<ol>
    <li>updates remote side by using the refs done with git add and git commit. refs come from the local sides</li>
    <li>git push</li>
</ol>
<li>fetch</li>
<ol>
    <li>downloads objects and refs from another git repo</li>
    <li>you can use special tags in order to download everything or mutliple files form a single repo while using one command</li>
    <li> git fetch origin or u can do something like git fetch "Path to the proper branch"</li>
</ol>
<li>merge</li>
<ol>
    <li>you can use git merge to put a combine a forked history into one aka merge branches together</li>
    <li>git merge works by merging the specified branch into the branch u are currently in it is alawyas a good idea to use git status before performing a git merge just to make sure u are in the right one</li>
    <li>git merge "branchname"</li>
</ol>
<li>pull</li>
<ol>
    <li>if the local branch is not up to date using this command will automatically pull the information form the git repo to make the local up to date.</li>
    <li> if not specified git pull will pull form the directory u are currently in if u want to pull from somewhere else you need to specify</li>
    <li>git pull </li>
    
    
</ol>
<li>branch</li>
<ol>
    <li>this command can be used to create,list and delete git branches</li>
    <li>the purpose of the branch command is to allow you to work on a project without directly affecting the live product  </li>
    <li>git branch "new Branch name"  git branch -D to force delete the branch. git branch -a will list all remote branches</li>
</ol>
<li>checkout</li>
<ol>
    <li>you can use git checkout to swtich branches or if needed to restore a working tree files</li>
    <li>update files within working branch to match the index if you want to update from somewhere else you must clarify what branch</li>
    <li>git checkout "branchname"</li>
</ol>
</ul>
<h1> git files & folders </h1>
<ul>
<li>.git folder </li>
<ol>
    <li></li>
    <li></li>
    <li></li>
</ol>
<li>.gitignore file</li>
<ol>
    <li> a .gitignore file is a file that doesnt not allow for the files inside of it git commited or pushed to git repo it is a good folder to keep from accidentally uploading private information like passwords  </li>
    <li>touch .gitignore then move files into the this</li>
</ol>
</ul>
<h1> GitHub </h1>

<ul>
<li>Pull requests</li>
<ol>
    <li></li>
    <li></li>
    <li></li>
</ol>
<li>SSH authentication to repositories</li>
<ol>
    <li></li>
    <li></li>
    <li></li>
</ol>
</ul>
<h1> Resources </h1>
<ul>
<li> man pages in command line </li>
<li>atlasssian.com</li>
</ul>
