#----- Git basic operations ----------------------------------------------------------------#
git init 	# in the target directory, initialize it as a repository
git init newrepo	# make the existed directory as a repository

#---Most commonly used operations---
git add filename
git commit -m "Adding files"
git commit -a -m "Changed some files"	# -a do not commit new files, only commit changes
git push origin master
#-----------------------------------

git clone ssh://example.com/~/www/project.git	# clone from remote
git push origin master			# here origin is remote repo, master is local repo
git push ssh://example.com/~/www/project.git	# push the current local repo
git pull	# merge the remote repo
git pull http://git.example.com/project.git		# clone from the non-default repo

git rm file
git branch test		# build a new branch
git checkout test	# change to other branch
git checkout master # change to the main/first/default branch
git merge test		# merge changes in test(branch) to master(branch)
git branch -d test	# delete test(branch)
#-------------------------------------------------------------------------------------------#
