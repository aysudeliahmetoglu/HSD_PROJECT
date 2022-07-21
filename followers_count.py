import instaloader

instagram = instaloader.Instaloader()
instagram.load_session_from_file("aysudeliahmetoglu")
profile=instaloader.Profile.from_username(instagram.context,"instagram")
print("Number of followers:", profile.followers)
followers= profile.get_followers()
followers_list = list()


for i in followers: 
    followers_list.append(i.username)
print(followers_list)