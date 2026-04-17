#!/usr/bin/env python3
"""Translate all visible French text in apex-consulting-template.html to English.
Applies to both standalone template and index-demo.html, then re-injects into index.html.
"""
import re, sys, io

# ═══════════════════════════════════════════════════════════════
# TRANSLATION DICTIONARY — order matters (longer first)
# ═══════════════════════════════════════════════════════════════
TRANS = [
    # ── Taglines & titles ──
    ("Apex Consulting — Agence Immobilière Premium Paris", "Apex Consulting — Premium Real Estate Paris"),
    ("Agence Immobilière Premium Paris", "Premium Real Estate Paris"),
    ("Parlons de Votre Projet", "Let's Talk About Your Project"),
    ("Votre prochain chez-vous", "Your Next Home"),
    ("est déjà là.", "is already here."),

    # ── Nav ──
    ("L'Agence", "The Agency"),
    ("Nos Services", "Our Services"),
    ("Notre équipe", "Our Team"),
    ("Notre méthode", "Our Method"),
    ("Propriétés", "Properties"),
    ("Actualités", "News"),
    ("Équipe", "Team"),
    ("Estimation gratuite", "Free Valuation"),
    ("Estimer mon bien →", "Value my property →"),
    ("Estimer mon bien", "Value my property"),
    ("Défiler", "Scroll"),
    ("contact us", "contact us"),
    ("Questions fréquentes", "Frequently Asked Questions"),

    # ── Hero / stats ──
    ("Biens vendus en 2024", "Properties sold in 2024"),
    ("Biens disponibles", "Available properties"),
    ("Clients qui nous recommandent", "Clients who recommend us"),
    ("Délai moyen pour vendre", "Average sale time"),
    ("Délai moyen de vente", "Average sale time"),
    ("Délai moyen vente", "Average sale time"),
    ("Prix moyen de transaction", "Average transaction price"),
    ("Prix moyen Paris", "Average price Paris"),
    ("Taux crédit 20 ans", "20-year mortgage rate"),

    # ── Services ──
    ("Vente & Estimation", "Sales & Valuation"),
    ("Achat & Accompagnement", "Purchase & Support"),
    ("Gestion Locative", "Rental Management"),
    ("Gestion locative", "Rental Management"),
    ("Conseil & Investissement", "Advisory & Investment"),
    ("Conseil en investissement", "Investment advisory"),
    ("Prestige & Investissement", "Prestige & Investment"),
    ("Location & Premier Achat", "Rental & First Purchase"),
    ("Investissement · Gestion Locative", "Investment · Rental Management"),
    ("Investissement · Conseils", "Investment · Advisory"),
    ("Conseils Vendeurs · Pratique", "Seller Tips · Practical"),
    ("Marché · Analyse", "Market · Analysis"),
    ("Service Gratuit · Sans Engagement", "Free Service · No Commitment"),
    ("Disponible · Réponse sous 2 heures", "Available · Response within 2 hours"),

    # ── Properties ──
    ("Voir le bien →", "View property →"),
    ("Voir le bien", "View property"),
    ("À vendre", "For sale"),
    ("À louer", "For rent"),
    ("EXCLUSIVITÉ", "EXCLUSIVE"),
    ("OPPORTUNITÉ", "OPPORTUNITY"),
    ("LIVRAISON T4 2025", "DELIVERY Q4 2025"),
    ("Avenue Victor Hugo, Paris 16ème", "Avenue Victor Hugo, Paris 16th"),
    ("Neuilly-sur-Seine · Centre", "Neuilly-sur-Seine · Centre"),
    ("La Défense · Prestige", "La Défense · Prestige"),
    ("Le Marais, Paris 3ème", "Le Marais, Paris 3rd"),
    ("Résidentiel · Paris Rive Droite", "Residential · Paris Right Bank"),
    ("No properties found", "No properties found"),
    ("Double hauteur 5m", "5m double ceiling"),
    ("Jardin 300m²", "300m² garden"),
    ("Jardin 800m²", "800m² garden"),
    ("Verrières", "Skylights"),
    ("Local commercial", "Commercial space"),
    ("Loft / Atypique", "Loft / Atypical"),
    ("Maison / Villa", "House / Villa"),

    # ── Roles / team ──
    ("Directeur & Fondateur", "Director & Founder"),
    ("Directrice Commerciale", "Sales Director"),
    ("Expert Patrimoine", "Wealth Expert"),
    ("Chargée de Clientèle", "Client Relations Manager"),

    # ── Testimonials / profiles ──
    ("Vendeurs · Paris 16ème · 1\u00a0850\u00a0000 €", "Sellers · Paris 16th · €1,850,000"),
    ("Vendeurs · Paris 16ème · 1 850 000 €", "Sellers · Paris 16th · €1,850,000"),
    ("Vendeurs · Boulogne-Billancourt · Maison 240m²", "Sellers · Boulogne-Billancourt · 240m² House"),
    ("Acquéreur · Neuilly-sur-Seine · Villa 380m²", "Buyer · Neuilly-sur-Seine · 380m² Villa"),
    ("Investisseur · Paris 8ème · 4 appartements", "Investor · Paris 8th · 4 apartments"),
    ("Investisseur expatrié · Londres → Paris", "Expat investor · London → Paris"),
    ("Primo-accédante · Paris 11ème · Appartement 78m²", "First-time buyer · Paris 11th · 78m² Apartment"),
    ("Vendeur · Paris 16ème", "Seller · Paris 16th"),

    # ── Zones ──
    ("Paris 1–4", "Paris Centre"),
    ("Paris 5–8", "Paris 5th–8th"),
    ("Paris 9–12", "Paris 9th–12th"),
    ("Paris 13–20", "Paris 13th–20th"),
    ("Côte d'Azur", "French Riviera"),

    # ── Forms ──
    ("Prénom ", "First name "),
    ("Prénom", "First name"),
    ("Nom ", "Last name "),
    ("Nom", "Last name"),
    ("Téléphone", "Phone"),
    ("Email ", "Email "),
    ("Votre message ", "Your message "),
    ("Votre message", "Your message"),
    ("Objet de votre demande ", "Subject of your request "),
    ("Informations complémentaires", "Additional information"),
    ("Je souhaite acheter un bien", "I want to buy a property"),
    ("Je souhaite vendre mon bien", "I want to sell my property"),
    ("Je veux une estimation gratuite", "I want a free valuation"),
    ("Autre demande", "Other request"),
    ("Obtenir mon estimation", "Get my valuation"),
    ("Sélectionner…", "Select…"),
    ("Sélectionner", "Select"),
    ("Adresse du bien ", "Property address "),
    ("Type de bien ", "Property type "),
    ("Surface (m²) ", "Area (m²) "),
    ("Surface habitable loi Carrez", "Habitable area (Carrez Law)"),

    # ── FAQ ──
    ("Combien de temps pour vendre mon bien ?", "How long does it take to sell my property?"),
    ("Comment se déroule une estimation ?", "How does the valuation process work?"),
    ("Quels sont vos honoraires ?", "What are your fees?"),
    ("Proposez-vous des biens off-market ?", "Do you offer off-market properties?"),
    ("Que comprend votre service de gestion locative ?", "What does your rental management service include?"),
    ("Travaillez-vous avec des acquéreurs étrangers ?", "Do you work with foreign buyers?"),

    # ── Footer / legal ──
    ("Mentions légales", "Legal Notice"),
    ("Politique de confidentialité", "Privacy Policy"),
    ("Confidentialité", "Privacy"),
    ("Carte Professionnelle T", "Professional Card T"),
    ("Membre FNAIM", "FNAIM Member"),
    ("Loi Alur · RGE Partenaires", "Alur Law · RGE Partners"),
    ("Dernière mise à jour : Octobre 2025", "Last updated: October 2025"),

    # ── Hours ──
    ("Lun-Ven 9h-19h · Sam 10h-17h", "Mon–Fri 9am–7pm · Sat 10am–5pm"),
    ("Lun–Ven 9h–19h · Sam 10h–17h", "Mon–Fri 9am–7pm · Sat 10am–5pm"),
    ("Lun–Ven : 9h – 19h", "Mon–Fri: 9am – 7pm"),
    ("Sam : 10h – 17h", "Sat: 10am – 5pm"),

    # ── Dates (months) ──
    ("Jan", "Jan"), ("Fév", "Feb"), ("Mar", "Mar"), ("Avr", "Apr"),
    ("Mai", "May"), ("Juin", "Jun"), ("Juil", "Jul"), ("Aoû", "Aug"),
    ("Sep", "Sep"), ("Oct", "Oct"), ("Nov", "Nov"), ("Déc", "Dec"),

    # ── Misc ──
    ("Rapport PDF de 12 pages remis en main propre ou par email",
     "12-page PDF report delivered in person or by email"),
    ("Analyse personnalisée par un expert senior du secteur",
     "Personalised analysis by a senior industry expert"),
    ("Conseils Vendeurs", "Seller Tips"),
    ("Aller au contenu principal", "Skip to main content"),
    ("Skip to main content", "Skip to main content"),

    # ── SEO description ──
    ("Apex Consulting, agence immobilière premium à Paris. Vente, achat, estimation et gestion locative de biens d'exception. 15 ans d'expertise · 247 transactions en 2024 · Réponse en 2h.",
     "Apex Consulting, premium real estate agency in Paris. Sales, purchase, valuation and rental management of exceptional properties. 15 years of expertise · 247 transactions in 2024 · Response in 2h."),
    ("L'immobilier d'exception, négocié avec précision. 15 ans d'expertise sur Paris et Île-de-France.",
     "Exceptional real estate, negotiated with precision. 15 years of expertise across Paris and Île-de-France."),
]

