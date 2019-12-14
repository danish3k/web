from Web_Test import website_testing
import pytest
A = website_testing.web_test()

def launch_website():
    val = A.launch()
    assert "We belive in Taste" == val , "test passed"
    print("Launch Test Successfull")
def close_wesite():
    A.close()
    print("Close test successfull")


launch_website()
close_wesite()