# Computer Science Tutoring Center


In order to add a Git submodule: 

* git submodule add <remote_url> <destination_folder>
* git commit -m "Added the submodule to the project."
* git push



To remove a submodule you need to:

* Delete the relevant section from the .gitmodules file.
* Stage the .gitmodules changes git add .gitmodules
* Delete the relevant section from .git/config.
* Run git rm --cached path_to_submodule (no trailing slash).
* Run rm -rf .git/modules/path_to_submodule (no trailing slash).
* Commit git commit -m "Removed submodule "
* Delete the now untracked submodule files rm -rf path_to_submodule