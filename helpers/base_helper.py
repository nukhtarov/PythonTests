def get_filtered_animal_name(pet_list: list) -> list:
    count = list()
    for pet in pet_list:
        category = pet.get('category', None)
        if category and "string" not in category.get('name'):
            count.append(category.get('name'))
    print(count)
    return count


def get_animal_with_photo(pet_list: list) -> dict:
    count = list()
    for pet in pet_list:
        if pet.get('photoUrls'):
            count.append(category.get('name'))
    return count