TRANS += [
    # ── Section labels ──
    ("01 — Properties en Vedette", "01 — Featured Properties"),
    ("Properties en Vedette", "Featured Properties"),
    ("02 — Notre Approche", "02 — Our Approach"),
    ("Notre Approche", "Our Approach"),
    ("03 — Baromètre du Marché", "03 — Market Barometer"),
    ("Baromètre du Marché", "Market Barometer"),
    ("04 — L'Team", "04 — The Team"),
    ("L'Team", "The Team"),
    ("05 — News & Insights", "05 — News & Insights"),

    # ── Floors ──
    ("32ème étage", "32nd floor"),
    ("3ème étage", "3rd floor"),
    ("16ème", "16th"),
    ("11ème", "11th"),
    ("8ème", "8th"),

    # ── Testimonials (full quotes) ──
    ('"Apex a vendu notre appartement du 16th en 21 jours, 40 000€ au-dessus de l\'estimation des deux autres agences consultées. Leur réseau d\'acheteurs est impressionnant."',
     '"Apex sold our 16th arrondissement apartment in 21 days, €40,000 above the estimate from the two other agencies we consulted. Their buyer network is impressive."'),
    ('"Apex a vendu notre appartement du 16ème en 21 jours, 40 000€ au-dessus de l\'estimation des deux autres agences consultées. Leur réseau d\'acheteurs est impressionnant."',
     '"Apex sold our 16th arrondissement apartment in 21 days, €40,000 above the estimate from the two other agencies we consulted. Their buyer network is impressive."'),
    ('"En tant qu\'expatrié basé à Londres, j\'avais besoin d\'une équipe en qui avoir une confiance totale. Antoine a géré l\'intégralité du dossier à distance. Résultat au-delà de mes attentes."',
     '"As an expat based in London, I needed a team I could fully trust. Antoine managed the entire case remotely. The outcome exceeded my expectations."'),
    ('"L\'estimation d\'Apex était précise à 2% près du prix de vente. Je recommande sans hésiter."',
     '"Apex\'s valuation was accurate to within 2% of the final sale price. I recommend them without hesitation."'),
    ('"L\'estimation fournie par l\'agence était à 2,3% près du prix final de vente. Un niveau de précision que nous n\'avions jamais vu ailleurs."',
     '"The agency\'s valuation was within 2.3% of the final sale price. A level of accuracy we\'ve never seen elsewhere."'),
    ('"La gestion locative d\'Apex est impeccable depuis 3 ans. Pas un seul jour de vacance sur mes 4 appartements. Les comptes rendus sont précis, les locataires soigneusement sélectionnés."',
     '"Apex\'s rental management has been impeccable for 3 years. Not a single day of vacancy across my 4 apartments. Reports are precise, tenants carefully selected."'),
    ('"Nous cherchions depuis 8 mois avec 3 autres agences. Apex a trouvé notre maison de rêve en 6 semaines, hors marché. Thomas a négocié 55 000€ de réduction. Je regrette de ne pas les avoir appelés en premier."',
     '"We\'d been searching for 8 months with 3 other agencies. Apex found our dream home in 6 weeks, off-market. Thomas negotiated €55,000 off the price. I regret not calling them first."'),
    ('"Premier achat immobilier, beaucoup d\'appréhension. Claire a répondu à chaque question avec patience. Nous avons signé avec une totale confiance."',
     '"First property purchase, lots of anxiety. Claire answered every question with patience. We signed with complete confidence."'),
    ('"0% vacance locative sur notre parc géré"', '"0% rental vacancy across our managed portfolio"'),
    ('"Économie moyenne : 47 000 € négociés"', '"Average savings: €47,000 negotiated"'),
    ("Économie moyenne", "Average savings"),
    ("négociés", "negotiated"),
    ("vacance locative", "rental vacancy"),

    # ── Address ──
    ("12 Avenue de la Grande Armée", "12 Avenue de la Grande Armée"),  # keep proper noun

    # ── ARIA / alt attributes ──
    ("Appartement haussmannien entièrement rénové", "Fully renovated Haussmann apartment"),
    ("Graphique d'évolution des taux immobiliers en 2025", "2025 real estate rates evolution chart"),
    ("Intérieur d'appartement mis en valeur pour la vente", "Apartment interior staged for sale"),
    ("Mayson de ville XIXème siècle avec jardin arboré", "19th-century townhouse with landscaped garden"),
    ("Penthouse avec terrasses panoramiques et vue sur Paris", "Penthouse with panoramic terraces and Paris views"),
    ("Villa d'architecte contemporaine avec piscine et jardin paysagé", "Contemporary architect villa with pool and landscaped garden"),
    ("28 jours délai moyen de vente", "28 days average sale time"),
    ("28 jours délai moyen pour vendre", "28 days average sale time"),
    ("Retour à l'accueil", "Back to home"),
    ("Articles récents", "Recent articles"),
    ("Bien en exclusivité", "Exclusive property"),
    ("Caractéristiques du bien", "Property features"),
    ("Caractéristiques", "Features"),
    ("Chiffres clés Apex Consulting", "Apex Consulting key figures"),
    ("Données du marché immobilier parisien", "Paris real estate market data"),
    ("Envoyer mon message à Apex Consulting", "Send my message to Apex Consulting"),
    ("Envoyer un email à Apex Consulting", "Send email to Apex Consulting"),
    ("Envoyer un email à Thomas Leroux", "Send email to Thomas Leroux"),
    ("Fermer la vidéo", "Close video"),
    ("Filtrer les propriétés par catégorie", "Filter properties by category"),
    ("Formulaire d'estimation immobilière", "Property valuation form"),
    ("Graphique d'évolution du prix au m² sur 12 mois", "12-month price per m² evolution chart"),
    ("Lecteur vidéo", "Video player"),
    ("Liens légaux", "Legal links"),
    ("Liste des propriétés en vedette", "List of featured properties"),
    ("Loft prestige Le Marais Paris 3ème — 1 450 000 euros", "Prestige loft Le Marais Paris 3rd — 1,450,000 euros"),
    ("Navigation témoignages", "Testimonial navigation"),
    ("Nos chiffres clés", "Our key figures"),
    ("Penthouse La Défense — 1 680 000 euros", "Penthouse La Défense — 1,680,000 euros"),
    ("Prix moyen au mètre carré Paris : 10 247 euros", "Average price per square metre Paris: 10,247 euros"),
    ("Réseaux sociaux Apex Consulting", "Apex Consulting social networks"),
    ("Stable par rapport au trimestre précédent", "Stable compared to previous quarter"),
    ("Taux de crédit immobilier : 3,85%", "Mortgage rate: 3.85%"),
    ("Télécharger le baromètre complet du marché immobilier", "Download the full real estate market report"),
    ("Témoignage de ", "Testimonial from "),
    ("Témoignage précédent", "Previous testimonial"),
    ("Témoignage suivant", "Next testimonial"),
    ("Témoignages clients", "Client testimonials"),
    ("Voir toutes nos actualités", "See all our news"),
    ("Voir toutes nos propriétés", "See all our properties"),
    ("Decrivez votre projet immobilier. Plus vous êtes précis, mieux nous pouvons vous répondre...",
     "Describe your real estate project. The more specific you are, the better we can help..."),
    ("Étage, travaux réalisés, situation locative, urgence particulière...",
     "Floor, work completed, rental status, special urgency..."),
    ("Isabelle et Laurent M.", "Isabelle & Laurent M."),
    ("Pierre et Anne-Sophie V.", "Pierre & Anne-Sophie V."),

    # ── Meta / SEO ──
    ("agence immobilière paris, immobilier luxe paris, estimation immobilière gratuite, vente appartement paris, achat appartement paris, gestion locative paris",
     "real estate agency paris, luxury real estate paris, free property valuation, apartment sale paris, apartment purchase paris, rental management paris"),
    ("Apex Consulting — Agence Immobilière Premium", "Apex Consulting — Premium Real Estate"),
    ("L'immobilier d'exception, négocié avec précision.",
     "Exceptional real estate, negotiated with precision."),
    ("Agence immobilière premium spécialisée dans les biens d'exception à Paris et Île-de-France.",
     "Premium real estate agency specialising in exceptional properties in Paris and Île-de-France."),
    ("Nos honoraires de transaction sont conformes à la loi ALUR. Pour une estimation, c'est entièrement gratuit.",
     "Our transaction fees comply with the ALUR law. Valuations are entirely free."),
    ("Notre délai moyen est de 28 jours pour un bien correctement estimé et bien présenté.",
     "Our average timeline is 28 days for a correctly valued and well-presented property."),

    # ── Hero / main copy ──
    ("L'immobilier d'exception, négocié avec précision. Depuis 2010, nous accompagnons les acheteurs et vendeurs les plus exigeants de la région parisienne.",
     "Exceptional real estate, negotiated with precision. Since 2010, we've guided the most demanding buyers and sellers in the Paris region."),
    ("Decouvrir nos propriétés", "Discover our properties"),
    ("Découvrir nos propriétés", "Discover our properties"),

    # ── Section comments & headers ──
    ("MÉTRIQUES", "METRICS"),
    ("PROPRIÉTÉS EN VEDETTE", "FEATURED PROPERTIES"),
    ("BAROMÈTRE", "BAROMETER"),
    ("ÉQUIPE", "TEAM"),
    ("TÉMOIGNAGES", "TESTIMONIALS"),

    # ── Properties section ──
    ("Des biens d'exception,", "Exceptional properties,"),
    ("sélectionnés pour vous.", "selected for you."),
    ("Une sélection de nos mandats exclusifs et des meilleures opportunités du marché.",
     "A selection of our exclusive mandates and the best market opportunities."),

    # ── Estimation / method ──
    ("Our Method d'estimation combine l'analyse en temps réel des transactions récentes dans votre secteur, l'expertise terrain de nos agents et une connaissance fine des tendances de marché. Vous recevez un rapport détaillé sous 48 heures, rédigé par un expert senior — pas un algorithme.",
     "Our valuation method combines real-time analysis of recent transactions in your area, our agents' field expertise, and deep knowledge of market trends. You receive a detailed report within 48 hours, written by a senior expert — not an algorithm."),
    ("🔒 Vos coordonnées sont protégées et ne seront jamais transmises à des tiers.",
     "🔒 Your contact details are protected and will never be shared with third parties."),
    ("J'accepte que mes données soient utilisées pour traiter ma demande d'estimation.",
     "I agree that my data may be used to process my valuation request."),
    ("Vos données sont protégées. Aucune obligation de mandat.",
     "Your data is protected. No mandate commitment required."),

    # ── Services section ──
    ("Quatre piliers d'excellence. Un seul objectif : votre intérêt à long terme.",
     "Four pillars of excellence. One objective: your long-term interest."),
    ("De la recherche à la remise des clés, nous négocions chaque détail pour que vous obteniez le meilleur bien au meilleur prix.",
     "From search to handover, we negotiate every detail so you get the best property at the best price."),
    ("Mise en valeur professionnelle, diffusion multi-canaux et réseau d'acheteurs qualifiés pour vendre vite et au juste prix.",
     "Professional staging, multi-channel distribution, and qualified buyer network to sell quickly at the right price."),
    ("Sélection rigoureuse des locataires, gestion administrative complète et optimisation de votre rendement locatif sans effort de votre part.",
     "Rigorous tenant selection, full administrative management, and rental yield optimisation with zero effort on your part."),
    ("Analyse de rentabilité, identification des opportunités et structuration fiscale pour maximiser votre patrimoine sur le long terme.",
     "Profitability analysis, opportunity identification, and tax structuring to maximise your wealth long-term."),

    # ── Barometer ──
    ("Le marché en temps réel.", "The market in real time."),
    ("Données actualisées chaque trimestre. Analyse rédigée par nos experts.",
     "Data updated every quarter. Analysis written by our experts."),
    ("Télécharger le baromètre complet", "Download the full report"),

    # ── Team ──
    ("Des experts à votre service.", "Experts at your service."),
    ("Plus de 15 ans d'expérience collective. Une présence sur Paris, Neuilly et la French Riviera.",
     "Over 15 years of collective experience. Presence in Paris, Neuilly and the French Riviera."),
    ('"Les meilleurs biens partent en moins de 10 jours. Mon rôle : que mes clients soient là quand ça arrive."',
     '"The best properties sell in under 10 days. My role: make sure my clients are there when it happens."'),
    ('"Acheter pour la première fois, ça fait peur. Mon rôle est de rendre ça simple et serein."',
     '"Buying for the first time is scary. My role is to make it simple and calm."'),

    # ── Testimonials intro ──
    ("Des résultats concrets, des histoires vraies.",
     "Real results, true stories."),

    # ── Remaining hero ──
    ("Exceptional real estate, negotiated with precision. Depuis 2010, nous accompagnons les acheteurs et vendeurs les plus exigeants de la région parisienne.",
     "Exceptional real estate, negotiated with precision. Since 2010, we've guided the most demanding buyers and sellers in the Paris region."),

    # ── FAQ answers ──
    ("Nos honoraires de transaction sont conformes à la loi ALUR et varient selon le type de mandat et le prix de vente. Ils vous sont communiqués par écrit avant toute signature. Pour la gestion locative, nous prélevons entre 6 et 9% des loyers charges comprises. Pour une estimation, c'est entièrement gratuit.",
     "Our transaction fees comply with the ALUR law and vary by mandate type and sale price. They're communicated to you in writing before any signature. For rental management, we charge between 6% and 9% of rent including charges. Valuations are entirely free."),
    ("Our average timeline is 28 days for a correctly valued and well-presented property. Cela peut varier selon le secteur et le type de bien. Nous vous donnons une fourchette réaliste dès le premier rendez-vous.",
     "Our average timeline is 28 days for a correctly valued and well-presented property. This may vary by area and property type. We give you a realistic range at the first meeting."),
    ("Oui. Environ 30% de nos mandats sont traités en off-market. Ces biens sont réservés à nos acheteurs enregistrés. Pour y accéder, il suffit de nous contacter et de définir ensemble vos critères de recherche.",
     "Yes. Around 30% of our mandates are handled off-market. These properties are reserved for our registered buyers. To access them, simply contact us and we'll define your search criteria together."),
    ("Notre expert se déplace à votre domicile pour une visite d'environ 45 minutes. Il analyse les données des transactions récentes dans votre secteur et vous remet un rapport sous 48h. C'est entièrement gratuit et sans obligation.",
     "Our expert visits your home for approximately 45 minutes. They analyse recent transaction data in your area and deliver a report within 48h. It's entirely free and without obligation."),
    ("Absolument. Nous accompagnons régulièrement des acheteurs internationaux (Royaume-Uni, États-Unis, Moyen-Orient, Asie du Sud-Est). Nos agents parlent couramment anglais et nous pouvons vous mettre en relation avec des notaires spécialisés dans les transactions internationales.",
     "Absolutely. We regularly assist international buyers (UK, USA, Middle East, Southeast Asia). Our agents are fluent in English and we can connect you with notaries specialised in international transactions."),
    ("Notre service comprend la mise en location, la gestion courante (quittances, relations locataire, travaux), les déclarations fiscales et la Garantie Loyers Impayés en option. Vous n'avez rien à faire.",
     "Our service covers letting, day-to-day management (receipts, tenant relations, works), tax filings, and optional Rent Guarantee Insurance. You have nothing to do."),

    # ── News section ──
    ("Le marché, décrypté.", "The market, decoded."),
    ("Toutes nos actualités", "All our news"),
    ("Taux immobiliers en 2025 : ce que les données de septembre signifient vraiment",
     "Mortgage rates in 2025: what September's data really means"),
    ("Après deux ans de hausse, les taux de crédit immobilier semblent se stabiliser. Ce que cela implique pour votre pouvoir d'achat...",
     "After two years of rises, mortgage rates appear to be stabilising. What this means for your purchasing power..."),
    ("Investir dans le neuf en 2025 : les quartiers parisiens à surveiller",
     "Investing in new-builds in 2025: Paris districts to watch"),
    ("Entre la fin du Pinel classique et l'essor du LMNP, les opportunités sont là pour qui sait où chercher...",
     "Between the end of the classic Pinel scheme and the rise of LMNP, opportunities are there for those who know where to look..."),
    ("Home staging : comment préparer votre bien pour maximiser sa valeur ?",
     "Home staging: how to prepare your property to maximise its value"),
    ("Un bien bien présenté se vend en moyenne 15% plus cher et 3 fois plus vite. Voici nos 8 étapes recommandées...",
     "A well-presented property sells on average 15% higher and 3× faster. Here are our 8 recommended steps..."),

    # ── Contact section ──
    ("Que vous vendiez, achetiez ou investissiez, nos experts sont disponibles pour vous guider à chaque étape de votre projet.",
     "Whether you're selling, buying or investing, our experts are available to guide you at every step of your project."),
    ("Disponible aujourd'hui · Réponse sous 2 heures",
     "Available today · Response within 2 hours"),
    ("Our Team répond sous 2 heures pendant les heures ouvrées.",
     "Our team responds within 2 hours during working hours."),
    ("J'accepte que mes données soient utilisées pour traiter ma demande.",
     "I agree that my data may be used to process my request."),
    ("🔒 Données protégées · Réponse garantie sous 2h ouvrées",
     "🔒 Data protected · Guaranteed response within 2 business hours"),

    # ── Footer ──
    ("SIRET : XXX XXX XXX 00042 · RCS Paris 123 456 789",
     "SIRET: XXX XXX XXX 00042 · RCS Paris 123 456 789"),
    ("Conçu avec soin par Vantage Web Agency",
     "Crafted with care by Vantage Web Agency"),
    ("Modal vidéo", "Video modal"),

    # ── Meta twitter ──
    ("Exceptional real estate, negotiated with precision.",
     "Exceptional real estate, negotiated with precision."),

    # ── Section comment ACTUALITÉS ──
    ("ACTUALITÉS", "NEWS"),

    # ── ARIA / alt final pass ──
    ("Appartement neuf BBC avec balcon plein sud", "Brand-new low-energy apartment with south-facing balcony"),
    ("Claire Petit, Client Relations Manager chez Apex Consulting", "Claire Petit, Client Relations Manager at Apex Consulting"),
    ("Immeubles neufs en construction dans Paris", "New buildings under construction in Paris"),
    ("Loft d'exception ancien atelier d'artiste", "Exceptional loft in a former artist's studio"),
    ("Thomas Leroux, Directeur et Fondateur d'Apex Consulting", "Thomas Leroux, Director and Founder of Apex Consulting"),
    ("1 247 biens disponibles", "1,247 properties available"),
    ("1,2 million d'euros de prix moyen de transaction", "€1.2 million average transaction price"),
    ("247 plus biens vendus en 2024", "247+ properties sold in 2024"),
    ("98 pourcent de clients qui nous recommandent", "98 percent of clients who recommend us"),
    ("Antoine Dubois sur LinkedIn", "Antoine Dubois on LinkedIn"),
    ("Apex Consulting sur Instagram", "Apex Consulting on Instagram"),
    ("Apex Consulting sur LinkedIn", "Apex Consulting on LinkedIn"),
    ("Apex Consulting sur YouTube", "Apex Consulting on YouTube"),
    ("Claire Petit sur LinkedIn", "Claire Petit on LinkedIn"),
    ("Sophie Martin sur LinkedIn", "Sophie Martin on LinkedIn"),
    ("Thomas Leroux sur LinkedIn", "Thomas Leroux on LinkedIn"),
    ("Chargement du site Apex Consulting", "Loading Apex Consulting site"),
    ("Consulter tous nos biens immobiliers", "View all our properties"),
    ("En baisse de 8 jours", "Down 8 days"),
    ("En hausse de 12%", "Up 12%"),
    ("En hausse de 2,3%", "Up 2.3%"),
    ("En savoir plus sur notre conseil en investissement", "Learn more about our investment advisory"),
    ("En savoir plus sur notre gestion locative", "Learn more about our rental management"),
    ("En savoir plus sur notre service d'achat et accompagnement", "Learn more about our purchase & support service"),
    ("Fermer le menu de navigation", "Close navigation menu"),
    ("Formulaire de contact Apex Consulting", "Apex Consulting contact form"),
    ("Lire l'article : Home staging, notre guide", "Read article: Home staging, our guide"),
    ("Lire l'article : Investir dans le neuf en 2025", "Read article: Investing in new-builds in 2025"),
    ("Lire l'article : Taux immobiliers en 2025", "Read article: Mortgage rates in 2025"),
    ("Mayson de ville Saint-Germain-en-Laye — 980 000 euros", "Townhouse Saint-Germain-en-Laye — 980,000 euros"),
    ("Menu de navigation mobile", "Mobile navigation menu"),
    ("Navigation du pied de page", "Footer navigation"),
    ("Nos services immobiliers", "Our real estate services"),
    ("Obtenir une estimation gratuite de votre bien", "Get a free valuation of your property"),
    ("Ouvrir le menu de navigation", "Open navigation menu"),
    ("Progression de lecture", "Reading progress"),
    ("Villa contemporaine Neuilly-sur-Seine — 2 850 000 euros", "Contemporary villa Neuilly-sur-Seine — 2,850,000 euros"),
    ('placeholder="12 rue du Faubourg, 75008 Paris"', 'placeholder="12 Faubourg Street, 75008 Paris"'),

    # ── Final remnants ──
    ('" jours"', '" days"'),
    ('>28 jours<', '>28 days<'),
    ('>45 jours<', '>45 days<'),
    ('Average sale time : 45 jours', 'Average sale time: 45 days'),
    ('"28 jours en moyenne pour trouver un acheteur"', '"28 days on average to find a buyer"'),
    ('100% gratuit, aucune obligation de signer un mandat', '100% free, no obligation to sign a mandate'),
    ('data-suffix=" jours"', 'data-suffix=" days"'),

    # ── Final cleanup ──
    (">Adresse<", ">Address<"),
    (">Appartement<", ">Apartment<"),
    (">Horaires<", ">Hours<"),
    (">Terrain<", ">Land<"),
    (">Tous<", ">All<"),
    (">NOUVEAU<", ">NEW<"),
    ("Investissement · Rental Management", "Investment · Rental Management"),
    ("Mayson", "Townhouse"),

    # ── Misc French remnants ──
    ("en Vedette", "Featured"),
    ("— Marc Dubernard,", "— Marc Dubernard,"),  # name unchanged
]

