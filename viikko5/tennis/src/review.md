Copilot teki yhden huomiom koodistani. Huomio oli että Etu- ja voittoilmoituksissa käytetään vääriä merkkijonoja
Refaktorointi muutti tulosmerkkijonot muotoon:

"Advantage {self.player1_name}"
"Win for {self.player1_name}"

Copilot huomautti, että olemassa olevat testit odottavat edelleen kirjaimellisia merkkijonoja:

"Advantage player1"
"Win for player1"

Tämä tekee refaktoroinnista taaksepäin epäyhteensopivan testien kanssa.

Copilotin ehdotus oli hyvä, koska tämä ehdotus korjasi testit jotka eivät toimineet refactoroinnin jälkeen oikein juuri tämän ongelman takia. Koin copilotin tekemän katselmoinnin erittäin hyödylliseksi, koska sen ehdotus koodin korjaamisen siihen muotoon, että testit taas toimivat.