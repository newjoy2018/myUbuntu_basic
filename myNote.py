source activate py3env_test
source deactivate	#in virtual env.

conda remove -n py3env --all

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
#-----About SSH-----#
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"	#generate a new ssh key
eval "$(ssh-agent -s)"		#Start the ssh-agent in the background
ssh-add ~/.ssh/id_rsa(name_above_defined)
xclip -sel clip < ~/.ssh/id_rsa.pub	# copy the public key and paste on Github
# The private and public ssh key should be in ~/.ssh
# Otherwise the permission will always be denied.
#-------------------------------------------------------------------------------------------#
#-----About Virtual Environment and Jupyter-----#
jupyter-notebook
python -m IPython notebook

#check which python are now using!
import sys
print(sys.executable)

# In the virtual environment, check if python and Jupyter runs in vir. Env.
which ipython
which jupyter 

# If not, use the following order to install them in the vir.env.
conda install jupyter
conda install ipython
#-------------------------------------------------------------------------------------------#

