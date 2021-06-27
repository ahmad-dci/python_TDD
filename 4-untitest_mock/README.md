# unittest.mock
mock is a way to test your function with out having any side effect 
for example if you want to write a code to delete some file and you dont want to touch any of your valuable files during testing 
mock is going to help you to do that so it wil simulate that you removing the file is exist 
as you can see in mock_test.py file we were trying to delete somefile1.txt but it will not relly be deleted and the test still passed 