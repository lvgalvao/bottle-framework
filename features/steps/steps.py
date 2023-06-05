from behave import given, when, then

@when('somar "{num1:d}" com "{num2:d}"')
def test_soma_dois_valoes(context, num1, num2):
    pass

@then('o resultado deve ser "{resultado:d}"')
def assert_result(context, result):
    pass