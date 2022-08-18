# Testing-Selenium-Python

My introduction to Selenium WebDriver with Python following the test automation university course.

I've added the repo created by the course instructor Andy Knight as a submodule in order to follow the course properly. 

## Fixtures

They are special functions that make sure everything gets set up, cleaned up and the dependencies are properly injected 

## Python packages

These files are headed by files called <__init__.py>, which is just for the machine to know that the you are using a package and to treat it as such 

## Different browsers

When writing automated tests with Selenium WebDriver or any web-based test, regardless of  language, one should always avoid hard-coding the browser into the tests because this limits the versatility of said tests. 

## Race conditions

These are situations in which multiple actors try to access the same resource without a clear order of operations, these can cause flakiness in testing. And must be handled properly. Specifically in Web UI race conditions can happen when the automation or test suite tries to interact with a page before it is fully loaded in order to avoid this, one should wait until the target element or property is fully loaded or it is ready to be interacted with
