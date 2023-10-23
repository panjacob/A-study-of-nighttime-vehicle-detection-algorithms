# -*- coding: utf-8 -*-

import re

# Provide the LaTeX content as a string
latex_content = r"""
\chapter{Wstęp}


Przedmiotem pracy jest sprawdzenie wybranych metod detekcji pojazdów w~porze nocnej, które mogą być wykorzystane w~celu zwiększenia widoczności pieszych na przejściach. Wykrycie pojazdu przez algorytm skutkowałoby zapaleniem się dodatkowego oświetlenia na przejściu w~taki sposób, żeby kierowca mógł odpowiednio wcześnie zareagować na pojawienie się na nim pieszego. W tym celu została zaproponowana platforma, która wykorzystując dane z kamery i~czujnika intensywności światła wykryje zbliżający się pojazd.

Z roku na rok ilość pojazdów na drogach w~Polsce, jak i~na świecie się zwiększa \cite{17_zarejestrowane_samochody,zarejestrowane_samochody_2}.
Ze statystyk transportu drogowego w~Polsce w~latach 2018-2019 wynika, że większość wypadków powodują kierujący pojazdami \cite{24_transport_drogowy}.
Badania przeprowadzone przez "International Transport Forum" \cite{18_piesi_poszkodowani} dowodzą, że w~niektórych krajach rozwiniętych (Wielka Brytania i~Stany Zjednoczone) na przestrzeni lat 2010 - 2019 wzrosła liczba wypadków z udziałem pieszych.

W Polsce w~roku 2022 wypadków, których przyczyną było nieustąpienie pierwszeństwa pieszemu na przejściu dla pieszych, było 11,6\%, a 3,5\% wypadków było spowodowanych z winy pieszego \cite{91_wypadki_policja}.

W pracy skupiono się na wykrywaniu pojazdów na przejściach dla pieszych, dlatego, że jest drugim najczęstszym miejscem wypadków \cite{91_wypadki_policja}. Na rysunku \ref{fig:statystyki_wypadkow} ukazano statystyki dotyczące miejsc wypadków w~Polsce. Na przejściach dla pieszych ma miejsce 12,6\% wszystkich wypadków. Informowanie kierujących pojazdy o uczestnikach ruchu przekraczających przejścia i~przejazdy jest poważnym problemem. Po zmroku widoczność pieszego na przejściu pogarsza się, zwłaszcza wtedy, kiedy z naprzeciwka nadjeżdża pojazd, który oślepia kierowcę z naprzeciwka. Proponowane rozwiązanie ma na celu pomóc w~redukcji wypadków z udziałem pieszych na drogach.

% W 2022 roku w~Polsce zarejestrowano 2251 wypadków spowodowanych przez kierowców, których przyczyną było nieustąpienie pierwszeństwa pieszemu na przejściu dla pieszych, co stanowi 11,6\% wszystkich wypadków \cite{91_wypadki_policja}. Z kolei liczba wypadków z winy pieszego spowodowanych nieostrożnym wejściem na jezdnię przed jadący pojazd, zza pojazdu lub innej przeszkody wyniosła 677. Na rysunku \ref{fig:statystyki_wypadkow} ukazano statystyki dotyczące miejsc wypadków w~Polsce. Drugim najczęstszym miejscem jest przejście dla pieszych i~stanowi 12,6\% wszystkich wypadków. Wypadki na przejazdach dla rowerzystów stanowią 3,6\% wszystkich wypadków. Informowanie uczestników ruchu przekraczających przejścia i~przejazdy o zbliżającym się pojeździe jest poważnym problemem. Po zmroku widoczność pieszego na przejściu pogarsza się, zwłaszcza wtedy, kiedy z naprzeciwka nadjeżdża pojazd. Proponowane rozwiązanie ma na celu pomóc w~redukcji wypadków z udziałem pieszych na drogach.

\begin{figure}[h]
    \centering
    \includegraphics[width=0.8\textwidth]{img/statystyki_wypadkow.png}
    \caption{Statystyki miejsc wypadków w~Polsce w~roku 2022. Opracowanie według statystyk policji\cite{91_wypadki_policja}}
    \label{fig:statystyki_wypadkow}
\end{figure}

Występują liczne badania, które zostały poświęcone wykrywaniu pojazdów w~dobrych warunkach oświetleniowych. W pracy "Structured learning via convolutional neural networks for vehicle detection" \cite{4_dobre_warunki_1} przeprowadzono badania wykorzystując splotową sieć neuronową do segmentacji binarnej do wykrywania pojazdów. W innej pracy \cite{5_dobre_warunki_2} badania poświęcono sieci splotowej w~celu detekcji pojazdów w~różnej skali. Przed dominacją sieci neuronowych wykorzystywane były inne algorytmy, takie jak maszyna wektorów nośnych wykorzystujące wyekstrahowane cechy przy pomocy \textit{Histogram Oriented Gradients} \cite{26_HOG}. W jednym z artykułów \cite{13_swiatla_tyl} wykorzystany został algorytm \textit{AdaBoost} \cite{14_adaboost}.

Poruszane są również tematy detekcji pieszych i~rowerzystów \cite{11_piesi_i_rowerzysci}.
Tworzone są też liczne prace skupiające się na wykrywaniu pojazdów. Część z nich skupia się na przednich światłach pojazdów \cite{12_swiatla_przod}, a część na wykrywaniu świateł z tyłu \cite{13_swiatla_tyl}. Wiele prac poświęconych jest detekcji pojazdów w~nocy \cite{2_wykrywanie_w_nocy,10_wykrywanie_w_nocy_2} jak i~śledzeniu ich \cite{16_sledzenie_swiatel}, które jest przydatne w~zastosowaniach monitoringu miejskiego.

Przeprowadzono też wiele badań poświęconych wykrywaniu pojazdów w~niekorzystnych warunkach. Praca zatytułowana "Robust Vehicle Detection and Distance Estimation Under Challenging Lighting Conditions" \cite{6_niekorzystne_warunki} proponuje segmentację cech Haar'a (ang. \textit{Haar-like features}) do detekcji pojazdów w~trudnych warunkach oświetleniowych. W innej pracy zatytułowanej "Raindrop-Tampered Scene Detection and Traffic".
Praca zatytułowana "Nighttime Visibility Analysis and Estimation Method in the Presence of Dense Fog" \cite{7_niekorzystne_warunki} skupiła się nad wykrywaniem pojazdów podczas gęstej mgły. Głównym problemem wykrywania pojazdów w~takich warunkach są powstające aureole wokół źródeł światła (ang. \textit{halos around light sources}). W obu pracach wykorzystywana jest segmentacja i~metody kontrastowe, do wykrycia anomalii. Inne badanie zatytułowane "Improving the Performance of Vehicle Detection System in Bad Weathers" \cite{0_niekorzystne_warunki} wykorzystało okno przesuwne Violi i~Jones'a (ang. \textit{Viola and Jones's sliding-window}) do detekcji. Badanie "Flow Estimation for Nighttime Traffic Surveillance" zajęto się problemem wykrywania pojazdów w~porze nocnej, gdzie na obiektywie kamery znajduje się woda.

W Polsce w~latach 2020-2022 najwięcej wypadków było w~ciągu dnia i~wynika to z tego, że wtedy jeździ najwięcej samochodów. Jednak w~nocy jest czterokrotnie większe prawdopodobieństwo, że jeśli zdarzył się wypadek, to był on śmiertelny \cite{91_wypadki_policja,99_wypadki_drogowe_2020_noc,98_wypadki_drogowe_2021_noc}.

Informacja o nadjeżdżającym pojeździe jest szczególnie istotna w~nocy, kiedy widoczność zarówno dla kierowcy, jak i~pieszego jest ograniczona. Praca skupia się na badaniu algorytmów wykrywania pojazdów w~porze nocnej, przy pomocy kamery \textit{RGB} i~czujnika intensywności światła. Po zachodzie słońca rzadko jest widoczna cała sylwetka samochodu. Na obrazie najbardziej widoczne są światła pojazdu. Na ich wykrywaniu skupia się algorytm. Światła mijania są trudne do wykrycia ze względu na to, że mogą być nieprawidłowo ustawione i~mogą spowodować oślepianie matrycy kamery. Częstym przypadkiem jest też, że jedna żarówka w~pojeździe jest uszkodzona tak jak na \ref{fig:jednoswiatlo}, w~wyniku czego na obrazie widoczne jest tylko jedno światło, co stanowi dodatkowe utrudnienie \cite{15_jedno_swiatlo}.

\begin{figure}[H]
    \centering
    \begin{subfigure}[b]{0.3\textwidth}
        \includegraphics[width=\textwidth]{img/jedno_swiatlo_przod.png}
        \caption{Pojazd z niesprawnym światłem}
        \label{fig:jednoswiatlo}
    \end{subfigure}
    \begin{subfigure}[b]{0.3\textwidth}
        \includegraphics[width=\textwidth]{img/odbicie.png}
        \caption{Odbicia świetlne}
        \label{fig:odbicie}
    \end{subfigure}
    \begin{subfigure}[b]{0.3\textwidth}
        \includegraphics[width=\textwidth]{img/zanieczyszczenie_swietlne.png}
        \caption{Oślepienie kamery}
        \label{fig:zanieczyszczenie_swietlne}
    \end{subfigure}

    \caption{Obrazy z opracowanego zbioru danych - zaprezentowano przypadki trudne do detekcji dla algorytmów uczenia maszynowego}
    \label{fig:przykladowe_obrazy}
\end{figure}

Współczesne prace do detekcji pojazdów w~nocy wykorzystują głębokie sieci neuronowe. Badanie zatytułowane "GAN-Based Day-to-Night Image Style Transfer for Nighttime Vehicle Detection" \ \cite{100_noc_gan} wykorzystało transferowanie stylu za pomocą sieci typu \textit{GAN} (ang. \textit{Generative Adversarial Network}) do rozszerzania zbioru danych i~
Faster-RCNN i~YOLO9000 \cite{101_YOLO9000} do detekcji obrazów. W innym badaniu "An Improved YOLOX Model and Domain Transfer Strategy for Nighttime Pedestrian and Vehicle Detection" \cite{102_yolo_noc} wykorzystano sieć detekcji YOLOX \cite{103_yolox2021} do detekcji pojazdów.
W badaniu "Design and Evaluation of a Vehicle Detection System in Low Light Conditions" \ wykorzystane zostały cykliczne generatywne sieci adwersarzy (ang. \textit{Cycle Generative Adversarial Networks}) do rozszerzenia zbioru i~sieci detekcji takie jak  YOLOv4, Faster-RCNN, ResNet, SSD MobileNetV2. Inne badania poruszające tę tematykę używały także algorytmów YOLOV3 \cite{1_yolo,27_yolov3} lub MobileNetV3 \cite{72_MobileNetv3} do wykrywania pojazdów.

W tym badaniu skupiono się na wykrywaniu pojazdów z wykorzystaniem głębokich sieci neuronowych. Zostały zebrane dane i~utworzone zostały dwa zbiory danych - do klasyfikacji i~detekcji. Za pomocą kamery i~czujnika zebrano dane wizualne i~informację o natężeniu światła. Następnie dane z czujnika zostały zsynchronizowane i~ręcznie oznaczone.

Pierwszym rodzajem badanych algorytmów były sieci detekcji.
Opisane zostały metody zastosowanych metod wykrywania obiektów i~ekstrakcji cech przy pomocy sieci neuronowych. Sprawdzono sieci CenterNet HourGlass104, CenterNet MobileNetV2 FPN, EfficentDet D0, EfficentDet D1, SSD MobileNetV2 FPNLite 320x320, SSD MobileNetV2 FPNLite 640, SSD MobileNetV2, SSD ResNet50, Faster RCNN ResNet50, YOLOV8n oraz YOLOV8s. Wymienione sieci zostały sprawdzone pod kątem metryk dokładności, precyzji i~czułości oraz wydajności na platformach docelowych. Przed treningiem zostały wykonane testy mające na celu jak najlepsze wytrenowanie wybranych sieci. Wszystkie algorytmy detekcji zostały wytrenowane na własnym zbiorze danych. Wyniki tych sieci zostały przeanalizowane pod kątem wybranych wcześniej metryk. Najlepszą siecią pod względem czasu treningu i~osiągniętych metryk jest YOLOV8s.

Dokonana została analiza przebiegu treningu i~różnice pomiędzy architekturami. Następnie zostały przedstawione przykłady detekcji wytrenowanych sieci oraz przeanalizowane zostały problemy związane z detekcją, takie jak znikanie wykrytego obiektu na kolejnej klatce, detekcja z bliska i~nietypowe oświetlenie pojazdów. Dodatkowo została przeprowadzona optymalizacja sieci, stosując redukcję kolorów na obrazach w~zbiorze danych.

Przeprowadzono testy wydajności na komputerze PC, dwóch mikrokomputerach z i~bez akceleratora. Każda z sieci została sprawdzona w~dwóch formatach zapisu i~wykazano różnice w~szybkości przetwarzania klatek. Przy wykorzystaniu formatów uniwersalnych szybsza okazała się platforma \textit{Nvidia Jetson Nano}, natomiast przy formatach mobilnych Raspberry Pi4. Na urządzeniach został wykorzystany również akcelerator sprzętowy. W przypadku wytrenowanych sieci odnotowano niewielkie przyspieszenie lub spowolnienie w~szybkości detekcji, z powodu nieobsługiwanych instrukcji przez TPU. Z tego powodu zostały sprawdzone specjalnie wyeksportowane sieci producenta, które uzyskały znacznie lepsze wyniki niż sieci, których obliczenia nie były wykonywane na akceleratorze.

Zostało sprawdzone również, jak sprawują się sieci detekcji wytrenowanych na innym zbiorze podczas klasyfikacji obrazu. Osiągnęły one gorsze metryki niż klasyfikatory, jednak w~badaniu wykazano dużą uniwersalność sieci detekcji. Następnie zbiór treningowy został ulepszony i~wyniki sieci detekcji osiągnęły porównywalne metryki z klasyfikatorami obrazów, cechując się bardzo wysoką czułością. Sieci detekcji mają jednak swoje zalety w~postaci lepszej wytłumaczalności decyzji, jak i~możliwość śledzenia obiektów. Badane również było jak algorytmy śledzenia ruchu takie, jakie BoT-SORT i~ByteTrack pomagają sieciom detekcji.
% W kontekście klasyfikacji obniżały lekko metryki dokładności i~precyzji, ale w~dużym stopniu zwiększały czułość.

Drugim rodzajem algorytmów były sieci przeznaczone do klasyfikacji, które można podzielić na te, które korzystały z obrazu lub danych z czujnika intensywności światła. W badaniu obrazów wykorzystano dwie sieci, jedna z nich to MobileNetV2, druga to autorska sieć splotowa. Dla porównania wykorzystano również prosty algorytm zliczający ilość jasnych pikseli. Podczas tworzenia sieci kładziony był szczególny nacisk na małą liczbę parametrów algorytmu. Dodatkowo sprawdzono jak sieci detekcji, takie jak YOLOV8n i~YOLOV8s radzą sobie w~zadaniu klasyfikacji binarnej. Wykorzystano również algorytmy śledzenia ruchu, które miały na celu polepszyć wyniki klasyfikacji detektorów. Wykorzystano dwie sieci klasyfikatorów, które wykorzystywały dane z czujnika intensywności światła. Obie były autorskimi rozwiązaniami, pierwsza sieć wykorzystywała sploty do ekstrakcji cech, a druga blok LSTM.

Dzięki badaniom udało się wybrać najlepsze rozwiązania w~zależności od platformy sprzętowej i~oczekiwanych wyników.



% Do testów wydajności zostały wykorzystane mikrokomputery Nvidia Jetson i~Raspberry Pi 4 oraz akcelerator obliczeniowy Google Coral TPU.



% W pracy skupiono się na badaniu wykrywania samochodów z wykorzystaniem głębokich sieci neuronowych. Zastosowane zostały algorytmy wykrywania takie jak detekcja obiektu na obrazie przy wykorzystaniu sieci takich jak SSD MobileNetV2, CenterNet MobileNetV2, Efficientdet oraz YOLOV8. Wspomniane algorytmy zostały porównane z prostszymi w~implementacji i~mniej wymagającymi obliczeniowo takimi jak klasyfikacja obrazu przy pomocy sieci neuronowej. Do porównania zostały zastosowane również algorytmy wykrywania takie jak obliczanie średniej jasności pikseli na obrazie lub analiza wartości z czujnika intensywności światła.


"""

# Define the regular expression pattern for finding \textit{sometext}
pattern = r'\\textit\{([^}]*)\}'

# Replace the matches with \mbox{\textit{sometext}}
replacement = r'\\mbox{\\textit{\1}}'
result = re.sub(pattern, replacement, latex_content)

# Print the modified content
print(result)