Ide:
Använda start iden, från classroom men att göra med annat tema

HP, Attackera styrka
Potions: Healing, STR potion
Potions används efter en battle när de behövdes för att vinna

En shop där man kan köpa potions och ksk nya vapen

Genomförandet av spelet: 
Det börjar med att man får en fråga om main menu, som har två punkter: den första är startgame och den andra exit. Väljer du starta så kommer du få en text som är storyn i spelet och berättar lite om det. Efter det får du en ny fråga som frågar om vilket namn du vill ha i spelet. När du valt det får du tre nya frågor, kolla stats, inventory eller gå in genom en dörr. Väljer man dörren så får man välja om man ska gå rakt fram, höger eller vänster. En av dörrarna kommer att vara en shop där man kan köpa vapen eller olika potions. I den andra dörren så kan man få en kista som kan ge olika grejer så som pengar man kan använda till shoppen eller potions, det kommer att finnas fake kistor som när man öppnar dem så är det ett monster istället. I den tredje så kan det finnas fällor som man tar skada av. Det kommer även att komma monster man kan besegra och ifall man gör det går upp en lvl per monster. Allt som kommer bakom dörrarna är slumpmässigt. 

Beroende på spelarens level så kommer monstrens svårighetsgrad bli svårare. 




Funktioner:
door() - Slumpar fram vad som ska hända bakom en dörr efter att man valt vilken man vill ha , m.h.a. if/elif/else och random modulen kan det slumpa fram styrkan på items man får i kistor, styrkan hos sitt monster och skada på fällor
player.print_inventory() - visar spelarens potions i en lista
item_exchange() - byter ut ens sämsta vapen mot den nya i kistan
player.print_stats() - skriver ut spelarens LVL, STR och HP
combat() - tar hand om striderna mellan spelaren och fiender

