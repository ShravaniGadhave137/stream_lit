import instaloader

# Create an instance of Instaloader
loader = instaloader.Instaloader()

# Set the profile name of the Instagram account you want to download posts from
profile_name = 'instagram_profile_name_here'

# Load the profile
profile = instaloader.Profile.from_username(loader.context, profile_name)

# Iterate over the posts and download them
for post in profile.get_posts():
    loader.download_post(post, target=profile_name)

print(f"Downloaded posts from {profile_name}")
