Feature: Python-Behave-Automation


  Scenario Outline: Serach for a PlayStation in Liverpool Store
     Given the user navigates to the "home" page
     When the user search for <article> in the store
     Then related articles to <article> should be displayed as suggestion
     When the user selects the <option> from the available options
     Then the user should be able to see the product detail page
    Examples:
      | article     | option        |
      | playstation | PlayStation 5 |
