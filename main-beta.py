import instaloader
import time

def download_instagram_photos(username, target_directory):
    loader = instaloader.Instaloader(download_pictures=True, download_videos=False, 
                                     download_video_thumbnails=False, download_geotags=False, 
                                     download_comments=False, save_metadata=False, dirname_pattern=target_directory)
    
    # login
    # loader.login(USERNAME, PASSWORD)

    # Load profile
    profile = instaloader.Profile.from_username(loader.context, username)

    print(f"Stored ID {profile.userid} for profile {username}.")
    
    # Profile pic
    loader.download_profilepic(profile)

    print(f"{username}\\{profile.profile_pic_url.split('/')[-1]}")
    print(f"Retrieving posts from profile {username}.")

    count = 0

    for post in profile.get_posts():
        loader.download_post(post, target=profile.username)
        count += 1
        
        print(f"[ {count}/{profile.mediacount} ] {post.date_utc}_UTC.jpg json")

        # todo another way to recive more photos
        if count % 12 == 0:
            print("Waiting for 60 seconds to avoid rate limit issues...")
            time.sleep(60)

if __name__ == "__main__":
    instagram_username = input("Enter the Instagram username: ")
    target_directory = input("Enter the target directory for downloads: ")

    download_instagram_photos(instagram_username, target_directory)
