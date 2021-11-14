#from build_profile import build_profile

#user_profile = build_profile('Giovanni', 'Pepi', location='campinas', age=27, sex='Male')

#import build_profile

#build_profile.build_profile('Giovanni', 'Pepi', location='campinas', age=27, sex='Male')
#print(user_profile)

from build_profile import build_profile as bp

user_profile = bp('Giovanni', 'Pepi', location='campinas', age=27, sex='Male')

