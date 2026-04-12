// fake-data.js - 10000+ prospects for Vantage CRM demo
(function(){
  var RD=[
    {r:'Attique \u2014 Ath\u00e8nes Partie 1',n:3500},
    {r:'Attique \u2014 Ath\u00e8nes Partie 2',n:3200},
    {r:'Mac. Centrale \u2014 Thessalonique',n:1500},
    {r:'Cr\u00e8te Est \u2014 H\u00e9raklion',n:800},
    {r:'Thessalie \u2014 Volos, Larissa',n:600},
    {r:'Cr\u00e8te Ouest \u2014 Chania',n:450},
    {r:'P\u00e9loponn\u00e8se \u2014 Kalamata',n:350},
    {r:'Cr\u00e8te Centre \u2014 R\u00e9thymnon',n:280},
    {r:'\u00c9g\u00e9e Sud Est \u2014 Rhodes, Kos',n:400},
    {r:'Dod\u00e9can\u00e8se \u2014 Rhodes',n:200},
    {r:'Cyclades \u2014 Mykonos, Santorin',n:150},
    {r:'Gr\u00e8ce Centrale \u2014 Lamia',n:120},
    {r:'\u00c9pire \u2014 Ioannina',n:100},
    {r:'Mix 1',n:80},
    {r:'Mix 2',n:50},
    {r:'Mix 3',n:30}
  ];
  var FAM=['Restauration','Beaut\u00e9','Auto','Artisans','Boulangerie','Sant\u00e9','Commerce','Services','Cafe & Bar'];
  var ST=['nouveau','appele','negociation','gagne','rappeler','maintenance','perdu'];
  var SW=[30,25,12,10,10,5,8];
  var VD=['vendeur 1','vendeur 2','vendeur 3'];
  var TT=['mobile','fixe','mobile,fixe'];
  var BZ=['Taverna','Caf\u00e9','Salon','Auto','Boulangerie','Pharmacie','Boutique','Garage','Spa','Bar','Pizzeria','Ouzeri','Gyros','Souvlaki','Trattoria','Studio','Gym','Hotel','Shop','Center','Bistro','Taberna','Psistaria','Kafeneio','Zacharoplasteio','Esthatorio','Mini Market','Superette','Optique','Clinique'];
  var GK=['\u039f\u03bb\u03c5\u03bc\u03c0\u03bf\u03c2','Acropolis','Aphrodite','Zeus','\u0391\u03b8\u03b7\u03bd\u03ac','\u03a0\u03bf\u03c3\u03b5\u03b9\u03b4\u03ce\u03bd','Apollon','Dionysos','Artemis','H\u00e9ra','Herm\u00e8s','Atlas','Ares','Titan','Calypso','Orpheus','Electra','Delphi','Sparta','Cnossos','Ikarus','Phaedra','Rhodes','Mykonos','Naxos','Corfu','Hydra','Santorin','P\u00e9gase','Cronos','Triton','Ga\u00efa','Iris','Eros','\u0394\u03ae\u03bc\u03b7\u03c4\u03c1\u03b1','\u039a\u03bd\u03c9\u03c3\u03cc\u03c2','\u039c\u03af\u03bd\u03c9\u03c2','\u0398\u03ac\u03bb\u03b1\u03c3\u03c3\u03b1','Meteora','Olympia','Plaka','Piraeus','Kifissia','Glyfada','Maroussi','Kolonaki','Pangrati','Exarchia','Monastiraki','Psiri','Kerameikos','Thissio','Koukaki'];
  var STR=['\u039f\u03b4\u03cc\u03c2 \u0395\u03c1\u03bc\u03bf\u03cd','\u039b\u03b5\u03c9\u03c6. \u0392\u03b1\u03c3. \u03a3\u03bf\u03c6\u03af\u03b1\u03c2','\u039f\u03b4\u03cc\u03c2 \u03a3\u03c4\u03b1\u03b4\u03af\u03bf\u03c5','\u03a0\u03bb. \u03a3\u03c5\u03bd\u03c4\u03ac\u03b3\u03bc\u03b1\u03c4\u03bf\u03c2','\u039f\u03b4\u03cc\u03c2 \u03a0\u03b1\u03bd\u03b5\u03c0\u03b9\u03c3\u03c4\u03b7\u03bc\u03af\u03bf\u03c5','\u039b\u03b5\u03c9\u03c6. \u039a\u03b7\u03c6\u03b9\u03c3\u03af\u03b1\u03c2','\u039f\u03b4\u03cc\u03c2 \u03a0\u03b1\u03c4\u03b7\u03c3\u03af\u03c9\u03bd','\u039f\u03b4\u03cc\u03c2 \u0391\u03ba\u03b1\u03b4\u03b7\u03bc\u03af\u03b1\u03c2','\u039f\u03b4\u03cc\u03c2 \u03a3\u03cc\u03bb\u03c9\u03bd\u03bf\u03c2','\u039f\u03b4\u03cc\u03c2 \u039c\u03b7\u03c4\u03c1\u03bf\u03c0\u03cc\u03bb\u03b5\u03c9\u03c2'];
  var CTY=['\u0391\u03b8\u03ae\u03bd\u03b1','\u0398\u03b5\u03c3\u03c3\u03b1\u03bb\u03bf\u03bd\u03af\u03ba\u03b7','\u0397\u03c1\u03ac\u03ba\u03bb\u03b5\u03b9\u03bf','\u03a7\u03b1\u03bd\u03b9\u03ac','\u03a1\u03cc\u03b4\u03bf\u03c2','\u0392\u03cc\u03bb\u03bf\u03c2','\u0399\u03c9\u03ac\u03bd\u03bd\u03b9\u03bd\u03b1','\u039a\u03b1\u03bb\u03b1\u03bc\u03ac\u03c4\u03b1','\u039b\u03b1\u03bc\u03af\u03b1','\u039b\u03ac\u03c1\u03b9\u03c3\u03b1','\u03a1\u03ad\u03b8\u03c5\u03bc\u03bd\u03bf','\u039c\u03cd\u03ba\u03bf\u03bd\u03bf\u03c2','\u03a3\u03b1\u03bd\u03c4\u03bf\u03c1\u03af\u03bd\u03b7','\u039a\u03c9\u03c2'];
  var NT=['Int\u00e9ress\u00e9 par le site','Rappeler semaine prochaine','A d\u00e9j\u00e0 un site','Budget limit\u00e9','Tr\u00e8s motiv\u00e9','Pas dispo avant 15h','Demande devis','RDV pris','En vacances','Veut page Instagram','H\u00e9sitant','Concurrent contact\u00e9','Client fid\u00e8le potentiel','Bon contact','Propri\u00e9taire absent','Num\u00e9ro incorrect','','','','',''];
  var FNA=['Nikos','Maria','Dimitris','Elena','Kostas','Sofia','Yannis','Anna','Giorgos','Katerina','Petros','Eleni','Stelios','Christina','Michalis','Ioanna','Vasilis','Despina','Thanasis','Vasia'];
  var LNA=['Papadopoulos','Nikolaou','Georgiou','Vasileiou','Konstantinou','Alexiou','Karagiannis','Makris','Pappas','Christodoulou','Papadakis','Oikonomou','Vlachos','Mavridis','Hatzigeorgiou','Stavridis'];
  var SFX=['','','','','','','','',' & Co',' Plus',' Pro',' Express',' Premium',' Center',' Greece',' Shop'];

  function pk(a){return a[Math.floor(Math.random()*a.length)]}
  function ri(a,b){return Math.floor(Math.random()*(b-a+1))+a}
  function wp(it,w){var t=0,i;for(i=0;i<w.length;i++)t+=w[i];var r=Math.random()*t,c=0;for(i=0;i<it.length;i++){c+=w[i];if(r<=c)return it[i]}return it[it.length-1]}
  function gm(){return '+30 6'+ri(90,99)+' '+ri(100,999)+' '+ri(1000,9999)}
  function gf(){return '+30 2'+ri(10,99)+ri(0,9)+' '+ri(100,999)+' '+ri(1000,9999)}
  function rd(d){var x=new Date();x.setDate(x.getDate()-ri(0,d));x.setHours(ri(8,20),ri(0,59),ri(0,59));return x.toISOString()}

  var P=[],id=1;
  RD.forEach(function(reg){
    for(var i=0;i<reg.n;i++){
      var nom=pk(BZ)+' '+pk(GK)+pk(SFX);
      var st=wp(ST,SW);
      var v=st==='nouveau'?(Math.random()>0.7?pk(VD):''):pk(VD);
      var cr=rd(120);
      P.push({
        id:id++,nom:nom,numero:Math.random()>0.3?gm():gf(),
        type_tel:pk(TT),famille:pk(FAM),categorie:pk(['A','B','C','']),
        region:reg.r,vendeur:v,status:st,notes:pk(NT),
        email:Math.random()>0.4?nom.replace(/[^a-zA-Z]/g,'').toLowerCase().slice(0,10)+ri(1,999)+'@gmail.com':'',
        instagram:Math.random()>0.6?'@'+nom.replace(/[^a-zA-Z]/g,'').toLowerCase().slice(0,12):'',
        facebook:'',rating:ri(0,5),
        adresse:pk(STR)+' '+ri(1,200)+', '+pk(CTY),
        blacklisted:false,created_at:cr,updated_at:cr,
        last_called_at:st!=='nouveau'?rd(30):null,
        total_calls:st==='nouveau'?0:ri(1,12),
        call_duration_total:st==='nouveau'?0:ri(30,900),
        call_date:st!=='nouveau'?rd(14):null
      });
    }
  });

  var CST=['gagne','negociation','maintenance','rappeler'];
  var C=[],cid=1;
  P.forEach(function(p){
    if(CST.indexOf(p.status)>=0){
      C.push({
        id:cid++,prospect_id:p.id,nom:p.nom,numero:p.numero,
        email:p.email,instagram:p.instagram,facebook:'',
        region:p.region,famille:p.famille,
        vendor_name:p.vendeur,business_name:p.nom,
        contact_name:pk(FNA)+' '+pk(LNA),
        sale_price:[350,450,500,600,750,900][ri(0,5)],
        site_status:p.status,project_id:null,hidden_by:[],
        notes:p.notes,with_maintenance:Math.random()>0.7,delivery_notes:'',
        created_at:p.created_at,updated_at:p.updated_at
      });
    }
  });

  var PJ=[
    {id:1,name:'Conqu\u00eate Ath\u00e8nes Nord',region:'Attique \u2014 Ath\u00e8nes Partie 1',vendor:'vendeur 1',vendeur:'vendeur 1',type:'all',families:'[]',target_sales:50,target_calls:500,status:'active',created_at:rd(60),updated_at:rd(5)},
    {id:2,name:'Campagne Thessalonique',region:'Mac. Centrale \u2014 Thessalonique',vendor:'vendeur 2',vendeur:'vendeur 2',type:'all',families:'[]',target_sales:25,target_calls:200,status:'active',created_at:rd(45),updated_at:rd(3)},
    {id:3,name:'Sprint Rhodes & Kos',region:'\u00c9g\u00e9e Sud Est \u2014 Rhodes, Kos',vendor:'vendeur 3',vendeur:'vendeur 3',type:'selection',families:'["Restauration","Cafe & Bar"]',target_sales:15,target_calls:100,status:'active',created_at:rd(30),updated_at:rd(1)},
    {id:4,name:'Cr\u00e8te H\u00e9raklion',region:'Cr\u00e8te Est \u2014 H\u00e9raklion',vendor:'vendeur 1',vendeur:'vendeur 1',type:'all',families:'[]',target_sales:20,target_calls:150,status:'active',created_at:rd(40),updated_at:rd(2)},
    {id:5,name:'Expansion P\u00e9loponn\u00e8se',region:'P\u00e9loponn\u00e8se \u2014 Kalamata',vendor:'vendeur 2',vendeur:'vendeur 2',type:'all',families:'[]',target_sales:10,target_calls:80,status:'active',created_at:rd(20),updated_at:rd(1)},
    {id:6,name:'Cyclades Premium',region:'Cyclades \u2014 Mykonos, Santorin',vendor:'vendeur 3',vendeur:'vendeur 3',type:'selection',families:'["Restauration"]',target_sales:8,target_calls:60,status:'active',created_at:rd(15),updated_at:rd(1)}
  ];
  PJ.forEach(function(proj){
    var rc=C.filter(function(c){return c.region===proj.region});
    rc.slice(0,Math.min(ri(8,25),rc.length)).forEach(function(c){c.project_id=proj.id});
  });

  var CH=[];
  for(var j=0;j<1000;j++){
    var p=pk(P);
    CH.push({id:j+1,prospect_id:p.id,prospect_name:p.nom,vendor_name:pk(VD),duration:ri(15,300),outcome:pk(['answered','no_answer','voicemail','busy','callback']),notes:pk(NT),created_at:rd(30)});
  }

  var VS=VD.map(function(v,i){
    return{id:i+1,vendor_name:v,total_calls:ri(400,1200),total_duration:ri(30000,100000),total_won:ri(30,100),total_lost:ri(10,40),current_streak:ri(1,18),longest_streak:ri(12,35),last_call_date:new Date().toISOString().slice(0,10),total_points:ri(1000,3000),created_at:rd(90),updated_at:rd(1)};
  });

  window.FAKE_PROSPECTS=P;
  window.FAKE_CLIENTS=C;
  window.FAKE_PROJECTS=PJ;
  window.FAKE_CALLS=CH;
  window.FAKE_VENDOR_STATS=VS;
  window.FAKE_REMINDERS=[];
  window.FAKE_BLACKLIST=[];
  window.FAKE_SCRIPTS=[];
  window.FAKE_BADGES=[];
  window.FAKE_PROSPECT_HISTORY=[];
  window.FAKE_PROJECT_OBJECTIVES=[];
  window.FAKE_ACTIVITY_LOG=[];
  window.FAKE_VENDOR_BADGES=[];
  console.log('DEMO: '+P.length+' prospects, '+C.length+' clients, '+PJ.length+' projets');
})();
