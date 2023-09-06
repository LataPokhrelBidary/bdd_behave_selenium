Feature: Facebook login functionality

  Scenario Outline: Test login with incorrect login credentials
    When user enter incorrect user name "<user_name>" and password "<password>"
    Then error message should be displayed
    Examples: credentials
      | user_name | password  |
      | zorrr4567 | pass4567 |
      | zorrr9887 | pass6544  |
