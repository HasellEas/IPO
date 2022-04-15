file = input("DIR: ")

with open(file, "r") as __:
    file_text = __.read()
nums = {}
file_text_split = file_text.split()
for __ in file_text_split:
    if str(__) in nums:
        nums[str(__)]+=1
    else:
        nums.update({str(__):0})
        nums[str(__)]+=1
for key, item in nums.items():
    print(str(key)+" повторяется "+str(item)+" раз")