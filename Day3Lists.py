'''
LIST : lists are used to store multiple items in a single variable 
       lists are created by using []
       eg : a = [2,3,"shashank"]
       List items are ordered ,changeable ,and allow duplicate values
       these list items are indexed ,meaning first item has index[0] and second index[1] etc
       the list is changeable
       list items can be of any data type
       negative indexing means starting from the end for eg : index[-1]
       you can specify range of indexes by giving start and end
       index[0:] by leaving the ending blank it will go to the end of the list
       index[:8] by leaving the start blank it will start from the 0 index of the list
       we can insert itmes in a list at a specific location by list.insert(2,"watermelon")
       to add an item at the end of the list we use the append keyword by list.append("watermelon")
       to append elements from another list we use the extend() method 
       eg : a = [2,3,4]
            b = [5,6,7]
            
            a.extend(b)
            
       we can remove an item by eg : list = [2,3,4]
                                     list.remove(2)
       remove specified item at an index by .pop(2)
       we can use .pop() only to remove last item of a list
       clear() method empties a list
       we can use .copy() to copy a list into another list  
       we can join lists by +,append(),extend()
                                       '''