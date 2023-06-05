# -- FILE: features/example.feature
Feature: Cadastro
  Scenario: Efetuar cadastro com sucesso
    Given Acessar o site "http://localhost:8080/cadastro"
    When insert "nome" "Luciano"
    And insert "sobrenome" "Filho"
    And insert "usuario" "Lvgalvao"
    And insert "sexo" "Masculino"
    And insert "senha" "123456"
    And insert "email" "lvgalvaofilho@gmail.com"
    And insert "nascimento" "06/03/1993"
    Then press button "Enviar"
    Then I should see 
    """
    Bem vindo Luciano
    Usuário: Lvgalvao
    Senha: 123456
    """