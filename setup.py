from distutils.core import setup

words = open('python-xrcctrl.spec','r').read().split()
version=words[words.index('Version:')+1] 

if __name__=='__main__':
    setup(
     name='xrcctrl',
     version=version,
     packages=['xrcctrl']
    )

