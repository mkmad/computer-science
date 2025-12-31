#!/bin/bash

# Exit on error
set -e

# Set Git Credentials
echo "Configuring Git Credentials..."
git config user.name "mkmad"
git config user.email "mohan.madhavan@yahoo.com"

# Ensure SSH Config exists
SSH_CONFIG_PATH="$HOME/.ssh/config"
HOST_ENTRY="Host github.com-mkmad"

if [ ! -f "$SSH_CONFIG_PATH" ] || ! grep -q "$HOST_ENTRY" "$SSH_CONFIG_PATH"; then
    echo "Adding SSH config for github.com-mkmad..."
    mkdir -p "$HOME/.ssh"
    cat <<EOT >> "$SSH_CONFIG_PATH"

#mkmad account
Host github.com-mkmad
   HostName github.com
   User git
   IdentityFile ~/.ssh/mkmad
   IdentitiesOnly yes
EOT
else
    echo "SSH config for github.com-mkmad already exists."
fi

# Update Submodules
echo "Updating submodules..."
# We use --init in case any new submodules were added
# We use --recursive to handle nested submodules
# We use --remote to fetch the latest changes from the remote branch
# We use --merge to merge the remote changes into the local branch
git submodule update --init --recursive --remote --merge

echo "Submodule update complete!"
