data=[{
"name": "Spidey One way home",
 "release_year": "2021",
 "rating": 9,
 "starring": [
 "Tom Hanks",
 "Tom Holland",
 "Mark Zucks",
 "Samy"],
 "runtime": 120,
 "totalReviews": 2000,
 "director": "Jon What"},
 {
 "name": "The Arrival of a Train",
 "release_year": "1896",
 "rating": 6,
 "starring": [
 "Shawn Ching",
 "Looker Blindspot",
 "Tom Hanks"],
 "runtime": 115,
 "totalReviews": 720,
 "director": "Ricky"},
 {
 "name": "Lost persuit of adventure",
 "release_year": "2005",
 "rating": 7.1,
 "starring": [
 "Jimmy simmon",
 "Catarina"],
 "runtime": 150,
 "totalReviews": 823,
 "director": "Ricky"},
 {
 "name": "Jungle Warrior",
 "release_year": "2016",
 "rating": 5.9,
 "starring": [
 "Stormer",
 "Carmony",
 "Tom Hanks"],
 "runtime": 150,
 "totalReviews": 1368,
 "director": "Whim Wailer"},
 {
 "name": "The Last of the us all",
 "release_year": "2005",
 "rating": 8.5,
 "starring": [
 "Samy",
 "George wise",
 "Pennywise"],
 "runtime": 120,
 "totalReviews": 1800,
 "director": "Jon What"}]

while True:

    filtering = input(str("filter through movie=1 or rating=2 or year=3 : "))

    name,rating,year = None ,None,None

    if filtering == "1":
            name= input("enter keyword: ")
    if filtering == "2":
            rating = float(input("enter rating: "))
    if filtering == "3":
            year = int(input("release year: "))


    for i in data:    
        if name and name in i["name"]:
            print(i)

        if rating and rating <= float(i["rating"]):
            print(i)

        if year and year <= int(i["release_year"]):
            print(i)
