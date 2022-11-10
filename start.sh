if [ -z $SOURCE_CODE ]
then
  echo "Cloning main Repository"
  git clone https://github.com/maullikpatell/trial-one.git /trial-one
else
  echo "Cloning Custom Repo from $SOURCE_CODE "
  git clone $SOURCE_CODE /trial-one
fi
cd /trial-one
pip install --upgrade pip
pip3 install -U -r requirements.txt
echo "Starting Bot...."
python3 -m main.py
