# Alex Farrell Webb
# Student No : 201682162


def fifo(cache, requests):
    '''
    Summary : Iterates through the requests list and appends to cache. If the cache becomes full and 
    there are still remaining requests, pops the oldest page from the cache and adds from the request list.

    Arguments:

    cache (empty list) - memory bank cache to be filled from requests page
    requests (list of integers) - list of page requests to be iterated through and added to cache

    Returns:

    cache list of max size 8
    
    '''
    #iterates through list and either adds, doesn't add or removes then adds a page to cache from the requests list 
    for i in requests:
        if i in cache:
            print('hit')
        elif len(cache) < 8:
            print('miss')
            cache.append(i)
        else:
            print('miss')
            cache.pop(0)
            cache.append(i)   
    print(cache)

def lfu(cache, requests):   
    ''''   
    Summary : Iterates through the requests list and appends to cache. Uses a dictionary to record number of requests for each page.
    If the cache becomes full and there are still remaining requests, the page in the cache with the least requests is removed,and new page 
    from requests is added. In the event of more than one page in the cache having the minimum number of requests, the smallest value page 
    (lowest number) is removed, and a new page from requests is added.
    
    Arguments:

    cache (empty list) - memory bank cache to be filled from requests page
    requests (list of integers) - list of page requests to be iterated through and added to cache

    Returns:

    cache list of max size 8
    
    '''
    #creates a dictionary that will keep track of how many times each page has appeared in the requests list
    requestDic = {}
    #iterates over requests in list
    for i in requests:

        #if the page is already in the cache or the cache is not full, simply takes no action or adds requested page into empty space
        if i in cache:
            print('hit')
        elif len(cache) < 8:
            print('miss')
            cache.append(i)
        #if cache is full, dictionary is used to check which page has least number of requests    
        else:
            print('miss')
            #finds the lowest request number from the dictionary
            valueList = list(requestDic.values())
            minValue = min(valueList)
            #if there is only one page with the lowest number of requests, that page is deleted from the cache
            if valueList.count(minValue) == 1:
                for page, requestNo in requestDic.items():
                    if requestNo == minValue:
                        cache.remove(page)
                        cache.append(i)
            #creates two lists, one with the number of requests of each page currently in the cache called cacheRequests
            #from this list all the pages with the lowest number of requests are placed into KillList change names
            #from KillList the smallest numbered page is removed from the cache, and the new page is added.
            else:
                killList = []
                cacheRequests = []
                for page in cache:
                    cacheRequests.append(requestDic[page])
                for page in cache:
                    if requestDic[page] == min(cacheRequests):        
                        killList.append(page)
                cache.remove(min(killList))
                cache.append(i)        
        #dictionary is updated with new request info
        if i in requestDic:
            requestDic[i] += 1
        else: 
            requestDic[i] = 1
    print(cache)    


'''
Main program

Summary:

Sets empty values for cache and requests, ready for user input. User is prompted to enter integers one at a time indefinitely
until they wish to stop, at which point they press 0. Once they press 0 they are prompted to choose which method to use to create the 
memory bank cache: Press 1 for First in First out (fifo), or press 2 for Least Frequently Used (lfu). Alternatively they can press Q to quit 
the program. Once they make their choice the cache is created with one of the methods, printed to the screen, then wiped and the user is returned 
to the main menu where they can start the process again.

'''
#first While loop is the 'main menu' which resets after each cache is created and printed then wiped
while True:
    cache = []
    requests = [] #put cache and requests here, it should work and if it doesnt just put it back at the start and end.

    #this While loop continues until the user presses 0 to stop submitting requests
    while True:

        userInput = input('Please enter the numbers to compile into cache. Press 0 when you are finished \n')
        try:
            if userInput == '0':
                break
            else:  
                requests.append(int(userInput))
        except ValueError:
            print('Please enter an integer')
            print('')
            continue   
    #this While loop asks provides the choice of which method to use to compile the cache
    while True:
        userChoice = input('Please select compile method: Press 1 for First in First out (fifo), press 2 for Least Frequently Used(lfu), or press Q to exit the program. \n')              
        if userChoice == '1':
            fifo(cache,requests)
            break
        elif userChoice == '2':
            lfu(cache,requests)
            break
        elif userChoice.upper() == 'Q':
            quit()
        else:
            print('Please enter 1, 2 or Q')
            print('')



  