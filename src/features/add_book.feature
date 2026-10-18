Feature: Lägg till bok

    Scenario: Möjlighet att lägga till bok

        Given Att jag som användare 
        When Går in på websidan 
        Then Vill jag kunna lägga till en bok som saknas i listan
   
    Scenario: Registrera boktitel och författare

        Given Att jag som användare 
        When Går in på websidan 
        Then Vill jag kunna lägga till en bok som saknas i listan
        Then Registrera och spara titel och författare
        Then Se boken i boklistan