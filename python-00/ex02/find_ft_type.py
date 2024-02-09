def all_thing_is_obj(item) -> int:
    if isinstance(item, list):
        print(f"List : {type(item)}")
    elif isinstance(item, tuple):
        print(f"Tuple : {type(item)}")
    elif isinstance(item, set):
        print(f"Set : {type(item)}")
    elif isinstance(item, dict):
        print(f"Dict : {type(item)}")
    elif isinstance(item, str):
        print(f"{item} is in the kitchen : {type(item)}")
    else:
        print(f"Type not found")
    return 42

def main():
    return 

if __name__ == '__main__':
    main()