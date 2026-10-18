Feature: Mina böcker

    Scenario: Mina favoritmarkerade böcker

    Given Att jag som användare
    When Går in på websidan
    When jag favoritmarkerar en bok i listan 
    Then ska knappen Mina böcker gå till lista som visar bara mina favoritmarkerade böcker
    