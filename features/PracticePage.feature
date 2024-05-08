Feature: Python-Behave-Automation


  Scenario: Serach for a PlayStation in Liverpool Store
     Given the user navigates to the "home" page
     When the user search for an article in the store
     | article     |
     | PlayStation |
    Then the suggested articles should be displayed