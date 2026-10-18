# Teorifrågor
# Dessutom ska du svara kortfattat på följande frågor i ANSWERS.md för att demonstrera dina 
# kunskaper.
# Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?
Enhetstest testar delar av koden
Integrationstest testar koddelar tillsammans och/eller funktioner och system
Regressionstest är tester som körs om i senare faser. Syftet är att kontrollera att befintlig funktionalitet fortfarande fungerar efter ändringar.
Prestandatest kontrollerar exempelvis svarstider för att kunna optimera koden där det behövs.

# Beskriv hur det går till när man arbetar med TDD.
Test-driven-development går ut på att man börjar med att skriva ett testfall som ska fallera och därefter bygger man på funktion för att testfallet ska fungera (refaktorering) och fokuserar på minsta möjliga för att lösa uppgiften. 

# Beskriv hur BDD skiljer sig från TDD.
Behavior-driven-development utgår från användarens perspektiv på systemet beskriven enligt modellen Given-When-Then och testar funktion och acceptans och TDD blir mer motsvarande enhetstester

# Tänk dig att du skulle göra en webbsida som liknar Läslistan, både frontend och backend. 
# Om du fick välja förutsättningslöst, vilka sorters tester skulle du vilja använda? Motivera ditt # val.
Jag skulle vilja göra enhetstester (TDD) och integrationstester mot backend samt funktion och acceptanstester enligt BDD mot frontend. Slutligen end-to-end tester som omfattar helt flöde och både backend och frontend.
