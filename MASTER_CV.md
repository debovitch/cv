# Master CV - Thierry DUCHASSIN

Document de reference destine a centraliser toutes les informations utiles pour generer ensuite des CV specialises : Flutter, iOS, mobile senior, full stack, freelance, LinkedIn, etc.

Ce document est volontairement complet et evolutif. Les sections marquees `A completer` devront etre enrichies au fur et a mesure du questionnaire.

## Informations personnelles

- **Nom** : Thierry DUCHASSIN
- **Titre professionnel** : Developpeur Mobile Senior iOS & Flutter
- **Localisation** : Saint-Laurent-sur-Saone, Auvergne-Rhone-Alpes, France
- **Mobilite** : deplacements ponctuels, jusqu'a quelques jours par mois
- **Teletravail** : preference full remote ; hybride acceptable sur la zone Macon / Lyon, dans un rayon d'environ 1h
- **Langues** :
  - Francais : natif
  - Anglais : courant, utilise pour les reunions techniques, la documentation technique, les code reviews et les entretiens
- **Email** : thierry.duchassin@gmail.com
- **Telephone** : +33 6 20 17 22 10
- **Site personnel / portfolio** : https://dodecamoon.com
- **GitHub** : https://github.com/debovitch/
- **LinkedIn** : https://www.linkedin.com/in/thierry-duchassin-05aa1962
- **Restrictions personnelles** : aucune restriction indiquee

## Resume professionnel

Developpeur Mobile Senior iOS & Flutter avec environ 15 ans d'experience dans la conception, le developpement et la publication d'applications mobiles B2B, B2C, e-commerce, SaaS et jeux. Expert Flutter depuis 2020, il intervient sur l'ensemble du cycle de vie produit : cadrage fonctionnel, architecture, UI, developpement mobile, backend, base de donnees, CI/CD, publication App Store / Play Store et monitoring.

Il a contribue a la livraison de plus de 10 applications et possede une experience concrete des architectures mobiles maintenables, du state management Flutter avec Provider, MobX et setState, des flavors, du Bluetooth, ainsi que des pipelines mobiles avec Bitrise et fastlane. Son experience backend couvre TypeScript / Node.js, Supabase / PostgreSQL, Docker, Laravel et des bases Symfony.

Reconnu pour son autonomie, sa force de proposition, la qualite de son code et sa capacite a livrer seul, il sait aussi optimiser les performances, notamment en reduisant la taille des payloads JSON et le cout des echanges reseau. Ancien professeur de mathematiques, il apporte une approche rigoureuse, structuree et pedagogique a la resolution de problemes techniques complexes.

## Points forts

- Expertise Flutter construite sur des applications iOS et Android publiees en production.
- Forte autonomie produit et technique, avec capacite a livrer une application complete de bout en bout.
- Double competence mobile et backend utile pour construire des produits SaaS mobiles complets.
- Experience significative en architecture mobile, qualite de code et publication stores.
- Capacite a intervenir sur des sujets techniques complexes : BLE, backend, roles, securite Supabase, monitoring, CI/CD.
- Profil structure et pedagogique issu d'un premier parcours de professeur de mathematiques.
- Experience de lead mobile avec definition d'architecture, code review et encadrement d'une petite equipe.

## Parcours professionnel

### Dodecamoon

- **Poste** : Developpeur mobile freelance / fondateur
- **Statut** : micro-entreprise
- **Periode** : depuis mars 2025
- **Contexte** : activite independante combinant missions clients et developpement de produits personnels
- **Objectif** : realiser des missions freelance et developper des produits mobiles propres

#### Cut it!

- **Type** : produit SaaS mobile motive par un besoin client
- **Statut** : publie sur iOS et Android
- **Objectif** : permettre a des vendeurs en magasin de selectionner un modele de telephone et de piloter une decoupeuse Silhouette pour decouper une protection adaptee
- **Utilisateurs cibles** : vendeurs en grands magasins et espaces operateurs, notamment Fnac, Darty et espaces SFR
- **Liens** :
  - Android : https://play.google.com/store/apps/details?id=com.dodecamoon.cutit
  - iOS : https://apps.apple.com/fr/app/cut-it/id6755288996

##### Role

Conception et realisation complete en autonomie :

- cadrage technique
- application mobile Flutter
- backend
- base de donnees
- admin web ReactJS
- deploiement
- publication App Store / Play Store
- monitoring

##### Stack technique

- Flutter
- ReactJS
- TypeScript / Node.js
- Supabase / PostgreSQL
- Supabase Storage
- Docker
- BLE
- Dokploy
- Firebase Crashlytics
- Play Console
- App Store Connect

