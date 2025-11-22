from space_photo import SpacePhoto
import deepl

API_KEY = "2buUh7TBSJnEtdEx13XoM5fjYBYJbaWnWbdh1JiR"


def main():
    photo = SpacePhoto(API_KEY)
    photo.load()
    photo.show_info()

if __name__ == "__main__":
    main()