madlib_dict = {
    "noun": "",
    "adjective": "",
    "verb": "",
}

madlib_dict["noun"] = input("Enter a noun: ")
madlib_dict["adjective"] = input("Enter an adjective: ")
madlib_dict["verb"] = input("Enter a verb: ")

print("The %s was over near the creek. It went walking too close and fell into the %s water.  As it floated down the creek, it %s and got stuck." %
      (madlib_dict["noun"], madlib_dict["adjective"], madlib_dict["verb"]))
