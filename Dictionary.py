# dictionary = {"key":"value"}

dict={"fname":"prabal",
      "lname":"kuinkel"}

# print(dict.get("fname2"))  since fname2 doesnot exist as key in dictionary ..this line wont throw error
print(dict["fname"])


# TO ACCESS ALL THE KEYS
      # method-1:access all at once
print(dict.keys())
      # method-2:access one key at a time
for keys in dict.keys():
      print(keys)
      print(dict[keys])

# TO ACCESS ALL THE VALUES
      # method-1:access all at once
print(dict.values())
      # method-2:access one value at a time
for values in dict.values():
      print(values)

