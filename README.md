# bwinf_petanque

Ridvan und Jenny spielen gerne Pétanque. Dabei
werfen die beiden Spielenden abwechselnd Kugeln
in Richtung einer Zielkugel. Sie wollen auch gerne
am Computer etwas Ähnliches spielen können und
haben sich dafür Folgendes überlegt:
Das Spielfeld ist quadratisch und besteht aus
13 × 13 Feldern, mit Koordinaten von (1,1) bis (13,13).
Die Zielkugel wird zufällig auf einem der Felder
platziert. Für einen Wurf wählt ein Spieler als Startfeld ein äußeres Feld, also ein Feld, bei dem mindestens eine Koordinate 1 oder 13 ist. Die Kugel landet
dann auf einem Zielfeld, das wie folgt bestimmt
wird:
Die Kugel fliegt gerade (links, rechts, oben oder
unten) in Richtung der Zielkugel, und zwar zufällig
0 bis 5 Felder weit und zufällig noch um 0 oder 1 Feld
orthogonal dazu. Wenn auf dem Zielfeld bereits
eine Kugel liegt, wird diese in Wurfrichtung um ein
Feld verschoben. Falls dort auch schon eine Kugel
liegt, wird diese ebenfalls verschoben, usw.
Nach einer bestimmten Anzahl von Runden ist das
Spiel zu Ende. Wenn die Zielkugel vom Feld
geschoben wird, endet das Spiel unentschieden.
Ansonsten gewinnt der Spieler, der die meisten
Kugeln neben der Zielkugel platzieren konnte.
## Aufgabe 4
Schreibe ein Programm, mit dem man dieses
Computer-Pétanque spielen kann.
Beschreibe, wie du Ridvans und Jennys
Überlegungen präzisiert hast, um das Spiel zu
realisieren.
