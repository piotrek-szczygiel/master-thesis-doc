# Minimizing interaction delay in collaborative web applications

In recent years, technologies have emerged to address the problem of unresponsive and slow websites.
This paper examines the impact of using WebAssembly, WebSocket and WebRTC technologies on the interaction delay in collaborative web applications.
WebAssembly allows programs compiled into a special binary format to run in a browser.
Three different programming languages that can compile to WebAssembly were analyzed and the performance of their resulting code was compared among themselves and with JavaScript.
Based on the results, the most promising language was selected, for which additional tests were then prepared to more closely examine the performance differences between it and JavaScript.
The WebSocket protocol provides a two-way channel for exchanging data over a single TCP connection.
It allows browsers to open an interactive communication session with an external server with less system load than alternatives such as continuous HTTP polling.
WebRTC is a project that provides browsers with the ability to communicate in real time through a set of programming interfaces.
It allows web applications to stream audiovisual media and exchange a variety of data between browsers, using UDP, TCP and SCTP protocols underneath.
The final test created a sample interactive web application, written in three versions: with JavaScript, WebAssembly and as a native application.
The communication layer in the application was provided by WebSocket and WebRTC technologies.
Differences in the local computation performance of each version of the application were investigated, and differences in communication latency were measured.
Based on all the tests performed, a set of recommended practices used in developing collaborative web applications was created.

# Minimalizacja opóźnienia w interakcji użytkowników korzystających z aplikacji webowych

W ciągu ostatnich lat pojawiły się technologie, których celem było podjęcie problemu mało responsywnych i wolnych stron internetowych.
W pracy tej zbadany został wpływ wykorzystania technologii WebAssembly, WebSocket oraz WebRTC na opóźnienia w interakcji użytkowników korzystających z aplikacji webowych.
Technologia WebAssembly umożliwia uruchamianie w przeglądarce programów skompilowanych do specjalnego binarnego formatu.
Przeanalizowano trzy różne języki programowania, które mogą kompilować się do WebAssembly oraz porównano wydajność ich kodu wynikowego między sobą oraz z językiem JavaScript.
Na podstawie uzyskanych wyników wybrano najbardziej obiecujący język, dla którego przygotowano następnie dodatkowe testy dokładniej badające różnice w wydajności między nim a JavaScript.
Protokół WebSocket zapewnia dwukierunkowy kanał wymiany danych poprzez pojedyncze połączenie TCP.
Umożliwia przeglądarkom otwarcie interaktywnej sesji komunikacji z zewnętrznym serwerem przy mniejszym obciążeniu systemu niż alternatywne rozwiązanie takie jak np. ciągłe odpytywanie HTTP.
WebRTC to projekt zapewniający przeglądarkom możliwość komunikacji w czasie rzeczywistym za pomocą zestawu interfejsów programowania.
Umożliwia aplikacjom webowym strumieniowanie mediów audiowizualnych oraz wymianę różnorodnych danych pomiędzy przeglądarkami, korzystając pod spodem z protokołów UDP, TCP oraz SCTP.
W finalnym teście stworzono przykładową interaktywną aplikację webową, napisaną w trzech wersjach: z użyciem JavaScript, WebAssembly oraz jako aplikację natywną.
Warstwę komunikacyjną w aplikacji zapewniły technologie WebSocket oraz WebRTC.
Zbadano różnice w wydajności lokalnych obliczeń każdej z wersji aplikacji oraz zmierzono różnice w opóźnieniach komunikacji.
Na podstawie wszystkich przeprowadzonych testów utworzono zbiór rekomendowanych praktyk wykorzystywanych przy tworzeniu kolaboratywnych aplikacji webowych.
