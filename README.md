Przedmiot:
Aplikacje internetowe 2

Dokumentacja projektowa aplikacji do predykcji i wizualizacji pogody na podstawie danych historycznych


Wykonali: 
Rejman Konrad
Marzec Adam
Matyaszek Mateusz
Wojdy³a Marek

Prowadz¹cy: dr in¿. Piotr Lasek
Rzeszów 2018/2019


•	Opis projektu
Celem projektu by³o stworzenie aplikacji webowej opartej na technologii Django. Aplikacja ma s³u¿yæ do predykcji i wizualizacji pogody na podstawie danych historycznych.  Projekt ten zosta³ zrealizowany na potrzeby przedmiotu Aplikacje internetowe 2.
•	Wymagania Systemowe
Aby uruchomiæ aplikacjê na komputerze musimy mieæ zainstalowany Python 3.6. oraz freamwork „Django”. Instalujemy go polenieniami:
py -m pip install --upgrade pip
py -m pip install django
•	Instrukcja Obs³ugi Aplikacji
1.	Przy pomocy konsoli przechodzimy do lokalizacji w którym znajdujê siê aplikacja:
 
2.	Uruchamiamy serwer poprzez polecenie "py manage.py runserver"
 
3.	Kopiujemy adres serwera i uruchamiamy go w przegl¹darce internetowej
 
4.	Nasza aplikacja znajdujê siê pod tym adresem: „http://127.0.0.1:8000/weather/”
•	Wygl¹d oraz dzia³anie aplikacji
Aplikacja przewiduje pogodê na aktualny miesi¹c dla miasta Rzeszów w formie (œrednia temperatura na miesi¹c oraz szansa opadów)
 
Udostêpnia archiwum pogodowe dla Rzeszowa dla 18 lat:
 




Przedstawia dane pogodowe w formie dwóch wykresów:
 
•	Panel administracyjny
 

Po zalogowaniu do panelu administracyjnego mo¿emy zarz¹dzaæ nasz¹ baz¹ danych:
 

•	Mechanika dzia³ania aplikacji
Lokalna baza danych pogody dla miasta Rzeszów zawiera takie informacje jak: œrednia temperatura oraz iloœæ dni z opadem w danym miesi¹cu w okresie 18 lat (od roku 2000 do 2017). 
Program sprawdza aktualny miesi¹c i na podstawie bazy danych – wylicza œredni¹ temperaturê wszystkich temperatur z wczeœniejszych lat dla tego miesi¹ca.
Podobnie wyliczana jest predykcja opadów. Wynik jest podawany w procentach. Œrednia iloœæ dni z opadem jest dzielona na iloœæ dni danego miesi¹ca – w ten sposób otrzymujemy prawdopodobieñstwo opadów na aktualny miesi¹c.
•	Technologie
W realizacji aplikacji wykorzystano nastêpuj¹ce technologie oraz narzêdzia:
•	Python 
To jêzyk skryptowy, interpretowany - co oznacza, ¿e piszemy skrypt a nastêpnie wykonujemy go za pomoc¹ interpretera. Python jest ³atwy w nauce, lecz mimo to jest bardzo potê¿ny. Dzia³a na wielu systemach, w tym na systemach wbudowanych.
•	Django 
To darmowy i open-source'owy framework do tworzenia aplikacji webowych, napisany w Pythonie.
•	HTML5 
To skrót od Hypertext Markup Language, co oznacza, ¿e jest on hipertekstowym jêzykiem znaczników. HTML opisuje strukturê strony internetowej, a jego elementami sk³adowymi s¹ znaczniki. Warto pamiêtaæ, ¿e HTML nie jest jêzykiem programowania, bo nie mo¿na w nim wykonywaæ np. obliczeñ. HTML pozwala nam zbudowaæ strukturê, czyli szkielet np. naszej strony internetowej.
•	CSS3 
Odpowiada za wygl¹d naszych stron internetowych. U¿ywaj¹c tego jêzyka mo¿emy zmieniæ na naszych stronach miêdzy innymi kolory i wielkoœci fontów. Kod CSS mo¿na umieœciæ w oddzielnym pliku z rozszerzeniem .css i "wstawiæ" go poprzez specjalny tag HTML. Mo¿na te¿ umieœciæ go bezpoœrednio w dokumencie HTML.
•	JavaScript 
JavaScript to jêzyk programowania, który umo¿liwia wdro¿enie na stronie internetowej skomplikowanych elementów, dziêki którym strona ta mo¿e nie tylko wyœwietlaæ statyczne informacje, ale równie¿ obs³ugiwaæ zmianê treœæ odpowiednio do sytuacji, wyœwietlaæ interaktywne mapy i animacje grafiki 2D/3D , wyœwietlaæ video itd. Jest to trzecia warstwa standardowych technologii internetowych
•	Bootstrap
Freamwork CSS, rozwijany przez programistów Twittera. Zawiera zestaw przydatnych narzêdzi u³atwiaj¹cych tworzenie interfejsu graficznego stron oraz aplikacji internetowych. Bazuje g³ównie na gotowych rozwi¹zaniach HTML oraz CSS (kompilowanych z plików Less[2]) i mo¿e byæ stosowany m.in. do stylizacji takich elementów jak teksty, formularze, przyciski, wykresy, nawigacje i innych komponentów wyœwietlanych na stronie. Framework korzysta tak¿e z jêzyka JavaScript.
•	Chart.js
Biblioteka ta zawiera animowane i interaktywnych wykresy oparte na elemencie canvas (HTML5) oraz zestawu skryptów JavaScript.

•	Pliki wchodz¹ce w sk³ad projektu:
Serwis pogody sk³ada siê z kilku widoków HTML odpowiedzialnych za wyœwietlanie konkretnych informacji w zale¿noœci od zapytania URL.
•	base.html – jest to bazowy plik, do którego wczytywane s¹ konkretne widoki. Zawiera w sobie stopkê strony internetowej. Dodatkowo posiada meta tagi w sekcji head, odpowiedzialne za import skryptów Chart.js, Bootstrap oraz posiada lokalne style css.
•	index.html – jest to plik zawieraj¹cy widok dla strony g³ównej serwisu. Wczytuje on informacje na temat przewidywanej temperatury oraz prawdopodobieñstwo opadów w aktualnym miesi¹cu. S¹ tam równie¿ zamieszczone linki do poszczególnych lat archiwa pogodowego.
•	year.html – plik ten odpowiada za wyœwietlanie archiwum pogodowego na konkretne lata w formie wykresów
Za wyœwietlaniem konkretnych widoków odpowiedzialne s¹ pliki:
•	urls.py – w nim okreœlany jest adres URL pod którym bêdzie wczytywany konkretny widok.
•	views.py – plik, w który zdefiniowane s¹ funkcje dla widoków. Najczêœciej pe³ni¹ one funkcjê kontrolerów wskazuj¹cych koñcowe pliki html przekazuj¹c do nich dane.
•	models.py – ten plik reprezentujê obiekty w bazie danych 
baza zawiera jedn¹ tabelê (Trials) zawieraj¹c¹ kolumny: 
- year – rok
- month – miesi¹c
- temp – œrednia temperatura
- fall – iloœæ dni z opadem w danym miesi¹cu


