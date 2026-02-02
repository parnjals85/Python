# Dictionary ek data structure hai jo key : value pair me data store karta hai.

# capitals = {
#     "India : New Delhi",
#     "Usa : Wasigton DC",
#     "Germeny : Berlin",
#     "Russia : Moscow" }
# # print(dir(capitals));
# # print(help(capitals));
# print(capitals.get("India"))


capitals = {
    "India": "New Delhi",
    "USA": "Washington DC",
    "Germany": "Berlin",
    "Russia": "Moscow"
}
# print(capitals.get("USA"))
# capitals.update({"Afanistan : Kabul"})
capitals.pop("Germany")
capitals.popitem() #clear the latets Key Value Pair
capitals.clear()
print(capitals)
