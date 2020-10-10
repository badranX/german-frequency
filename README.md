The problem with many available frequency lists is that they don't take word morphologies into account. For example, in English, "playing" and "played" might be found seperated in a frequency list. This code adresses this issue by taking morphology into account. An experiment word list order by frequency is in the "5000.txt" file.

## Example:
The file 5000.txt (in the 'data' folder) contains top 5000 German words ranked by frequency based on German movie subtitles. It only display one form of each group of word morphologies. The list was just generated from the code available here and needs some refinement.

- The data was generated via [LuminosoInsight](https://github.com/LuminosoInsight/wordfreq) and [german-morph-dictionaries](https://github.com/DuyguA/german-morph-dictionaries).

## Top 1000 German word (ommiting their morphologies):

     1	ich
     2	ein
     3	nicht
     4	und
     5	zu
     6	wird
     7	kann
     8	mit
     9	ja
    10	wie
    11	auf
    12	dass
    13	aber
    14	gut
    15	weiß
    16	so
    17	von
    18	hier
    19	sagen
    20	bitte
    21	für
    22	komm
    23	machen
    24	wenn
    25	keine
    26	muss
    27	diese
    28	nein
    29	mehr
    30	noch
    31	da
    32	tun
    33	nur
    34	soll
    35	schon
    36	auch
    37	mal
    38	als
    39	jetzt
    40	um
    41	aus
    42	dann
    43	hör
    44	doch
    45	oder
    46	dachte
    47	bei
    48	nichts
    49	wo
    50	etwas
    51	Mann
    52	oh
    53	also
    54	danke
    55	immer
    56	warum
    57	ganz
    58	weg
    59	vor
    60	liebe
    61	glaube
    62	leben
    63	wieder
    64	finden
    65	sehr
    66	okay
    67	denn
    68	möchte
    69	über
    70	brauchen
    71	vielleicht
    72	anderen
    73	nehmen
    74	fall
    75	wirklich
    76	einfach
    77	halt
    78	Frau
    79	nie
    80	hey
    81	hause
    82	bringen
    83	tag
    84	zeit
    85	leid
    86	weil
    87	warte
    88	verstehe
    89	lange
    90	fahren
    91	reden
    92	bleiben
    93	jeder
    94	nun
    95	schön
    96	heute
    97	sicher
    98	junge
    99	fragen
    100	Gott
    101	weiter
    102	jemand
    103	arbeit
    104	damit
    105	kennen
    106	Jahre
    107	bis
    108	kleine
    109	erst
    110	zurück
    111	große
    112	helfen
    113	na
    114	sprechen
    115	Kinder
    116	zwei
    117	hallo
    118	alter
    119	Leute
    120	Vater
    121	Freund
    122	genau
    123	versuchen
    124	morgen
    125	passiert
    126	klar
    127	richtig
    128	spielen
    129	neue
    130	darf
    131	ab
    132	gerade
    133	durch
    134	Geld
    135	letzte
    136	töten
    137	gleich
    138	recht
    139	menschen
    140	sterben
    141	raus
    142	Mutter
    143	ob
    144	paar
    145	nächste
    146	Herr
    147	bekommen
    148	Namen
    149	wohl
    150	krieg
    151	scheiße
    152	verdammt
    153	suchen
    154	erzählt
    155	nacht
    156	läuft
    157	essen
    158	selbst
    159	her
    160	ohne
    161	schnell
    162	tot
    163	stimmt
    164	holen
    165	gar
    166	wieso
    167	treffen
    168	beide
    169	dort
    170	natürlich
    171	stellen
    172	später
    173	Sache
    174	niemand
    175	ordnung
    176	ruf
    177	dinge
    178	liegt
    179	Mädchen
    180	vergessen
    181	seit
    182	welche
    183	ach
    184	davon
    185	zeigen
    186	Problem
    187	allein
    188	verloren
    189	dafür
    190	drei
    191	hin
    192	rein
    193	schau
    194	abend
    195	sorgen
    196	unter
    197	angst
    198	Welt
    199	schaffen
    200	fühle
    201	schlafen
    202	Musik
    203	Hand
    204	zusammen
    205	wahr
    206	ziehen
    207	Bruder
    208	Moment
    209	genug
    210	echt
    211	setzen
    212	Sohn
    213	gegen
    214	wenig
    215	toll
    216	einmal
    217	sonst
    218	Familie
    219	erinnern
    220	pass
    221	Schatz
    222	nennen
    223	dabei
    224	sofort
    225	ende
    226	Augen
    227	bevor
    228	stunden
    229	Minuten
    230	entschuldigen
    231	einzige
    232	schlecht
    233	fangen
    234	plan
    235	verschwinden
    236	hoch
    237	trinken
    238	fertig
    239	angerufen
    240	wann
    241	schicken
    242	Woche
    243	Hilfe
    244	verrückt
    245	früher
    246	darüber
    247	Land
    248	ne
    249	bereit
    250	daran
    251	wichtig
    252	teil
    253	Kopf
    254	dazu
    255	schlagen
    256	schreiben
    257	reicht
    258	verlassen
    259	eigentlich
    260	Stadt
    261	nett
    262	Grund
    263	kurz
    264	hoffe
    265	Typ
    266	Wort
    267	gern
    268	Auto
    269	sitzen
    270	kämpfen
    271	bedeutet
    272	egal
    273	Tür
    274	Kerl
    275	falsch
    276	Uhr
    277	anfangen
    278	glück
    279	lernen
    280	schwer
    281	einige
    282	schuld
    283	schlimm
    284	Waffe
    285	retten
    286	tragen
    287	bisschen
    288	scheint
    289	darauf
    290	bald
    291	wünschte
    292	kaufen
    293	Tod
    294	ruhe
    295	kümmern
    296	runter
    297	voll
    298	Monate
    299	ruhig
    300	arm
    301	Polizei
    302	eigenen
    303	draußen
    304	Idee
    305	wagen
    306	hinter
    307	herz
    308	Geschichte
    309	folgen
    310	versprochen
    311	bestimmt
    312	Teufel
    313	Tochter
    314	ziemlich
    315	vorbei
    316	Schwester
    317	hi
    318	Ahnung
    319	fast
    320	Job
    321	gerne
    322	dran
    323	wach
    324	umbringen
    325	gewinnen
    326	sogar
    327	überhaupt
    328	stark
    329	vertrauen
    330	Ort
    331	drin
    332	frei
    333	lachen
    334	darum
    335	heiraten
    336	woher
    337	steckt
    338	je
    339	Wasser
    340	hasse
    341	fliegen
    342	laut
    343	während
    344	endlich
    345	erwartet
    346	oben
    347	lügen
    348	laden
    349	klingt
    350	Traum
    351	niemals
    352	schließen
    353	glücklich
    354	bezahlen
    355	fünf
    356	etwa
    357	beweise
    358	ernst
    359	Feuer
    360	miss
    361	chance
    362	schießen
    363	Wahrheit
    364	anders
    365	gestern
    366	Blut
    367	vier
    368	verkaufen
    369	möglich
    370	zimmer
    371	erklären
    372	Gesicht
    373	süß
    374	platz
    375	eben
    376	benutzt
    377	Freundin
    378	Antwort
    379	Captain
    380	deshalb
    381	ändern
    382	buch
    383	freut
    384	beginnen
    385	Bett
    386	schiff
    387	spaß
    388	zwischen
    389	schreit
    390	fest
    391	Hund
    392	entschuldigung
    393	oft
    394	manchmal
    395	solche
    396	wiedersehen
    397	wein
    398	aufhören
    399	verdient
    400	wohnen
    401	Bild
    402	äh
    403	versteckt
    404	Gefühl
    405	Nachricht
    406	schule
    407	unten
    408	funktioniert
    409	Papa
    410	bloß
    411	i
    412	geschehen
    413	Arsch
    414	hart
    415	dauert
    416	böse
    417	werfen
    418	dumm
    419	ehrlich
    420	zeug
    421	brechen
    422	John
    423	aussehen
    424	zahlen
    425	langsam
    426	dasselbe
    427	Nummer
    428	wohin
    429	leicht
    430	verbrechen
    431	entscheiden
    432	besuch
    433	Eltern
    434	singen
    435	bewegen
    436	menge
    437	öffnen
    438	König
    439	drauf
    440	wahrscheinlich
    441	irgendwie
    442	drehen
    443	krank
    444	Befehl
    445	interessiert
    446	Telefon
    447	hübsch
    448	tanzen
    449	hierher
    450	irgendwas
    451	zuerst
    452	verletzt
    453	bereits
    454	gestohlen
    455	opfer
    456	Hölle
    457	Arzt
    458	Straße
    459	erledigt
    460	direkt
    461	Doktor
    462	froh
    463	großartig
    464	steig
    465	sondern
    466	Fehler
    467	hängt
    468	schwarze
    469	erfahren
    470	willkommen
    471	besorgt
    472	vorstellen
    473	kaum
    474	Millionen
    475	klappe
    476	erkennen
    477	Sekunden
    478	sechs
    479	Kumpel
    480	stück
    481	Geschäft
    482	Mord
    483	zehn
    484	Büro
    485	wert
    486	acht
    487	Idiot
    488	Aufgabe
    489	himmel
    490	ehre
    491	fehlt
    492	bauen
    493	vermisst
    494	halb
    495	zweite
    496	überall
    497	ansehen
    498	küssen
    499	licht
    500	perfekt
    501	völlig
    502	zerstört
    503	herausfinden
    504	trotzdem
    505	still
    506	hm
    507	erde
    508	bieten
    509	schwierig
    510	weh
    511	schade
    512	person
    513	Luft
    514	angriff
    515	behalten
    516	cool
    517	druck
    518	Foto
    519	tief
    520	wunder
    521	normal
    522	schwöre
    523	spannende
    524	schrecklich
    525	deswegen
    526	danach
    527	sinn
    528	lustig
    529	erschossen
    530	fuß
    531	melden
    532	fassen
    533	regeln
    534	ziel
    535	stören
    536	Körper
    537	treten
    538	überleben
    539	Kaffee
    540	gefährlich
    541	erreichen
    542	wow
    543	beruhigen
    544	Wind
    545	links
    546	raum
    547	übernehmen
    548	guck
    549	blöd
    550	Party
    551	Onkel
    552	selber
    553	nochmal
    554	nachdem
    555	Rest
    556	wahl
    557	komisch
    558	Leiche
    559	kostet
    560	Witz
    561	Sam
    562	drüben
    563	rot
    564	persönlich
    565	deutsche
    566	weise
    567	irgendwo
    568	haare
    569	Beine
    570	Pferd
    571	tja
    572	genauso
    573	wunderbar
    574	Schlüssel
    575	Krankenhaus
    576	vorsichtig
    577	damals
    578	zwar
    579	verzeihen
    580	beeil
    581	Gefängnis
    582	unglaublich
    583	ärger
    584	kraft
    585	seltsam
    586	Wohnung
    587	heilige
    588	kalt
    589	stolz
    590	Boss
    591	Arschloch
    592	Zukunft
    593	Geist
    594	irgendeine
    595	nachgedacht
    596	bekannt
    597	merken
    598	rolle
    599	Mund
    600	Entscheidung
    601	gedanken
    602	außerdem
    603	offen
    604	wovon
    605	fürchte
    606	nähe
    607	karte
    608	Boden
    609	Mörder
    610	sobald
    611	schmerz
    612	Mist
    613	Michael
    614	super
    615	irre
    616	klasse
    617	Schluss
    618	Angebot
    619	beschützen
    620	bericht
    621	stopp
    622	interessant
    623	solange
    624	Charlie
    625	entfernt
    626	Sicherheit
    627	Gäste
    628	eher
    629	verändert
    630	erwischt
    631	jemals
    632	besonders
    633	Brief
    634	verlangt
    635	aufgenommen
    636	Agent
    637	wenigstens
    638	wette
    639	absolut
    640	Lady
    641	unmöglich
    642	Liebling
    643	Informationen
    644	nötig
    645	traurig
    646	heraus
    647	Tiere
    648	Geheimnis
    649	mitnehmen
    650	nutzen
    651	rennen
    652	sieben
    653	Meinung
    654	Vogel
    655	verwenden
    656	Präsident
    657	punkt
    658	hinten
    659	besitz
    660	Soldaten
    661	Hotel
    662	fick
    663	dunkel
    664	tisch
    665	gewissen
    666	Zug
    667	feind
    668	plötzlich
    669	schützen
    670	verheiratet
    671	wunderschön
    672	aufhalten
    673	frank
    674	verliebt
    675	Handy
    676	zählt
    677	Kleid
    678	schnappen
    679	griff
    680	treiben
    681	Bewegung
    682	riecht
    683	überlegen
    684	springen
    685	vorher
    686	erhalten
    687	Verzeihung
    688	beenden
    689	tatsächlich
    690	Anwalt
    691	York
    692	Peter
    693	Geschenk
    694	Streit
    695	blick
    696	bescheid
    697	verfolgt
    698	feiern
    699	Seele
    700	schritt
    701	Finger
    702	Möglichkeit
    703	verraten
    704	überprüfen
    705	Fenster
    706	kochen
    707	besonderes
    708	überrascht
    709	verhaftet
    710	erlaubt
    711	augenblick
    712	zurückkommen
    713	schnitt
    714	spüren
    715	angenommen
    716	Tasche
    717	packen
    718	Beziehung
    719	Chef
    720	schwach
    721	Polizist
    722	wählen
    723	genießen
    724	obwohl
    725	kennenzulernen
    726	rauchen
    727	handeln
    728	verpasst
    729	preis
    730	angetan
    731	Test
    732	behandelt
    733	fisch
    734	gezwungen
    735	verbunden
    736	dagegen
    737	rum
    738	Max
    739	Boot
    740	rücken
    741	dringend
    742	Schwein
    743	ständig
    744	überzeugt
    745	Bier
    746	aufwachen
    747	leer
    748	atmen
    749	willen
    750	unterwegs
    751	Verbindung
    752	jagen
    753	Eier
    754	zuhause
    755	partner
    756	Gesetz
    757	Hochzeit
    758	betrogen
    759	ewig
    760	Weiss
    761	fressen
    762	naja
    763	Frieden
    764	herum
    765	fremden
    766	geboren
    767	rüber
    768	David
    769	manche
    770	Richtung
    771	bar
    772	müde
    773	irgendetwas
    774	reiß
    775	Paris
    776	gemeinsam
    777	sauber
    778	Unfall
    779	Volk
    780	Flugzeug
    781	beschäftigt
    782	herkommen
    783	Schuss
    784	ermordet
    785	geschenkt
    786	mitten
    787	aufgeregt
    788	lösen
    789	derjenige
    790	Firma
    791	blau
    792	wirkt
    793	erwachsen
    794	Beispiel
    795	ring
    796	Ohren
    797	decke
    798	beobachtet
    799	wozu
    800	Harry
    801	grab
    802	verflucht
    803	Paul
    804	Kontrolle
    805	Berg
    806	Wald
    807	getrennt
    808	furchtbar
    809	leisten
    810	liste
    811	Vorsicht
    812	Kamera
    813	Professor
    814	Computer
    815	frisch
    816	aufpassen
    817	Schuhe
    818	wild
    819	wofür
    820	Kontakt
    821	darin
    822	sonne
    823	leck
    824	dahin
    825	Rose
    826	Bullen
    827	gold
    828	starten
    829	Baum
    830	menschliche
    831	dick
    832	warm
    833	entspann
    834	dritte
    835	irgendwann
    836	Erinnerung
    837	Mark
    838	jedenfalls
    839	kaputt
    840	hoffentlich
    841	Hoffnung
    842	tschüss
    843	sowieso
    844	leise
    845	unbedingt
    846	trauen
    847	zumindest
    848	Überraschung
    849	runde
    850	bisher
    851	heil
    852	Drogen
    853	Hunger
    854	offensichtlich
    855	gewarnt
    856	Held
    857	neben
    858	ergibt
    859	nick
    860	gesund
    861	Patienten
    862	erwähnt
    863	sauer
    864	brennt
    865	Glas
    866	Geburtstag
    867	Gericht
    868	nerven
    869	angekommen
    870	vergeben
    871	entdeckt
    872	Maschine
    873	übel
    874	mitgebracht
    875	Regierung
    876	Henry
    877	unterschied
    878	unschuldig
    879	Schicksal
    880	Armee
    881	schlampe
    882	klingelt
    883	Nase
    884	schuldig
    885	lächeln
    886	angestellt
    887	Tante
    888	Kirche
    889	betrunken
    890	Hose
    891	verdächtigen
    892	Bord
    893	Untertitel
    894	Situation
    895	übrig
    896	irgendwelche
    897	unternehmen
    898	erlebt
    899	Lied
    900	vorbereitet
    901	ausgehen
    902	Stein
    903	vermutlich
    904	Gebäude
    905	Drink
    906	Grad
    907	Alex
    908	Majestät
    909	diesmal
    910	vertrag
    911	Ehemann
    912	ha
    913	verantwortlich
    914	stöhnt
    915	klopfen
    916	probieren
    917	regen
    918	Zeitung
    919	Kugel
    920	vergnügen
    921	geklaut
    922	ball
    923	klug
    924	hinterlassen
    925	fantastisch
    926	witzig
    927	gegenüber
    928	Ben
    929	schmeckt
    930	Show
    931	verbrannt
    932	Gesellschaft
    933	miteinander
    934	aufstehen
    935	Lust
    936	verhalten
    937	Insel
    938	abholen
    939	erfolg
    940	Dorf
    941	abhauen
    942	Freude
    943	grenze
    944	ran
    945	nämlich
    946	aufgetaucht
    947	beten
    948	loch
    949	Gruppe
    950	grüß
    951	fliehen
    952	grün
    953	Zeichen
    954	heim
    955	Tee
    956	übrigens
    957	bombe
    958	eis
    959	quatsch
    960	nervös
    961	soweit
    962	indem
    963	Blumen
    964	unterschreiben
    965	Achtung
    966	empfangen
    967	erscheinen
    968	bemerkt
    969	hals
    970	flucht
    971	kapiert
    972	Don
    973	Weihnachten
    974	Sarah
    975	Bob
    976	Vergangenheit
    977	entweder
    978	Sheriff
    979	geheim
    980	weder
    981	anziehen
    982	jawohl
    983	Gespräch
    984	ungefähr
    985	entkommen
    986	zuvor
    987	Position
    988	Amerika
    989	bestellt
    990	verboten
    991	glückwunsch
    992	Königin
    993	Staaten
    994	Adresse
    995	Messer
    996	Meer
    997	drinnen
    998	behauptet
    999	mitkommen
    1000	herein
