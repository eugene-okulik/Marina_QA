my_dict = {}
my_dict["tuple"] = (3, 15, "Test", 27, 15)
my_dict["set"] = {36, 89, 11, "Bug", 89, 45}
my_dict["list"] = [52, "Homework", 4, 47, 2.52, "Test"]
my_dict["dict"] = {
    "one": "7",
    "two": [27, 35, 43],
    "three": "trip",
    "four": 56,
    "five": 98,
}

print(my_dict)
print(my_dict["tuple"][-1])
my_dict["list"].append("Summer")
my_dict["list"].pop(1)
my_dict["dict"][("i am a tuple",)] = "new value"
my_dict["dict"].pop("four")
my_dict["set"].add("Task")
my_dict["set"].remove(11)
print(my_dict)