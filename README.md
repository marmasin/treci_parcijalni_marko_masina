# **Parcijalni Ispit - Razvoj Web Aplikacija u Programskom Jeziku Python**

## **Upute za Rješavanje Zadatka**


1. **Priprema okruženja:**
   - Kreirajte "fork" repozitorija.
   - Dodijelite repozitoriju naziv u formatu `treci_parcijalni_ime_prezime` (primjer: `treci_parcijalni_pero_peric`). 
   - **VAŽNO:** Nemojte kreirati "clone" repozitorija jer nemate pravo mijenjanja.

---

### 2. **Postavljanje projekta**
#### Struktura projekta:
```
offers_calculator/            # Glavni direktorij Django projekta
│
├── db.sqlite3                # SQLite baza podataka
│
├── offers_calculator/        # Direktorij glavnih postavki projekta
│   ├── __init__.py           # Oznaka za Python paket
│   ├── asgi.py               # Konfiguracija za ASGI server
│   ├── settings.py           # Postavke projekta
│   ├── urls.py               # Globalne rute aplikacije
│   ├── wsgi.py               # Konfiguracija za WSGI server
│   └── manage.py             # Glavna skripta za upravljanje projektom
│
├── accounts/                 # Aplikacija za upravljanje korisnicima (Django User model)
│   ├── __init__.py
│   ├── admin.py              # Registracija modela u admin sučelju
│   ├── apps.py               # Konfiguracija aplikacije
│   ├── models.py             # Modeli za korisnike
│   ├── serializers.py        # Serializacija podataka za REST API (opcionalno)
│   ├── urls.py               # Rute aplikacije za korisnike
│   ├── views.py              # Pogledi za korisnike
│   └── migrations/           # Migracije baze podataka
│       └── __init__.py
│
├── products/                 # Aplikacija za upravljanje proizvodima
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py             # Modeli za proizvode
│   ├── serializers.py        # Serializacija podataka za REST API (opcionalno)
│   ├── urls.py               # Rute aplikacije za proizvode
│   ├── views.py              # Pogledi za proizvode
│   └── migrations/
│       └── __init__.py
│
├── offers/                   # Aplikacija za upravljanje ponudama
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py             # Modeli za ponude
│   ├── serializers.py        # Serializacija podataka za REST API (opcionalno)
│   ├── urls.py               # Rute aplikacije za ponude
│   ├── views.py              # Pogledi za ponude
│   └── migrations/
│       └── __init__.py
│
├── scripts/                  # Direktorij za Python skripte koje pomažu u administraciji i inicijalizaciji projekta
│   └── seed_database.py      # Skripta za inicijalno popunjavanje baze podataka s testnim podacima (seed)
│
├── templates/                # Globalni direktorij za HTML predloške
│   ├── base.html             # Osnovni HTML predložak za aplikaciju
│   ├── users/
│   │   └── user_list.html    # Predložak za prikaz korisnika
│   ├── products/
│   │   └── product_list.html # Predložak za prikaz proizvoda
│   └── offers/
│       └── offer_list.html   # Predložak za prikaz ponuda
│
└── static/                   # Globalni direktorij za statičke datoteke
    ├── css/                  # CSS datoteke
    ├── js/                   # JavaScript datoteke
    └── images/               # Slike
```
#### Koraci:
   - Nakon što ste kreirali fork, klonirajte repozitorij s vašeg GitHub profila na lokalno računalo koristeći GitHub Desktop ili drugu omiljenu metodu.
   - **Nakon kloniranja**, kreirajte novu lokalnu granu nazvanu `ispit`
   - Sve promjene unosite isključivo unutar grane ispit
   - Instalirajte sve potrebne module pomoću `requirements.txt` kako biste osigurali da aplikacija ima sve potrebne biblioteke.
     
1. Klonirajte repozitorij:
   ```bash
   git clone https://github.com/vaše-korisničko-ime/treci_parcijalnit.git
   cd parcijalni-ispit
   ```

2. Kreirajte virtualno okruženje:
   ```bash
   python -m venv venv
   ```

3. Aktivirajte virtualno okruženje:
   - **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. Instalirajte potrebne module:
   ```bash
   pip install -r requirements.txt
   ```

5. Pokrenite migracije:
   ```bash
   python manage.py migrate
   ```

6. Kreirajte administratorski račun:
   ```bash
   python manage.py createsuperuser
   ```

7. Popunite bazu podataka:
   ```bash
   python manage.py runscript seed_database
   ```

8. Pokrenite razvojni server:
   ```bash
   python manage.py runserver
   ```
   - Aplikaciju otvorite u pregledniku na adresi: `http://127.0.0.1:8000`.

---

### 3. **Zadaci za implementaciju**
Dodajte novu Django aplikaciju **customers** za rad s podacima o tvrtkama (kupcima). 
- **Model Customer**:
  - `name` (ime tvrtke)
  - `vat_id` (OIB tvrtke)
  - `street` (ulica)
  - `city` (grad)
  - `country` (država)
  
Ažurirajte postojeće modele i funkcionalnosti:
- **Offer**:
  - Korisnik (`User`) sada predstavlja osobu koja je kreirala ponudu.
  - Kupac (`Customer`) je tvrtka za koju je ponuda napravljena.
- Implementirajte:
  - Kreiranje novih kupaca.
  - Ažuriranje postojećih kupaca.
  - Prikaz svih kupaca u tablici.
  - Omogućite odabir kupca prilikom kreiranja ponude.

---

#### Napomena:
- Prilikom implementacije vodite računa o modularnosti i slojevima aplikacije. Koristite klase za sve glavne funkcionalnosti i pridržavajte se zadane strukture aplikacije.

### Dodatne Upute

-  **Rješenja koja imaju mijenjan ostatak koda neće biti ocijenjena.**
- Uporabite `TypeHints` prema uputama u komentarima kako biste osigurali konzistentnost tipova podataka.

## Podnošenje Rješenja

1. Nakon što završite implementaciju:
   - Napravite commit za sve promjene koje ste unijeli koristeći opciju `git commit`.
   - Pushajte granu na vaš GitHub repozitorij `git push`.
  
     
2. Otvorite **Pull Request** iz grane `ispit` prema grani `main`.

   - U Pull Requestu:
     - **Autor:** Vaše ime – osoba koja je radila ispit
     - **Reviewer:** Predavač (kojem ste dali pristup kao suradniku)

       
2. **Podjela Repozitorija s Predavačem**:
   - Otvorite vaš repozitorij na GitHubu.
   - Kliknite na karticu **Settings** (Postavke) u repozitoriju.
   - Pronađite opciju **Collaborators** (Suradnici) i dodajte predavača kao **Contributor**.
   - Unesite GitHub korisničko ime predavača, odaberite ga s popisa, te mu pošaljite pozivnicu za pristup.
   - Predavač će imati pravo pregledati vaš kod i provjeriti zadatke.

> ⚠️ Provjerite da su sve promjene **commitane i pushane** prije nego što dodate predavača, kako bi mogao vidjeti kompletno rješenje.

> **Napomena:** Ako se upute ne budu striktno slijedile, ispit neće biti pregledan.

> **Rok predaje:** 15.7.2025 do 21:00h

---

**Sretno!**
