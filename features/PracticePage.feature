Feature: Stori-QA-Automation-Challenge


  Scenario: run a simple test
     Given the user navigates to "AutomationPractice" page
      When the user writes a word and selects the a country from the available list
        | word | country              |
        | Me   | Mexico               |
        | Uni  | United States (USA)  |
        | Uni  | United Arab Emirates |
        | Fr   | France               |
      When the user wants to select an option from the dropdown
        | option  |
        | Option2 |
        | Option3 |
      Then the user switches to a new window and validate hte "30 DAY MONEY BACK GUARANTEE" is present on the page
