FILE_NAME = "allow_list.txt"

def get_allowed_ips(file_name:str=FILE_NAME):
    with open(file_name, "r") as file:
        for allowed_addr in file.readlines():
            yield allowed_addr.strip()

def is_in_file(addr:str, file_name:str=FILE_NAME) -> bool:
    for allowed_addr in get_allowed_ips(file_name):
        if addr == allowed_addr:
            return True
    return False

def remove_ips(remove_list:list|set|tuple, file_name:str=FILE_NAME)->None:
    remove_set = set(remove_list)
    new_list = []
    for item in get_allowed_ips(file_name):
        if item not in remove_set:
            new_list.append(item)
    with open(file_name, "w") as file:
        file.write("\n".join(new_list))

def add_ips(add_list:list|set|tuple, file_name:str=FILE_NAME)->None:
    new_list = set()
    for item in get_allowed_ips(file_name):
        new_list.add(item)
    for item in set(add_list):
        new_list.add(item)
    new_list = list(new_list)
    with open(file_name, "w") as file:
        file.write("\n".join(new_list))

def main():
    add_list = [
        "12.34.56.211",
        "12.34.56.211",
        "12.24.53.212",
    ]
    add_list.extend((f"12.24.53.{x}" for x in range(0,128)))
    add_list.extend((f"12.24.51.{x}" for x in range(0,128)))
    add_ips(add_list)
    tests = ("12.34.56.211", "12.24.53.212", "1.1.1.1", "12.24.51.12",)
    for tester in tests:
        print(f"{tester} in file? {is_in_file(tester)}")
    remove_list = [
        "12.24.51.12",
        "12.24.51.18",
        "12.24.51.101", 
    ]
    remove_ips(remove_list)
    print(f"removal finished for {remove_list}.")
    for tester in tests:
        print(f"{tester} in file? {is_in_file(tester)}")

if __name__ == "__main__":
    main()