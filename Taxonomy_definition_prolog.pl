/*
    -----------------------------------------------
            AI ASSIGNMENT - 3
        PROLOG LOGIC PROGRAMMING

        Submitted by: Meda Rukmini
        Roll number: S20180010102
        Section: B, UG - 2.
    ------------------------------------------------
*/

% Question 1.

/*
    Predicates for species - name and subspecies - name are
    given below.
*/

/*
    Species - name predicates are defined below
*/

species-name("African wild dog","Lycaon pictus").

species-name("Common fox","Vulpes vulpes").

species-name("Arctic fox","Vulpes lagopus").

species-name("Fennec fox","Vulpes zerda").

species-name("Red wolf","Canis rufus").

species-name("Coyote","Canis latrans").

species-name("Gray wolf","Canis lupus").

species-name("Dog","Canis lupus").

/*
    Subspecies - name predicates are defined below.
    These predicates are defined for the special case of Dog and
    Gray wolf.
*/


subspecies-name("Dog","Canis lupus familiaris").

subspecies-name("Gray wolf","Canis lupus").


% Question 2.

/*
    Species - genus predicates are defined below
*/


species-genus("Lycaon pictus","Lycaon").

species-genus("Vulpes vulpes","Vulpes").

species-genus("Vulpes lagopus","Vulpes").

species-genus("Vulpes zerda","Vulpes").

species-genus("Canis rufus","Canis").

species-genus("Canis latrans","Canis").

species-genus("Canis lupus","Canis").

species-genus("Canis lupus familiaris","Canis").

% Question 3.

/*
    Genus - family predicates are defined below
*/


genus-family("Lycaon","Canidae").

genus-family("Vulpes","Canidae").

genus-family("Canis","Canidae").


% Question 4.

/*
    Predicates for common genus and common species to query are defined below.
*/

common-genus(X,Y):- 
    
    species-name(X,Z1),
    
    species-name(Y,Z2),
    
    species-genus(Z1,S),
    
    species-genus(Z2,S),

    X\=Y.

common-species(X,Y):- 

    species-name(X,Z),
    
    species-name(Y,Z),

    X\=Y.

% Question 5.

/*
    Predicate for relation path is defined below which finds the appropriate path
    from one symbol animal to another.
*/

relation-path(A,B,X):- 
    
    species-name(A,S1),
    
    species-name(B,S2),
    
    species-genus(S1,G1),
    
    species-genus(S2,G2),    
    
    ( 
    
        S1=S2 ->
        
            subspecies-name(A,SuS1),
            
            subspecies-name(B,SuS2),
            
            X=[A,SuS1,S1,SuS2,B];
            
            G1=G2 ->
            
            (
            
                ((A=="Dog");(A=="Gray wolf"))->
            
                subspecies-name(A,SuS1),
            
                X=[A,SuS1,S1,G1,S2,B];
            
                ((B=="Dog");(B=="Gray wolf"))->
                    
                    subspecies-name(B,SuS2),
                
                    X=[A,S1,G1,S2,SuS2,B];
                
                    X=[A,S1,G1,S2,B]
            );
            
            (
                
                ((A=="Dog");(A=="Gray wolf"))->
                    
                    subspecies-name(A,SuS1),
                    
                    X=[A,SuS1,S1,G1,'Canidae',G2,S2,B];
                
                ((B=="Dog");(B=="Gray wolf"))->
                
                    subspecies-name(B,SuS2),
                    
                    X=[A,S1,G1,'Canidae',G2,S2,SuS2,B];
                    
                    X=[A,S1,G1,'Canidae',G2,S2,B]
            
            )
        
    ).


