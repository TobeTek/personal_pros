import requests
import utils 

def create_new_avatar(avatar_style:str, base_url:str):    
    seed = utils.generate_random_seed()
    request_url = utils.generate_api_url(seed=seed, avatar_style=avatar_style, base_url=base_url)
    resp = requests.get(request_url)
    data = resp.content
    utils.write_to_file(data=data, file_name=seed, file_path=r"C:/Users/user/desktop/pp")
