# Py_project_RTU1
# GitHub Lietotāju Analīzes Rīks

## Projekta uzdevums

Šis projekts ir izveidots ar mērķi analizēt GitHub lietotāju profilus, izmantojot GitHub API. Lietotājs var apskatīt informāciju par jebkuru GitHub lietotāju, tostarp:

- pamata profila informāciju (vārds, lokācija, uzņēmums, u.c.),
- publiskos repozitorijus un to statistiku (zvaigznes, dakšas, skatītāji),
- sekotājus un sekoto lietotāju sarakstu.

Izvēlne ir interaktīva un darbojas no komandrindas, ļaujot izvēlēties starp vairākām funkcionalitātēm.

## Izmantotās Python bibliotēkas

Projektā tiek izmantotas šādas Python bibliotēkas:

- **`requests`**  
  Šī bibliotēka tiek izmantota HTTP pieprasījumu nosūtīšanai uz GitHub API, lai iegūtu datus par lietotājiem, viņu repozitorijiem, sekotājiem un sekotajiem.

- **`datetime`**  
  Izmanto, lai konvertētu un formatētu datuma un laika datus no ISO formāta cilvēkam lasāmā formā.

## Izmantotās datu struktūras

Projektā tiek izmantotas vairākas pielāgotas datu struktūras (funkcijas) datu ieguvei un apstrādei:

- **`fetch_user_info(user)`**  
  Atgriež konkrētā GitHub lietotāja informāciju kā vārdnīcu (`dict`).

- **`fetch_repos(user)`**  
  Iegūst visus publiskos repozitorijus un to metadatus. Dati tiek saglabāti kā saraksts ar vārdnīcām (`list[dict]`).

- **`fetch_followers(user)` / `fetch_following(user)`**  
  Iegūst visus sekotājus un sekotos, saglabājot tos sarakstā (`list`).

- **`calculate_average_stars(repos)`**, **`calculate_total_forks(repos)`**, **`calculate_total_watchers(repos)`**  
  Skaitliskās funkcijas, kas apstrādā repozitoriju datus un atgriež atbilstošu statistiku.

## Lietošanas instrukcija

1. **Programmas palaišana**  
   Palaidiet skriptu ar Python:  
   ```bash
   python main.py
   ```

2. **Galvenā izvēlne**  
   Programma parāda izvēlni ar šādām iespējām:
   - 1: Parādīt lietotāja informāciju
   - 2: Parādīt repozitoriju statistiku
   - 3: Parādīt sekotāju sarakstu
   - 4: Parādīt sekoto sarakstu
   - 0: Iziet

3. **Lietotāja izvēle**  
   Iespējams izvēlēties vienu no iepriekšdefinētiem lietotājiem (piem., `mojombo`, `galvez`), vai ievadīt savu GitHub lietotājvārdu.

4. **Sekotāju un sekoto saraksts**  
   Ja tiek izvēlēta opcija parādīt sekotājus vai sekotos, būs iespēja ievadīt, cik daudz no tiem rādīt, vai izvēlēties rādīt visus (`all`).

## Piezīmes

- Autentifikācijai tiek izmantots GitHub personīgais piekļuves tokens (token), kas nodrošina piekļuvi API ar lielāku pieprasījumu limitu.
- Ieteicams nepublicēt tokenus publiski (tie šajā kodā būtu jāglabā `.env` failā vai jāizmanto droša vides mainīgo sistēma).
