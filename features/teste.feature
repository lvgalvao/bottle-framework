# -- FILE: features/example.feature
Feature: Soma
"""
Sendo um usuário eu quero somar dois números para que seja possível receber o resultado
"""
  Scenario: Soma de inteiros positivos
    When somar "2" com "2"
    Then o resultado deve ser "4"

  Scenario: Soma de inteiros negativos
    When somar "-2" com "-2"
    Then o resultado deve ser "-4"