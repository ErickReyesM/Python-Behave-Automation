Feature: Stori-QA-Automation-Challenge


  Scenario Outline: run a simple test
     Given the user navigates to "AutomationPractice" page
      When the user writes the <word>
      And selects the <country> from the available list
      When the user wants to select an option from the dropdown
        | option  |
        | Option2 |
        | Option3 |
      Then behave will test it for us!

    Examples:
      | word | country              |
      | Me   | Mexico               |
      | Uni  | United States (USA)  |
      | Uni  | United Arab Emirates |
      | Fr   | France               |