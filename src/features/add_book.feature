Feature: Lägg till bok

    Scenario: Möjlighet att lägga till bok

        Given Att jag som användare 
        When Går in på websidan 
        Then Ser boklistan och möjlighet Lägg till bok
   
    Scenario: Registrera boktitel och författare

        Given Att jag som användare 
        When Går in på websidan 
        When Saknar en bok i listan som visas
        And lägger till en bok som saknas i listan
        Then vill jag se den tillagda boken i boklistan