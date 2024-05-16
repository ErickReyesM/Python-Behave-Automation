Feature: Python-Behave-Automation


  @product_details
  Scenario Outline: Serach for an article and validate the product details in Liverpool Store
     Given the user navigates to the "home" page
     When the user search for <article> in the store
     Then related articles to <article> should be displayed as suggestion
     When the user selects the <option> from the available options
     Then the user should be able to see the product detail page
    Examples:
      | article     | option        |
      | playstation | PS5           |

  @filters
  Scenario: Validate the size and price filters searching an article
    Given the user navigates to the "home" page
    When the user search for "smart tv" in the store
    And the user navigates to the results page to see the available options
    And the user apply the filters to get a specific product
      | size        | price        | brand |
      | 55 pulgadas | 10000-700000 | sony  |
    Then the user should be able to see the results