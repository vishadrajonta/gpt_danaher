#Goal: To get one caption downloaded and stored to a variable. The latest one, why not? 

import instaloader


import instaloader
test = instaloader.Instaloader()
acc = input('Enter the Account Username: ')
test.download_profile(acc, profile_pic_only = False)

