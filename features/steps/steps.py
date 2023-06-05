from behave import when, then, given
from selenium import webdriver
from selenium.webdriver.common.by import By


dic = {'nome': 'name',
       'sobrenome': 'lastName',
       'usuario': 'username',
       'senha': 'passwd',
       'sexo': 'gender',
       'email': 'email',
       'nascimento': 'age',
       'Enviar': 'btnSend'}

@given('Acessar o site "{page}"')
def access_page(context, page):
    context.ff = webdriver.Firefox()
    context.ff.get(page)

@when('insert "{field}" "{value}"')
def insert_values_on_fields(context, field, value):
    context.ff.find_element(By.ID, dic[field]).send_keys(value)

@then('press button "{button}"')
def press_button(context, button):
    context.ff.find_element(By.ID, dic[button]).click()

@then('I should see')
def read_text(context):
    text = context.ff.find_element(By.ID, 'text').text
    assert text == context.text, print(text, context.text)