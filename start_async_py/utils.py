import secrets
from os import path

RANDOM_SEED_SIZE = 10


def generate_random_seed():
    return secrets.token_urlsafe(RANDOM_SEED_SIZE)


def generate_api_url(seed, avatar_style, base_url, extension=".png"):
    url = base_url.format(avatar_style=avatar_style, seed=seed+extension)
    print(url)
    return url 



def write_to_file(data: str, file_name: str, file_path: str = "my_profile_pics"):
    try:
        with open(path.join(file_path, file_name+".png"), "wb") as file:
            file.write(data)
    except Exception as e:
        print(f"\n\n\n{e}\n\n")
