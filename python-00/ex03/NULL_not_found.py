def NULL_not_found(object: any) -> int:
    obj_type = type(object)

    if object:
        if object != object:
            print(f"Cheese: {object} {obj_type}")
        else:
            print(f"Type not found")
            return 1
    else:
        if object is None:
            print(f"Nothing: {object} {obj_type}")
        elif object is False:
            print(f"Fake: {object} {obj_type}")
        elif object == 0:
            print(f"Zero: {object} {obj_type}")
        elif object == "":
            print(f"Empty: {object} {obj_type}")
    return 0


def main():
    return 

if __name__ == '__main__':
    main()