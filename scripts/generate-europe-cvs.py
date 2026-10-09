#!/usr/bin/env python3
"""Generate static, editable European CVs from translations of the two French sources.

Run from any directory: python3 scripts/generate-europe-cvs.py
The original cv-apple.html and cv-flutter.html are never modified.
"""
from copy import deepcopy
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Keep qualifications in their original French form alongside descriptive translations.
# These descriptions do not claim equivalence with a foreign qualification.
LOCALES = {
    "en-eu": {
        "lang": "en", "market": "European / international", "photo": False,
        "labels": ["Professional profile", "Technical skills", "Professional experience",
                   "Earlier experience", "Education", "Languages", "Working approach"],
        "print": "Print / Save PDF", "back": "All versions", "location": "Mâcon, France",
        "titles": ["Senior iOS Developer", "Senior Flutter Developer"],
        "summary": [
            "Mobile developer with 15 years of experience delivering B2B, B2C, e-commerce, SaaS and gaming applications. End-to-end ownership from functional scoping and architecture to UI, backend, CI/CD, App Store releases and monitoring.",
            "Mobile developer with 15 years of experience, including 6 years with Flutter. Builds complete products spanning mobile apps, Node.js backends, Supabase and Firebase, and React.js administration interfaces, from architecture to store releases."
        ],
        "skilllines": [
            ["Swift, SwiftUI, Objective-C, UIKit; Liquid Glass interfaces.",
             "Swift Concurrency, async/await; Clean Architecture, MVVM, Observable.",
             "Unit testing, CI/CD, App Store releases; Codex."],
            ["Flutter for iOS, Android and Web; MVVM, MobX, feature-based architecture.",
             "Node.js, TypeScript, React.js, Supabase/PostgreSQL, Firebase.",
             "Bluetooth Low Energy (BLE), proprietary protocols; testing, CI/CD and store releases."]
        ],
        "jobs": ["Freelance Mobile Developer / Founder", "Lead Mobile Developer",
                 "Native iOS Developer", "Native Android Developer", "Mobile Developer", "Mathematics Teacher"],
        "dates": ["Mar 2025 - Present", "Jan 2020 - Nov 2024", "Jan 2016 - Jan 2020",
                  "Sep 2015 - Jan 2016", "Sep 2011 - Sep 2015", "Sep 2002 - Sep 2011"],
        "cut": "Complete SaaS product: Flutter apps published on the App Store and Google Play; BLE control of a Silhouette cutting machine; Node.js/TypeScript backend, Supabase/PostgreSQL, authenticated React.js admin interface and Dokploy deployment.",
        "impact": "The mobile app is used every 3 minutes on average by several hundred users across approximately 100 establishments.",
        "tetra": "Connect Four for iPhone/iPad with an unbeatable AI, SwiftUI views, Clean Architecture, MVVM with Observable, unit tests and a Liquid Glass UI.",
        "tetrad": "3D Connect Four with an AI written in C, served over WebSocket by a Mongoose server.",
        "life": [
            "Led a two-developer team on Gabby, a private social network for families with a dependent relative, with Flutter apps for iOS, Android and Web.",
            "Feature-based MVVM architecture with MobX; build flavours, authentication, notifications, localisation, time zones, Stripe payments, CI/CD and App Store / Google Play releases."
        ],
        "itelios": "Developed Swift iOS e-commerce applications using Salesforce for CDiscount, Pimkie, Orchestra and Casino. MVVM architecture and reactive programming with RxSwift.",
        "itron": "Native Android development in Java, with a strong focus on unit and integration testing.",
        "mayflower": "Built native iOS and Android apps and cross-platform solutions using Titanium and JavaScript.",
        "teacher": "Developed mathematical rigour, structured reasoning, teaching skills and the ability to explain complex concepts.",
        "degrees": [
            ["Professional bachelor's degree in Mobile and Embedded Computing",
             "Licence professionnelle d'Informatique Mobile et Embarquée",
             "IUT Lyon 1, Bourg-en-Bresse; work-study programme at EP Factory"],
            ["French national mathematics teaching qualification", "CAPES de mathématiques", "IUFM de Lyon"],
            ["Bachelor's degree in Mathematics", "Licence de Mathématiques", "Université Claude Bernard Lyon"]
        ],
        "english": "English", "fluent": "Fluent",
        "approach": "Combines autonomous product delivery, mobile architecture and testing with team leadership and experience explaining technical concepts.",
        "mobility": "Based in Mâcon, France; mobility within the Lyon area and occasional business travel.",
    },
    "de": {
        "lang": "de", "market": "Deutschland / Österreich / deutschsprachige Schweiz", "photo": True,
        "labels": ["Kurzprofil", "Technische Kompetenzen", "Berufserfahrung",
                   "Weitere Berufserfahrung", "Ausbildung", "Sprachen", "Arbeitsweise"],
        "print": "Drucken / Als PDF speichern", "back": "Alle Versionen", "location": "Mâcon, Frankreich",
        "titles": ["Senior iOS-Entwickler", "Senior Flutter-Entwickler"],
        "summary": [
            "Mobile-Entwickler mit 15 Jahren Erfahrung in B2B-, B2C-, E-Commerce-, SaaS- und Spiele-Anwendungen. Eigenständige Umsetzung des gesamten Produktzyklus: Anforderungsanalyse, Architektur, UI, Backend, CI/CD, App-Store-Veröffentlichung und Monitoring.",
            "Mobile-Entwickler mit 15 Jahren Erfahrung, davon 6 Jahre mit Flutter. Entwicklung vollständiger Produkte mit mobilen Apps, Node.js-Backends, Supabase und Firebase sowie React.js-Administrationsoberflächen - von der Architektur bis zur Store-Veröffentlichung."
        ],
        "skilllines": [
            ["Swift, SwiftUI, Objective-C, UIKit; Liquid-Glass-Oberflächen.",
             "Swift Concurrency, async/await; Clean Architecture, MVVM, Observable.",
             "Unit-Tests, CI/CD, App-Store-Veröffentlichung; Codex."],
            ["Flutter für iOS, Android und Web; MVVM, MobX, Architektur nach Features.",
             "Node.js, TypeScript, React.js, Supabase/PostgreSQL, Firebase.",
             "Bluetooth Low Energy (BLE), proprietäre Protokolle; Tests, CI/CD und Store-Veröffentlichung."]
        ],
        "jobs": ["Freiberuflicher Mobile-Entwickler / Gründer", "Lead Mobile-Entwickler",
                 "Entwickler für native iOS-Apps", "Entwickler für native Android-Apps", "Mobile-Entwickler", "Mathematiklehrer"],
        "dates": ["03/2025 - heute", "01/2020 - 11/2024", "01/2016 - 01/2020",
                  "09/2015 - 01/2016", "09/2011 - 09/2015", "09/2002 - 09/2011"],
        "cut": "Vollständige SaaS-Lösung: Flutter-Apps im App Store und bei Google Play; BLE-Steuerung einer Silhouette-Schneidemaschine; Node.js-/TypeScript-Backend, Supabase/PostgreSQL, React.js-Administration mit Authentifizierung und Deployment mit Dokploy.",
        "impact": "Die mobile App wird im Durchschnitt alle 3 Minuten von mehreren hundert Nutzern in etwa 100 Einrichtungen verwendet.",
        "tetra": "Vier gewinnt für iPhone/iPad mit unbesiegbarer KI, SwiftUI-Ansichten, Clean Architecture, MVVM mit Observable, Unit-Tests und Liquid-Glass-UI.",
        "tetrad": "Dreidimensionales Vier gewinnt mit einer KI in C, bereitgestellt über WebSocket mit einem Mongoose-Server.",
        "life": [
            "Leitung eines Teams aus zwei Entwicklern für Gabby, ein privates soziales Netzwerk für Familien mit einem pflegebedürftigen Angehörigen; Flutter-Apps für iOS, Android und Web.",
            "MVVM-Architektur mit MobX nach Features; Build-Flavors, Authentifizierung, Benachrichtigungen, Lokalisierung, Zeitzonen, Stripe-Zahlungen, CI/CD und Veröffentlichung im App Store und bei Google Play."
        ],
        "itelios": "Entwicklung von iOS-E-Commerce-Apps in Swift mit Salesforce für CDiscount, Pimkie, Orchestra und Casino. MVVM-Architektur und reaktive Programmierung mit RxSwift.",
        "itron": "Native Android-Entwicklung in Java mit Schwerpunkt auf Unit- und Integrationstests.",
        "mayflower": "Native iOS- und Android-Apps sowie plattformübergreifende Lösungen mit Titanium und JavaScript.",
        "teacher": "Mathematische Präzision, strukturiertes Denken, Didaktik und Vermittlung komplexer Zusammenhänge.",
        "degrees": [
            ["Berufsorientierter Bachelorabschluss in mobiler und eingebetteter Informatik",
             "Licence professionnelle d'Informatique Mobile et Embarquée",
             "IUT Lyon 1, Bourg-en-Bresse; duale Ausbildung bei EP Factory"],
            ["Französische Lehramtsqualifikation für Mathematik", "CAPES de mathématiques", "IUFM de Lyon"],
            ["Bachelorabschluss in Mathematik", "Licence de Mathématiques", "Université Claude Bernard Lyon"]
        ],
        "english": "Englisch", "fluent": "Fließend",
        "approach": "Eigenständige Produktentwicklung, mobile Architektur und Tests, ergänzt durch Teamleitung und Erfahrung in der Vermittlung technischer Inhalte.",
        "mobility": "Wohnort Mâcon, Frankreich; mobil im Raum Lyon und für gelegentliche Dienstreisen.",
    },
    "es": {
        "lang": "es", "market": "España", "photo": True,
        "labels": ["Perfil profesional", "Competencias técnicas", "Experiencia profesional",
                   "Experiencia anterior", "Formación", "Idiomas", "Forma de trabajar"],
        "print": "Imprimir / Guardar PDF", "back": "Todas las versiones", "location": "Mâcon, Francia",
        "titles": ["Desarrollador sénior iOS", "Desarrollador sénior Flutter"],
        "summary": [
            "Desarrollador móvil con 15 años de experiencia en aplicaciones B2B, B2C, comercio electrónico, SaaS y videojuegos. Autonomía en todo el ciclo del producto: definición funcional, arquitectura, UI, backend, CI/CD, publicación en App Store y monitorización.",
            "Desarrollador móvil con 15 años de experiencia, incluidos 6 años con Flutter. Desarrollo de productos completos con aplicaciones móviles, backend Node.js, Supabase y Firebase e interfaces de administración React.js, desde la arquitectura hasta la publicación."
        ],
        "skilllines": [
            ["Swift, SwiftUI, Objective-C, UIKit; interfaces Liquid Glass.",
             "Swift Concurrency, async/await; Clean Architecture, MVVM, Observable.",
             "Pruebas unitarias, CI/CD y publicación en App Store; Codex."],
            ["Flutter para iOS, Android y Web; MVVM, MobX, arquitectura por funcionalidades.",
             "Node.js, TypeScript, React.js, Supabase/PostgreSQL, Firebase.",
             "Bluetooth Low Energy (BLE), protocolos propietarios; pruebas, CI/CD y publicación."]
        ],
        "jobs": ["Desarrollador móvil freelance / Fundador", "Desarrollador móvil líder",
                 "Desarrollador iOS nativo", "Desarrollador Android nativo", "Desarrollador móvil", "Profesor de matemáticas"],
        "dates": ["mar. 2025 - actualidad", "ene. 2020 - nov. 2024", "ene. 2016 - ene. 2020",
                  "sept. 2015 - ene. 2016", "sept. 2011 - sept. 2015", "sept. 2002 - sept. 2011"],
        "cut": "Solución SaaS completa: apps Flutter publicadas en App Store y Google Play; control BLE de una máquina de corte Silhouette; backend Node.js/TypeScript, Supabase/PostgreSQL, administración React.js con autenticación y despliegue con Dokploy.",
        "impact": "La aplicación móvil se utiliza, de media, cada 3 minutos por varios cientos de usuarios en aproximadamente 100 establecimientos.",
        "tetra": "Cuatro en raya para iPhone/iPad con IA imbatible, vistas SwiftUI, Clean Architecture, MVVM con Observable, pruebas unitarias e interfaz Liquid Glass.",
        "tetrad": "Cuatro en raya en 3D con IA escrita en C, accesible por WebSocket mediante un servidor Mongoose.",
        "life": [
            "Liderazgo de un equipo de dos desarrolladores para Gabby, una red social privada para familias con un familiar dependiente; aplicaciones Flutter para iOS, Android y Web.",
            "Arquitectura MVVM con MobX por funcionalidades; flavors, autenticación, notificaciones, localización, zonas horarias, pagos Stripe, CI/CD y publicación en App Store y Google Play."
        ],
        "itelios": "Desarrollo en Swift de aplicaciones iOS de comercio electrónico con Salesforce para CDiscount, Pimkie, Orchestra y Casino. Arquitectura MVVM y programación reactiva con RxSwift.",
        "itron": "Desarrollo Android nativo en Java, con especial atención a las pruebas unitarias y de integración.",
        "mayflower": "Aplicaciones nativas iOS y Android y soluciones multiplataforma con Titanium y JavaScript.",
        "teacher": "Rigor matemático, razonamiento estructurado, pedagogía y explicación de conceptos complejos.",
        "degrees": [
            ["Titulación universitaria francesa de orientación profesional en Informática Móvil y Embebida",
             "Licence professionnelle d'Informatique Mobile et Embarquée",
             "IUT Lyon 1, Bourg-en-Bresse; formación en alternancia en EP Factory"],
            ["Cualificación francesa para la enseñanza de matemáticas", "CAPES de mathématiques", "IUFM de Lyon"],
            ["Titulación universitaria francesa en Matemáticas", "Licence de Mathématiques", "Université Claude Bernard Lyon"]
        ],
        "english": "Inglés", "fluent": "Fluido",
        "approach": "Desarrollo autónomo de productos, arquitectura móvil y pruebas, junto con liderazgo de equipo y experiencia en la explicación de conceptos técnicos.",
        "mobility": "Residencia en Mâcon, Francia; movilidad en la zona de Lyon y viajes profesionales puntuales.",
    },
    "it": {
        "lang": "it", "market": "Italia / Svizzera italiana", "photo": True,
        "labels": ["Profilo professionale", "Competenze tecniche", "Esperienza professionale",
                   "Esperienze precedenti", "Formazione", "Lingue", "Metodo di lavoro"],
        "print": "Stampa / Salva PDF", "back": "Tutte le versioni", "location": "Mâcon, Francia",
        "titles": ["Sviluppatore senior iOS", "Sviluppatore senior Flutter"],
        "summary": [
            "Sviluppatore mobile con 15 anni di esperienza in applicazioni B2B, B2C, e-commerce, SaaS e videogiochi. Autonomia nell'intero ciclo del prodotto: analisi funzionale, architettura, UI, backend, CI/CD, pubblicazione su App Store e monitoraggio.",
            "Sviluppatore mobile con 15 anni di esperienza, di cui 6 con Flutter. Realizzazione di prodotti completi con app mobile, backend Node.js, Supabase e Firebase e interfacce di amministrazione React.js, dall'architettura alla pubblicazione sugli store."
        ],
        "skilllines": [
            ["Swift, SwiftUI, Objective-C, UIKit; interfacce Liquid Glass.",
             "Swift Concurrency, async/await; Clean Architecture, MVVM, Observable.",
             "Test unitari, CI/CD e pubblicazione su App Store; Codex."],
            ["Flutter per iOS, Android e Web; MVVM, MobX, architettura per funzionalità.",
             "Node.js, TypeScript, React.js, Supabase/PostgreSQL, Firebase.",
             "Bluetooth Low Energy (BLE), protocolli proprietari; test, CI/CD e pubblicazione."]
        ],
        "jobs": ["Sviluppatore mobile freelance / Fondatore", "Lead Developer Mobile",
                 "Sviluppatore iOS nativo", "Sviluppatore Android nativo", "Sviluppatore mobile", "Insegnante di matematica"],
        "dates": ["mar 2025 - oggi", "gen 2020 - nov 2024", "gen 2016 - gen 2020",
                  "set 2015 - gen 2016", "set 2011 - set 2015", "set 2002 - set 2011"],
        "cut": "Soluzione SaaS completa: app Flutter pubblicate su App Store e Google Play; controllo BLE di una macchina da taglio Silhouette; backend Node.js/TypeScript, Supabase/PostgreSQL, amministrazione React.js con autenticazione e deployment con Dokploy.",
        "impact": "L'app mobile viene utilizzata in media ogni 3 minuti da diverse centinaia di utenti in circa 100 strutture.",
        "tetra": "Forza quattro per iPhone/iPad con IA imbattibile, viste SwiftUI, Clean Architecture, MVVM con Observable, test unitari e UI Liquid Glass.",
        "tetrad": "Forza quattro in 3D con IA scritta in C, accessibile via WebSocket attraverso un server Mongoose.",
        "life": [
            "Guida di un team di due sviluppatori per Gabby, un social network privato per famiglie con un parente non autosufficiente; app Flutter per iOS, Android e Web.",
            "Architettura MVVM con MobX per funzionalità; flavors, autenticazione, notifiche, localizzazione, fusi orari, pagamenti Stripe, CI/CD e pubblicazione su App Store e Google Play."
        ],
        "itelios": "Sviluppo in Swift di app iOS per l'e-commerce con Salesforce per CDiscount, Pimkie, Orchestra e Casino. Architettura MVVM e programmazione reattiva con RxSwift.",
        "itron": "Sviluppo Android nativo in Java, con particolare attenzione ai test unitari e di integrazione.",
        "mayflower": "App native iOS e Android e soluzioni multipiattaforma con Titanium e JavaScript.",
        "teacher": "Rigore matematico, ragionamento strutturato, didattica e spiegazione di concetti complessi.",
        "degrees": [
            ["Titolo universitario francese professionalizzante in Informatica Mobile ed Embedded",
             "Licence professionnelle d'Informatique Mobile et Embarquée",
             "IUT Lyon 1, Bourg-en-Bresse; formazione in alternanza presso EP Factory"],
            ["Qualifica francese per l'insegnamento della matematica", "CAPES de mathématiques", "IUFM de Lyon"],
            ["Titolo universitario francese in Matematica", "Licence de Mathématiques", "Université Claude Bernard Lyon"]
        ],
        "english": "Inglese", "fluent": "Fluente",
        "approach": "Sviluppo autonomo di prodotti, architettura mobile e test, con esperienza nella guida di team e nella spiegazione di concetti tecnici.",
        "mobility": "Residente a Mâcon, Francia; mobilità nell'area di Lione e trasferte occasionali.",
    },
    "nl": {
        "lang": "nl", "market": "Nederland / Vlaanderen", "photo": False,
        "labels": ["Profiel", "Technische vaardigheden", "Werkervaring",
                   "Eerdere werkervaring", "Opleiding", "Talen", "Werkwijze"],
        "print": "Afdrukken / PDF opslaan", "back": "Alle versies", "location": "Mâcon, Frankrijk",
        "titles": ["Senior iOS-ontwikkelaar", "Senior Flutter-ontwikkelaar"],
        "summary": [
            "Mobile developer met 15 jaar ervaring in B2B-, B2C-, e-commerce-, SaaS- en game-applicaties. Zelfstandige uitvoering van de volledige productcyclus: functionele analyse, architectuur, UI, backend, CI/CD, App Store-publicatie en monitoring.",
            "Mobile developer met 15 jaar ervaring, waarvan 6 jaar met Flutter. Ontwikkelt complete producten met mobiele apps, Node.js-backends, Supabase en Firebase en React.js-beheerinterfaces, van architectuur tot publicatie in de appstores."
        ],
        "skilllines": [
            ["Swift, SwiftUI, Objective-C, UIKit; Liquid Glass-interfaces.",
             "Swift Concurrency, async/await; Clean Architecture, MVVM, Observable.",
             "Unit-tests, CI/CD en App Store-publicatie; Codex."],
            ["Flutter voor iOS, Android en Web; MVVM, MobX, architectuur per feature.",
             "Node.js, TypeScript, React.js, Supabase/PostgreSQL, Firebase.",
             "Bluetooth Low Energy (BLE), bedrijfseigen protocollen; tests, CI/CD en publicatie."]
        ],
        "jobs": ["Freelance mobile developer / Oprichter", "Lead mobile developer",
                 "Native iOS-ontwikkelaar", "Native Android-ontwikkelaar", "Mobile developer", "Wiskundedocent"],
        "dates": ["2025 - heden", "2020 - 2024", "2016 - 2020", "2015 - 2016", "2011 - 2015", "2002 - 2011"],
        "cut": "Complete SaaS-oplossing: Flutter-apps gepubliceerd in de App Store en Google Play; BLE-aansturing van een Silhouette-snijmachine; Node.js/TypeScript-backend, Supabase/PostgreSQL, React.js-beheerinterface met authenticatie en deployment via Dokploy.",
        "impact": "De mobiele app wordt gemiddeld elke 3 minuten gebruikt door enkele honderden gebruikers bij ongeveer 100 vestigingen.",
        "tetra": "Vier op een rij voor iPhone/iPad met een onverslaanbare AI, SwiftUI-views, Clean Architecture, MVVM met Observable, unit-tests en een Liquid Glass-interface.",
        "tetrad": "Vier op een rij in 3D met AI geschreven in C, via WebSocket beschikbaar op een Mongoose-server.",
        "life": [
            "Leidde een team van twee ontwikkelaars voor Gabby, een besloten sociaal netwerk voor families met een zorgafhankelijk familielid; Flutter-apps voor iOS, Android en Web.",
            "MVVM-architectuur met MobX per feature; build-flavors, authenticatie, notificaties, lokalisatie, tijdzones, Stripe-betalingen, CI/CD en publicatie in de App Store en Google Play."
        ],
        "itelios": "Ontwikkelde iOS-e-commerce-apps in Swift met Salesforce voor CDiscount, Pimkie, Orchestra en Casino. MVVM-architectuur en reactief programmeren met RxSwift.",
        "itron": "Native Android-ontwikkeling in Java, met nadruk op unit- en integratietests.",
        "mayflower": "Native iOS- en Android-apps en platformonafhankelijke oplossingen met Titanium en JavaScript.",
        "teacher": "Wiskundige nauwkeurigheid, gestructureerd denken, didactiek en uitleg van complexe concepten.",
        "degrees": [
            ["Franse beroepsgerichte bacheloropleiding Mobiele en Embedded Informatica",
             "Licence professionnelle d'Informatique Mobile et Embarquée",
             "IUT Lyon 1, Bourg-en-Bresse; werk-leren bij EP Factory"],
            ["Franse onderwijsbevoegdheid voor wiskunde", "CAPES de mathématiques", "IUFM de Lyon"],
            ["Franse bacheloropleiding Wiskunde", "Licence de Mathématiques", "Université Claude Bernard Lyon"]
        ],
        "english": "Engels", "fluent": "Vloeiend",
        "approach": "Zelfstandige productontwikkeling, mobiele architectuur en tests, gecombineerd met teamleiding en ervaring in het uitleggen van technische concepten.",
        "mobility": "Woont in Mâcon, Frankrijk; inzetbaar in de regio Lyon en voor incidentele zakenreizen.",
    },
    "fr-eu": {
        "lang": "fr", "market": "France / Belgique francophone / Suisse romande / Luxembourg", "photo": True,
        "labels": ["Profil", "Compétences techniques", "Expérience professionnelle",
                   "Expériences antérieures", "Formation", "Langues", "Méthode de travail"],
        "print": "Imprimer / Enregistrer en PDF", "back": "Toutes les versions", "location": "Mâcon, France",
        "titles": ["Développeur senior iOS", "Développeur senior Flutter"],
        "summary": [
            "Développeur mobile avec 15 ans d'expérience dans les applications B2B, B2C, e-commerce, SaaS et jeux. Autonome sur tout le cycle produit : cadrage fonctionnel, architecture, UI, backend, CI/CD, publication App Store et monitoring.",
            "Développeur mobile avec 15 ans d'expérience, dont 6 années en Flutter. Conception de produits complets : applications mobiles, backend Node.js, Supabase et Firebase, interfaces d'administration React.js, de l'architecture au déploiement sur les stores."
        ],
        "skilllines": [
            ["Swift, SwiftUI, Objective-C, UIKit ; interfaces Liquid Glass.",
             "Swift Concurrency, async/await ; Clean Architecture, MVVM, Observable.",
             "Tests unitaires, CI/CD, publication App Store ; Codex."],
            ["Flutter iOS, Android et Web ; MVVM, MobX, architecture par fonctionnalités.",
             "Node.js, TypeScript, React.js, Supabase/PostgreSQL, Firebase.",
             "Bluetooth Low Energy (BLE), protocoles propriétaires ; tests, CI/CD et publication."]
        ],
        "jobs": ["Développeur mobile freelance / Fondateur", "Lead développeur mobile",
                 "Développeur iOS natif", "Développeur Android natif", "Développeur mobile", "Professeur de mathématiques"],
        "dates": ["Mars 2025 - aujourd'hui", "Janv. 2020 - nov. 2024", "Janv. 2016 - janv. 2020",
                  "Sept. 2015 - janv. 2016", "Sept. 2011 - sept. 2015", "Sept. 2002 - sept. 2011"],
        "cut": "Solution SaaS complète : apps Flutter publiées sur App Store et Google Play ; pilotage BLE d'une découpeuse Silhouette ; backend Node.js/TypeScript, Supabase/PostgreSQL, administration React.js avec authentification et déploiement Dokploy.",
        "impact": "Application mobile utilisée toutes les 3 minutes en moyenne par plusieurs centaines d'utilisateurs répartis sur une centaine d'établissements.",
        "tetra": "Puissance 4 sur iPhone/iPad avec IA imbattable, vues SwiftUI, Clean Architecture, MVVM avec Observable, tests unitaires et UI Liquid Glass.",
        "tetrad": "Puissance 4 en 3D avec IA en C, servie en WebSocket par un serveur Mongoose.",
        "life": [
            "Lead d'une équipe de deux développeurs sur Gabby, réseau social privé pour les familles ayant un proche dépendant ; applications Flutter iOS, Android et Web.",
            "Architecture MVVM avec MobX par fonctionnalités ; flavors, authentification, notifications, localisation, fuseaux horaires, paiement Stripe, CI/CD et publication App Store / Google Play."
        ],
        "itelios": "Développement Swift d'applications e-commerce iOS utilisant Salesforce pour CDiscount, Pimkie, Orchestra et Casino. Architecture MVVM et programmation réactive avec RxSwift.",
        "itron": "Développement Android natif en Java, avec un fort accent sur les tests unitaires et d'intégration.",
        "mayflower": "Applications natives iOS et Android et solutions multiplateformes Titanium en JavaScript.",
        "teacher": "Rigueur mathématique, structuration de la pensée, pédagogie et transmission de concepts complexes.",
        "degrees": [
            ["Licence professionnelle d'Informatique Mobile et Embarquée", "",
             "IUT Lyon 1, Bourg-en-Bresse ; alternance chez EP Factory"],
            ["CAPES de mathématiques", "", "IUFM de Lyon"],
            ["Licence de Mathématiques", "", "Université Claude Bernard Lyon"]
        ],
        "english": "Anglais", "fluent": "Courant",
        "approach": "Autonomie sur le cycle produit, architecture mobile et tests, complétées par le leadership d'équipe et l'expérience de la transmission de concepts techniques.",
        "mobility": "Basé à Mâcon, France ; mobile sur Lyon et déplacements professionnels ponctuels.",
    },
}

