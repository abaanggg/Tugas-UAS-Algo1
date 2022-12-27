def insertion_sort(nums):
    # Start on the second element as we assume the first element is sorted
    for i in range(1, len(nums)):
        item_to_insert = nums[i]
        # And keep a reference of the index of the previous element
        j = i - 1
        # Move all items of the sorted segment forward if they are larger than
        # the item to insert
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        # Insert the item
        nums[j + 1] = item_to_insert
        
     


def pencarian_linear(L, e):
  found = False
  for i in range(len(L)):
     if e == L[i]:
     	found = True
  return found
  
 ## quiz
 
#1. Modifikasi dua algoritma (fungsi) diatas , sehingga dapat melakukan sorting dan pencarian sebuah angka , hanya didalam satu / sebuah fungsi (menjadi satu fungsi/ menggunakan satu fungsi saja)
  