# ── Standalone words/short strings (applied after phrases) ──
SHORT_TRANS = [
    (">Nom<", ">Last name<"),
    (">Prénom<", ">First name<"),
    (">Téléphone<", ">Phone<"),
    (">Email<", ">Email<"),
    ('"Nom"', '"Last name"'),
    ('"Prénom"', '"First name"'),
    ('"Téléphone"', '"Phone"'),
    ("lang=\"fr\"", "lang=\"en\""),
    ("locale=\"fr_FR\"", "locale=\"en_US\""),
    ("og:locale\" content=\"fr_FR\"", "og:locale\" content=\"en_US\""),
]


def translate(text):
    for fr, en in TRANS:
        text = text.replace(fr, en)
    for fr, en in SHORT_TRANS:
        text = text.replace(fr, en)
    return text


def process_file(path):
    with io.open(path, 'r', encoding='utf-8') as f:
        s = f.read()
    original_len = len(s)
    s = translate(s)
    with io.open(path, 'w', encoding='utf-8') as f:
        f.write(s)
    print(f"  {path}: {original_len} → {len(s)} chars")


if __name__ == '__main__':
    print("Translating French → English...")
    process_file('apex-consulting-template.html')
    process_file('index-demo.html')
    print("Done. Re-run inject-apex.py to update index.html.")