LOCALES["en-gb"] = deepcopy(LOCALES["en-eu"])
LOCALES["en-gb"].update({
    "lang": "en-GB", "market": "United Kingdom / remote AI project",
    "summary": [
        "Senior iOS developer with 15 years of mobile experience, spanning Swift/SwiftUI apps, e-commerce and SaaS products. Brings mobile architecture, asynchronous programming, unit testing and CI/CD experience, together with nine years of mathematics teaching, to mobile engineering evaluation tasks.",
        "Senior mobile developer with 15 years of experience, including 6 years with Flutter. Delivers production mobile apps and full-stack products with Node.js/TypeScript and React.js. Combines MVVM/MobX architecture, testing and CI/CD with nine years of mathematics teaching, relevant to explaining and evaluating coding problems."
    ],
    "approach": "Interested in applying production mobile development and mathematics teaching experience to the design of realistic coding tasks and clear verification criteria for AI evaluation. This interest builds on unit and integration testing, mobile architecture and structured reasoning.",
})

COMPANIES = ["Dodecamoon", "LifeStoneLink", "Itelios", "Itron", "Mayflower / EP Factory", "Éducation Nationale"]


def e(value):
    return escape(value, quote=True)


def bullets(items):
    return "<ul>" + "".join(f"<li>{item}</li>" for item in items) + "</ul>"


