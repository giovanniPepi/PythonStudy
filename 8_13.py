def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know abvout a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Giovanni', 'Pepi', location='campinas', age=27, sex='Male')
print(user_profile)