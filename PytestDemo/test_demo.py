from demo_operations import demo_operations
import pytest

demo_object =""

 
def setup_module(module):
    global demo_object
    demo_object = demo_operations()

@pytest.mark.numbers
def test_add():
    assert demo_object.add(3,4) == 7

@pytest.mark.string
def test_add_string():
    assert demo_object.add("Hello ","World") == "Hello World"

@pytest.mark.numbers
def test_product():
    result = demo_object.product(2,5) 
    assert result == 10
    assert isinstance(result,int)


@pytest.mark.string
def test_product_string():
    assert demo_object.product("Hello",3) == "HelloHelloHello" 


@pytest.mark.parametrize('element1, element2, result',
[
    (3,4,7),
    ("Hello","World","HelloWorld"),
    (4.5,5.5,10)
])
def test_add_int(element1,element2,result): 
    assert demo_object.add(element1,element2) == result

@pytest.mark.parametrize('ele1, ele2, ele3',[
    (3,2,6),
    ("Hello",2,"HelloHello"),
])
def test_prod_string(ele1,ele2,ele3):
    assert demo_object.product(ele1,ele2) == ele3