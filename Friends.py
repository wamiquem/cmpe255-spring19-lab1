users =[
    { "id":0, "name": "Hero" },
    { "id":1, "name": "Dunn" },
    { "id":2, "name": "Sue" },
    { "id":3, "name": "Chi" },
    { "id":4, "name": "Thor" },
    { "id":5, "name": "Clive" },
    { "id":6, "name": "Hicks" },
    { "id":7, "name": "Devin" },
    { "id":8, "name": "Kate" },
    { "id":9, "name": "Klein" }    
]

friendship = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 6),
    (6, 7),
    (6, 8),
    (7, 8),
    (8, 9)
]

#added flag as an argument in this method so that the print is executed only when this method is called specifically
def num_friends(user, flag):
    '''
    Find number of friends for a given user
    '''

    #for the specified user, get the id from the list of dictionary
    for user_data in users:
        if user_data["name"] == user:
            user_id = user_data["id"]
    
    #counter to track total number of friends
    num_of_friends = 0
    
    #increment ‘num_of_friends’ for each tuple if user_id exists in the list of tuple ‘friendship’ 
    for friendship_data in friendship:
        if friendship_data[0] == user_id or friendship_data[1] == user_id:
            num_of_friends += 1
    
    #using below string variable to hold “friends” for multiple friends or “friend” for single friend
    friend_tag = "friends"
    if num_of_friends == 1:
        friend_tag = "friend"
    if flag == True:
        print("**Number of Friends**")
        print(user + " has %d " %num_of_friends + friend_tag)
    
    #returning num_of_friends to reuse this method in the method sort_by_num_friends() 
    return num_of_friends

def sort_by_num_friends():
    '''README.md
    Sort from "most friends" to "least friends"
    '''
    
    #below list will be appended with tuple of all user and corresponding number of friends
    sorted_friends_list = []
    
    #for each user, get the number of friends from the method num_friends and append this as a tuple in the sorted_friends_list
    for user in users:
        num_of_friends = num_friends(user["name"],False)
        sorted_friends_list.append((num_of_friends,user["name"]))
    
    #sort the list sorted_friends_list by using the library method sort(). reverse=True for descending sort
    sorted_friends_list.sort(reverse=True)
    
    print("**Sorting - Max to min Friends**")
    for friend in sorted_friends_list:
        friend_tag = "friends"
        if friend[0] == 1:
            friend_tag = "friend"
        print(friend[1] + " has %d " %friend[0] + friend_tag)

num_friends("Hero", True)

sort_by_num_friends()