def experience(d, index, items):
    last = " experience-last" if index == 5 else ""
    content = bullets(items) if index == 0 else "<p>" + "<br>".join(items) + "</p>"
    return f"""<article class="experience{last}">
      <div class="experience-head">
        <div><h3>{e(d['jobs'][index])}</h3><p>{e(COMPANIES[index])}</p></div>
        <time>{e(d['dates'][index])}</time>
      </div>
      {content}
    </article>"""


def panel(title, content, extra_class=""):
    return f'<section class="panel glass {extra_class}"><h2>{e(title)}</h2>{content}</section>'


def render_cv(locale, track):
    d = LOCALES[locale]
    i = 0 if track == "apple" else 1
    title = d["titles"][i]
    labels = d["labels"]
    photo = '<div class="hero-media"><img class="portrait" src="assets/profile.png" alt="Thierry Duchassin"></div>' if d["photo"] else ""
    no_photo = " hero-no-photo" if not d["photo"] else ""
    # Reuse the original contact markup, including its SVG icons and grid.
    source = (ROOT / f"cv-{track}.html").read_text(encoding="utf-8")
    contact_start = source.index('<address class="contact glass"')
    contact_end = source.index('</address>', contact_start) + len('</address>')
    contact = source[contact_start:contact_end].replace("Mâcon · mobile sur Lyon", e(d["location"]))
    contact = contact.replace('aria-label="Coordonnées"', 'aria-label="Contact"')
    current = [f"<strong>Cut it!</strong> : {e(d['cut'])}<br><strong>{e(d['impact'])}</strong>"]
    if i == 0:
        current.insert(0, f"<strong>TetraC</strong> : {e(d['tetra'])}")
    else:
        current.append(f'<strong><a href="https://tetrad.dodecamoon.com">TetraD</a></strong> : {e(d["tetrad"])}')
    skill_items = (
        ["Swift / SwiftUI", "Objective-C / UIKit", "Liquid Glass", "Swift Concurrency",
         "Async / Await", "Clean Architecture", "MVVM / Observable", d["skilllines"][0][2]]
        if i == 0 else
        ["Flutter iOS / Android / Web", "MVVM / MobX", "Node.js / TypeScript / React.js",
         "Supabase / PostgreSQL / Firebase", d["skilllines"][1][2]]
    )
    skills = '<ul class="soft-list">' + "".join(f"<li>{e(s)}</li>" for s in skill_items) + "</ul>"
    education = '<div class="education">'
    for year, degree in zip(["2012", "2002", "2000"], d["degrees"]):
        # Official degree names stay in French, as on the original CVs.
        # The descriptive translation is available on hover, without duplicating
        # a long qualification twice in the narrow education panel.
        name = degree[1] or degree[0]
        education += f'<article><time>{year}</time><h3 lang="fr" title="{e(degree[0])}">{e(name)}</h3><p>{e(degree[2])}</p></article>'
    education += '</div>'
    information = f'<p class="information-compact">{e(d["english"])} : {e(d["fluent"])}<br>{e(d["mobility"])}</p>'
    experiences = experience(d, 0, current) + experience(d, 1, [e(s) for s in d["life"]])
    experiences += "".join(experience(d, index, [e(d[key])]) for index, key in enumerate(["itelios", "itron", "mayflower", "teacher"], start=2))
    return f"""<!doctype html>
<html lang="{e(d['lang'])}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="{e(title)} - Thierry Duchassin - {e(d['market'])}">
  <title>Thierry Duchassin | {e(title)} | {e(d['market'])}</title>
  <link rel="icon" href="assets/{'apple' if i == 0 else 'flutter'}-favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="cv-europe-resume.css">
</head>
<body>
  <nav class="toolbar" aria-label="{e(d['back'])}">
    <a href="cv-europe.html">{e(d['back'])}</a>
    <button type="button" onclick="window.print()">{e(d['print'])}</button>
  </nav>
  <main class="resume" aria-label="Curriculum vitae - Thierry Duchassin">
    <section class="sheet sheet-cover" aria-label="Page 1">
      <header class="hero glass{no_photo}">
        <div class="hero-copy">
          <p class="eyebrow">Senior Mobile Developer</p>
          <h1>Thierry Duchassin</h1>
          <p class="headline">{e(title)}</p>
          <p class="summary">{e(d["summary"][i])}</p>
        </div>
{photo}
      </header>
      <div class="top-strip">{contact}</div>
      <div class="content-grid">
        <aside class="sidebar">
          {panel(labels[5], information, "information-panel")}
          {panel(labels[1], skills)}
          {panel(labels[4], education)}
        </aside>
        <section class="section timeline">
          <h2>{e(labels[2])}</h2>
          {experiences}
        </section>
      </div>
    </section>
  </main>
</body>
</html>
"""


