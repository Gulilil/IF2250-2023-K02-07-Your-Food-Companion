
from src.controller.controller import Controller


class InventoryManager: 
  Stored_Food_Data_Header = ["Food Name", "Cost", "Expired Due", "Quantity", "Status"]
  Consumed_Food_Data_Header = ["Food Name", "Eaten Date", "Quantity", "Status"]
  Expired_Food_Data_Header = ["Food Name", "Cost", "Expired Date", "Quantity", "Status"]
  categoryList = [
          'dairy products',
          'meat and poultry',
          'seafood products',
          'fruits and vegetables',
          'grains and cereals',
          'snacks and sweets',
          'beverages',
          'others'
      ]
  categoryKey = ['dairy', 'meat', 'poultry', 'seafood', 
                 'fruits', 'vegetables', 'grains', 'cereals',
                 'snacks', 'sweets', 'beverages', 'others']

  # GETTER
  def getStoredFoodHeader(self):
      return self.Stored_Food_Data_Header
  
  def getConsumedFoodHeader(self):
      return self.Consumed_Food_Data_Header
  
  def getExpiredFoodHeader(self):
      return self.Expired_Food_Data_Header

  def getStaleFoodData(self, category):
      res = []
      ctrl = Controller()
      if (category != None):
        temp = ctrl.get_stale_food_with_category(category)
      else :
        temp = ctrl.get_stale_food()
      for i in temp:
          arr = []
          arr.append(i[len(i)-2]) # insert name
          arr.append(i[3]) #insert cost
          arr.append(i[4]) #insert expired date
          arr.append(i[1]) #insert quantity
          arr.append("Stale")
          res.append(arr)
      return res

  def getGoodFoodData(self, category):
      res = []
      ctrl = Controller()
      if (category != None):
        temp = ctrl.get_good_food_with_category(category)
      else :
        temp = ctrl.get_good_food()
      for i in temp:
          arr = []
          arr.append(i[len(i)-2]) # insert name
          arr.append(i[3]) #insert cost
          arr.append(i[4]) #insert expired date
          arr.append(i[1]) #insert quantity
          arr.append("Good")
          res.append(arr)
      return res

  def getStoredFoodData(self, category):
      res = []
      stale = self.getStaleFoodData(category)
      good = self.getGoodFoodData(category)
      for i in stale:
          res.append(i)
      for i in good:
          res.append(i)
      return res

  def getExpiredFoodData(self, category):
      res = []
      ctrl = Controller()
      if (category != None):
        temp = ctrl.get_expired_food_with_category(category)
      else :
        temp = ctrl.get_expired_food()
      for i in temp:
          arr = []
          arr.append(i[len(i)-2]) # insert name
          arr.append(i[3]) #insert cost
          arr.append(i[4]) #insert expired date
          arr.append(i[1]) #insert quantity
          arr.append("Expired")
          res.append(arr)
      return res

  def getConsumedFoodData(self, category):
      res = []
      ctrl = Controller()
      if (category != None):
        temp = ctrl.get_eaten_food_with_category(category)
      else :
        temp = ctrl.get_eaten_food()
      for i in temp:
          arr = []
          arr.append(i[len(i)-2]) # insert name
          arr.append(i[4]) #insert Consumed date
          arr.append(i[1]) #insert quantity
          arr.append("Consumed")
          res.append(arr)
      return res

  def getLastFoodID(self):
      ctrl = Controller()
      allFood = ctrl.get_food()
      for i in allFood:
          id = int(i[0])
      return id
  
  def getCategoryFromKey(self, k):
      for i in self.categoryList:
          if k.lower() in i:
              return i
      return "others"
          

  # PERCENTAGE
  def goodPercentage(self):
      c = Controller()
      temp = c.get_food()
      allCount = 0
      for i in temp:
          allCount+=1
      good = c.get_good_food()
      goodCount = 0
      for i in good:
          goodCount +=1
      return goodCount/allCount*100

  def stalePercentage(self):
      c = Controller()
      temp = c.get_food()
      allCount = 0
      for i in temp:
          allCount+=1
      stale = c.get_stale_food()
      staleCount = 0
      for i in stale:
          staleCount +=1
      return staleCount/allCount*100

  def expiredPercentage(self):
      c = Controller()
      temp = c.get_food()
      allCount = 0
      for i in temp:
          allCount+=1
      expired = c.get_expired_food()
      expiredCount = 0
      for i in expired:
          expiredCount +=1
      return expiredCount/allCount*100

  # CATEGORIES
  def getCategoriesArray(self):
      c= Controller()
      temp = c.get_distinct_category()
      arr = []
      for i in temp:
          arr.append(i[0])
      return arr

  def getFoodCountCategory(self, arrCategory):
      c = Controller()
      res = []
      for i in arrCategory:
        temp = c.get_food_with_category(i)
        count = 0
        for j in temp:
            count +=1
        res.append(count)
      return res

  # VALUE
  def getTotalValueInventory(self):
      temp = self.getStoredFoodData(None)
      value = 0
      for i in temp:
          value += i[1]
      return value

  def getTotalWasteExpired(self):
      temp = self.getExpiredFoodData(None)
      waste = 0
      for i in temp:
          waste += i[1]
      return waste
    
  # VALIDATION
  def isItemInputValid(self, arr):
      # name = arr[0][1] # is not needed to be checked
      category = arr[1][1]
      cost = arr[2][1]
      quantity = arr[3][1]
      expiredDate = arr[4][1]
      # notes = arr[5][1] # is not needed to be checked
      if not self.isNumber(cost):
          return (False, "Cost Invalid")
      if not self.isNumber(quantity):
          return (False, "Quantity Invalid")
      if not self.isValidDate(expiredDate):
          return (False, "Expiry Date Invalid")
      return (True, None)


  def isNumber(self, n):
      try :
          int(n)
          return True
      except:
          return False

  def isValidDate(self, date):
      months31 = [1,3,5,7,8,10,12]
      arr = date.split("-")
      print(arr)
      if (len(arr) != 3):
          return False
      else :
          if (len(arr[0]) != 2 or len(arr[1]) != 2 or len(arr[2]) != 4):
              return False
          for i in range(3):
              if (not self.isNumber(arr[i])):
                  return False
              else :
                  arr[i] = int(arr[i])
                  if (arr[i] < 0):
                      return False
          if (arr[1] > 12):
              return False
          if (arr[1] == 2): # February
              if (arr[0] > 29):
                  return False
          if (arr[1] in months31): # Months with 31 days
              if (arr[0] > 31):
                  return False
          else : # Months with 30 days
              if (arr[0] > 30):
                  return False
          return True
              
          