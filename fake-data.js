// fake-data.js - Standalone fake data generator for Vantage CRM demo
(function(){
  var REGIONS=['Cr\u00e8te Est \u2014 H\u00e9raklion','Cr\u00e8te Ouest \u2014 Chania','Attique \u2014 Ath\u00e8nes Partie 1','Attique \u2014 Ath\u00e8nes Partie 2','Mac. Centrale \u2014 Thessalonique','\u00c9g\u00e9e Sud Est \u2014 Rhodes, Kos','P\u00e9loponn\u00e8se \u2014 Kalamata','Thessalie \u2014 Volos, Larissa','Dod\u00e9can\u00e8se \u2014 Rhodes','Cyclades \u2014 Mykonos, Santorin','Cr\u00e8te Centre \u2014 R\u00e9thymnon','Gr\u00e8ce Centrale \u2014 Lamia','\u00c9pire \u2014 Ioannina','Mix 1','Mix 2','Mix 3'];
  var FAMILLES=['Restauration','Beaut\u00e9','Auto','Artisans','Boulangerie','Sant\u00e9','Commerce','Services','Cafe & Bar'];
  var STATUSES=['nouveau','appele','negociation','gagne','rappeler','maintenance','perdu'];
  var VENDORS=['vendeur 1','vendeur 2','vendeur 3'];
  var CATEGORIES=['A','B','C',''];
  var TYPE_TELS=['mobile','fixe','mobile,fixe',''];
  var NAMES=[
    '\u03a4\u03b1\u03b2\u03ad\u03c1\u03bd\u03b1 \u039f\u03bb\u03c5\u03bc\u03c0\u03bf\u03c2','Caf\u00e9 Acropolis','Salon Aphrodite','Auto Zeus','Boulangerie Ath\u00e9na',
    '\u0395\u03c3\u03c4\u03b9\u03b1\u03c4\u03cc\u03c1\u03b9\u03bf \u03a0\u03bf\u03c3\u03b5\u03b9\u03b4\u03ce\u03bd','\u039a\u03bf\u03bc\u03bc\u03c9\u03c4\u03ae\u03c1\u03b9\u03bf \u0391\u03c6\u03c1\u03bf\u03b4\u03af\u03c4\u03b7','Garage H\u00e9racl\u00e8s','\u03a6\u03bf\u03cd\u03c1\u03bd\u03bf\u03c2 \u0394\u03ae\u03bc\u03b7\u03c4\u03c1\u03b1',
    'Caf\u00e9 Parthenon','\u03a4\u03b1\u03b2\u03ad\u03c1\u03bd\u03b1 \u039c\u03b9\u03bd\u03ce\u03c4\u03b1\u03c5\u03c1\u03bf\u03c2','Bar Dionysos','Salon H\u00e9ra','Auto Herm\u00e8s',
    'Boulangerie Olympe','\u0395\u03c3\u03c4\u03b9\u03b1\u03c4\u03cc\u03c1\u03b9\u03bf \u0391\u03c1\u03b9\u03ac\u03b4\u03bd\u03b7','\u039a\u03bf\u03c5\u03c1\u03b5\u03af\u03bf \u0391\u03c0\u03cc\u03bb\u03bb\u03c9\u03bd','Garage Ares',
    '\u03a6\u03bf\u03cd\u03c1\u03bd\u03bf\u03c2 \u03a0\u03b7\u03bd\u03b5\u03bb\u03cc\u03c0\u03b7','Caf\u00e9 Mykonos','\u03a4\u03b1\u03b2\u03ad\u03c1\u03bd\u03b1 \u03a3\u03b1\u03bd\u03c4\u03bf\u03c1\u03af\u03bd\u03b7','Bar Ikarus','Salon Calypso',
    'Auto Titan','Boulangerie Cr\u00e8te','\u0395\u03c3\u03c4\u03b9\u03b1\u03c4\u03cc\u03c1\u03b9\u03bf \u039d\u03ad\u03bc\u03b5\u03c3\u03b9\u03c2','Spa Ga\u00efa','Garage P\u00e9gase',
    '\u03a6\u03bf\u03cd\u03c1\u03bd\u03bf\u03c2 \u0397\u03bb\u03af\u03b1\u03c2','Caf\u00e9 Rhodes','\u03a4\u03b1\u03b2\u03ad\u03c1\u03bd\u03b1 \u039a\u03bd\u03c9\u03c3\u03cc\u03c2','Bar Orph\u00e9e','Salon Pers\u00e9phone',
    'Auto Cronos','Boulangerie Delphes','Pharmacie Ascl\u00e9pios','\u039a\u03b1\u03c4\u03ac\u03c3\u03c4\u03b7\u03bc\u03b1 \u0395\u03c1\u03bc\u03ae\u03c2',
    '\u03a4\u03b1\u03b2\u03ad\u03c1\u03bd\u03b1 \u0398\u03ac\u03bb\u03b1\u03c3\u03c3\u03b1','Caf\u00e9 Meteora','Salon Electra','\u0395\u03c3\u03c4\u03b9\u03b1\u03c4\u03cc\u03c1\u03b9\u03bf \u03a6\u03bf\u03af\u03b2\u03bf\u03c2',
    'Bar Ath\u00e9na','Garage Triton','Boulangerie Naxos','\u039a\u03bf\u03bc\u03bc\u03c9\u03c4\u03ae\u03c1\u03b9\u03bf \u038a\u03c1\u03b9\u03c2',
    '\u03a4\u03b1\u03b2\u03ad\u03c1\u03bd\u03b1 \u039b\u03b5\u03c9\u03bd\u03af\u03b4\u03b1\u03c2','Caf\u00e9 Sparti','Auto Achille','\u0395\u03c3\u03c4\u03b9\u03b1\u03c4\u03cc\u03c1\u03b9\u03bf \u03a0\u03bb\u03ac\u03c4\u03c9\u03bd\u03b1\u03c2',
    'Salon Daphn\u00e9','\u03a6\u03bf\u03cd\u03c1\u03bd\u03bf\u03c2 \u039a\u03ad\u03c1\u03ba\u03c5\u03c1\u03b1','Bar Apollon','Garage Minos',
    '\u03a4\u03b1\u03b2\u03ad\u03c1\u03bd\u03b1 \u0396\u03ac\u03ba\u03c5\u03bd\u03b8\u03bf\u03c2','Caf\u00e9 Thessalonique','Boulangerie Hydra','\u0395\u03c3\u03c4\u03b9\u03b1\u03c4\u03cc\u03c1\u03b9\u03bf \u039f\u03b4\u03c5\u03c3\u03c3\u03ad\u03b1\u03c2',
    '\u039a\u03b1\u03c4\u03ac\u03c3\u03c4\u03b7\u03bc\u03b1 \u0391\u03b8\u03b7\u03bd\u03ac','Salon S\u00e9l\u00e9n\u00e9','Auto Prom\u00e9th\u00e9e','Bar Pos\u00e9idon',
    '\u03a4\u03b1\u03b2\u03ad\u03c1\u03bd\u03b1 \u0399\u03b8\u03ac\u03ba\u03b7','\u03a6\u03bf\u03cd\u03c1\u03bd\u03bf\u03c2 \u03a0\u03ac\u03c4\u03bc\u03bf\u03c2','Caf\u00e9 Corinthie','\u0395\u03c3\u03c4\u03b9\u03b1\u03c4\u03cc\u03c1\u03b9\u03bf \u0391\u03af\u03bf\u03bb\u03bf\u03c2'
  ];
  var STREETS=['\u039f\u03b4\u03cc\u03c2 \u0395\u03c1\u03bc\u03bf\u03cd','\u039b\u03b5\u03c9\u03c6\u03cc\u03c1\u03bf\u03c2 \u0392\u03b1\u03c3\u03b9\u03bb\u03af\u03c3\u03c3\u03b7\u03c2 \u03a3\u03bf\u03c6\u03af\u03b1\u03c2','\u039f\u03b4\u03cc\u03c2 \u03a3\u03c4\u03b1\u03b4\u03af\u03bf\u03c5','\u03a0\u03bb\u03b1\u03c4\u03b5\u03af\u03b1 \u03a3\u03c5\u03bd\u03c4\u03ac\u03b3\u03bc\u03b1\u03c4\u03bf\u03c2','\u039f\u03b4\u03cc\u03c2 \u03a0\u03b1\u03bd\u03b5\u03c0\u03b9\u03c3\u03c4\u03b7\u03bc\u03af\u03bf\u03c5','\u039b\u03b5\u03c9\u03c6\u03cc\u03c1\u03bf\u03c2 \u039a\u03b7\u03c6\u03b9\u03c3\u03af\u03b1\u03c2','\u039f\u03b4\u03cc\u03c2 \u03a0\u03b1\u03c4\u03b7\u03c3\u03af\u03c9\u03bd','\u039f\u03b4\u03cc\u03c2 \u0391\u03ba\u03b1\u03b4\u03b7\u03bc\u03af\u03b1\u03c2','\u039f\u03b4\u03cc\u03c2 \u03a3\u03cc\u03bb\u03c9\u03bd\u03bf\u03c2','\u039f\u03b4\u03cc\u03c2 \u039c\u03b7\u03c4\u03c1\u03bf\u03c0\u03cc\u03bb\u03b5\u03c9\u03c2'];
  var CITIES=['\u0391\u03b8\u03ae\u03bd\u03b1','\u0398\u03b5\u03c3\u03c3\u03b1\u03bb\u03bf\u03bd\u03af\u03ba\u03b7','\u0397\u03c1\u03ac\u03ba\u03bb\u03b5\u03b9\u03bf','\u03a7\u03b1\u03bd\u03b9\u03ac','\u03a1\u03cc\u03b4\u03bf\u03c2','\u0392\u03cc\u03bb\u03bf\u03c2','\u0399\u03c9\u03ac\u03bd\u03bd\u03b9\u03bd\u03b1','\u039a\u03b1\u03bb\u03b1\u03bc\u03ac\u03c4\u03b1','\u039b\u03b1\u03bc\u03af\u03b1','\u039b\u03ac\u03c1\u03b9\u03c3\u03b1','\u03a1\u03ad\u03b8\u03c5\u03bc\u03bd\u03bf','\u039c\u03cd\u03ba\u03bf\u03bd\u03bf\u03c2','\u03a3\u03b1\u03bd\u03c4\u03bf\u03c1\u03af\u03bd\u03b7','\u039a\u03c9\u03c2'];
  var NOTES_POOL=['Int\u00e9ress\u00e9 par le site web','Rappeler la semaine prochaine','A d\u00e9j\u00e0 un site, veut refaire','Budget limit\u00e9','Tr\u00e8s motiv\u00e9','Pas disponible avant 15h','Demande devis personnalis\u00e9','A recommand\u00e9 un ami','En vacances','Souhaite page Instagram aussi','','','',''];

  function pick(arr){return arr[Math.floor(Math.random()*arr.length)]}
  function randInt(a,b){return Math.floor(Math.random()*(b-a+1))+a}
  function greekMobile(){return '+30 6'+randInt(90,99)+' '+String(randInt(100,999))+' '+String(randInt(1000,9999))}
  function greekFixed(){return '+30 2'+randInt(10,99)+randInt(0,9)+' '+String(randInt(100,999))+' '+String(randInt(1000,9999))}
  function randomDate(daysBack){var d=new Date();d.setDate(d.getDate()-randInt(0,daysBack));d.setHours(randInt(8,20),randInt(0,59),randInt(0,59));return d.toISOString()}
  function randomEmail(name){var s=name.replace(/[^a-zA-Z]/g,'').toLowerCase().slice(0,10);return s+(s?'':'biz')+randInt(1,999)+'@gmail.com'}

  var FAKE_PROSPECTS=[];
  for(var i=0;i<200;i++){
    var nom=i<NAMES.length?NAMES[i]:NAMES[i%NAMES.length]+' '+randInt(2,9);
    var isMobile=Math.random()>0.3;
    var status=pick(STATUSES);
    var vendeur=status==='nouveau'?(Math.random()>0.7?pick(VENDORS):''):pick(VENDORS);
    var created=randomDate(90);
    FAKE_PROSPECTS.push({
      id:i+1, nom:nom, numero:isMobile?greekMobile():greekFixed(),
      type_tel:pick(TYPE_TELS), famille:pick(FAMILLES), categorie:pick(CATEGORIES),
      region:pick(REGIONS), vendeur:vendeur, status:status, notes:pick(NOTES_POOL),
      email:randomEmail(nom), instagram:Math.random()>0.6?'@'+nom.replace(/[^a-zA-Z]/g,'').toLowerCase().slice(0,12):'',
      facebook:'', rating:randInt(0,5),
      adresse:STREETS[randInt(0,STREETS.length-1)]+' '+randInt(1,150)+', '+pick(CITIES),
      blacklisted:false, created_at:created, updated_at:created,
      last_called_at:status!=='nouveau'?randomDate(30):null,
      total_calls:status==='nouveau'?0:randInt(1,8),
      call_duration_total:status==='nouveau'?0:randInt(30,600),
      call_date:status!=='nouveau'?randomDate(14):null
    });
  }

  var CLIENT_STATUSES=['gagne','negociation','maintenance','rappeler'];
  var FAKE_CLIENTS=[];var cid=1;
  FAKE_PROSPECTS.forEach(function(p){
    if(CLIENT_STATUSES.indexOf(p.status)>=0){
      FAKE_CLIENTS.push({
        id:cid++, prospect_id:p.id, nom:p.nom, numero:p.numero,
        email:p.email, instagram:p.instagram, facebook:'',
        region:p.region, famille:p.famille, vendor_name:p.vendeur,
        site_status:p.status, project_id:null, hidden_by:'', notes:p.notes,
        created_at:p.created_at, updated_at:p.updated_at
      });
    }
  });

  var FAKE_PROJECTS=[
    {id:1,name:'Campagne Cr\u00e8te Est',region:'Cr\u00e8te Est \u2014 H\u00e9raklion',vendor:'vendeur 1',status:'active',created_at:randomDate(60),updated_at:randomDate(5)},
    {id:2,name:'Ath\u00e8nes Expansion',region:'Attique \u2014 Ath\u00e8nes Partie 1',vendor:'vendeur 2',status:'active',created_at:randomDate(45),updated_at:randomDate(3)},
    {id:3,name:'Rhodes & Kos Sprint',region:'\u00c9g\u00e9e Sud Est \u2014 Rhodes, Kos',vendor:'vendeur 3',status:'active',created_at:randomDate(30),updated_at:randomDate(1)}
  ];
  var projClients=FAKE_CLIENTS.filter(function(c){return c.region===FAKE_PROJECTS[0].region});
  projClients.slice(0,Math.min(5,projClients.length)).forEach(function(c){c.project_id=1});
  var projClients2=FAKE_CLIENTS.filter(function(c){return c.region===FAKE_PROJECTS[1].region});
  projClients2.slice(0,Math.min(4,projClients2.length)).forEach(function(c){c.project_id=2});

  var FAKE_CALLS=[];
  for(var j=0;j<150;j++){
    var p=pick(FAKE_PROSPECTS);
    FAKE_CALLS.push({
      id:j+1, prospect_id:p.id, prospect_name:p.nom, vendor_name:pick(VENDORS),
      duration:randInt(15,300), outcome:pick(['answered','no_answer','voicemail','busy','callback']),
      notes:pick(NOTES_POOL), created_at:randomDate(30)
    });
  }

  var FAKE_VENDOR_STATS=VENDORS.map(function(v,idx){
    return{id:idx+1, vendor_name:v, total_calls:randInt(80,250), total_duration:randInt(5000,25000),
      total_won:randInt(5,30), total_lost:randInt(3,15), created_at:randomDate(60), updated_at:randomDate(1)};
  });

  window.FAKE_PROSPECTS=FAKE_PROSPECTS;
  window.FAKE_CLIENTS=FAKE_CLIENTS;
  window.FAKE_PROJECTS=FAKE_PROJECTS;
  window.FAKE_CALLS=FAKE_CALLS;
  window.FAKE_VENDOR_STATS=FAKE_VENDOR_STATS;
  window.FAKE_REMINDERS=[];
  window.FAKE_BLACKLIST=[];
  window.FAKE_SCRIPTS=[];
  window.FAKE_BADGES=[];
  window.FAKE_PROSPECT_HISTORY=[];
  window.FAKE_PROJECT_OBJECTIVES=[];
  window.FAKE_ACTIVITY_LOG=[];
  window.FAKE_VENDOR_BADGES=[];
})();
