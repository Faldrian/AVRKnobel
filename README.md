### Knobelgeschenk in AVR-Form

Dieses Projekt ist ein Geschenk für einen Freund, der das Rätsel mittlerweile gelöst hat, weshalb ich es hier veröffentlichen kann.

Es handelt sich hierbei um ein Rätsel in Form eines ATMega8-Mikrocontrollers, der drei verschiedene Verhalten zeigt:

1. Es wird an einem Port eine Morse-Sequenz ausgegeben, die sich z.B. mit einer LED visualisieren lässt.
2. Es werden zwei Ports benutzt um Daten auszugeben; Ein Port ist die DATA-Leitung, der andere eine primitive CLOCK. Hier wird ein Textblock übertragen.
3. Wie 2., nur dass ein SVGZ-Bild übertragen wird.

Die jeweiligen Stufen geben in ihrer Payload Hinweise darauf, wie man die nächste Stufe aktiviert. So muss man sich (sofern man dem Rätsel folgt) durch die Stufen arbeiten um bis zu Verhalten 3 und damit dem Finale zu gelangen.  
Ein anderer möglicher Weg wäre natürlich, dass man sich den Programmcode mit einem Programmer vom Chip dumpt und dann den auseinandernimmt... wenn das für den Rätselnden die spaßigere Version ist, gerne. ;)

Viel Spaß mit dem Stück Rätselsoftware, möge es dem einen oder anderen eine Inspiration für Geschenke an ihre Nerds sein.

PS.: Hinweise für das Debugging / Lösungssetup mit dem Raspberry Pi stehen in `tutorial.md`.
