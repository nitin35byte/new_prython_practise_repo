# from playwright.api.syn import sync_playwright
#
# def playwrighttest():
#     with sync_playwright as p:
#         browser=p.chromium.launch(headless=False)
#         context=browser.new_context()
#         page=context.new_page()
#         page.go_to()
#
#
#         page.fill
#         page.click
#         page.send_files
#         page.set_input_files
#         page.once(idalogue , lambda dialogue :dialog.accept())
#         page.screenshot()
#         page.frame_locator


a = "welcome To Cognizant nitin"

word=[]
duplicate=[]
for i in a:
    if i in word:
        duplicate.append(i)
    else:
        word.append(i)

print(f"duplicate word is {set(duplicate)}")
print(f"unique word word is {word}")


arr=[1,2,4,7,0,3,6]
min_ele=arr[0]
sec_min=arr[0]

for i in arr:
    if i <min_ele:
        sec_min=min_ele
        min_ele=i
    elif sec_min < i  < min_ele:
        sec_min=i

print(min_ele,sec_min)