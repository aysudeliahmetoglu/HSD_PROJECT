import instaloader

instagram = instaloader.instaloader()
instagram.load_session_from_file("aysudeliahmetoglu")
profile=instaloader.Profile.from_username(instagram.context,"hsdyalova")
print("Takipçi sayısı:", profile.followers)
takipciler = profile.get_followers()
takipciler_listesi = list()


for i in takipciler: 
    takipciler_listesi.append(i.username)
print(takipciler_listesi)