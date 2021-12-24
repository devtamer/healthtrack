# Setup Notes for PgAdmin 4 and PostgreSQL 12 on MacOS

1. If you do not have Homebrew installed on your Mac, do so by running this in the terminal:
<code>/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"</code> 

2. Install PostgreSQL 12.9 by running: <code>brew install postgresql@12</code>

3. Install PgAdmin4 by running: <code>brew install --cask pgadmin4</code>

4. Verify that PostgreSQL is on your path by running <code>psql -V</code> to check the current version.
    - If this command returns an error of not found, then you need to add the location to the path
    - Run: <code>echo 'export PATH="/usr/local/opt/postgresql@12/bin:$PATH"' >> ~/.zshrc</code>

