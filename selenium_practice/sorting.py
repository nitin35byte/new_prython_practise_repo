from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Function to extract table data
def extract_table_data(driver, xpath):
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath))
    )
    elements = driver.find_elements(By.XPATH, xpath)
    state=[]
    for ele in elements:
        countries = ele.text.strip()
        state.append(countries)
    # return [element.text.strip() for element in elements]
    return state

# Function to validate sorting
def is_sorted(data):
    for i in range(len(data) - 1):
        if data[i] > data[i + 1]:  # Compare current element with the next one
            return False, i + 1  # Return False and the position of the unsorted element
    return True, None


# Main script
if __name__ == "__main__":
    # Start Selenium WebDriver
    driver = webdriver.Chrome()  # Use appropriate driver
    driver.get('https://tin.tin.nsdl.com/pan/Country.html')  # Replace with the actual URL

    # Define XPath for the table column
    xpath = "(//tbody)[2]/tr/td[2]"  # Adjust this XPath to your table column
    column_data = extract_table_data(driver, xpath)
    print(column_data)

    # Validate if the column is sorted
    sorted_status, position = is_sorted(column_data)

    if sorted_status:
        print("The table data is sorted.")
    else:
        print(f"The table data is not sorted. The unsorted position is at index {position} (1-based index).")

    # Close the driver
    driver.quit()





driver = webdriver.Chrome()  # Use appropriate driver
driver.get('https://tin.tin.nsdl.com/pan/Country.html')  # Replace with the actual URL

    # Define XPath for the table column
xpath = "(//tbody)[2]/tr/td[2]"  # Adjust this XPath to your table column
extract_data= driver.find_elements(By.XPATH , xpath)
column_data=[]
for data in extract_data:
    column_data.append(data.text)

print(column_data)
is_sorted=True
for data in range(len(column_data)-1):
    if column_data[data] > column_data[data+1]:
        is_sorted= False
        break
    # Validate if the column is sorted
if is_sorted:
    print("The table data is sorted.")
else:
    print(f"The table data is not sorted. The unsorted position is at index(1-based index).")

d=driver.find_element(By.XPATH,"//table[1]/tbody[1]//tr[11]")
print(d.text)
def bubbesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] >arr[j+1]:
                arr[j] , arr[j+1]=arr[j+1] , arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubbesort(arr)
print("Sorted array t:", arr)
a =['nishant' , 'mukesh','chaudhary','mishara','jha']
b=[1,2,3,4,5,6]
is_sorted=True
for i in range(len(b)-1):
    if b[i] >b[i+1]:
        is_sorted=False
        break

if is_sorted:
    print("hum sorted hain bhai chill")

else:
    print("hum sorted nain hai bhai chill")