##### Fonctionnalites

- Communication BLE avec protocole proprietaire
- Commandes machine vers decoupeuse Silhouette
- Decouverte et pairing Bluetooth
- Authentification complete
- Gestion des roles
- Administration des utilisateurs
- Administration des etablissements
- Stockage de modeles de telephones en CSV
- Statistiques d'usage

##### Securite

- Mise en place de Row Level Security sur Supabase
- Controle d'acces selon les roles
- Securisation de la base de donnees Supabase sans impacter les performances

##### Deploiement et monitoring

- Backend deploye via Dokploy
- Admin web ReactJS deploye via Dokploy
- Applications Flutter buildees en ligne de commande
- Monitoring via Firebase Crashlytics
- Monitoring Supabase
- Logs serveur backend via Dokploy

##### Difficultes techniques

- Comprendre le protocole machine de la decoupeuse
- Fiabiliser la communication BLE
- Gerer les roles
- Securiser Supabase sans degrader les performances
- Concevoir le flow complet d'authentification

##### Resultats

- Applications iOS et Android publiees
- 90 etablissements
- 265 utilisateurs
- Environ 1 decoupe toutes les 3 minutes en moyenne pendant les horaires d'ouverture des magasins
- Acces admin de demonstration disponible sur l'environnement de developpement

#### TetraC

- **Type** : jeu iPhone / iPad de type Puissance 4
- **Nom** : TetraC
- **Statut** : developpement local, proche publication
- **Nature** : produit personnel et commercial
- **Modele economique** : achats in-app prevus

##### Role

- Conception du jeu
- Developpement iOS
- Architecture
- Tests unitaires et UI

##### Stack technique

- Swift
- SwiftUI
- MultipeerConnectivity
- Swift Testing
- XCTest UI

##### Architecture

- Architecture en couches
- MVVM

##### Fonctionnalites techniques

- Adversaire algorithmique
- Generation de defis
- Decouverte de pairs
- Synchronisation d'etat
- Reconnexion
- Tests unitaires et UI

### LifeStoneLink

- **Poste** : Lead developpeur mobile
- **Periode** : janvier 2020 - novembre 2024
- **Secteur** : sante, service a la personne, accompagnement des personnes dependantes
- **Projet principal** : ecosysteme Gabby
- **Raison du depart** : fin de collaboration dans un contexte de ralentissement d'activite

#### Produit - Gabby

Gabby est un reseau social familial pour les proches de personnes dependantes vivant en EHPAD, en residence seniors ou a domicile.

L'ecosysteme comprend plusieurs applications :

- **Gabby Famille** : application destinee aux familles des residents
- **Gabby Partenaire** : application destinee aux professionnels de l'aide a domicile
- **Gabby Residence** : application destinee aux residences et professionnels

#### Applications publiees

- Gabby Famille Android : https://play.google.com/store/apps/details?id=com.seregena.gabby.family
- Gabby Famille iOS : https://apps.apple.com/fr/app/gabby-famille/id1629696620
- Gabby Partenaire iOS : https://apps.apple.com/fr/app/gabby-partenaire/id1631566485
- Gabby Partenaire Android : https://play.google.com/store/apps/details?id=com.seregena.gabby.partner
- Gabby Residence Android : https://play.google.com/store/apps/details?id=com.seregena.gabby.staff

#### Role

- Lead d'une equipe de 2 developpeurs mobiles
- Definition de l'architecture mobile
- Code review
- Developpement Flutter iOS / Android
- Suivi de production
- Support applicatif

#### Perimetre technique

- Architecture Flutter MVVM
- Organisation par features
- State management avec MobX et Provider
- Utilisation ponctuelle de setState
- Developpement des ecrans et parcours applicatifs
- Integration des webservices .NET
- Authentification
- Notifications
- Paiement
- Fonctionnalites offline
- CI/CD
- Publication App Store / Play Store
- Monitoring
- Support production

#### Backend / API

- Backend existant en .NET
- Role cote mobile : consommation des webservices

#### Optimisation

- Identification d'un probleme de performance lie a des payloads JSON trop profonds et trop volumineux
- Demande d'adaptation des webservices pour ne remonter que les donnees utiles a l'application mobile
- Resultat : amelioration de la fluidite et des performances cote mobile

#### Informations a completer

- Niveau des deux developpeurs encadres
- Details du mentoring, de la coordination et des code reviews
- Outils CI/CD utilises
- Details du fonctionnement offline
- Details du paiement
- Outil de notifications et cas d'usage
- Outils de monitoring et actions menees a partir des crashs
- Defis techniques et organisationnels principaux
- Resultats chiffres eventuels

