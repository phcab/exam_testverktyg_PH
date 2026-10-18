

Feature: Boklista
 
    Scenario: Boklista

        Given Att jag som användare 
        When Går in på websidan 
        Then Vill jag kunna se lista över böcker

    Scenario: Favoritmarkera en bok i boklistan

        Given Att jag som användare
        When Går in på websidan
        When jag favoritmarkerar en bok i listan
        Then ska boken vara favoritmarkerad

    Scenario: Ta bort en favoritmarkering från en bok i boklistan
        Given Att jag som användare
        When Går in på websidan
        When jag favoritmarkerar en bok i listan
        Then ska boken vara favoritmarkerad
        When tar bort en favoritmarkering i boklistan
        Then boken visas utan favoritmarkering i boklistan
    