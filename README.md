Przedmiot:
Aplikacje internetowe 2

Dokumentacja projektowa aplikacji do predykcji i wizualizacji pogody na podstawie danych historycznych


Wykonali: 
Rejman Konrad
Marzec Adam
Matyaszek Mateusz
Wojdy�a Marek

Prowadz�cy: dr in�. Piotr Lasek
Rzesz�w 2018/2019


�	Opis projektu
Celem projektu by�o stworzenie aplikacji webowej opartej na technologii Django. Aplikacja ma s�u�y� do predykcji i wizualizacji pogody na podstawie danych historycznych.  Projekt ten zosta� zrealizowany na potrzeby przedmiotu Aplikacje internetowe 2.
�	Wymagania Systemowe
Aby uruchomi� aplikacj� na komputerze musimy mie� zainstalowany Python 3.6. oraz freamwork �Django�. Instalujemy go polenieniami:
py -m pip install --upgrade pip
py -m pip install django
�	Instrukcja Obs�ugi Aplikacji
1.	Przy pomocy konsoli przechodzimy do lokalizacji w kt�rym znajduj� si� aplikacja:
 
2.	Uruchamiamy serwer poprzez polecenie "py manage.py runserver"
 
3.	Kopiujemy adres serwera i uruchamiamy go w przegl�darce internetowej
 
4.	Nasza aplikacja znajduj� si� pod tym adresem: �http://127.0.0.1:8000/weather/�
�	Wygl�d oraz dzia�anie aplikacji
Aplikacja przewiduje pogod� na aktualny miesi�c dla miasta Rzesz�w w formie (�rednia temperatura na miesi�c oraz szansa opad�w)
 
Udost�pnia archiwum pogodowe dla Rzeszowa dla 18 lat:
 




Przedstawia dane pogodowe w formie dw�ch wykres�w:
 
�	Panel administracyjny
 

Po zalogowaniu do panelu administracyjnego mo�emy zarz�dza� nasz� baz� danych:
 

�	Mechanika dzia�ania aplikacji
Lokalna baza danych pogody dla miasta Rzesz�w zawiera takie informacje jak: �rednia temperatura oraz ilo�� dni z opadem w danym miesi�cu w okresie 18 lat (od roku 2000 do 2017). 
Program sprawdza aktualny miesi�c i na podstawie bazy danych � wylicza �redni� temperatur� wszystkich temperatur z wcze�niejszych lat dla tego miesi�ca.
Podobnie wyliczana jest predykcja opad�w. Wynik jest podawany w procentach. �rednia ilo�� dni z opadem jest dzielona na ilo�� dni danego miesi�ca � w ten spos�b otrzymujemy prawdopodobie�stwo opad�w na aktualny miesi�c.
�	Technologie
W realizacji aplikacji wykorzystano nast�puj�ce technologie oraz narz�dzia:
�	Python 
To j�zyk skryptowy, interpretowany - co oznacza, �e piszemy skrypt a nast�pnie wykonujemy go za pomoc� interpretera. Python jest �atwy w nauce, lecz mimo to jest bardzo pot�ny. Dzia�a na wielu systemach, w tym na systemach wbudowanych.
�	Django 
To darmowy i open-source'owy framework do tworzenia aplikacji webowych, napisany w Pythonie.
�	HTML5 
To skr�t od Hypertext Markup Language, co oznacza, �e jest on hipertekstowym j�zykiem znacznik�w. HTML opisuje struktur� strony internetowej, a jego elementami sk�adowymi s� znaczniki. Warto pami�ta�, �e HTML nie jest j�zykiem programowania, bo nie mo�na w nim wykonywa� np. oblicze�. HTML pozwala nam zbudowa� struktur�, czyli szkielet np. naszej strony internetowej.
�	CSS3 
Odpowiada za wygl�d naszych stron internetowych. U�ywaj�c tego j�zyka mo�emy zmieni� na naszych stronach mi�dzy innymi kolory i wielko�ci font�w. Kod CSS mo�na umie�ci� w oddzielnym pliku z rozszerzeniem .css i "wstawi�" go poprzez specjalny tag HTML. Mo�na te� umie�ci� go bezpo�rednio w dokumencie HTML.
�	JavaScript 
JavaScript to j�zyk programowania, kt�ry umo�liwia wdro�enie na stronie internetowej skomplikowanych element�w, dzi�ki kt�rym strona ta mo�e nie tylko wy�wietla� statyczne informacje, ale r�wnie� obs�ugiwa� zmian� tre�� odpowiednio do sytuacji, wy�wietla� interaktywne mapy i animacje grafiki 2D/3D , wy�wietla� video itd. Jest to trzecia warstwa standardowych technologii internetowych
�	Bootstrap
Freamwork CSS, rozwijany przez programist�w Twittera. Zawiera zestaw przydatnych narz�dzi u�atwiaj�cych tworzenie interfejsu graficznego stron oraz aplikacji internetowych. Bazuje g��wnie na gotowych rozwi�zaniach HTML oraz CSS (kompilowanych z plik�w Less[2]) i mo�e by� stosowany m.in. do stylizacji takich element�w jak teksty, formularze, przyciski, wykresy, nawigacje i innych komponent�w wy�wietlanych na stronie. Framework korzysta tak�e z j�zyka JavaScript.
�	Chart.js
Biblioteka ta zawiera animowane i interaktywnych wykresy oparte na elemencie canvas (HTML5) oraz zestawu skrypt�w JavaScript.

�	Pliki wchodz�ce w sk�ad projektu:
Serwis pogody sk�ada si� z kilku widok�w HTML odpowiedzialnych za wy�wietlanie konkretnych informacji w zale�no�ci od zapytania URL.
�	base.html � jest to bazowy plik, do kt�rego wczytywane s� konkretne widoki. Zawiera w sobie stopk� strony internetowej. Dodatkowo posiada meta tagi w sekcji head, odpowiedzialne za import skrypt�w Chart.js, Bootstrap oraz posiada lokalne style css.
�	index.html � jest to plik zawieraj�cy widok dla strony g��wnej serwisu. Wczytuje on informacje na temat przewidywanej temperatury oraz prawdopodobie�stwo opad�w w aktualnym miesi�cu. S� tam r�wnie� zamieszczone linki do poszczeg�lnych lat archiwa pogodowego.
�	year.html � plik ten odpowiada za wy�wietlanie archiwum pogodowego na konkretne lata w formie wykres�w
Za wy�wietlaniem konkretnych widok�w odpowiedzialne s� pliki:
�	urls.py � w nim okre�lany jest adres URL pod kt�rym b�dzie wczytywany konkretny widok.
�	views.py � plik, w kt�ry zdefiniowane s� funkcje dla widok�w. Najcz�ciej pe�ni� one funkcj� kontroler�w wskazuj�cych ko�cowe pliki html przekazuj�c do nich dane.
�	models.py � ten plik reprezentuj� obiekty w bazie danych 
baza zawiera jedn� tabel� (Trials) zawieraj�c� kolumny: 
- year � rok
- month � miesi�c
- temp � �rednia temperatura
- fall � ilo�� dni z opadem w danym miesi�cu