### Itelios

- **Poste** : Developpeur iOS natif
- **Periode** : janvier 2016 - janvier 2020
- **Contexte connu** : developpement natif iOS en Swift d'applications e-commerce utilisant Salesforce pour de grandes entreprises telles que CDiscount, Pimkie, Orchestra et Casino

#### Informations a completer

- Secteur exact et contexte de l'entreprise
- Clients et projets principaux
- Taille des equipes
- Role exact
- Technologies iOS utilisees
- Architecture
- Outils
- CI/CD
- Tests
- Defis techniques
- Resultats et impacts
- Raisons du depart

### Itron

- **Poste** : Developpeur Android natif
- **Periode** : septembre 2015 - janvier 2016
- **Contexte connu** : developpement Android natif en Java, avec un accent important sur les tests unitaires et les tests d'integration

#### Informations a completer

- Secteur et produit
- Contexte projet
- Role exact
- Stack Android
- Architecture
- Tests
- Resultats
- Raisons du depart

### Mayflower

- **Poste** : Developpeur mobile
- **Periode** : septembre 2011 - septembre 2015
- **Contexte connu** : applications natives iOS et Android, solutions multiplateformes Titanium en JavaScript

#### Informations a completer

- Secteur et type d'entreprise
- Clients ou produits principaux
- Role exact
- Technologies iOS / Android / Titanium
- Projets marquants
- Architecture
- Tests
- Publications stores
- Resultats
- Raisons du depart

### Education Nationale

- **Poste** : Professeur de mathematiques des lycees et colleges
- **Periode** : septembre 2002 - septembre 2011

#### Apports professionnels transferables

- Rigueur mathematique
- Pedagogie
- Structuration de la pensee
- Transmission de connaissances
- Capacite a expliquer des sujets complexes
- Gestion de groupes

#### Informations a completer

- Niveaux enseignes
- Responsabilites particulieres
- Projets pedagogiques
- Lien avec la reconversion vers le developpement logiciel

## Projets marquants

### Cut it!

Voir section Dodecamoon.

### TetraC

Voir section Dodecamoon.

### Gabby

Voir section LifeStoneLink.

### Autres projets

A completer.

## Competences techniques

### Langages

- Dart
- Swift
- Java
- JavaScript
- TypeScript
- PHP
- SQL

### Mobile

- Flutter
- iOS natif
- SwiftUI
- UIKit
- Android natif
- Applications iPhone
- Applications iPad
- Publication App Store
- Publication Play Store
- BLE
- MultipeerConnectivity

### Flutter

- Architecture complete d'application
- Publication iOS / Android
- Flavors
- Provider
- MobX
- setState
- Integration API
- Bluetooth
- CI/CD mobile

### iOS / Apple

- Swift
- SwiftUI
- UIKit
- Objective-C
- Core Data
- Swift Concurrency
- async/await
- Task
- actors
- @MainActor
- Observation
- Combine
- AVFoundation
- iCloud KVS
- MultipeerConnectivity
- Swift Testing
- XCTest UI

### Android

- Java
- Android natif
- Tests unitaires
- Tests d'integration

### Frontend web

- ReactJS

### Backend

- TypeScript / Node.js
- Laravel
- Bases Symfony
- Webservices .NET consommes cote mobile
- pm2

### Bases de donnees et stockage

- PostgreSQL
- Supabase
- Supabase Storage
- CSV

### Cloud / DevOps / Deploiement

- Docker
- Dokploy
- Bitrise
- fastlane
- pm2

### Monitoring / analytics

- Firebase Crashlytics
- Firebase Analytics
- Play Console
- App Store Connect
- Monitoring Supabase
- Logs backend via Dokploy
- OneSignal

### Architecture logicielle

- MVVM
- Architecture en couches
- Organisation par features
- Injection de dependances
- Repository pattern : a confirmer
- Protocoles et separation des responsabilites

### Qualite

- Code review
- Tests unitaires
- Tests UI
- Tests d'integration
- Architecture maintenable
- Performance
- Securite
- Accessibilite
- Localisation

### Methodologies et posture

- Autonomie forte
- Force de proposition
- Cadrage technique
- Support production
- Publication stores
- Encadrement de developpeurs
- Pedagogie

## Architecture logicielle

Architectures et patterns reellement mentionnes :

- MVVM
- Architecture en couches
- Organisation par features
- Injection de dependances
- Separation des responsabilites via protocoles
- State management Flutter avec MobX, Provider et setState

