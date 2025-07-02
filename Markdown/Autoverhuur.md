Autoverhuur

sqlite database, te vinden in GIT/phyton

Tabellen:
Auto
- AutoID
- AutoMerkID
- AutoBrandstofID
- AutoType
- AutoVerbruik
- AutoTankCapaciteit
- AutoTankInhoud
- AutoActief

Create Table Auto  (
    AutoID integer primary key autoincrement,
    AutoMerkID integer NOT NULL, 
    AutoBrandstofID integer NOT NULL, 
    AutoType TEXT NOT NULL,
    AutoVerbruik integer NOT NULL,
    AutoTankCapaciteit integer NOT NULL, 
    AutoTankInhoud integer NOT NULL,
    AutoActief Boolean default true
); 

Create Index AutoMerk on Auto (AutoMerkID);
Create Index AutoBrandstof on Auto (AutoBrandstofID);

Merk
- MerkID
- MerkNaam
- MerkActief

Create Table Merk (
    MerkID integer primary key autoincrement, 
    MerkNaam TEXT not null, 
    MerkActief boolean default true
 ); 

Brandstof
- BrandstofID
- BrandstofOmschrijving
- BrandstofActief

