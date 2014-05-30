# Facebook Selenium

Selenium test for Facebook. Login and click friend requests,
private messages and notifications buttons

## This section is for setting up
```
pip install virtualenv
virtualenv facebook
```

## Used as a reminder on how to setup good commit
```
source facebook/scripts/activate
pip install -r requirements.txt
cd .git/hooks
ln -s ../../pre-commit.sh pre-commit
cd -
```

## For running the tests

```
touch facebook/lib/site-packages/facebook.pth

echo "~/code/py/facebook_selenium" >> facebook/lib/site-packages/facebook.pth

python tests/test_facebook.py
```