### A completer / confirmer

- Usage exact du Repository pattern
- Usage de Clean Architecture
- Usage de MVC, VIPER, Redux, Bloc, CQRS, Event Driven ou autres patterns

## Leadership

- Lead d'une equipe de 2 developpeurs mobiles chez LifeStoneLink
- Definition de l'architecture mobile de Gabby
- Code reviews
- Encadrement technique
- Contribution principale tout en pilotant une petite equipe
- Pedagogie issue de l'experience de professeur de mathematiques

### A completer

- Niveau des developpeurs encadres
- Mentoring formel ou informel
- Participation au recrutement
- Animation de reunions techniques
- Decisions d'architecture majeures
- Gestion de priorisation ou relation produit

## Formation

### 2012 - Licence professionnelle d'Informatique Mobile et Embarquee

- **Etablissement** : IUT Lyon 1, Bourg-en-Bresse
- **Modalite** : alternance chez EP Factory

### 2002 - CAPES de mathematiques

- **Etablissement** : IUFM de Lyon

### 2000 - Licence de Mathematiques

- **Etablissement** : Universite Claude Bernard Lyon 1

### Autoformation, veille et certifications

A completer.

## Realisations remarquables

- Conception et livraison complete de Cut it!, SaaS mobile Flutter publie sur iOS et Android.
- Mise en place d'une communication BLE avec protocole proprietaire vers une decoupeuse Silhouette.
- Construction d'un backend TypeScript / Node.js avec Supabase / PostgreSQL, roles, authentification et statistiques.
- Securisation d'une base Supabase via Row Level Security.
- Deploiement d'un backend et d'un admin ReactJS via Dokploy.
- Livraison d'un produit utilise par 90 etablissements et 265 utilisateurs.
- Produit Cut it! utilise a un rythme moyen d'environ 1 decoupe toutes les 3 minutes pendant les horaires d'ouverture des magasins.
- Lead technique Flutter sur l'ecosysteme Gabby, compose de plusieurs applications iOS et Android publiees.
- Definition d'une architecture Flutter MVVM organisee par features.
- Optimisation des performances de Gabby par reduction de la profondeur et du volume des payloads JSON.
- Developpement d'un jeu iOS SwiftUI de type Puissance 4 avec adversaire algorithmique, defis et multijoueur local via MultipeerConnectivity.

## Centres d'interet

A completer uniquement avec les centres d'interet apportant une valeur professionnelle.

## Mots-cles ATS

Flutter, Dart, iOS, Android, Swift, SwiftUI, UIKit, Objective-C, Java, mobile development, senior mobile developer, Flutter developer, iOS developer, mobile engineer, App Store, Play Store, publication stores, MVVM, architecture mobile, architecture en couches, state management, Provider, MobX, setState, Bluetooth, BLE, MultipeerConnectivity, Firebase, Crashlytics, analytics, Supabase, PostgreSQL, Row Level Security, RLS, TypeScript, Node.js, ReactJS, Docker, Dokploy, pm2, Bitrise, fastlane, CI/CD, backend, SaaS, B2B, B2C, e-commerce, jeux mobiles, performance mobile, JSON optimization, webservices, .NET APIs, authentication, roles, authorization, offline, notifications push, OneSignal, code review, lead developer, technical leadership, tests unitaires, tests UI, tests d'integration, Swift Testing, XCTest, accessibilite, localisation, monitoring, production support, clean code, qualite de code, autonomie, force de proposition.

## Axes d'amelioration

- Completer les details de LifeStoneLink : CI/CD, offline, paiement, notifications, monitoring, defis et resultats chiffres.
- Detailer l'experience Itelios : clients, projets, architecture, technologies, responsabilites et impacts.
- Detailer l'experience Itron : produit, contexte, architecture Android, tests et resultats.
- Detailer l'experience Mayflower : projets, technologies, publications stores et resultats.
- Enrichir les projets personnels ou open source eventuels.
- Evaluer le niveau de maitrise de chaque competence technique.
- Confirmer les architectures reellement utilisees au-dela de MVVM et architecture en couches.
- Ajouter les certifications, conferences, formations continues et veille technique.
- Identifier des metriques supplementaires : crash rate, volumes utilisateurs, gains de performance, temps de chargement, reduction d'erreurs, delais de livraison.
- Clarifier les contributions backend selon les experiences.
- Completer les raisons de depart pour chaque experience.
- Ajouter les centres d'interet pertinents uniquement s'ils renforcent le positionnement professionnel.
