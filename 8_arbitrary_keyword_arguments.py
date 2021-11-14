# ** causes python to create an empty dictionary and accept entries

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know abvout a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)