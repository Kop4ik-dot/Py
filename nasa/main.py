from space_photo import SpacePhoto
from json_storage import JsonStorage
import deepl

API_KEY = "2buUh7TBSJnEtdEx13XoM5fjYBYJbaWnWbdh1JiR"


def main():
    photo = SpacePhoto(API_KEY)
    photo.load()
    photo.show_info()

    storage = JsonStorage()
    storage.save_entry(photo.load())
    print("File saved in ", storage.filename)

if __name__ == "__main__":
    main()
    #json
