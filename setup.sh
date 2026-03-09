
wget https://www.python.org/ftp/python/3.10.8/Python-3.10.8.tgz
tar xzf Python-3.10.8.tgz
rm Python-3.10.8.tgz
cd Python-3.10.8
./configure --enable-optimizations --prefix=$HOME
make altinstall prefix=~/local
cd ../
rm .bash_profile

echo 'export PATH=$HOME/local/bin:/usr/local/bin:/usr/bin:/bin:/usr/local/games:/usr/games' >>~/.bash_profile

cp $HOME/local/bin/python3.10 $HOME/local/bin/python3

$HOME/local/bin/python3 -V
$HOME/local/bin/python3 -V
$HOME/local/bin/python3 -m pip install --upgrade pip
$HOME/local/bin/python3 -m pip install -r core8/requirements.txt
$HOME/local/bin/python3 -m pip install -r requirements.in
$HOME/local/bin/python3 -m pip install wikitextparser
$HOME/local/bin/python3 -m pip install pipreqs
$HOME/local/bin/python3 -m pip install requests
$HOME/local/bin/python3 -m pip install python-dateutil
$HOME/local/bin/python3 -m pip install --upgrade regex==2022.10.31
rm -r -f Python-3.10.8