def render_catalog():
    markets = {
        "en-gb": ("Royaume-Uni · offre LinkedIn", "Anglais britannique, sans photo. Profil ciblé sur les tâches d'évaluation d'IA : tests, architecture et pédagogie. À privilégier pour l'offre partagée."),
        "en-eu": ("Europe · équipes internationales", "Anglais, sans photo. Version générale pour les annonces en anglais, notamment en Irlande, aux Pays-Bas et dans les pays nordiques."),
        "de": ("Allemagne · Autriche · Suisse alémanique", "Allemand, dates mois/année et photo existante. La photo est facultative ; retirer l'image si l'annonce ou l'employeur préfère un CV sans photo."),
        "es": ("Espagne", "Espagnol, dates et intitulés localisés, photo existante facultative. Choisir l'anglais si l'annonce demande une candidature en anglais."),
        "it": ("Italie · Suisse italienne", "Italien, dates et intitulés localisés, photo existante facultative. Diplômes français conservés avec une description, sans équivalence locale déclarée."),
        "nl": ("Pays-Bas · Flandre", "Néerlandais, sans photo, dates à l'année et présentation concise. Préférer l'anglais pour les annonces et les équipes anglophones."),
        "fr-eu": ("France · Belgique · Suisse romande · Luxembourg", "Français, photo existante facultative. Coordonnées internationales et pays de résidence explicite ; aucun engagement de relocation ajouté."),
    }
    cards = ""
    for locale, (name, description) in markets.items():
        cards += f"""<article class="variant"><h3>{e(name)}</h3><p>{e(description)}</p>
        <nav aria-label="{e(name)}"><a href="cv-apple-{locale}.html">CV iOS</a><a href="cv-flutter-{locale}.html">CV Flutter</a></nav></article>"""
    return f"""<!doctype html>
<html lang="fr">
<head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>CV européens - Thierry Duchassin</title><link rel="stylesheet" href="cv-europe.css"></head>
<body><main class="catalog">
  <p class="kicker">Thierry Duchassin · candidatures européennes</p>
  <h1>Le bon CV pour chaque candidature</h1>
  <p>14 nouveaux CV statiques, dérivés uniquement de <a href="cv-apple.html">cv-apple.html</a> et <a href="cv-flutter.html">cv-flutter.html</a>.
  Chaque version reprend la présentation des originaux : bandeau, cartes glass, coordonnées avec icônes, colonne latérale et expériences. Le format est une page A4 avec texte sélectionnable.</p>
  <div class="variants">{cards}</div>
  <h2>Pour l'offre partagée</h2>
  <p><a href="https://www.linkedin.com/jobs/view/4475916337">Mobile Developer | €80/hr | Remote - The Ai Training Company</a>,
  consultée le 9 octobre 2026 : annonce au Royaume-Uni, en anglais, pour contribuer à un projet d'évaluation d'IA.
  Les versions en-gb rapprochent les expériences réelles de ces besoins. L'expérience de création de benchmarks,
  de vérificateurs déterministes ou de solutions de référence n'est pas affirmée, car elle n'apparaît pas dans les CV sources.</p>
  <h2>Imprimer ou exporter</h2>
  <ol><li>Ouvrir la version choisie, puis utiliser son bouton « Imprimer / Enregistrer en PDF » (ou Cmd+P / Ctrl+P).</li>
  <li>Choisir A4, orientation portrait, échelle 100 % et les marges définies par la page.</li>
  <li>Désactiver les en-têtes et pieds de page du navigateur pour éviter l'URL et la date automatiques.
  Le bouton et la navigation disparaissent à l'impression. Les couleurs restent lisibles en noir et blanc.</li>
  <li>Enregistrer en PDF et relire la page avant de déposer le fichier. Exemple de nom :
  Thierry-Duchassin-Senior-Flutter-Developer-UK.pdf.</li></ol>
  <h2>Choisir et personnaliser</h2>
  <ul><li>La langue et les instructions de l'annonce priment sur les usages généraux du pays.
  Ces variantes sont des choix éditoriaux adaptés aux marchés indiqués, pas des formats officiels obligatoires.</li>
  <li>Une traduction du CV ne signifie pas que vous parlez cette langue. Seul l'anglais courant, attesté par les sources,
  figure dans la rubrique langues. Aucun niveau CECRL n'est inventé.</li>
  <li>L'âge, le permis de conduire et la situation familiale sont omis pour privilégier les informations utiles au poste.
  La photo est un choix facultatif sur certaines versions ; elle peut être retirée en supprimant l'élément
  <code>img.portrait</code>.</li>
  <li>La résidence reste Mâcon, France, et la mobilité reste Lyon avec déplacements ponctuels.
  Le travail à distance depuis la France, la relocation, la disponibilité et l'autorisation de travail doivent être
  précisés selon votre situation et les conditions de chaque annonce.</li>
  <li>Les diplômes conservent leurs noms français ; les traductions sont descriptives et ne constituent pas une
  reconnaissance d'équivalence. Aucun employeur, résultat chiffré ou savoir-faire supplémentaire n'a été inventé.</li>
  <li>Adapter le titre, le résumé et l'ordre des points à chaque annonce. Si Europass est explicitement demandé,
  utiliser son format officiel ; ces documents ne sont pas des CV Europass.</li></ul>
  <h2>Sources sur les usages</h2>
  <ul class="sources">
    <li><a href="https://nationalcareers.service.gov.uk/careers-advice/cv-sections">National Careers Service - Royaume-Uni</a> :
    clarté, police lisible, expérience récente en premier, absence d'âge et de nationalité.</li>
    <li><a href="https://www.arbeitsagentur.de/vor-ort/zav/working-and-living-in-germany/newsletter-iss/01-2026/bewerbung">Bundesagentur für Arbeit - Allemagne</a> :
    deux pages maximum, chronologie inversée et photo facultative.</li>
    <li><a href="https://eures.europa.eu/living-and-working/living-and-working-conditions-europe/living-and-working-conditions-netherlands_en">EURES - Pays-Bas</a> :
    CV concis, généralement deux pages A4, dates simplifiées.</li>
    <li><a href="https://eures.europa.eu/living-and-working/living-and-working-conditions-europe/living-and-working-conditions-spain_en">EURES - Espagne</a> :
    candidature en espagnol et format A4, sauf instruction contraire.</li>
    <li><a href="https://eures.europa.eu/living-and-working/living-and-working-conditions-europe/living-and-working-conditions-italy_en">EURES - Italie</a> :
    suivre la procédure indiquée dans l'annonce.</li>
    <li><a href="https://europass.europa.eu/en/create-europass-cv">Europass</a> :
    outil européen de création de CV, à utiliser quand le recruteur le demande.</li>
  </ul>
  <h2>Maintenance</h2>
  <p>Les fichiers HTML sont autonomes avec les feuilles de style locales cv-europe-resume.css, cv-piwio.css et cv-apple.css et les images du dossier assets ;
  ils fonctionnent sans serveur ni JavaScript pour afficher le CV. Les textes traduits sont centralisés dans
  scripts/generate-europe-cvs.py. Après modification de ce script, lancer
  <code>python3 scripts/generate-europe-cvs.py</code>. Cette commande régénère les 14 CV et ce catalogue,
  en écrasant les modifications directes de ces fichiers générés.</p>
</main></body></html>
"""


if __name__ == "__main__":
    for locale in LOCALES:
        for track in ["apple", "flutter"]:
            (ROOT / f"cv-{track}-{locale}.html").write_text(render_cv(locale, track), encoding="utf-8")
    (ROOT / "cv-europe.html").write_text(render_catalog(), encoding="utf-8")
    print(f"Generated {len(LOCALES) * 2} CVs and cv-europe.html.")
