import json
import requests


with open("data.json", "r") as f:
    data=json.load(f)
print(data)
street_name=data["adddres"]["streetAdres"]
print(f"name is {street_name}")

last_name=data.get("lastName")
print(f"name is {last_name}")

#extract data from nested data
street_address = data.get("adddres", {}).get("streetAdres")
print("Street Address:", street_address)

street_address = data.get("adddres", {}).get("streetAdres")
print("Street Address:", street_address)


#extract ata from list of dictionary
number= data.get("Phone Number", [{}])[0].get("Landline")
print("Street Address:", number)

numb= data["Phone Number"][0]["Mobile"]
print(numb)


# import json
# import unittest  # ✅ Import unittest
#
# class TestJsonParsing(unittest.TestCase):  # ✅ Define a test class
#     def setUp(self):
#         """Load JSON data before each test"""
#         with open("data.json", "r") as f:
#             self.data = json.load(f)
#
#     def test_last_name(self):
#         """Test extracting last name"""
#         last_name = self.data.get("lastName")
#         self.assertEqual(last_name, "Chaudhary")  # ✅ Correct way to assert in unittest
#
#     def test_street_address(self):
#         """Test extracting street address"""
#         street_address = self.data.get("adddres", {}).get("streetAdres")
#         self.assertEqual(street_address, "l-137 Street")  # ✅ Assert expected value
#
#     def test_landline_number(self):
#         """Test extracting landline number"""
#         number = self.data.get("Phone Number", [{}])[0].get("Landline")
#         print(number)
#         self.assertEqual(number, "80768962675")
#
#     def test_mobile_number(self):
#         numb = data["Phone Number"][0]["Mobile"]
#         print(f"number is {numb}")
#         self.assertEqual(numb , "9821295572")
#
#
# # if __name__ == "__main__":
# #     unittest.main()
